with open('sort_clothes.txt') as clothes:
    data = clothes.readline()
clothes = data.strip().split(',')
unique_clothes = set(clothes)
sorted_unique_clothes = sorted(unique_clothes)

print("clothes", clothes)
print("unique_clothes", unique_clothes)
print("sorted_unique_clothes", sorted_unique_clothes)
print("first 3 of sorted_unique_clothes", sorted_unique_clothes[0:3])


# unique_clothes = []
# for each_cloth in sorted_clothes:
#     if each_cloth not in unique_clothes:
#         unique_clothes.append(each_cloth)
# print(unique_clothes)
# print(unique_clothes[0:3])
# print(sorted_clothes)
# print(sorted_clothes[0:3])
# print(sorted_clothes[:3])
