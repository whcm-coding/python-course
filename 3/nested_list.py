my_list = [
    ['valid', 2, 3, 4],
    ['invalid', 4, 5],
    ['valid', 6, 7],
    ['invalid', 8, 9, 10, 11]
]


def print_selected_number(the_list):
    for each_item in my_list:
        if each_item[0] == 'valid':
            print('有效数据：', end='')
            for nested_item in each_item:
                if (isinstance(nested_item, int)):
                    print(nested_item, end='')
            print('\n', end='')
        else:
            print('无效数据')


print_selected_number(my_list)
