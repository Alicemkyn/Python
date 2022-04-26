###### TRCIN(Turkish Republic Citizen Identification Number) Generator ########
# Should be 11 digits(first 9 digit is original digit + 2 last digit is checksum)
# 0 cant be the x[0]
# random.randint 9 digit number > convert to str > iterate for int
#((sum of 1,3,5,7,9 digits )* 7) - (sum of 2,4,6,8 digits) % 10 = 10th digit- i in x[::2] -- i in x[1::2]
# Sum of every digit 1...+10= % 10 is 11th digit
# Ataturk's tcn= 100000001+cheksum digits

# def rnd_generate():#Generates 9 digit random number
#     """random 9 digit number generator

#     Returns:
#         int: 9 digit random number
#     """
#     import random
#     a = random.randint(100000001,999999999)
#     return a

# def w_pattern(digit):#Algorithmic Weight Pattern
#     total= 0
#     total1 = 0
#     tenth = int()
#     eleventh = int()
#     a = str(digit)
#     liste = [digit]
#     for i in a[::2]:
#         total += int(i)
#     total *= 7
#     for j in a[1::2]:
#         total1 += int(j)
#     tenth = (total - total1) % 10
#     liste.append(tenth)
#     total = 0
#     for i in liste:
#         for j in str(i):
#             total += int(j)

#     eleventh = total % 10
#     liste.append(eleventh)
#     a = "".join(str(x) for x in liste )
#     return a

# print(w_pattern(rnd_generate()))

######################################################################################################

# To find next or previous one = without cheksum digits -29999 or + 29999
# This program returns 20 tckn once it is executed.
# This one has same algotrithm as above but this is not a function.

# l = 20 # Returns 20 values
# digit = 333852669 # mine number raw (without last 2 digits(checksum digits))
# while l > 1:
#     digit += 29999 # everytime it turns it finds the next person after me
#     total= 0
#     total1 = 0
#     tenth = int()
#     eleventh = int()
#     a = str(digit)
#     liste = [digit]
#     for i in a[::2]:
#         total += int(i)
#     total *= 7
#     for j in a[1::2]:
#         total1 += int(j)
#     tenth = (total - total1) % 10
#     liste.append(tenth)
#     total = 0
#     for i in liste:
#         for j in str(i):
#             total += int(j)
#     eleventh = total % 10
#     liste.append(eleventh)
#     a = "".join(str(x) for x in liste )
#     print(a)
#     l -=  1