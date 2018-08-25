import re


def check_inclusion(password):
    rules = ['[a-z]+', '[A-Z]+', '[\d]+', '[\.\+\*\?!,<>%\^:@#\$&]+']
    rating = 0

    for rule in rules:
        rule_formated = r'{}'.format(rule)
        if re.search(rule_formated, password):
            rating += 1

    return rating


def check_length(password):
    rating = 0

    if len(password) >= 10:
        rating += 2

    return rating


def check_blacklist(password):
    rating = 2

    blacklist = ['123', '123qwe', 'password1', '123456', 'admin']

    for bad_password in blacklist:
        if re.search(bad_password, password):
            rating = 0
            break

    return rating


def check_prohibited(password):
    rating = 0
    rules = ['\d{2,4}[\.-]\d{2}[\.-]\d{2,4}', '\+?\d+[-(\s]\d+[-)\s].+']

    for rule in rules:
        rule_formated = r'{}'.format(rule)
        if not re.search(rule_formated, password):
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
    rating = check_inclusion(password)
    rating += check_length(password)
    rating += check_blacklist(password)
    rating += check_prohibited(password)

    return rating


if __name__ == '__main__':
    password = input('Enter the password to calculate its complexity: ')
    rating = get_password_strength(password)
    rating_description = get_rating_description(rating)

    print('Your password rating is {} ({})'.format(rating, rating_description))
