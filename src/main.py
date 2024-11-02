import time
from scratch import Scratch


if __name__ == "__main__":
    username = input()
    password = input()

    sc = Scratch(username,password)
    users = sc.get_followers(username)
    users.sort()

    for user in users:
        sc.invite_curator(user,35841742)
        time.sleep(2)
        print('test')