class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        mid_index = (len_nums1 + len_nums2) // 2 + 1
        indexes = [0, 0]
        if (len_nums1 + len_nums2) % 2 == 1:
            for i in range(mid_index):
                if i == mid_index - 1:
                    return self.get_min_next_num(nums1, nums2, indexes)
                self.get_min_next_num(nums1, nums2, indexes)
        else:
            before_value = 0
            for i in range(mid_index):
                if i == mid_index - 1:
                    return (self.get_min_next_num(nums1, nums2, indexes) + before_value) / 2
                before_value = self.get_min_next_num(nums1, nums2, indexes)


    def get_min_next_num(self, nums1, nums2, indexes):
        index1 = indexes[0]
        index2 = indexes[1]
        if index1 >= len(nums1) or (index2 < len(nums2) and nums1[index1] > nums2[index2]):
            indexes[1] += 1
            return nums2[index2]
        else:
            indexes[0] += 1
            return nums1[index1]


nums1_ =[1, 2]
nums2_ = [3, 4]
a = Solution()
print(a.findMedianSortedArrays(nums1_, nums2_))
nums1_ = [1, 3]
nums2_ = [2, 4, 5]
print(a.findMedianSortedArrays(nums1_, nums2_))
nums1_ = [1]
nums2_ = []
print(a.findMedianSortedArrays(nums1_, nums2_))