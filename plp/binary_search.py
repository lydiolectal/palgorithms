import unittest

def search_insert(nums, target):
    low = 0
    high = len(nums)
    while low != high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            high = mid
        else:
            low = mid + 1
    return low

# finds the index i of an element such that nums[i] > nums[i-1], nums[1+1]
# if there are multiple peaks, it doesn't matter which one we return
# assumes that there is such a peak
def peak_element(nums):
    return peak_helper(nums, 0, len(nums))

def peak_helper(nums, low, high):
    mid = (low + high) // 2
    if low == high:
        return False
    if is_peak(nums, mid):
        return mid
    # go left
    elif mid == len(nums) - 1 or nums[mid - 1] > nums[mid]:
        return peak_helper(nums, low, mid)
    # go right
    else:
        return peak_helper(nums, mid + 1, high)

def is_peak(nums, i):
    if i == 0 or nums[i-1] < nums[i]:
        if i == len(nums) - 1 or nums [i+1] < nums[i]:
            return True
    return False

class TestFriendCircle(unittest.TestCase):

    def test_not_found(self):
        nums = [1,3,5,6]
        target = 7
        self.assertEqual(search_insert(nums, target), 4)

    def test_peak_element(self):
        nums = [1,2,3,1]
        self.assertIn(peak_element(nums), [2])

        nums = [1,2,1,3,5,6,4]
        self.assertIn(peak_element(nums), [1, 5])
