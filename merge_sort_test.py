#coding: utf-8

def MergeSort(plist):
    '''归并排序（分治法思想）'''
    n = len(plist)
    #递归结束回弹条件
    if n <=1:
        return plist
    mid = n//2
    #对mid值右边的list进行拆分
    left_list = MergeSort(plist[:mid])
    #对mid值左边的list进行拆分
    right_list = MergeSort(plist[mid:])
    '''以上为递归操作，是不断深入的，而这个操作的实体就是mid = n//2，不断重复这个操作，深度不断加深，最后触及if条件触底反弹
    开始对划分好的左右list一层一层的做处理，而做处理就是要实现要达到的目的，下面的return就是为了返回上一级，继续对当前级的左右list进行
    下面的步骤处理。因此要放在递归语句的下面'''

    #将两个list按照大小顺序合并到一起
    left_sign,right_sign = 0,0
    result = []
    while left_sign is not len(left_list) and right_sign is not len(right_list):
        if left_list[left_sign] <= right_list[right_sign]:
            result.append(left_list[left_sign])
            left_sign +=1
        elif left_list[left_sign] >right_list[right_sign]:
            result.append(right_list[right_sign])
            right_sign +=1
    result += left_list[left_sign:]                  #这两行的意思就是说左右肯定会有一方先走到头，那么就会跳出，此时就要在result后面直接加上没
    result +=right_list[right_sign:]                 #走完的那一侧剩余的部分
    return result


if __name__ == "__main__":
    li = [54, 26, 93, 999, 77, 100000, 44, 55, 20,60,2,9,5,80]
    print(li)
    sorted_li = MergeSort(li)
    print(li)
    print(sorted_li)



