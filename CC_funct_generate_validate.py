###### CC VALIDITY CHECKER ########
# https://www.youtube.com/watch?v=PNXXqzU4YnM&t=184s  check it out for Luhn's Algorithm
# https://www.validcreditcardnumber.com/ check here.
# IIN numbers to create perfection about credit card generation.To see how, check this out (below)
# https://www.investopedia.com/terms/i/issuer-identification-number-iin.asp#:~:text=The%20issuer%20identification%20number%20%28IIN%29%20refers%20to%20the,to%20the%20issuer%20and%20its%20partnering%20network%20provider.?msclkid=3f4ce2d4c27911ec838b57111e97c196

# Weight pattern is 2-1-2-1-2-1-2-1...
# Should be 16 digits
# [::2]*2 and [1::2]*1 if result > 10 while multiplication then twodigit % 10 and twodigit//10 sum the results 
# if multiplication result > 10 then twodigit % 10 and twodigit//10 sum is the results 
# Sum of the last generated 16 digit list should be divisible by ten. 'x % 10 == 0'  So last digit of sum should be zero
# Randomly create number in interval of IIN checking method

#Function list
# ccnumber lenght check if it is 16 or not
# Weight pattern calculator and making list put of it 
# Sum of the list calculator and mod 10 checker
# IIN checker:
    # American Express: 34, 37
    # Discover Card: 6011, 622126 to 622925, 624000 to 626999, 628200 to 628899, 64, 65
    # Mastercard: 2221 to 2720, 51 to 55
    # Visa: 4
# Randomly create number in interval of IIN checking method .randint
##### Djem tryin Python  #########

##### Generator ######
def randomIIN():#Random 16 digits generator *raw
    """This function generates 16 digit numbers within specificly 
    determined intervals.

    Returns:
        randomint : no args
    """
    import random
    randval0 = random.randint(3400000000000000,3499999999999999)
    randval1 = random.randint(3700000000000000,3799999999999999)
    randval2 = random.randint(4000000000000000,4999999999999999)
    randval3 = random.randint(5100000000000000,5199999999999999)
    randval4 = random.randint(6011000000000000,6011999999999999)
    return randval0, randval1, randval2, randval3, randval4

def chklen(*digits):
    """This function checks if cc number lenght is 16

    Returns:
        returns tuple: takes * argument to unpack the tuple
    """
    verified_digits = tuple()
    for i in digits:
        if len(str(i)) == 16:
            verified_digits += (i,)
    else:
        pass
    return verified_digits

def w_pattern(*digits):#weight pattern
    """This function adds values and mutates them through specific
    weight pattern
    mutable digits = * args
    """
    dgt_str = [str(x) for x in digits]

    verified_list = []
    needed_list = []

    for i in dgt_str:
        newlist = []
        result = 0
        k = 1
        for h in i[::2]:
            a = int(h) * 2
            if a < 10:
                newlist.append(a)
            else:
                a = (a % 10) + (a // 10)
                newlist.append(a)
            for j in i[k:k+1]:
                    newlist.append(int(j))
                    k += 2
        for m in newlist:
            result += m
        if (result % 10) == 0:
            newlist = "".join(str(x) for x in newlist)
            if len(newlist) == 16:
                verified_list ="".join(str(z) for z in newlist)
                needed_list.append(i)
        else:
            continue
    if not needed_list:
        pass
    else:
        return needed_list 
    
def identifier(digits):#Issuer Identification Number
    """IIN checker shows the card type

    Args:
        digits (list): 

    Returns:
        list: IIN 
    """
    if not digits:
        pass
    else:
        for i in digits:
            if i[0:2] == "34" or i[:2] == "37":
                return i,'Amex'
            elif i[0] == "4":
                return i,'Visa'
            elif i[:2] == "51":
                return i,'Mastercard'
            else:
                return i,'Discovery Card'    
    


for i in range(1,101): 
    print(identifier(w_pattern(*chklen(*randomIIN()))))