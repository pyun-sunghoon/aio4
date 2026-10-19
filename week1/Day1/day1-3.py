# 사용자로부터 데이터를 입력받아서(5개) 리스트에 저장하고
# 저장된 리스트의 값 중에서 짝수만 출력해 보기

scores = []
for i in range(5) :
  scores.append(int(input(f"{1+i} : 숫자를 입력하세요 : ")))


print('리스트변수의 값 : ', scores)
for i in scores :
  if i % 2 == 0:
    print(i)