# a = [1, 3, 5, 7, 9]

# for i in range(len(a)):
#     print(a[i])

# def print_list(lis1):
#     for element in lis1:
#         print(element, end=" ")
        
# print_list([324, 5, 2, 2])
# def sum_of_list(lis1):
#     sum = 0
#     for num in lis1:
#         sum += num
#     return sum

# print(sum_of_list([324, 5, 2, 2]))

def decrement_elements(lis1):
    lis2 = []
    for num in lis1:
        lis2.append(num-1)
        
    for num2 in lis2:
        print(num2, end=" ")

decrement_elements([54, 43, 2, 1, 5])