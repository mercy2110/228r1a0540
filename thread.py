import threading
import time


'''def cal_fun():
    print("thread")
t1=threading.Thread(target=cal_fun(),args=(10,1))
t1.start()
'''
def f_square(n):
    print("square=",n*n)
    for i in 5:
        time.sleep(0.5)
    print("square=",n*n)
def f_cube(n):
    print("cube=",n*n*n)
    for i in 5:
        time.sleep(0.7)
    print("cube=",n*n*n)
t1=threading.Thread(target=f_square,args=(5))
t2=threading.Thread(target=f_cube,args=(101))
t1.start()
t2.start()
t1.join()
t2.join()