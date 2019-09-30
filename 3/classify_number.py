my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def classify_number(the_list):
    # 偶数
    even_list = []
    # 奇数
    odd_list = []

    for each_item in the_list:
        if each_item % 2 == 0:
            even_list.append(each_item)
        else:
            odd_list.append(each_item)
    all_number_list = ['偶数', '奇数']
    all_number_list.insert(1, even_list)
    all_number_list.append(odd_list)
    print(all_number_list)


classify_number(my_list)
