#coding:utf-8

#选择排序

def Selcet_sort(alist):
    n = len(alist)
    if n == 0:
        return None
    cur = 0
    while cur<n:
        min_index = cur
        for i in range(cur,n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[cur],alist[min_index] = alist[min_index],alist[cur]
        cur += 1

#插入排序

def Insert_sort(alist):
    n = len(alist)
    for i in range(1,n):
        for j in range(i,-1,-1):
            if alist[j]>alist[i]:
                alist[j],alist[i] = alist[i],alist[j]
                i = j

#快速排序

def Qucik_sort(alist,first,last):
    if first>=last:
        return
    mid_value = alist[first]
    low = first
    high = last
    while low<high:
        while low<high and alist[high]>=mid_value:
            high -= 1
        alist[low] = alist[high]
        while low<high and alist[low]<mid_value:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid_value
    Qucik_sort(alist,first,low-1)
    Qucik_sort(alist,low+1,last)

#归并排序

def Merge_sort(alist):
    n = len(alist)
    if n <=1:
        return alist
    mid_index = n//2
    left_list =Merge_sort(alist[:mid_index])
    right_list = Merge_sort(alist[mid_index:])

    result = []
    left_sign,right_sign = 0,0
    while left_sign <len(left_list) and right_sign <len(right_list):
        if left_list[left_sign] <= right_list[right_sign]:
            result.append(left_list[left_sign])
            left_sign += 1
        elif left_list[left_sign] > right_list[right_sign]:
            result.append(right_list[right_sign])
            right_sign += 1
    result += left_list[left_sign:]
    result += right_list[right_sign:]
    return result

#二分查找
def GetNumberOfK( data, k):
    # write code here
    n = len(data)
    low = 0
    last = n - 1
    num = 0
    while low <= last:
        mid = (low + last) // 2
        if low >= last:
            return num
        if data[mid] == k:
            num += 1
            if data[low] == k and data[last] == k:
                num += 2
            elif data[low] == k or data[last] == k:
                num += 1

            last -= 1
                # low += 1
        elif data[mid] > k:
            last = mid - 1
        if data[mid] < k:
            low = mid + 1



if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    li1 = [1,2,3,3,3,3,4,5]
    print(li1)
    #Selcet_sort(li)
    #Insert_sort(li)
    # Qucik_sort(li,0,len(li)-1)
    #li_sort = Merge_sort(li)
    print(GetNumberOfK(li1,3))
    # print(li_sort)



