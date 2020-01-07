import unittest

def lengthOfLongestSubstring(s):
    substring_dictionary = {}
    substring = ""
    max_length = None

    if s == "":
        return 0

    if len(s) == 1:
        return 1

    else:
        for char in s:
            if char not in substring:
                substring += char

                print('substring ->', substring)
            else:
                substring_dictionary[substring] = len(substring)
                if char == substring[-1]:
                    substring = char
                else:
                    substring = substring[-1] + char
         
        substring_dictionary[substring] = len(substring)
   
        for item in substring_dictionary:
            if max_length == None:
                max_length = substring_dictionary[item]
            elif substring_dictionary[item] > max_length:
                max_length = substring_dictionary[item]

        return max_length
        

class TestFunction(unittest.TestCase):
    def test_meth(self):
        self.assertEqual(lengthOfLongestSubstring("pwwkew"),3)
        self.assertEqual(lengthOfLongestSubstring(" "),1)
        self.assertEqual(lengthOfLongestSubstring("ae"),2)
        self.assertEqual(lengthOfLongestSubstring("dvdf"),3)



if __name__ == "__main__":
    unittest.main()
