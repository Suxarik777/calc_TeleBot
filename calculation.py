from digit_transformation import digit_formatting_complex, digit_formatting_rational


def calc_operation_complex(dct_lst_user_id):
    value_lst = digit_formatting_complex(dct_lst_user_id)
    digit_1, digit_2, operation = value_lst

    if operation == '+':
        return summa(digit_1, digit_2)
    if operation == '-':
        return sub(digit_1, digit_2)
    if operation == '*':
        return mult(digit_1, digit_2)
    if (operation == '/') and (digit_2 != 0):
        return div(digit_1, digit_2)
    else:
        return 'Ошибка деления на 0!'

def calc_operation_rational(dct_lst_user_id):
    value_lst = digit_formatting_rational(dct_lst_user_id)
    digit_1, digit_2, operation = value_lst

    if operation == '+':
        return summa(digit_1, digit_2)
    if operation == '-':
        return sub(digit_1, digit_2)
    if operation == '*':
        return mult(digit_1, digit_2)
    if (operation == '/') and (digit_2 != 0):
        return div(digit_1, digit_2)
    else:
        return 'Ошибка деления на 0!'


def summa(digit_1, digit_2):
    return digit_1 + digit_2


def sub(digit_1, digit_2):
    return digit_1 - digit_2


def mult(digit_1, digit_2):
    return digit_1 * digit_2


def div(left_value, right_value):
    return left_value / right_value