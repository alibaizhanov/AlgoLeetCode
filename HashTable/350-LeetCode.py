##Best Solution https://leetcode.com/problems/intersection-of-two-arrays-ii/discuss/82241/ac-solution-using-java-hashmap

class Solution(object):
    def intersect(self, nums1, nums2):
        
        hashDict = dict()
        result = []
        
        for i in range(len(nums1)):
            
            if hashDict.get(nums1[i])!=None:
                hashDict[nums1[i]] = hashDict.get(nums1[i]) + 1
            else:
                hashDict[nums1[i]]=1
            
        
        for j in range(len(nums2)):
            
            if hashDict.get(nums2[j])!=None and hashDict.get(nums2[j])>0:
                result.append(nums2[j])
                hashDict[nums2[j]] = hashDict.get(nums2[j])-1
        
        return result