def print_list(the_list, level):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, level)
        else:
            print(each_item)


def print_lol(the_list, level):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, level)
        else:
            for l in range(level):
                print('\t', end='')
            print(each_item)


clothes = [
    ["真丝小衫女洋气2019年夏季新款韩版宽松", [79.00, "包邮"]],
    "successful祺舰店",
    ["印花雪纺衫女2019春秋新款", [72.00, "包邮"]],
    "罗应桃22",
    ["小香风针织开衫2018秋季新款针织衫外套", [168.00, "包邮"]],
    "doider朵尼丹尔旗舰店",
]
# print(clothes[0][1])
# print_list(clothes, 2)
