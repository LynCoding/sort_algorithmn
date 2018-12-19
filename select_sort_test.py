#coding:utf-8

'''def SelcetSort(alist):
    n = len(alist)
    for i in range(0,n-1):
        cur = i
        for j in range(i,n):
            if alist[cur]>alist[j]:
                cur = j
        alist[i], alist[cur] = alist[cur], alist[i]'''


def SelcetSort(alist):
    n = len(alist)
    for i in range(0,n-1):
        for j in range(i,n):
            if alist[i]>alist[j]:
                alist[i],alist[j] = alist[j],alist[i]


if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    SelcetSort(li)
    print(li)