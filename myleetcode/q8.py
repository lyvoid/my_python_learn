class Solution:
    def myAtoi(self, str_):
        """
        :type str: str
        :rtype: int
        """
        max_po_int = [2, 1, 4, 7, 4, 8, 3, 6, 4, 8]
        max_po_int_len = len(max_po_int)
        str_ = str_.strip()
        zero_ord = ord('0')
        nine_ord = ord('9')
        is_op = False
        if str_.startswith('-'):
            is_op = True
            str_ = str_[1:]
        elif str_.startswith('+'):
            str_ = str_[1:]
        if str_ == "":
            return 0
        if not zero_ord <= ord(str_[0]) <= nine_ord:
            return 0
        i = 0
        result = 0
        is_overflow = False
        is_pending = True
        result_len = 0
        while i < len(str_) and zero_ord <= ord(str_[i]) <= nine_ord:
            cur_num = ord(str_[i]) - 48
            if result_len > 0:
                result_len += 1
            if result_len == 0 and cur_num != 0:
                result_len += 1
            if max_po_int_len < result_len:
                is_overflow = True
                break
            if max_po_int_len == result_len:
                if (cur_num >= 8 and is_op) or (cur_num >= 7 and not is_op):
                    if is_pending:
                        is_overflow = True
                        break
            if is_pending and cur_num != max_po_int[i]:
                is_pending = False
                if cur_num > max_po_int[i]:
                    is_overflow = True
            result = result * 10 + cur_num
            i += 1
        if result_len < max_po_int_len:
            is_overflow = False
        if is_overflow:
            return -2147483648 if is_op else 2147483647
        return -result if is_op else result


print(Solution().myAtoi("2147483646"))
