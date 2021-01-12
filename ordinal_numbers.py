ordinal_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for nums in ordinal_nums:
    if nums == 1:
        print(str(nums) + 'st')
    elif nums == 2:
        print(str(nums) + 'nd')
    elif nums == 3:
        print(str(nums) + 'rd')
    else:
        print(str(nums) + 'th')