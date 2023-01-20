# 在同一个类的实例之间做排序，但是它们原生并不支持比较操作


class User:

    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


users = [User(32), User(25), User(10)]

s_users = sorted(users, key=lambda u: u.user_id)

print(s_users)

from operator import attrgetter

a_users = sorted(users, key=attrgetter('user_id'))
print(a_users)