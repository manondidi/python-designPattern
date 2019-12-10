from memoPattern.Memo import Memo


class User:
    def __init__(self):
        self.user_name = ''
        self.tel = ''

    def create_memo(self):
        return Memo(self.user_name, self.tel)

    def load_memo(self, memo):
        self.user_name = memo.user_name
        self.tel = memo.tel
