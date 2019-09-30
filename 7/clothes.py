with open('clothes.txt',  encoding="utf-8") as clothes:
    data = clothes.readline()
    clothes = data.strip().split(',')
    shop = {
        'name': clothes[0],
        'date':  clothes[1],
        'price': clothes[2:]
    }
    unique_clothes = set(shop['price'])

    sorted_unique_clothes = sorted(unique_clothes)

    print(shop['name'], "价格最低的三条数据为：", sorted_unique_clothes[0:3])

    # shop = clothes[0]
    # date = clothes[1]
    # clothes = clothes[2:]
    # print(sorted_unique_clothes)
