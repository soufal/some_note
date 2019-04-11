
def getRes_HashMap(nums, target):
    result = []
    for i, value in enumerate(nums):
        if (target - value) in nums[i+1:]:
            result.append((value, target - value))
    return result

if __name__ == "__main__":
    len_nums = int(input())
    nums = [int(i) for i in input().split()]
    nums = sorted(nums)
    target = int(input())
    result = getRes_HashMap(nums, target)
    if len(result) != 0:
    	for i in result:
    		print(str(i).replace(',','').lstrip('(').rstrip(')'))
    else:
    	print('NULL\n')

