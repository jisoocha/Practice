# https://careercup.com/question?id=5931067269709824

# Given a string (1-d array) , find if there is any sub-sequence that repeats itself.
# Here, sub-sequence can be a non-contiguous pattern, with the same relative order.
#
# Eg:
#
# 1. abab <------yes, ab is repeated
# 2. abba <---- No, a and b follow different order
# 3. acbdaghfb <-------- yes there is a followed by b at two places
# 4. abcdacb <----- yes a followed by b twice
#
# The above should be applicable to ANY TWO (or every two) characters in the string and optimum over time.
#
# In the sense, it should be checked for every pair of characters in the string.
#


class Solution:
    def __init__(self):
        self.test_cases = [('abab', True),
                           ('abba', False),
                           ('acbdaghfb', True),
                           ('abcdacb', True)]

    def generate_character_pairs(self):
        characters = 'abcdefghijklmnopqrstuvwxyz'
        return [(l1, l2) for l1 in characters for l2 in characters]

    def sub_sequence_repeats(self, text):
        character_pairs = self.generate_character_pairs()

        for (l1, l2) in character_pairs:

            # s1: l1 ('a') detected, s2: l1 & l2 ('a..b') detected once
            s1, s2 = False, False

            for l in text:
                if not s1:
                    if l == l1:
                        s1 = True
                else:
                    if l == l2:
                        if not s2:
                            s1 = False
                            s2 = True
                        else:
                            return True
        return False

    def test(self):
        for test_case in self.test_cases:
            if self.sub_sequence_repeats(test_case[0]) != test_case[1]:
                return False
        return True


if __name__ == '__main__':
    print(Solution().test())