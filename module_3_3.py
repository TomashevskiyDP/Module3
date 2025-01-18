# Самостоятельная работа по уроку "Распаковка позиционных параметров"

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(8, 'stroka', False)
print_params(3, 'pizza')
print_params(88)
print_params(a=5, b='banana', c=False)
print_params(a=2, b='star')
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [8, 'stroka', False]
values_dict = {'a': 5, 'b': 'banana', 'c': False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)