with open('clothes.txt') as clothes:
    data = clothes.readline()
clothes = data.strip().split(',')
# clothes.sort()
# print(clothes)

# print(sorted(clothes))


def sanitize(cloth_price):
    if '-' in cloth_price:
        splitter = '-'
    elif ':' in cloth_price:
        splitter = ':'
    else:
        return float(cloth_price)
    (yuan, fen) = cloth_price.split(splitter)
    return float(yuan + '.' + fen)


cloth_price = [sanitize(each_price) for each_price in clothes]
# for each_price in clothes:
#     cloth_price.append(sanitize(each_price))

print(sorted(cloth_price))
