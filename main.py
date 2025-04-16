from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    # YOUR ANSWER
    result: List[int] = [0, 0]
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if (nums[i] + nums[j] == target):
                result[0] = i
                result[1] = j
    return result