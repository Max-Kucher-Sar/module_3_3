# 1st task
def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params(b = 25)
print_params(c = [1, 2, 3])

# 2nd task
values_list = [2, 'string', True]
values_dict = {'a': 3, 'b': 'word', 'c': False}
print_params(*values_list)
print_params(**values_dict)

# 3rd task
values_list2 = [13, 'name']
print_params(*values_list2, 42)