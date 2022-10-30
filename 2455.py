'''
2455. Average Value of Even Numbers That Are Divisible by Three
'''

def averageValue(nums) -> int:
    result = []
    for num in nums:
        if num %3 ==0 and num %2 ==0:
            result.append(num)
    
    return int(sum(result)/len(result)) if result else 0

print(averageValue(nums = [1,2,4,7,10,30,12,6]))