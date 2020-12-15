# Leetcode重复元素相似题解法

题目链接：

#### [217. 存在重复元素](https://leetcode-cn.com/problems/contains-duplicate/)

#### [219. 存在重复元素 II](https://leetcode-cn.com/problems/contains-duplicate-ii/)

#### [220. 存在重复元素 III](https://leetcode-cn.com/problems/contains-duplicate-iii/)

## 一、重复元素I

**题目**：

给定一个整数数组，判断是否存在重复元素。如果任意一值在数组中出现至少两次，函数返回 `true` 。如果数组中每个元素都不相同，则返回 `false` 。

**解法**：

该题的解题方法比较多，这里列举三种：

### 1.1 利用list函数

我们只需要先判断该元素是否存在list集合中，如果存在，直接直接返回false，如果不存在，那么将这个数添加到list的末尾，进行下一个判断，但是需要注意一点，list的in的查找时间复杂度为O(1)，因此在整个代码的时间复杂度为O($N^2$)，当输入的值较大时，可能会超时

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = []
        for i in nums:
            if i not in a:
                a.append(i)
            else:
                return True
        return False
```

因此，这种方法不推荐

### 1.2 利用set函数

我们知道，set函数的存储方式与list不同，list是通过线型存储，所有元素在内存中地址连续，如果要查找一个元素，就直接从第一个遍历到最后一个，如果有这个元素就返回True。但是set在python中是用hash实现，因此查找的时间的复杂度直接从O（N）降到O（1）。这样整个代码的时间复杂度就直接降到O（N）。以下就是利用set改进list的代码

```python
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = set()
        for i in nums:
            if i not in a:
                a.add(i)
            else:
                return True
        return False
```

但是别忘了，set还自带去重功能，因此我们只需要将传入的数组经过转换变成set，然后在判断转换后set的长度与原先的list是否相同即可。因此代码也只用一行即可

```python
def containsDuplicate(self, nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)
```

### 1.3 利用字典

字典是一个通过键值对保存的数据结构，并且字典的查找事件复杂度也为0（1）。因此我们可以将元素作为键入，然后在依次查看后面的元素是否存在字典中即可。

```python
def containsDuplicate(self, nums: List[int]) -> bool:
    hash_map = {}
    for i in nums:
        if i in hash_map:
            return True
      	else:
            hash_map(i) = 0 # 后面的值随便取
    return False
```

## 二、重复元素II

**题目**：

给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。

**解法**：

该题同样有至少三种解法，原理与I差不多，只是在原来的基础上添加一个滑动窗口，只需要在这个滑动窗口内判断是否有重复元素即可。

### 2.1 list解法

用list的思路大致是这样的，先创建一个滑动窗口，在窗口内预先放入nums的前k+1个数。然后在依次利用set去重功能判断这个窗口是否符合长度不相等这个条件即可。

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
		k += 1
        
        def check(win):
            return len(win) != len(set(win))
        window = nums[:k]
        if check(window):  # 判断第一个窗口是否符合要求
            return True
        for i in range(k, len(nums)):
            window.append(nums[i])
            window = window[1:]
            if check(window):
                return True
        return False
```

这个方法有一个缺陷，即列表在删除头元素的时候，后面的元素会依次往前放，这样列表的删除头元素操作的时间复杂度就达到了O（N），也会因此大大提高整个的时间复杂度，因此这样的方法在提交的时候一般都是超时的。那么就直接利用set来拯救一下代码吧

### 2.2 set解法

set解法与list稍微有些不同，因为list方法主要靠的是set函数的间接去重法，但是入果直接使用set的话，那就不能一开始就直接放入，需要从第一个元素开始，依次判断该元素是否存在set函数内，如果存在，那么就返回True，如果不存在，先将该元素加入到set内，然后判断整个set长度是否大于k，如果大于，那就将头元素去掉即可。

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for i in range(len(nums)):
            if nums[i] in window:
                return True
            window.add(nums[i])
            if len(window) > k:
                window.remove(nums[i-k])
        return False
```

### 2.3 字典解法

字典与前面不同的是，这里不再使用滑动窗口，而是改用下标直接判断，第一步也是从第一个元素开始往后，如果该元素存在字典里，那就返回True，如果不存在，那么直接在字典中按照该值与该值的下标进行存储即可。

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in hash_map and i - hash_map[num] <= k:
                return True
            else:
                hash_map[num] = i
        return False
```

## 三、重复元素III

**题目**：

在整数数组 nums 中，是否存在两个下标 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值小于等于 t ，且满足 i 和 j 的差的绝对值也小于等于 ķ 。如果存在则返回 true，不存在返回 false。

**题解**：

该题的大致思路还是与第二题差不多，之不过判断条件语句需要进行变换，这里就只取一个例子，同样是滑动窗口，利用set函数达到效果。

先看代码：

```python
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # set
        window = set()
        for i in range(len(nums)):
            num = nums[i]
            if t == 0:
                if num in window:
                    return True
            else:
                if num in window or i > k and len(window) < k:
                    return True
                for j in window:
                    if num-t <= j <= num+t:
                        return True
            window.add(num)
            if len(window) > k:
                window.remove(nums[i-k])
        return False
```

上面的代码与题目二主要差别的地方就在需要在窗口内进行再次判断。如果窗口内的每一个值都不在num的[-t,t]范围内，则进入下个循环，如果存在，那么直接返回True即可，这里还有一个需要注意的是，如果t是0，那就直接是第二题的解题思路，也用来规避例题中10000长度的“bt”。