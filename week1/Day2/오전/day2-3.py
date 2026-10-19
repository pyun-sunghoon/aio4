class SafeProfile:
    def __init__(self):
        pass
    def get(self, key):
        return True
    def set(self,key):
        return True

user_profile = SafeProfile()

if user_profile and user_profile.get('is_v'):
    print('성공')
else:
    print('실패')