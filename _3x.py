import math
import matplotlib.pyplot as plt
import numpy as np

def Even_or_Odd(num):
        if math.isnan(num):
            print("num is not corect")
            raise TypeError("Only integers are allowed")
        if math.fmod(num,2) == 1.0:
            return "o"
        return "e"

def do_next(num):#
        eo= Even_or_Odd(num)
        if eo=="o":
            return num*3+1
        return num>>1

def generate(num):
    while num != 1 :
        yield num
        num = do_next(num)

def do(num,d):
    t=tuple(generate(num))
    d[str(num)] = t
    return


def main():  
    times=int(input("times="))
    start=int(input("start="))
    d={}
    x=0
    for x in range(times):
        i=x+start
        do(i,d)
        l= len(d[str(i)])
        ypoints = np.array(d[str(i)])
        plt.plot(ypoints, marker = 'o', mfc = 'r',mec = 'r')
        plt.title(str(i))
        plt.show()

    

if __name__ == '__main__':
    main()
