import random
while True:
    password_length = input("What is the length of your password: (1-20): ")
    if password_length.isdigit():
        password_length = int(password_length)
        if 1 <= password_length <= 20:
            break
        else:
            print("Length between 1 to 20")
    else:
        print("password must be a digit")


characters_alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
characters_symbol = '~!@#$%^&*())_+?><|'
characters_number = '1234567890'


def generate_password():
    password = ''
    if security_type == 'w':
        for _ in range(password_length):
            password += random.choice(characters_alphabet)
        print(f'your password is : {password}')

    elif security_type == 'm':
        for _ in range(password_length):
            choice = random.choice([characters_alphabet, characters_number])
            password += random.choice(choice)
        print(f'your password is : {password}')

    else:
        for _ in range(password_length):
            choice = random.choice([characters_alphabet, characters_number, characters_symbol])
            password += random.choice(choice)
        print(f'your password is : {password}')


security_type = input("What is the security type (w(weak),m(medium),s(strong): ").lower()
generate_password()
