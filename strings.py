# s = ""

# length_of_string = 0

# for letter in s:
#     length_of_string += 1

# print(length_of_string)

#Program to search for a char in a string

    
#print(find_index_of_char_in_string("geeksforgeeks", "z"))

#Program t check if a string is a substring of another

# def substring_check(txt, pat):
#     length_of_string = len(txt)
#     length_of_substring = len(pat)
    
#     for i in range(length_of_string):
#         total_letters_matched = 0
#         while total_letters_matched < length_of_substring and txt[i + total_letters_matched] == pat[total_letters_matched]:
#             total_letters_matched += 1
        
#         if total_letters_matched == length_of_substring:
#             return i
    
#     return -1

# print(substring_check("geeksforgeeks", "xyz"))

#Insert a char in string at a given position

# def insert_char_into_str(s, c, pos):
#     new_string = s[0:pos] + c + s[pos:]
#     return new_string

# print(insert_char_into_str("HelloWorld", "!", 5))

# Deleting of char in string

# def del_char(str, pos):
#     deleted_char = str[pos]
#     new_str = ""
#     for character in str:
#         if character != deleted_char:
#             new_str += character
    
#     return new_str

# print(del_char("HelloWorld", 0))

# Reverse a string

# string = "Hello"

# print(string[::-1])


# def left_rotation(s, d):
#     new_string = ""
#     for letter in s[d:]:
#         new_string += letter
#     new_string = new_string + s[0:d] 
#     return new_string
# print(left_rotation("qwertyu", 2))

# class Solution(object):
#     def isPalindrome(self, s):
#         self.s = s
#         self.b = "".join(char for char in self.s if char.isalnum()).lower()
#         print(self.b)
        
#         left = 0
#         right = len(self.b) - 1
#         while left < right:
            
#             if self.b[left] != self.b[right]:
#                 return False
        
#             left += 1
#             right -= 1
#         return True
        
        
# new = Solution()
# print(new.isPalindrome("A man, a plan, a canal: Panama"))
# s = "python is the best"
# s.replace("best", "worst")
# print(s)

# import collections

# q = collections.deque()

# q.append(10)
# q.append(20)
# q.append(15)
# print(q)
# print(len(q))



#String slicing
# s = "GeeksforGeeks"
# print(s[1:4])
# print(s[:3])
# print(s[3:])
# print(s[::-1])






#string iteration
# s = "Python"
# for char in s:
#     print(char)


#update a string
# s = "hello ge eks"
# # s = "H" + s[1:]
# # print(s)
# # s2 = s.replace("geeks", "Geeks")
# # print(s2)





# #length
# print(s.replace(" ", ""))
# def find_length(s):
#     return len(s)

# print(find_length("abc"))
# print(find_length("GeeksforGeeks"))
# print(find_length(""))

# def search_char(ch, s):
    # if ch in s:
    #     return s.index(ch)
    # else:
    #     return -1
    
#     for i in range(len(s)):
#         if s[i] == ch:
#             return i
#     return -1
    
# print(search_char("k", "geeksforgeeks"))
# def is_substring(txt, pat):
#     pat = pat.lower().replace(" ", "")
#     if pat in txt:
#         return txt.index(pat)
#     else:
#         return -1
    
# print(is_substring("geeksforgeeks", "F O R"))

# def insert_into_string(s, c,pos):
#     s = s[:pos] + c + s[pos:]
#     return s

# print(insert_into_string("Geeks", "A", 3))
# print(insert_into_string("HelloWorld", "!", 5))

# def delete_char(str, pos):
#     return str[:pos] + str[pos +1:]

# print(delete_char("GeeksforGeeks", 5))
# print(delete_char("HelloWorld", 0))

# def check_if_same(s1, s2):
#     if s1 == s2:
#         return "Yes"
#     else:
#         return "No"

# print(check_if_same("abc", "abc"))
# print(check_if_same("", ""))
# print(check_if_same("GeeksforGeeks", "Geeks"))

# def reverse_string(s):
#     stack = []
#     reversed_string = ""
#     for char in s:
#         stack.append(char)
 
#     while len(stack) > 0:
#         reversed_string += stack.pop()
        
#     return reversed_string
    
# print(reverse_string("abcd"))

def rotate_string(s, d):
    rotated_string = s[d:] + s[:d]
    return rotated_string

print(rotate_string("qwertyu", 2))