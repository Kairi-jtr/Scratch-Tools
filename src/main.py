import time
from scratch import Scratch

if __name__ == '__main__':
    print('Scratchのユーザー名を入力してください:')
    username = input()
    print('Scratchのパスワードを入力してください:')
    password = input()

    sc = Scratch(username,password)
    followers = sc.get_followers(username)

    for user in followers:
        sc.invite_curator(user,35841742)
        time.sleep(2)
    
    print('すべてのユーザーの招待に成功しました！')