try:
    a=int(input("enter a value"))
    b=int(input("enter b value"))
    #c=a/b
    print("value of c:",a/b)
    x=[1,2,3,4]
    print(x[5])
except NameError:
    print("b value is not mentioned")
except ZeroDivisionError:
    print("Arithmatic exception")
except ValueError:
    print("Value Error")
except IndexError:
    print("Array index out of bound")
except KeyError:
    print("Key error")
except IOError:
    print("File input or output error")
print("After exception")