#  P is one-dimensional array of integers. Write a Java program search for a data VAL from P. If VAL is present in the array then “element found ” otherwise “element not found” should be displayed. 

arr = [2,3,4,25,7,45,8,34,9]
target = 0
for i in arr:
    if i ==target:
        print("Element found ")
        break
else:
    print("element not found ")
