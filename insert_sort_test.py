#coding: utf-8

def InsertSort(plist):
    n = len(plist)
    for i in range(1,n):
        for j in range(i,-1,-1):
            if plist[j]>plist[i]:
                plist[j],plist[i] = plist[i],plist[j]
                i = j


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    InsertSort(li)
    print(li)