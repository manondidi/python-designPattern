from memoPattern.User import User
from memoPattern.Memo import Memo

if __name__ == '__main__':
    user = User()
    user.user_name = 'manondidi'
    user.tel = '18050400000'
    memo = user.create_memo()
    print(user.__dict__)
    print('篡改数据后')
    user.tel = ''
    print(user.__dict__)
    print('读档')
    user.load_memo(memo)
    print(user.__dict__)
