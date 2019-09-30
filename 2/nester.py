def print_list(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)


def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
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
# print_list(clothes)
