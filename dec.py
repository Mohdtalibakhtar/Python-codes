# def fun(talib):
#     def exec():
#         print("executing now")
#         talib()
#         print("Executed")
#     return exec
#
# def what_is_python():
#     print("Python is a programming language")
#
# what_is_python = fun(what_is_python())
# what_is_python()

def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec

@dec1
def what_is_python():
    print("Python is a programming language")

# who_is_harry = dec1(who_is_harry)

what_is_python()