import re
import sys
import string
import os
import argparse
from getpass import getpass


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--blacklist', help='Path to blacklist file')
    return parser.parse_args()


def check_password_inclusion_values(password):
    patterns = [r'[a-z]+', r'[A-Z]+',
                r'{}'.format(re.escape(string.punctuation))]
    rating = 0

    for pattern in patterns:
        if re.search(pattern, password):
            rating += 1

    return rating


def check_password_length(password):
    rating = 0
    min_password_length = 10

    if len(password) >= min_password_length:
        rating += 2

    return rating


def load_blacklist(filepath):
    try:
        with open(filepath) as blacklist_file:
            blacklist_list = blacklist_file.read().splitlines()

        return blacklist_list
    except (TypeError, IOError):
        return None


def check_password_in_blacklist(password, blacklist_list):
    if password not in blacklist_list:
        rating = 2
    else:
        rating = 0

    return rating


def check_password_prohibited_values(password):
    rating = 0
    patterns = [r'\d{2,4}[\.-]\d{2}[\.-]\d{2,4}', r'\+?\d+[-(\s]\d+[-)\s].+']

    for pattern in patterns:
        if not re.search(pattern, password):
            rating += 1

    return rating


def get_rating_description(rating):
    if rating <= 5:
        return 'Weak'
    elif rating <= 7:
        return 'Good'
    else:
        return 'Strong'


def get_password_strength(password, blacklist_list):
    rating = []
    rating.append(check_password_inclusion_values(password))
    rating.append(check_password_length(password))
    rating.append(check_password_prohibited_values(password))

    if blacklist_list:
        rating.append(check_password_in_blacklist(password, blacklist_list))

    return sum(rating)


if __name__ == '__main__':
    args = parse_args()

    password = getpass(
               prompt='Enter the password to calculate its complexity: ')

    if not password:
        sys.exit('You entered empty password')

    blacklist_list = load_blacklist(args.blacklist)

    if not blacklist_list:
        print("Failed to read blacklist file. This check will be skipped")

    rating = get_password_strength(password, blacklist_list)
    rating_description = get_rating_description(rating)

    print('Your password rating is {} ({})'.format(rating, rating_description))
