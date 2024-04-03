from typing import List


class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        total = sum(nums)
        if total % k != 0:
            return False
        ptr = 0
        while ptr < nums.__len__():
            if nums[ptr] == 0:
                ptr += 1
                continue
            if nums[ptr] < 0:
                return False
            else:
                if nums.__len__() - ptr < k:
                    return False
                temp = nums[ptr]
                # del from nums[ptr]
                have_next = False
                next_ptr = ptr
                for i in range(k):
                    nums[ptr + i] -= temp
                    if nums[ptr + i] < 0:
                        return False
                    elif nums[ptr + i] > 0:
                        if not have_next:
                            next_ptr = ptr + i
                            have_next = True
                ptr = next_ptr
        return True
