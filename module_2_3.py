#from main2 import my_list
#numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9]  # Предполагаемый список чисел
#for number in numbers:
    #if number > 0:
        #print(number) # Выводит каждый положительный элемент списка
from operator import index

# числа = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# положительные = []
# index = 0
# while index < len(числа):
#   if числа[index] < 0:
#     break
# положительные.append(числа[index])
# index += 1
# print(положительные)

# numbers = [1, 2, 3, 4, 5]
# index = 0
# while index < len(numbers):
#     if numbers[index] % 2 == 0:
#         index += 1
#         continue
#     print(numbers[index])
#     index += 1

my_list_ = [42,69,322,13,0,99,-5,9,8,7,-6,5]
#number_1 = [42,69,322,13,99,9,8,7,5]
#number_2 = [-5,-6]
index = 0
while index < len(my_list_):
    if my_list_[index] > 0:
        print(my_list_[index])
        index += 1
        continue
    elif my_list_[index] < 0:
        print(my_list_[index])
        index += 1
        continue
    else:
        break