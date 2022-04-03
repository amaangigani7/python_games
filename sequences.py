# computer_parts = ["computer",
#                   "monitor",
#                   "keyboard",
#                   "mouse",
#                   "mouse mat"]


# for number, part in enumerate(computer_parts):
#     print(number, part)

# # Lists are iterable
#
# for part in computer_parts:
#     print(part)
#
# print(computer_parts[2])
# print(computer_parts[0:3]) # Forms another list
# print(computer_parts[-1])
#
# # Lists are mutable unlike strings
# shopping_list = ["eggs", "spam", "flour", "milk"]
# another_list = shopping_list
# print(id(shopping_list))
# print(id(another_list))
#
# shopping_list += ["cookies"]
# print(id(shopping_list))
# print(another_list)
# result = True
# another_result = result
# print(id(result))
# print(id(another_result))
#
# result = False
# print(id(result))

# even = [2, 4, 6, 8]
# odd = []
# for i in range(0, 10):
#     if i % 2 != 0:
#         odd.append(i)
#
# even.extend(odd)
# even.sort(reverse=True)
# print(even)

# print("mississipi".count('s'))


# current_choice = "-"
# computer_parts = []
#
# while current_choice != "0":
#     if current_choice in '12345':
#         print("Adding {}".format(current_choice))
#         if current_choice == '1':
#             computer_parts.append("computer")
#     else:
#         print("Please enter a number.")
#         print("1: Computer")
#         print("2: monitor")
#         print("3: keyboard")
#         print("4: mouse")
#
#     current_choice = input()
#
# print(computer_parts)
# equivalent = ''
#
# i = 15
# a = i - 9
# a = 64 + a
# equivalent += chr(a)
# print(equivalent)

# inp = "move-hyphens-to-front"
# count = 0
# final = ""
# for i in inp:
#     if i == '-':
#         count += 1
#     else:
#         final += i
# print("-"*count, final)

# for index, char in enumerate('abcdefgh'):
#     print(index, char)

# pangram = "The quick brown fox jumps over the lazy dog"
#
# # returns a list
# print(sorted(pangram, key=str.casefold))
#
# numbers = [10.3, 1.2, 4.5, 9.8]
# numbers.sort()
# print(numbers)

# digits = sorted('457821369')
# print(digits)
#
# for index, value in enumerate(digits):
#     if value >= 1:
#         stop = index
#         break
#
# print(stop)
# del digits[]


# def no_of_carries(num1, num2):
#     if num1 == 0 and num2 == 0:
#         return 0
#     carry = 0
#     for i in reversed(range(10)):
#         sum = num1 % 10 + num2 % 10 + carry
#         if sum > 9:
#             carry += 1
#         # else:
#         #     carry = 0
#
#         num1 //= 10
#         num2 //= 10
#         if carry == 0:
#             return 0
#         else:
#             return carry
#
#
# print(no_of_carries(786, 457))

# n = 32
# count = 0
# while n > 0:
#     n = n//2
#     print(n)
#     count += 1
#
# count -= 1
# print(count)

# n = str(input())
# if str(n[::-1]) == str(n):
#     print('Pallindrome')


# data = [[104, 105, 111, 152, 365],
#         [104, 105, 111],
#         [104, 105, 111, 152],
#         [104, 152, 365]]

# min_val = 105
# max_val = 200
#
# for index in range(len(data) - 1, -1, -1):
#     if data[index] < min_val or data[index] > max_val:
#         print(index, data)
#         del data[index]

# for item in data:
#     for index, number in enumerate(item):
#         if number == 105:
#             del item[index]
#
# print(data)

# flowers = ['Daffodil', 'Evening Primrose', 'Iris', 'Tiger Lily']
#
# separator = ' | '
# o = separator.join(flowers)
# print(o)

# pangram = "The quick brown fox " \
#           "jumps over the lazy dog"
#
# words = pangram.split()
# print(words)