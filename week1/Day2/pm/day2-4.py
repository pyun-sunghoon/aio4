# 리스트에서 불량을 모두 지우고 정상만 남게
items = ['정상','불량','불량','정상','불량']
for idx, item in reversed(list(enumerate(items))):
    if item == '불량':
        del items[idx]

print(f'검수결과 : {items}')

