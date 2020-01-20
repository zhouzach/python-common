nums = [0,1,2,3,4,5,6,7,8,9]
print(nums[-1])

nums1=nums[2:5]
print(nums1)

nums2=nums[:5]
print(nums2)

nums3=nums[3:]
print(nums3)

nums4=nums[3:-1]
print(nums4)

#从索引位置3开始，以步长-1开始反向遍历列表
nums5=nums[3::-1]
print(nums5)

#从索引位置5开始，以步长2开始正向遍历列表
nums6=nums[5::2]
print(nums6)

nums7=nums[::3]
print(nums7)

