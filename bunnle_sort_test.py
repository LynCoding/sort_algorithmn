#coding: utf_8
import timeit

def bubble_sort(alist):#使用的容器为顺序表
    n = len(alist)
    for i in range(n-1):
        count = 0
        for j in range(n-1-i):
            if alist[j]>alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]
                count +=1
        if count == 0:
            return alist
    return alist


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    bubble_sort(li)
    print(li)



