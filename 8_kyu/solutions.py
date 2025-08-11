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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def sp_eng(sentence):
#     return "english" in sentence.lower()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# text = 'dsad'
# print(text.capitalize())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def parse_float(string):
#     try:
#         return float(string)
#     except:
#         return None

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def array_plus_array(arr1,arr2):
#     return sum(arr1) + sum(arr2)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def remove_exclamation_marks(s):
#     return s.replace("!", "")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def hello(name=""):
#     return f"Hello, {name.capitalize()}!" if name else "Hello, World!"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# import random

# class Ghost(object):
#     def __init__(self):
#         self.color = random.choice(["white", "yellow", "purple", "red"])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# import math

# def dating_range(age):
#     if age <= 14:
#         min_age = math.floor(age - 0.10 * age)
#         max_age = math.floor(age + 0.10 * age)
#     else:
#         min_age = math.floor(age / 2 + 7)
#         max_age = math.floor((age - 7) * 2)
#     return f"{min_age}-{max_age}"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def add_extra(list_of_numbers):
#     return list_of_numbers + [None]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def sum_array(a):
#     return sum(a)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def move(position, roll):
#     return position + roll * 2

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def bool_to_word(boolean):
#     return "Yes" if boolean == True else "No"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def simple_multiplication(number) :
#     return number * 8 if number % 2 == 0 else number * 9

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def sp_eng(sentence):
#     return "english" in sentence.lower()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def alias_gen(f_name: str, l_name: str) -> str:
#     first_letter = f_name[0].upper()
#     last_letter = l_name[0].upper()

#     if not first_letter.isalpha() or not last_letter.isalpha():
#         return "Your name must start with a letter from A - Z."

#     return f"{FIRST_NAME[first_letter]} {SURNAME[last_letter]}"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

