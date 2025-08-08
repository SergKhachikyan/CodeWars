# my_list = [-3,-2,0,1]

# for i in range(len(my_list)):
#     if my_list[i] - my_list[i - 1] == 2:
#         print(my_list[i])
#         break
# else:
#     print("None")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def sakura_fall(y):
#     if y <= 0:
#         return 0
#     return 400 / y

# print(sakura_fall(5))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def was_package_received_yesterday(tz_from, tz_to, start, duration):
#     utc_departure = start - tz_from
#     utc_arrival = utc_departure + duration

#     local_arrival = utc_arrival + tz_to

#     return local_arrival < 0

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def _all(seq, fun):
#     return all(fun(x) for x in seq)

# def sum_mix(arr):
#     summ = 0
#     for i in arr:
#         summ += int(i)
#     return summ

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def switch_it_up(number):
#     numbers_dict = {
#         0: "zero",
#         1: "one",
#         2: "two",
#         3: "three",
#         4: "four",
#         5: "five",
#         6: "six",
#         7: "seven",
#         8: "eight",
#         9: "nine"
#     }
#     if number in numbers_dict:
#         return numbers_dict[number]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# my_list = [9, 3, '7', '3']
# summ = 0
# for i in my_list:
#     summ += int(i)
# print(summ)

# my_tuple = (1, 2, 3, 4, 5)

# for i in my_tuple:
#     if i > 9:
#         print(True)
# else:
#     print(False)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def calculator(x, y, op):
#     if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
#         return "unknown value"

#     if op == '+':
#         return x + y
#     elif op == '-':
#         return x - y
#     elif op == '*':
#         return x * y
#     elif op == '/':
#         return x / y if y != 0 else "unknown value"
#     else:
#         return "unknown value"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def logical_calc(array, op):
#     return {'AND': all(array), 'OR': any(array), 'XOR': sum(array) % 2 == 1}[op]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# start = int(input("enter start: "))
# end = int(input("enter end: "))

# if start == 0 and end == 0:
#     print("INVALID")
# if end < start:
#     print("INVALID")

# summ = 0
# for i in range(start,end,start):
#     summ += i
    
# print(summ)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def correct(s):
#     my_list = [i for i in s]

#     for i in range(len(my_list)):
#         if my_list[i] == '0':
#             my_list[i] = 'O'
#         if my_list[i] == '5':
#             my_list[i] = 'S'
#         if my_list[i] == '1':
#             my_list[i] = 'I'
#     return ''.join(my_list)
# print(correct("L0ND0N"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def merge_arrays(arr1, arr2):
#     return sorted(set(arr1 + arr2))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def get_size(w,h,d):
#     surface_area = 2 * (w * h + w * d + h * d)
#     volume = w * h * d
#     return [surface_area, volume]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def remove_char(s):
#     return s[1:-1]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def hex_to_dec(s):
#     return int(s,16)