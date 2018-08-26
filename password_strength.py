import re
import sys
import string
import os
from getpass import getpass


def check_password_inclusion_values(password):
    rules = [r'[a-z]+', r'[A-Z]+', r'{}'.format(re.escape(string.punctuation))]
    rating = 0

    for rule in rules:
        if re.search(rule, password):
            rating += 1

    return rating


def check_password_length(password):
    rating = 0
    min_password_length = 10

    if len(password) >= min_password_length:
        rating += 2

    return rating


def check_password_in_blacklist(password):
    rating = 2

    blacklist_path = 'blacklist.txt'

    if not os.path.exists(blacklist_path):
        print("Can't find blacklist file. This check will be skipped")
        rating = 0
    else:
        with open(blacklist_path) as blacklist_file:
            blacklist_list = blacklist_file.read().splitlines()

        if password in blacklist_list:
            rating = 0

    return rating


def check_password_prohibited_values(password):
    rating = 0
    rules = [r'\d{2,4}[\.-]\d{2}[\.-]\d{2,4}', r'\+?\d+[-(\s]\d+[-)\s].+']

    for rule in rules:
        if not re.search(rule, password):
            rating += 1

    return rating


def get_rating_description(rating):
    if rating <= 5:
        return 'Weak'
    elif rating <= 7:
        return 'Good'
    else:
        return 'Strong'


def get_password_strength(password):
    rating = []
    rating.append(check_password_inclusion_values(password))
    rating.append(check_password_length(password))
    rating.append(check_password_in_blacklist(password))
    rating.append(check_password_prohibited_values(password))

    return sum(rating)


if __name__ == '__main__':
    password = getpass(
               prompt='Enter the password to calculate its complexity: ')

    if not password:
        sys.exit('You entered empty password')

    rating = get_password_strength(password)
    rating_description = get_rating_description(rating)

    print('Your password rating is {} ({})'.format(rating, rating_description))
