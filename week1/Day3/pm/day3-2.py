# class PromptEmptyError(Exception):
#     pass

# prompt = ""

# if not prompt.strip():
#     try:
#         raise PromptEmptyError()
#     except PromptEmptyError as e:
#         print("프롬프트는 반드시 제공되어야 합니다.")

# print('정상종료')


for i in range(5):
    
    try:
        in1 = int(input())
    except:
        print("error")
        break
    finally:
        print("finally")
    