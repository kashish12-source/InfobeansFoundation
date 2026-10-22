def f1():
    print("f1 call")
    def f2():
        print("f2 call")
    return f2
f2 = f1()
f2()
print(f2())

print(f1())
