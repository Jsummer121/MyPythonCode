# 两数之和

Leetcode链接：[两数之和](https://leetcode-cn.com/problems/two-sum/)

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

##### 示例

```
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
```

## 方法一、

第一种方法，不多说可以直接暴力搜索（但是基本上会超时的）：

1. 第一个指针，从第一个元素到最后一个元素，
2. 第二个指针从当前指针下一个元素到最后一个元素
3. 一次判断第一个指针所指向的值与第二个指针指向的值相加所得到的值是否为target，如果是，则返回两个数字的下标，如果不是则继续寻找

从上面可以清楚的看出当前代码的时间复杂度为O($n^2$)。如果把这行代码带进去，一般输入10**5长度的列表，每个把小时出不来答案，因此这个代码看看就好，不用太多在意

```python
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Len = len(nums)
        for i in range(Len):
            for j in range(i+1,Len):
                if nums[i] + nums[j] == target:
                    return [i,j]
```

今天提交了代码，这暴力解法的居然都能通过了，莫名奇怪。

## 方法二、

第二种方法是添加一个hash表，用来存储已经查找过的元素和当前元素的下标。此时需要引用enumerate函数，来生成包含元素和元素下标的一个列表。因为我们知道字典的查找速度为O(1)，因此我们可以把整个时间复杂度从O($n^2$)下降到O(1)。整个思想方法如下：

1. 从第一个元素开始查找到最后一个元素
2. 获取target-该元素的值，如果这个值存在hash表中，则返回这俩数的下表
3. 如果不存在，则把该值作为键，把该值的下表作为值存入表中。

```python
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None
```







