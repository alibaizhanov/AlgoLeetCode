##https://leetcode.com/problems/degree-of-an-array/discuss/108647/Python-O(n)-concise-with-explanation-(two-approaches)

class Solution(object):
    def findShortestSubArray(self, nums):
        nums_map, deg, min_len = collections.defaultdict(list), 0, float('inf')
        for index, num in enumerate(nums):
            nums_map[num].append(index)
            deg = max(deg, len(nums_map[num]))
        for num, indices in nums_map.items():
            if len(indices) == deg:
                min_len = min(min_len, indices[-1] - indices[0] + 1)
        return min_len