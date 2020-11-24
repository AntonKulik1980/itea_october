# class stack():
#
#     def __init__(self):
#         self.stack = []
#
#     def add(self,value):
#         if value not in self.stack:
#             self.stack.append(value)
#             return True
#         else:
#             return False
#
#     def remove(self):
#         if len(self.stack) <=0:
#             return("No elements")
#         else:
#             return self.stack.pop()
#
#     def get_stack(self):
#         return self.stack
# stack.add(1)
# print(stack.get_stack())


class Stack:

    def __init__(self):
        self.stack = []

    def add(self, dataval):

        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False


    def remove(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()

    def peek(self):
        return self.stack[-1]




AStack = Stack()
AStack.add(1)
AStack.add(2)
AStack.add(3)
print(AStack.peek())

