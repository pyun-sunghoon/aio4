def preprocess_legacy(data) -> list:
    res = []

    for row in data:
        # 치명적 결함: 'score' 키가 없거나 'N/A' 문자열이면 즉시 프로그램 강제 종료!
        # 치명적 결함: 100점을 초과하는 이상치(120점)도 걸러내지 못하고 1.2로 잘못 정규화함!
        try:
            score = float(row["score"])
            if score < 0 or socre > 100:
                res.append("score 값이 0~100 범위를 벗어났습니다.")
            res.append(round(score / 100.0, 4))

        except TypeError as e:
            print(f"TypeError e:{e}") # raise TypeError("score 값이 숫자가 아닙니다.")
            res.append("score 값이 숫자가 아닙니다")
        except KeyError as e:
            print(f"KeyError e:{e}") # raise TypeError("score 값이 숫자가 아닙니다.")
            res.append("score key 값이 없습니다.")
        except Exception as e:
            print(f"Exception e:{e}") # pass
            res.append(f"Exception e:{e}")

        return res 
        

list_data = [
    {"score":200.1}
]

result = preprocess_legacy(list_data)
print(result)