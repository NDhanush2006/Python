"""
Private(like)attributes & Methods:-->
Conceptual implementation in python:-
Private(like)attributes & Methods aremeant to be used only within the class and are not accesible
from outside the class
        # Private -(__Variable_name)

"""


class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)


s = Account(10101, 4455)
print(s.acc_no)
# print(s.acc_pass)
print(s.reset_pass())
