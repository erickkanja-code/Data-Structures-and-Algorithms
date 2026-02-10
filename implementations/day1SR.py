# s = "aabaa"
# for letter in s:
#     new_string = s.removeprefix(letter)
#     print(new_string)
#     if new_string == new_string[::-1]:
#         print("True")
#         break
#     else:
#         print("False")
s = "nurses run "
s = s.strip()
result = "FALSE"
for i in range(len(s)):
    new = s[:i] + s[i+1:]
    if new == new[::-1]:
        result = "TRUE"
        
        break
print(result)


