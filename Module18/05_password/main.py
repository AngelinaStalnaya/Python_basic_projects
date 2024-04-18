password = input('Придумайте пароль: ')
digits = '1234567890'


def digit_count(password):
    digits_count = 0
    for i in password:
        if i in digits:
            digits_count += 1
    return digits_count

digits_count = digit_count(password)

while password.islower() == True or len(password) < 8 or digits_count < 3:
    print('Пароль ненадёжный. Попробуйте еще раз.')
    password = input('Придумайте пароль: ')
    digits_count = digit_count(password)
else:
    print('Это надежный пароль!')