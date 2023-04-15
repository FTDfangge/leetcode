from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort_get_ans_count(num_list: List[int], left, right) -> int:
            if left >= right:
                return 0
            else:
                mid = (left + right) // 2
                ans = merge_sort_get_ans_count(num_list, left, mid) + merge_sort_get_ans_count(num_list, mid + 1, right)
                temp = []
                l_ptr = left
                r_ptr = mid + 1
                while l_ptr <= mid and r_ptr <= right:
                    if num_list[l_ptr] <= num_list[r_ptr]:
                        ans += r_ptr - mid - 1
                        temp.append(num_list[l_ptr])
                        l_ptr += 1
                        continue
                    else:
                        temp.append(num_list[r_ptr])
                        r_ptr += 1
                        continue

                while l_ptr <= mid:
                    if num_list[l_ptr] > num_list[r_ptr - 1]:
                        ans += r_ptr - mid - 1
                    temp.append(num_list[l_ptr])
                    l_ptr += 1

                while r_ptr <= right:
                    temp.append(num_list[r_ptr])
                    r_ptr += 1
                num_list[left:right + 1] = temp
                return ans

        return merge_sort_get_ans_count(nums, 0, nums.__len__() - 1)


print(Solution().reversePairs([7, 6, 5, 4]) == 6)
print(Solution().reversePairs([7, 5, 6, 4]) == 5)
print(Solution().reversePairs([5, 5, 5, 5]) == 0)
print(Solution().reversePairs([1, 2, 1, 2, 1]) == 3)
