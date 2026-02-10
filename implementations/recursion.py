# def sum_numbers(n):
#     if n == 0:
#         return 0
#     else:
#         return n + sum_numbers(n-1)

# print(sum_numbers(5))

# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
    
# print(fact(3))
count = 0
def collatz(n):
    global count
    if n <= 1:
        return 0
    elif n % 2 == 0:
        count +=1
        collatz(n/2) 