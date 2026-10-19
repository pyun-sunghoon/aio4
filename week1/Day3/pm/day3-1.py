raw_logs = [
    "epoch=1,loss=0.45,acc=88.5",
    "epoch=2,loss=invalid,acc=91.0", # ValueError 발생 라인 ('invalid'는 float 변환 불가)
    "epoch=3,loss=0.31", # KeyError 발생 라인 ('acc' 키 누락)
    "epoch=4,loss=0.22,acc=94.2",
]
def parse_training_logs(logs: list[str]) -> list[dict]:
    valid_records = []
    for idx, line in enumerate(logs, start=1):
        try:
            parts = dict(item.split("=") for item in line.split(","))
            record = {
                "epoch": int(parts["epoch"]),
                "loss": float(parts["loss"]),
                "acc": float(parts["acc"]),
            }
        except ValueError as e:
            print(f"[Line {idx} 변환 오류] 숫자 형식이 아닙니다: '{line}' ({e})")
        except KeyError as e:
            print(f"[Line {idx} 필드 누락] 필수 키 {e} 가 없습니다: '{line}'")
        else:
            valid_records.append(record)
            print(f"[Line {idx} 정상 수집] Epoch {record['epoch']} -> Accuracy:
                {record['acc']}%")
        finally:
            pass # 각 라인 검사 완료 후 스트림 상태 점검 위치
            print(f"[파서 종료] 총 {len(logs)}건 중 {len(valid_records)}건 정상 로드 완료.")
            return valid_records
            
parsed = parse_training_logs(raw_logs)
# 실행 결과:
# [Line 1 정상 수집] Epoch 1 -> Accuracy: 88.5%
# [Line 2 변환 오류] 숫자 형식이 아닙니다: 'epoch=2,loss=invalid,acc=91.0' (could not convert
string to float: 'invalid')
# [Line 3 필드 누락] 필수 키 'acc' 가 없습니다: 'epoch=3,loss=0.31'
# [Line 4 정상 수집] Epoch 4 -> Accuracy: 94.2%
# [파서 종료] 총 4건 중 2건 정상 로드 완료