from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        ans = [folder[0]]
        for i in range(1, folder.__len__()):
            if folder[i].__len__() <= ans[-1].__len__():
                ans.append(folder[i])
                continue
            if folder[i][:ans[-1].__len__()] == ans[-1] and folder[i][ans[-1].__len__()] == '/':
                # is sub-folder
                continue
            else:  # is next folder
                ans.append(folder[i])
        return ans


print(Solution().removeSubfolders(folder=["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]))
print(Solution().removeSubfolders(folder=["/a", "/a/b/c", "/a/b/d"]))
print(Solution().removeSubfolders(folder=["/a/b/c", "/a/b/ca", "/a/b/d"]))
