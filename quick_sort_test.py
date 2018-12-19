#coding: utf-8

def QuickSort(plist,first,last):
    #if low >=high:             #错误条件。
       # return
    if first>=last:
        return
    low = first
    high = last
    mid_value = plist[first]
    while low<high:
        while low<high and plist[high]>=mid_value:
            high-=1
        plist[low] = plist[high]
        while low<high and plist[low]<mid_value:
            low+=1
        plist[high] = plist[low]
    plist[low] = mid_value
    QuickSort(plist,first,low-1)                #递归注意参数传递
    QuickSort(plist,low+1,last)



if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20, 1, 8, 10, 22]
    print(li)
    QuickSort(li, 0, len(li) - 1)
    print(li)


