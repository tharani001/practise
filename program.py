print("Hello World")
import sys
x = range(1000)
print(sys.getsizeof(x)) 

print(x)
print(1,1,2,3,4,sep="&")

mylist = [1,2,3,4,5]
print(mylist)
print(*mylist)
print(*mylist,sep="&")
print(pow(3,2,3)) # x**y%z

#Data Types
num = 3
print(num, type(num))
num1 = 3.1
print(num1, type(num1))
num2 = True
print(num2, type(num2))
num3 = "anime"
print(num3, type(num3))
num4 = 3+3j
print(num4, type(num4))
num5 = ""
print(num5, type(num5))

#Typecasting
num6 = ""
print(bool(num6))
num7 = " "
print(bool(num7))

#Strings
name = """
Tharani got no "chill" """
print(name)

# Python strings are immutable; python string methods don't modify the original string

#capitalize
txt = "Strings are immutable"
capitalized_str = txt.capitalize()
print(capitalized_str)

#count
txt1 = """Python is a high level interpreted programming language meaning that it executes the code line by line.
Python is an object oriented programming language.
Python is a dynamically typed language.
"""
word_count = txt1.count("Python")
print(word_count) # doesn't count overlapped substring


#find
print(txt1.find("Python"))

#format
txt2 = "Python is a {} level interpreted {} language meaning that it executes the code line by line."
print("\n",txt2.format("high","Programming"))

#isalpha
print(txt2.isalpha()) # Spaces are not allowed.

#isalnum
print(txt2.isalnum())

#isnumeric
nums = "123445 "
print(nums.isnumeric()) # Spaces are not allowed.

#isupper
print(txt.isupper())

#islower
print(txt.islower())

#upper
print(txt.upper())

#lower
print(txt.lower())

#title
print(txt.title())

#swapcase
print(txt.swapcase())

#split
print(txt.split())

#join
print(" ".join(txt.split()))

#replace
print(txt.replace("Strings", "Python Strings"))

#string slicing
# Forward slicing: start < end
print(txt[:2])
print(txt[-5:-2])

#backward slicing: start > end
print(txt[::-1])
print(txt[8:2:-1])
print(txt[-2:-9:-2])

#tuple
tup  = (1,)
print(tup, type(tup))

mytup = (1,2,3,4)

it,it1,*it2 = mytup
print(it,it1)
print(*it2)

print(mytup+(4,))
print(mytup*4)

a = 0
b = 1

for num in range(10):
    print(a)
    c = a+b
    a = b
    b = c 


string1 = "genai is the future"

result  =""
for idx in range(len(string1)-1, -1,-1):
    result += string1[idx]
print(result)

print(string1[::-1])

nums = [11,1,1,1,23,4,23,45,45]

print(list(set(nums))) # order is not preserved

print(list(dict.fromkeys(nums))) # dictionary method preserves the order

dups = []

unique = set()

for num in nums:
    if num not in unique:
        unique.add(num)
    else:
        dups.append(num)

print(list(unique)) # didn't preserve the order

print(sorted(nums)[-2])

print(sorted(list(dict.fromkeys(nums)))[-2]) # remove the duplicates first


print(list(dict.fromkeys(nums,12)))

dic = {"adf":12, "fd":23}

print(list(dic))

n = 13
flag = True
for nums in range(2,n):
    if n % nums == 0:
        flag =  False
        break
    else:
        continue
if flag:
    print("prime")
else:
    print("Composite")

count = 0
for num in range(1,n+1):
    if n%num == 0:
        count += 1
if count == 2:
    print("Prime")
else:
    print("Composite")

nums = [11,1,1,1,23,4,23,45,45]

freq = {}

for num in nums:
    if num not in freq:
        freq[num] = 1
    else:
        freq[num] += 1
print(freq)

from collections import Counter

print(dict(Counter(nums)))

print(dic)
print(max(dic, key=dic.get))
print(min(dic, key=dic.get))
print(dict(sorted(dic.items(),key=lambda x: x[1],reverse=True)))
print({v:k for k,v in dic.items()})

import random
print(random.choices([1,2,3,4,5],weights=[num for num in range(5)],k = 2))
print(random.choice([1,2,3,4,5]))

# Count overlapped substring
ipt_str = "bababcq"
substring = "bab"

count = 0
for idx in range(len(ipt_str)-len(substring)+1):
    if ipt_str[idx:(idx + len(substring))] == substring:
        count += 1

print(count)

from PIL import Image

img = Image.open("sample_img.jpg").convert("RGB")

width, height = img.size

pixels = img.load()


for py in range(height):
    for px in range(width):
        r,g,b = img.getpixel((px,py))
        newr = g
        newg = r
        newb = 0
        pixels[px,py] = (newr, newg, newb)
# img.show()


# The rate at which the time taken increases with respect to input size is called Time complexity.

n = 1 # O(1) ---  Constant Time complexity

# O(n) is the time complexity while looping through an iterable
# O(n) is the time complexity while doing `LINEAR` search
# O(log n) is the time complexity while doing `BINARY` search
# O(2**n) is the time complexity while doing recursion.
# O(n!) is the worst time complexity program.

# O(n**2) is the time complexity while using nested loops

# O(N**2) Time complexity
nums = [2,7,11,15]
target = 9
for idx in range(len(nums)):
    for idy in range(idx+1, len(nums)):
        if nums[idx] + nums[idy] == target:
            print(idx, idy)
            break


# O(N) Time complexity
for idx in range(len(nums)):
    num1 = target - nums[idx]
    if num1 in nums and idx != nums.index(num1):
        print(idx, nums.index(num1))
        break


# Recursion -  it calls itself. When a function hits the return, it gets terminated automatically.

# Base case is something which terminates the function.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))


def sum_of_n(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_n(n-1)
print(sum_of_n(10))

from itertools import permutations

sample = "ABC"

print(list(permutations(sample)))

print(["".join(x) for x in list(permutations(sample))])
print(["".join(("10","12"))])


# def fib(n):

#     if n == 1 or n == 0:
#         return n
#     else:
#         return fib(n-2) + fib(n-1)

# print(fib(12))

# Dynamic Programming is used when there is a overlapping subproblem

# Memoization is a technique where we store the results of expensive function calls in a dictionary (cache) so that when the same inputs occur again, we can retrieve the result instantly instead of recalculating.

memo = {}

def fibo(n):
    if n in memo:
        return memo[n]
    if n == 1 or n == 0:
        value = n
    else:
        value = fibo(n-1) + fibo(n-2)
    memo[n] = value
    return value

print(fibo(12))


nums = 1234

num_list = [num for num in str(nums)]
print(int("".join(num_list[::-1])))

# Palindrome string reads the same forward and backward.
chk_str = "amma"

def chk_palindrome(str):
    for idx in range(0,len(str)//2):
        if str[idx] != str[len(str)-1-idx]:
            return "Not a palindrome"
    return "palindrome"

print(chk_palindrome(chk_str))


# Longest common subsequence -  Subsequence means characters must appear in same order but do not need to be consecutive.

A = "eg"
B = "efgh"

def lcs(i,j):
    if i == 0 or j == 0:
        return 0
    elif A[i-1] == B[j-1]:
        return 1 + lcs(i-1,j-1)
    else:
        return max(lcs(i-1,j), lcs(i,j-1))

print(lcs(len(A), len(B)))

# Memoization is a technique to speed up the program by storing the results in a place before the function calls.

memo = {}

def lcs_memo(i,j):
    k = str(i) + str(j)
    if k in memo:
        return memo[k]
    if i == 0 or j == 0:
        return 0
    elif A[i-1] == B[j-1]:
       value = 1 + lcs_memo(i-1,j-1)
    else:
        value =  max(lcs_memo(i-1,j), lcs_memo(i,j-1))
        memo[k] = value
    return value
print(lcs_memo(len(A), len(B)))


grid = [
    [1,2,4],
    [2,4,5],
    [4,7,9]
]
rows = len(grid)
cols = len(grid[0])

print([[0 for col in range(cols)] for row in range(rows)])

# Linear search time complexity is O(N)

# Binary search is an effective technique whose time complexity is O(log n)

# Binary search is applied on sorted arrays ONLY.

sorted_arr = [1,2,4,7.9,10]
left = 0
right = len(sorted_arr) - 1

target = 7.9
def binary_search(arr):
    global left, right
    while left <= right:
        mid = (left + right) // 2

        if sorted_arr[mid] == target:
            return mid
        elif sorted_arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
print(binary_search(sorted_arr))

# if you want to modify something inside a function, you must ensure it's local or explicitly tell Python to use a global/nonlocal variable! 

# Peak index in a mountain array

mountain_arr = [12,23,45,67,98,78,72,61,42,31,22,10]

print(mountain_arr.index(max(mountain_arr))) # index of peak element

for idx in range(len(mountain_arr)):
    if mountain_arr[idx+1] < mountain_arr[idx]:
        print(idx)
        break

def peakIndex(arr):
    left = 0
    right = len(arr)-1

    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid+1]:  # Peak is on the left
            right = mid
        else:  # Peak is on the right
            left = mid + 1
            
    return left  # or return right (both are same at the end)

print(peakIndex(mountain_arr))


# Count Frequency
#Method -  1
freq = [1,2,2,2,4,1]
num_counts = {}
for num in freq:
    num_counts[num] = freq.count(num)
print(num_counts)

# Method - 2
count_freqs = {}

nums = [12,2,3,4,2,34,4]
for num in nums:
    if num not in count_freqs:
        count_freqs[num] = 1
    else:
        count_freqs[num] += 1
print(count_freqs)

# Method - 3 

from collections import Counter

print(dict(Counter(nums)))
