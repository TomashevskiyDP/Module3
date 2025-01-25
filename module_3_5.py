# Самостоятельная работа по уроку "Рекурсия"

def remove_zeros(number):
    if number % 10 == 0:
        number //= 10


def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    elif len(str_number) == 1:
        return int(str_number)




result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402310)
print(result2)