a = 1000
def f1():
    a = 2000
    def f2():
        a = a+2
        print(f"a inside f2 {a}")
        