# 各排序算法的简易理解

## 一、冒泡排序

### 基本思路		

​		最基础的排序方法，给定一个数组，从最后一个元素开始，依次与前面相邻的元素进行比较，如果该元素小于前面的元素，则交换元素位置，重复该步骤，直到到达第一个（也可以从前往后）。然后一次循环。

### 代码实现

```python
def bubble_sort(alist):
    n = len(alist)
    for i in range(n):
        for j in range(i+1,n):
            if alist[i] > alist[j]:
                alist[i],alist[j] = alist[j],alist[i]
    return alist


if __name__ == '__main__':
    li = [1, 2, 4, 7, 54, 8, 5, 3, 5, 9, 5, 3]
    print(bubble_sort(li))
```

### 复杂度

| 排序名称 | 平均时间复杂度 | 最好情况下 | 最坏情况下 | 空间复杂度 | 是否稳定 |
| -------- | :------------: | :--------: | :--------: | :--------: | :------: |
| 冒泡排序 |    O($n^2$)    |    O(n)    |  O($n^2$)  |    O(1)    |   稳定   |

## 二、选择排序

### 基本思路

​		首先，给定一个下标，从0开始，然后从该指针下一个元素开始往后找，如果该元素小于此指针的下标，则交换位置，继续下一个。

### 代码实现

```python
def choose_sort(alist):
    n = len(alist)
    for i in range(n):
        index = i
        for j in range(i + 1, n):
            if alist[index] > alist[j]:
                alist[index], alist[j] = alist[j], alist[index]
    return alist


if __name__ == '__main__':
    li = [1, 2, 4, 67, 4, 2, 4, 67, 9, 5, 2, 4, 8, 9, 5, 3]
    print(choose_sort(li))
```

### 复杂度

| 排序名称 | 平均时间复杂度 | 最好情况下 | 最坏情况下 | 空间复杂度 | 是否稳定 |
| -------- | :------------: | :--------: | :--------: | :--------: | :------: |
| 选择排序 |    O($n^2$)    |  O($n^2$)  |  O($n^2$)  |    O(1)    |  不稳定  |

## 三、插入排序

### 基本思路

​		类似从第一个元素开始遍历，然后从后往前进行冒泡排序

### 代码实现

```python
def init_sort(alist):
    n = len(alist)
    for i in range(n):
        for j in range(i, 0, -1):
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]
    return alist


if __name__ == '__main__':
    li = [12, 5, 3, 2, 5, 78, 4, 3, 2, 4, 7, 8, 5, 4, 212, 6]
    print(init_sort(li))
```

### 复杂度

| 排序名称 | 平均时间复杂度 | 最好情况下 | 最坏情况下 | 空间复杂度 | 是否稳定 |
| -------- | :------------: | :--------: | :--------: | :--------: | :------: |
| 插入排序 |    O($n^2$)    |    O(n)    |  O($n^2$)  |    O(1)    |   稳定   |

## 四、快速排序

### 基本思路

​		选择中间值，分出左半边和右半边，然后循环该操作，直到传入的值符合结束要求。

​		细化：对于传入的数组，有开始指针和结束指针，然后开始指针设为中间值，从结束指针开始往前移动，如果该值小于中间值，则把结束指针上的值与开始指针进行位置交换，然后由开始指针往前移动，如果值大于中间值，则与结束指针的值进行交换，重复上述操作，直到开始指针和结束指针的值相等，此时数组分为中间值，中间值左边部分，中间值右边部分。然后把这些部分再次递归调用函数，直到传入的参数的开始指针大于等于结束指针时，返回函数。

### 代码实现

```python
def fast_sort(alist, first, last):
    # 判断该函数是否结束
    if first >= last:
        return
    mid_val = alist[first]
    low = first
    high = last
    while low < high:
        # 如果开始指针小于结束指针并且结束指针指向的值大于等于中间值
        while low < high and alist[high] >= mid_val:
            # 结束指针往左移动一位
            high -= 1
        # 当上层循环结束时，说明开始指针等于结束指针或者结束指针小于中间值
        # 则需要将结束指针指向的值放到开始指针指向的位置
        alist[low] = alist[high]
        # 接下来由开始指针进行判断，如果开始指针小于结束指针并且开始指针指向的值小于中间值
        while low < high and alist[low] < mid_val:
            # 开始指针往右移动一位
            low += 1
        # 当上层循环结束时，说明开始指针等于结束指针或者开始指针大于中间值
        # 则需要将开始指针指向的值放到结束指针指向的位置
        alist[high] = alist[low]
    # 如果上层循环结束，说明开始指针和结束指针指向同一个位置，则把中间值放到开始指针所指位置（也可以是结束指针）
    alist[low] = mid_val

    # 结束以上的工作，说明该数组在first到end之间，已经分出了三部分（即中间值，中间值的左半部分和中间值的右半部分），接下来即可将左半部分和右半部分放入函数进行重新递归。
    fast_sort(alist, first, low - 1)
    fast_sort(alist, low + 1, last)


if __name__ == '__main__':
    li = [1, 2, 4, 6, 4, 3, 65, 7, 4, 2, 5, 7, 8, 54, 3, 2, 76, 6, 43, 2, 8]
    fast_sort(li, 0, len(li)-1)
    print(li)
```

### 复杂度

| 排序名称 | 平均时间复杂度 | 最好情况下 | 最坏情况下 |  空间复杂度  | 是否稳定 |
| -------- | :------------: | :--------: | :--------: | :----------: | :------: |
| 快速排序 |    O(nlogn)    |  O(nlogn)  |  O($n^2$)  | O(logn)~O(n) |  不稳定  |

## 无、归并排序

### 基本思路

​		先递归分解数组，再合并数组。

​		细化：【1.拆分数组】传入数组，获取该数组的中间位置（向下取整或者整除2），然后重复上诉操作，直至传入函数的数组达到了长度为1。【2-1.创建数组】因为每个传入的数组都被分为两个部分（前半部分和后半部分），给定两个指针，分别指向每个数组的第一个元素，然后创建一个新的数组用来存放这两个数组合并后的数组。【2-2.合并数组】对两个指针的值进行判断，那个值小，就将哪个值放入新数组，该指针往右移动一个位置。重复上述操作直至某个指针达到该指针所在列表的长度。【2-3.压入多余数组】因为会存在一个数组已经全部压入新数组了但是另一个并没有放入，所以要判断哪个数组还有剩余，把这些元素全部压入

### 代码实现

```python
def merge_sort(alist):
    # 判断传入的数组长度是否小于1，如果是返回该数组
    if len(alist) < 2:
        return alist

    mid = len(alist) // 2  # 获取中间值

    # left_li,right_li:采用归并排序后形成的新的有序的列表
    left_li = merge_sort(alist[:mid])
    right_li = merge_sort(alist[mid:])

    # 下面是将两个数组合并成一个新的数组
    left_pointer = 0
    right_pointer = 0
    result = []
    # 如果左指针小于左列表长度并且右指针小于右列表的长度
    while left_pointer < len(left_li) and right_pointer < len(right_li):
        # 如果左列表下的左指针所指向的值小于右边的，则把该值放入新列表
        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            # 不然就把右边的值放入新列表指针加一
            result.append(right_li[right_pointer])
            right_pointer += 1
    # 当结束上层循环说明，某个指针已经达到了该列表的长度，另一个列表还有多余的值需要全部传入新数组
    if left_pointer < len(left_li):
        # 也可以使用extend方法而不能使用append。
        # extend是将传入的列表挨个值放入列表，但是append是将整个放入
        result += left_li[left_pointer:]
    if right_pointer < len(right_li):
        result += right_li[right_pointer:]
    return result


if __name__ == '__main__':
    li = [1, 3, 65, 6, 4, 23, 65, 87, 5, 3, 3, 7, 7, 4, 3, 237, 9, 9865, 3, 2, 57]
    print(merge_sort(li))
```

### 复杂度

| 排序名称 | 平均时间复杂度 | 最好情况下 | 最坏情况下 | 空间复杂度 | 是否稳定 |
| -------- | :------------: | :--------: | :--------: | :--------: | :------: |
| 归并排序 |    O(nlogn)    |  O(nlogn)  |  O(nlogn)  |    O(n)    |   稳定   |

## 六、希尔排序

### 基本思路

​		给定一个间隔，然后在列表上根据间隔的个数先排列，然后循环直到该间隔全部排完。等该间隔完了以后缩小间隔继续循环

​		细化：假设初始间隔为4，该指针从该间隔开始到数组末尾进行判断，如果该指针所指向的值小于该指针的大小减去间隔*n的值，则将两个位置进行交换。重复上诉操做，然后间隔减一变成3，继续上面的操作，直到间隔为0完成排序

### 代码实现

```python
# -*- coding: utf-8 -*-


def shell_sort(alist):
    n = len(alist)
    gap = 4
    while gap > 0:
        for i in range(gap, n):
            tmp = alist[i]
            j = i
            while j >= gap and alist[j - gap] > tmp:
                alist[j] = alist[j - gap]
                j -= gap
            alist[j] = tmp
        gap -= 1


# 新的思路，即不指定gap的大小，而是由n决定，根据1,4,13来一次一次的改变，
def Knuth_shell_sort(alist):
    # h=1 h=3*h+1 ...
    n = len(alist)
    h = 1
    while h < n/3:
        h = 3*h+1
    gap = h
    while gap > 0:
        for i in range(gap, n):
            temp = alist[i]
            j = i
            while j >= gap and alist[j - gap] > temp:
                alist[j] = alist[j - gap]
                j -= gap
            alist[j] = temp
        gap = int((gap-1)/3)


if __name__ == '__main__':
    li = [1, 3, 6, 5, 4, 43, 7, 9, 7, 54, 3, 6, 9, 7, 5, 3, 6, 9, 65, 3, 43, 7, 4, 3, 5, 87, 54, 4, 7, 96]
    shell_sort(li)
    print("普通希尔排序：")
    print(li)
    li = [1, 3, 6, 5, 4, 43, 7, 9, 7, 54, 3, 6, 9, 7, 5, 3, 6, 9, 65, 3, 43, 7, 4, 3, 5, 87, 54, 4, 7, 96]
    Knuth_shell_sort(li)
    print("Knuth希尔排序：")
    print(li)

```

### 复杂度

| 排序名称 |  平均时间复杂度   |  最好情况下  | 最坏情况下 | 空间复杂度 | 是否稳定 |
| -------- | :---------------: | :----------: | :--------: | :--------: | :------: |
| 归并排序 | O(nlogn)~O($n^2$) | O($n^{1.3}$) |  O($n^2$)  |    O(1)    |  不稳定  |

## 总结

| 排序名称 |  平均时间复杂度   |  最好情况下  | 最坏情况下 |  空间复杂度  | 是否稳定 |
| -------- | :---------------: | :----------: | :--------: | :----------: | :------: |
| 冒泡排序 |     O($n^2$)      |     O(n)     |  O($n^2$)  |     O(1)     |   稳定   |
| 选择排序 |     O($n^2$)      |   O($n^2$)   |  O($n^2$)  |     O(1)     |  不稳定  |
| 插入排序 |     O($n^2$)      |     O(n)     |  O($n^2$)  |     O(1)     |   稳定   |
| 快速排序 |     O(nlogn)      |   O(nlogn)   |  O($n^2$)  | O(logn)~O(n) |  不稳定  |
| 归并排序 |     O(nlogn)      |   O(nlogn)   |  O(nlogn)  |     O(n)     |   稳定   |
| 归并排序 | O(nlogn)~O($n^2$) | O($n^{1.3}$) |  O($n^2$)  |     O(1)     |  不稳定  |