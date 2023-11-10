class UserInputError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)


userinput = 'a'

try:
    if (not userinput.isdigit()):
        raise UserInputError('用户输入错误')
except UserInputError as ue:
    print(ue)
finally:
    del userinput
