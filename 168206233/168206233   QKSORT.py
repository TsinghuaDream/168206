#coding:utf-8

def partion(nums,left,right):
    key = nums[left]
    while left < right:
        # right下标位置开始，向左边遍历，查找不大于基准数的元素
        while left < right and nums[right] >= key:
            right -= 1
        if left < right:  # 找到小于准基数key的元素,然后交换nums[left],nums[right]
            nums[left],nums[right] = nums[right],nums[left]
        else:   # left〉=right 跳出循环
            break
        # left下标位置开始，向右边遍历，查找不小于基准数的元素
        while left < right and nums[left] < key:
            left += 1
        if left < right:  # 找到比基准数大的元素，然后交换nums[left],nums[right]
            nums[right],nums[left] = nums[left],nums[right]
        else: # left〉=right 跳出循环
            break
    return left  #此时left==right 所以返回right也是可以的

#realize from book "data struct" of author 严蔚敏
def quick_sort_standord(nums,left,right):
    if left < right:
        key_index = partion(nums,left,right)
        quick_sort_standord(nums,left,key_index)
        quick_sort_standord(nums,key_index+1,right)

if __name__ == '__main__':
    nums = [5, 6, 4, 2, 3,1]
    print nums
    quick_sort_standord(nums,0,len(nums)-1)
    print nums
