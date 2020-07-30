import re


def validate(email):
    return re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email)


if __name__ == '__main__':
    email = input()
    if validate(email):
        print("Email was valid")
    else:
        print("Email was not valid")
