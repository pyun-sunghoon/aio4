# 리스트 컴프리핸션
result = []
list_1 = [1,2,3,4,5]
# for i in list_1:
#     if i % 2 == 0:
#         result.append(i)

#result = [i for i in list_1 if i%2 == 0]
result = [i*2 for i in list_1]

print(result)


menu = ['아메리카노', '라떼', '초코']
ice_menu = ['아이스 '+i for i in menu]
len_menu = [i for i in menu if len(i) % 2 == 0]

print(len_menu)


ages = [20, 15, 60, 25, 30, 45, 5]
print([i for i in ages if i >= 20])
print(['성인' if i>=20 else '미성년' for i in ages])

if "":
    print("abc")

import re
#help(re.sub)
print(type(re.IGNORECASE))