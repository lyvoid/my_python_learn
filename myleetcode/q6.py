class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if s == "":
            return ""
        if numRows == 1:
            return s
        result_list = []
        len_s = len(s)
        max_col = len_s // (numRows - 1) + 1
        for row in range(numRows):
            if row == 0 or row == numRows - 1:
                for col in range(max_col):
                    order = 2 * (numRows - 1) * col + row
                    if order < len_s:
                        result_list.append(s[order])
                    else:
                        break
                continue
            for col in range(max_col):
                order = 2 * (numRows - 1) * col + row
                if order < len_s:
                    result_list.append(s[order])
                else:
                    break
                order = 2 * (numRows - 1) * col + row + 2 * (numRows - row - 1)
                if order < len_s:
                    result_list.append(s[order])
                else:
                    break
        return "".join(result_list)


s = "PAYPALISHIRING"
numRows = 4
print(Solution().convert(s, numRows))