from collections import UserList

class MyUniqueList(UserList):
    def replace_in_middle(self, item):
        count = -1
        for i in self:
            count += 1
        self[int(count/2)] = item


mylist = MyUniqueList([1, 2, 3, 4, 5])
print(mylist)
mylist.replace_in_middle('CFG')
print(mylist)