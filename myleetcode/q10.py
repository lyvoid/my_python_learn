class ReElement:
    def __init__(self, pattern: str):
        self.recur_times = 0
        self.match_end_pos = -1
        self.is_match_all = False
        if pattern.startswith("."):
            self.is_match_all = True
        self.is_match_many = False
        self.match_char = pattern[0]
        if pattern.endswith("*"):
            self.is_match_many = True
        self.next = None
        self.next_re_element = None

    def judge(self, c, pos):
        if self.is_match_all:
            result = True
        else:
            result = self.match_char == c
        self.next = self.next_re_element
        if result and self.is_match_many:
            self.next = self
        if result:
            self.match_end_pos = pos
        else:
            self.match_end_pos = pos - 1
        if self.is_match_many and result:
            self.recur_times += 1
        if self.is_match_many:
            return True
        return result

    def recur(self):
        self.match_end_pos -= 1
        self.recur_times -= 1

    def is_finished(self):
        if self.match_end_pos == -1 and not self.is_match_many:
            return False
        if self.next_re_element is None:
            return True
        cur_re = self
        while cur_re.next_re_element is not None:
            if not cur_re.next_re_element.is_match_many:
                return False
            cur_re = cur_re.next_re_element
        return True


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        first_re = None
        cur_elem = None
        for i in range(len(p)):
            before_elem = cur_elem
            if p[i] == '*':
                continue
            if i + 1 < len(p) and p[i+1] == '*':
                cur_elem = ReElement(p[i:i+2])
            else:
                cur_elem = ReElement(p[i])
            if before_elem is not None and \
                    cur_elem.is_match_many and \
                    cur_elem.match_char == before_elem.match_char and \
                    before_elem.is_match_many:
                cur_elem = before_elem
                continue
            if first_re is None:
                first_re = cur_elem
            if before_elem is not None:
                before_elem.next_re_element = cur_elem

        i = 0
        cur_re = first_re
        recur_stack = []
        while True:
            is_match = False
            if i < len(s):
                cur_char = s[i]
                if cur_re is not None:
                    is_match = cur_re.judge(cur_char, i)
                    i = cur_re.match_end_pos + 1
                    if cur_re.recur_times > 0 and cur_re not in recur_stack:
                        recur_stack.append(cur_re)

            if ((is_match and i == len(s)) or len(s) == 0) and (cur_re is None or cur_re.is_finished()):
                return True

            if not is_match:
                if len(recur_stack) == 0:
                    return False
                else:
                    recur_elem = recur_stack[-1]
                    recur_elem.recur()
                    cur_re = recur_elem.next_re_element
                    if recur_elem.recur_times == 0:
                        recur_stack.pop()
                    i = recur_elem.match_end_pos + 1
            else:
                cur_re = cur_re.next


print(Solution().isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*a*a*b"))
