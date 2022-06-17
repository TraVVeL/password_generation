import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
ambivalent = 'il1Lo0O'


class Error(Exception):
    """ Common base class for all non-exit exceptions. """
    pass


class NoSuchType(Error):
    """ Inappropriate argument type. """
    pass


class ValueSmall(Error):
    """ Called when the value is less than one."""
    pass


class ValueNotInteger(Error):
    """ Called when the value has a type other than integer."""
    pass


def check_int(prompt="Enter: "):
    while True:
        num = input(prompt)
        try:
            if not num.isdigit():
                raise ValueNotInteger
            elif int(num) < 1:
                raise ValueSmall
            else:
                return int(num)
        except ValueNotInteger:
            print("Ввод должен быть целочисленным числом ")
        except ValueSmall:
            print("Число должно быть больше или равно единицы")


def check_includes(rec="Enter: "):
    while True:
        include = input(rec)
        try:
            if include not in ['+', '-', 'y', 'n', 'yes', 'no']:
                raise NoSuchType
            else:
                return include
        except NoSuchType:
            print("Ведённые данные должны быть верны")


def do_calc():
    pass_count = check_int('Количество паролей для генерации ?: ')
    pass_length = check_int('Длина вашего пароля ?: ')
    include_digits = check_includes('Включать ли цифры +/- ?: ')
    include_uppercase = check_includes('Включать ли прописные буквы +/- ?: ')
    include_lowercase = check_includes('Включать ли строчные буквы +/- ?: ')
    include_chars = check_includes('Включать ли символы (!#$%&*+-=?@^_) +/- ?: ')
    include_ambivalent = check_includes('Исключать ли неоднозначные символы (il1Lo0O) +/- ?: ')

    def password_choice():
        data = []
        included_chars = ''
        data.append(digits), data.append(lowercase_letters), data.append(uppercase_letters), data.append(punctuation)
        choices = [include_digits, include_uppercase, include_lowercase, include_chars]

        for i in range(len(choices)):
            if choices[i] in ['+', 'y', 'yes']:
                included_chars += data[i]

        if include_ambivalent in ['+', 'y', 'yes']:
            for j in ambivalent:
                included_chars = included_chars.replace(j, '')
        else:
            included_chars += data[0]

        return included_chars

    def password():
        chars = []

        print('Ваши пароли:')
        for i in range(1, pass_count + 1):
            for j in range(1, pass_length + 1):
                chars += random.choice(password_choice())
                if len(chars) == pass_length:
                    print(i, '. ', *chars, sep='')
                    chars = []

    password()


do_calc()
