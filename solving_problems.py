#Problem 1 Perfect Number

# while True:
#     tot = 0
#     numb = int(input("Enter a number to see if it is a Perfect Number:"))
#     for i in range(1,numb):
#         if numb % i == 0:
#             tot += i
#     if tot == numb:
#         print(numb, "Is a Perfect Number")
#     else:
#         print(numb,"This isn't a perfect number...")

# ------------or----------------

# while True:
#     tot = 0
#     i = 1
#     numb = int(input("Enter a Number:"))
#     while i < numb:
#         if numb % i == 0:
#             tot += i
#         i += 1
#     if tot == numb:
#         print("Number is Perfect")      
#     else:
#         print("NOT PERFECT")

#Problem 2 Armstrong Number

# while True:
#     a = input("Enter A Number:")
#     len_a = len(a)
#     a = int(a)
#     kalan = 0
#     toplam = 0
#     real_a = a
#     while a > 0:
#         kalan = a % 10
#         toplam += kalan ** len_a
#         a //= 10
#     if toplam == real_a :
#         print("This is a armstrong number")
#     else:
#         print("NOT ARMSTRONG NUMBER")
        
#Problem 3

# for i in range(1,11):
#     print("=========================")
#     for j in range (1,11):
#         print (f"{i}x{j}={i*j}")


#Problem 4

# top = 0
# while True:
#     print("press q to quit")
#     a = input("sayi")
#     if a == "q" or a == "Q" :
#         break
#     a = int(a)
#     top += a
# print(top)    
        
 
 
#Problem 5

# for i in range(1,101):
#     if i % 3 != 0:
#         continue
#     print (i)


#Problem 6

# liste = [x for x in range(1,101) if x % 2 == 0]
# print(liste)


#Problem 7

# list = [1,3,4,5,6,7,8,12,54,23,11,75,22,9]
# list_even = []
# list_odd = []
# for i in list:
#     if i % 2 == 0:
#         list_even.append(i)
#     else:
#         list_odd.append (i)
# list_even.sort(),list_odd.sort()
# print(list_even,list_odd)


#Problem 8

# for i in range(101):
#     for j in range(2,i + 1):
#         if i % j == 0:
#             if i == j:
#                 print(i)
#             break ## KILIt NOKTA burda break


#Problem 9

# fakt = 1
# for i in range(1,101):
#     fakt *= i
# print(fakt)


#Problem 10

# a = 1
# b = 1
# fibonacci = [a,b]

# for i in range(1,101):
#     a, b = b, b + a
#     fibonacci.append(b)
# print(fibonacci)


#Problem 11

# balance = 0
# while True:
#     print("WELCOME TO ATM\n1-Check Balance\n2-Add Money\n3-Withdrawaln\--For exit press q")
#     a = input()
#     if a == "q" or a == "Q":
#         print("G O O D  B Y E")
#         break
#     elif a == "1":
#         print(balance,"You remaining balance")
#     elif a == "2":
#         b = int(input("How Much ?"))
#         balance += b
#     elif a == "3":
#         d = int(input("How Much ?"))
#         if d > balance:
#             print("insufficient funds....")
#         else:
#             balance -= d
#     else:
#         print("u made a wrong choice")



#Problem 12

# username_sys = "alicem"
# password_sys = "123456789"
# wrong = 3
# new_user = ""
# new_password = ""
# while True:
#     a = input("If u are a member please press to m to log in for sign up press s ")
#     while True:
#         if a == "m" or a == "M":
#             b = input("username: ")
#             c = input("password: ")
#             if b != username_sys and c == password_sys or d != new_user and e == new_password:
#                 wrong -= 1
#                 print("Wrong user name Remaining wrong attempt is:",wrong)
#             elif b == username_sys and c != password_sys or d == new_user and e != new_password:
#                 wrong -= 1
#                 print("Wrong password Remaining wrong attempt is:", wrong)
#             elif b != username_sys and c != password_sys or d != new_user and e != new_password:
#                 wrong -= 1
#                 print("Wrong pass and username Remaining wrong attempt is:",wrong)
#             else:
#                 print("Welcome to System")
#                 break
#             if wrong == 1:
#                 print("LAST WRONG ATTEMPT !")
#             if wrong == 0:
#                 print ("Failed too many times,Come back later")
#                 break
#         elif a == "s" or a == "S":
#             while True:
#                 d = input("Username: ")
#                 if d == username_sys:
#                     print("This name is already taken try another one")    
#                 else:
#                     print("This username is free.Created.")
#                     break        
#             while True:
#                 e = input("Password: ")
#                 if len(e) < 9:
#                     print("Password should be more than 9 digits try again")    
#                 else:
#                     print("Succesfully created new account!")
#                     new_password += e
#                     new_user += d
#                     break
#             break           
#         else:
#             print("Pressed Wrong Button try again to choose ")
#             break                
                    


#Problem 13

# s = "A man , a plan , a canal: Panama"
# s1 = "".join(i for i in s if i.isalnum())
# s1 = s1.lower() 
# print(s1)
# if s1 == s1[::-1]:
#     print("Is Palindrome")
# else:
#     print("Not a Palindrome")


#Problem 14

# list = [1,3,4,5,6,7,8,12,54,23,11,75,22,9]
# while True:
#     a = int(input("hangi sayi varmi kontrol et"))
#     if a in list:
#         print(list.index(a),"Var")
#     else:
#         print("yok")


#Problem 15

# for i in range(10):
#     print(f"{i}"*i)

#Problem 16

# for i in range(10):
#     print("ONGUN"*i)


#Problem 17

# while True:
#     a = int(input("kilo"))
#     b = float(input("metre cinsinden boy"))
#     kitle = a / (b * b)
#     if kitle < 18.5:
#         print("zayif")
#     elif kitle >= 18.5 and kitle <25:
#         print("normal")
#     elif kitle >= 25 and kitle < 30:
#         print("fazla Kilolu")
#     else:
#         print("Obez")


#Problem 18

# while True:
#     c =int (input("deger girin"))
#     b =int (input("deger girin"))
#     a=int (input("deger girin"))
#     list=[]
#     list.extend((a,b,c))
#     list.sort()
#     print(list[-1])


#Problem 19 - 26 kadar olanlar zaman kaybi gibi geldi o yuzden simdilik bu aralikta olan bazi problemleri 
#kodlayip birakiyorum....



#Problem 20

# while True:
#     a = input("Sekil Sec.\n1- Dortgen\n2-Ucgen")
#     if a == "Dortgen" or a == "DORTGEN" or a == "dortgen" or a== "1":
#         b = int(input("b kenari")) 
#         c = int(input("c kenari"))
#         d = int(input("d kenari")) 
#         e = int(input("e kenari"))
#         if b == c and d == e or b == d and c == e or c == d and b == e:
#             print ("Bu bir dikdortgen")
#         else:
#             print ("Dortgen Klasik")            
      
#     elif a == "Ucgen" or a == "UCGEN" or a == "ucgen" or a == "2":
#         b = int(input("b kenari "))
#         c = int(input("c kenari ")) 
#         d = int(input("d kenari "))
#         if b + c > d and b + d > c and c + d > b:
#             if abs(b) == abs(c) and abs(b) == abs(d):
#                 print("Eskenar ucgen")
#             elif abs(b) == abs(c) or abs(c) == abs(d) or abs(b) == abs(d):
#                 print("Ikizkenar Ucgen")
#             else:
#                 print("Cesit kenar Ucgen")
#         else:
#             print("Bu kenar uzunluklarindan Ucgen OLUSAMAZ!")
                
#     else:
#         print("yanlis secim yaptiniz")


#Problem 25

# a = int(input("a sayi girin"))
# b = int(input("b sayi girin"))

# print(f"a = {a} ---- b = {b}")

# a,b = b,a

# print(f"a = {a} ---- b = {b}")

# #Problem 26
# while True:
#     a = int(input("a kenarini giriniz: "))
#     b = int(input("b kenarini giriniz: "))
#     c = ((a**2) + (b**2))**0.5
#     print(c,"Iki kenari dik olan ucgenin c kenar uzunlugu")
        
    
    
          
#Problem 27 

# remainindataScientist = ['Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS']
# reversedata = remainindataScientist[::-1]
# reversedata = "".join(str(i) for i in reversedata if i.isalnum)
# reversedata = reversedata.lower()
# lentot= 100
# remaining = 0
# remaining=lentot -len(reversedata)
# print(remaining)

# remainindataScientist = ['Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS']
# rev_str = "".join(str(i) for i in remainindataScientist[::-1] if i.isalnum()) ### burada combolar fenaaaaaaa
# rev_str = rev_str.lower()
# print(rev_str)
# rev_str = rev_str[::-1]
# print(rev_str)
# remaining = 100- len(rev_str)
# print(remaining,rev_str)

#Problem 28

# def perfect (number):
#     total = 0
#     for i in range(1,number):
#         if number % i == 0:
#             total += i 
#     return total == number
# for i in range(1,1001):
#     if perfect(i):
#         print(i)


# def perfect():
#     for i in range(1,1001):
#         total = 0
#         for j in range(1,i):
#             if i % j == 0:
#                 total += j
#         if total == i:
#             print(i)


# perfect()


#Problem 29

# def gcd(no1,no2):
#     i = 1
#     while i < no1 and i < no2:
#         if no1 % i == 0 and no2 % i == 0:
#             gcd = i
#         i += 1
#     return gcd
# print(gcd(150,345))

# #rep rep rep
# def gcd(no1,no2):
#     i = 1
#     while i < no1 and i < no2:
#         if not(no1 % i) and not(no2 % i):
#             gcd = i
#         i += 1
#     return gcd
# print(gcd(1455657,675375))


#Problem 30

# def lcm(no1,no2):
#     i = 2
#     lcm = 1
#     while True:
#         if no1 % i == 0 and no2 % i == 0:
#             lcm *= i
#             no1 /= i
#             no2 /= i
#         elif no1 %i != 0 and no2 % i == 0:
#             lcm *= i
#             no2 /= i
#         elif no1 % i ==0 and no2 % i != 0:
#             lcm *= i
#             no1 /= i
#         else:
#             i += 1
#         if no1 == 1 and no2 == 1:
#             break
#     return lcm
# print(lcm(15,20))


#Problem 31

# def read(number):
#     a = str(number)
#     if len(a) > 2:
#         return "this function works only with 2 digit numbers"
#     else:
#         ones = ["","bir","iki","uc","dort","bes","alti","yedi","sekiz","dokuz"]
#         tens = ["","on","yirmi","otuz","kirk","elli","altmis","yetmis","seksen","doksan"]
#         one = number % 10
#         ten = number // 10
#         return tens[ten] + "" + ones[one]
# print(read(99))

#Problem 32

# def pisagor():
#     for i in range(1,101):
#         for j in range(1,101):
#             c = ((i**2) + (j**2))** 0.5
#             if c == int(c):
#                 print(i,j,int(c))
# pisagor()

# #rep rep rep v_2
# def pisagor():
#     for i in range(1,101):
#         for j in range(1,101):
#             c = ((i ** 2) + (j **2))** 0.5
#             if c == int(c):
#                 return i,j,int(c)
# print(pisagor())


#Problem 33
# import random
# import time
# rndm = random.randint(1,1000)
# hak = 10
# while True:
#     a = int(input("Lutfen 1 ile 1000 arasinda bir sayi girin"))
#     if a < rndm:
#         hak -= 1
#         time.sleep(2)
#         print("daha buyuk bir sayi girin\nKalan hakkiniz: ", hak)
#     elif a > rndm:
#         hak -=1
#         time.sleep(2)
#         print("daha kucuk bir sayi girin\nKalan hakkiniz: ", hak)
#     else:
#         time.sleep(2)
#         print("Tebrikler...\nHakkiniz: ", hak, "sayi: ",rndm) 
#         break
#     if hak == 0:
#         print("hakkiniz kalmadi")
#         break

#Problem 34
# class Hayvan():
#     def __init__(self,cins,isim,renk):
#         self.cins = cins
#         self.isim = isim
#         self.renk = renk
#     def showinfo (self):
#         print(f"Cins:{self.cins}\nIsim:{self.isim}\nRenk:{self.renk}")
#     def isimdegistir(self,yeniisim):
#         self.isim = yeniisim
# class Dog(Hayvan):
#     def __init__(self,cins,isim,renk,gender):
#         super().__init__(cins,isim,renk)
#         self.gender = gender
#     def showinfo(self):
#         print(f"Cins:{self.cins}\nIsim:{self.isim}\nRenk:{self.renk}\nGender:{self.gender}")
# class Bird(Hayvan):
#     def __init__(self,cins,isim,renk,kanatsayisi):
#         super().__init__(cins,isim,renk)
#         self.kanatsayisi = kanatsayisi
#     def showinfo(self):
#         print(f"Cins:{self.cins}\nIsim:{self.isim}\nRenk:{self.renk}\nKanat sayisi:{self.kanatsayisi}")
# class At(Hayvan):
#     def __init__(self,cins,isim,renk,toynaksayisi):
#         super().__init__(cins,isim,renk)
#         self.toynaksayisi = toynaksayisi
#     def showinfo(self):
#         print(f"Cins:{self.cins}\nIsim:{self.isim}\nRenk:{self.renk}\nToynak sayisi:{self.toynaksayisi}")
# midilli = At("yaris ati","Mule","kirli gri",4)
# pitbull = Dog("saldirgan kopek","el chapo","piano black","carnivores")
# kanarya = Bird("muhabbet kusu","boncuk","rainbow",2)

# midilli.isimdegistir("essoluessek")
# pitbull.showinfo()
# print("----------")
# midilli.showinfo()
# print("----------")
# kanarya.showinfo()
# print("----------")


#Problem 35 Try Except Hata Bloklari
# liste = ["345","sadas","324a","14","kemal"]
# for i in liste:
#     try:
#         i = int(i)
#         print(i,"bu kisim int olarak try bloguna girip dogrulugunu kanitladigi icin bastirilmistir")
#     except:
#         i = str(i)
#         print(i,"bu kisim str olarak except bloguna girmistir")
####rep rep rep

# liste = ["345","sadas","324a","14","kemal"]
# for i in liste:
#     try:
#         i = int(i)
#         print(i,"Int olan liste elemanlari")
#     except ValueError:
#         pass
#     finally:
#         print("FINALLY WORKS FOR NOTHING")


#Problem 36
# def even(sayi):
#     if sayi % 2 == 0:
#         return sayi
#     else:
#         raise ValueError("sayi tek degil reiz")
# liste = [2,3,4,12,23,36,48,51,43,31]

# for i in liste:
#     try:
#         print(even(i))
#     except:
#         pass





#Problem 37 Composite Numbers in range(2,1001)

# liste = []
# composite_liste = []
# for i in range(2,1001):
#     for j in range(2,i+1):
#         if i % j == 0:
#             if i == j:
#                 liste.append(i)
#             break
# for i in range(2,1001):
#     for j in liste:
#         if i % j == 0:
#             c = i / j
#             if c in liste:
#                 composite_liste.append(i)
#             break
# print(composite_liste)                  


# ## Composite Numbers function
# def composite(sayi):
#     """
# Composite numbers are initialized by multiplying of 2 prime numbers.
# Floor number is 2 so determine the ceil number to see the list of composite numbers in determined interval   
#     """
#     liste = []
#     composite_liste = []
#     for i in range(2,sayi):
#         for j in range(2,(i+1)):
#             if i % j == 0:
#                 if i == j:
#                     liste.append(i)
#                 break
#     for i in range(2,sayi):
#         for j in liste:
#             if i % j == 0:
#                 c = i / j
#                 if c in liste:
#                     composite_liste.append(i)
#                 break
#     print("-----COMPOSITE LIST-----")
#     return composite_liste
# print(composite(1001))

    



#Problem 38 (uncle's)

# liste = [*range(1,101)]
# while len(liste) > 1:
#     son_eleman = liste[-1]
#     for i in liste[1::2]:
#         liste.remove(i)
#     if son_eleman in liste:
#         liste.pop(0)
# print(liste)

############# Turn it into a function:

# def iteleme(kaca_kadar):#1 kaliyor 2 list.remove
#     """
#     Halkadaki son numarayi yazin.1 den baslayip 2 yi egale edecek sekilde halka
#     verdiginiz son numaraya gore son 1 elemani kalacak sekilde sonlanacaktir.
#     Bu fonksiyon size listede kalan son kahramani gosterecektir.
#     """
#     liste = [*range(1,kaca_kadar)]
#     while len(liste) > 1:
#         last_item = liste[-1]
#         for i in liste[1::2]:
#             liste.remove(i)
#         if last_item in liste:
#             liste.pop(0)
#     return liste 

# def kakalama(kaca_kadar):#1 list.remove 2 kaliyor
#     """
#     Halkadaki son numarayi yazin.1 egale edip 2 kalacak sekilde halka
#     verdiginiz son numaraya gore son 1 elemani kalacak sekilde sonlanacaktir.
#     Bu fonksiyon size listede kalan son kahramani gosterecektir.
#     """
#     liste = [*range(1,kaca_kadar)]
#     while len(liste) > 1:
#         son_sayi = liste[-1]
#         for i in liste[::2]:
#             liste.remove(i)
#         if son_sayi in liste:
#             liste.pop(0)
#     return liste
# print(kakalama(10))


#Problem 39 (Luhn's CC validator algorithm)
##### Generator ######
# def randomIIN():#Random 16 digits generator *raw
#     """This function generates 16 digit numbers within specificly 
#     determined intervals.

#     Returns:
#         randomint : no args
#     """
#     import random
#     randval0 = random.randint(3400000000000000,3499999999999999)
#     randval1 = random.randint(3700000000000000,3799999999999999)
#     randval2 = random.randint(4000000000000000,4999999999999999)
#     randval3 = random.randint(5100000000000000,5199999999999999)
#     randval4 = random.randint(6011000000000000,6011999999999999)
#     return randval0, randval1, randval2, randval3, randval4

# def chklen(*digits):
#     """This function checks if cc number lenght is 16

#     Returns:
#         returns tuple: takes * argument to unpack the tuple
#     """
#     verified_digits = tuple()
#     for i in digits:
#         if len(str(i)) == 16:
#             verified_digits += (i,)
#     else:
#         pass
#     return verified_digits

# def w_pattern(*digits):#weight pattern
#     """This function adds values and mutates them through specific
#     weight pattern
#     mutable digits = * args
#     """
#     dgt_str = [str(x) for x in digits]

#     verified_list = []
#     needed_list = []

#     for i in dgt_str:
#         newlist = []
#         result = 0
#         k = 1
#         for h in i[::2]:
#             a = int(h) * 2
#             if a < 10:
#                 newlist.append(a)
#             else:
#                 a = (a % 10) + (a // 10)
#                 newlist.append(a)
#             for j in i[k:k+1]:
#                     newlist.append(int(j))
#                     k += 2
#         for m in newlist:
#             result += m
#         if (result % 10) == 0:
#             newlist = "".join(str(x) for x in newlist)
#             if len(newlist) == 16:
#                 verified_list ="".join(str(z) for z in newlist)
#                 needed_list.append(i)
#         else:
#             continue
#     if not needed_list:
#         pass
#     else:
#         return needed_list 
    
# def identifier(digits):#Issuer Identification Number
#     """IIN checker shows the card type

#     Args:
#         digits (list): 

#     Returns:
#         list: IIN 
#     """
#     if not digits:
#         pass
#     else:
#         for i in digits:
#             if i[0:2] == "34" or i[:2] == "37":
#                 return i,'Amex'
#             elif i[0] == "4":
#                 return i,'Visa'
#             elif i[:2] == "51":
#                 return i,'Mastercard'
#             else:
#                 return i,'Discovery Card'    
    


# for i in range(1,101): 
#     print(identifier(w_pattern(*chklen(*randomIIN()))))

############################### Validity Checker ######################################

# def chk(ccno = input("Enter CC number should be 16 digits:\n")):
    
#     if len(str(ccno)) == 16:
#         return ccno
#     else:
#         print("16 haneli degil")
#         pass
# def wp(ccno):
#     lst = []
#     k = 1
#     result = 0
#     a = int()
    
#     for i in str(ccno)[::2]:
#         a = (int(i) * 2)
#         if a < 10:
#                 lst.append(a)
#         else:
#                 a = (a % 10) + (a // 10)
#                 lst.append(a)
#         for j in str(ccno)[k:k+1]:
#             lst.append(int(j))
#             k += 2
#             break
#     for i in lst:
#         result += int(i)
#     if result % 10 == 0:
#         return ccno,"Valid card"
#     else:
#         print("Kart valid degil")
#         pass

# print(wp(chk()))




#Problem 40
###### TRIN(Turkish Republic Identification Number) Generator ########
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
#     a = random.randint(100000000,999999999)
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




#Problem 41 TicTacToe From Stoneage






#Problem 42
#list = [1,2,6,12,234,"123","12344","osman","helloworld123",(123,3333,11123)]
# def lstto_str(list):
#     ttl = 0
#     for i in list:
#         str(i)
#         for j in str(i):
#             try:
#                 ttl += int(j)
#             except:
#                 pass
#     return ttl
# print(lstto_str(list))

#######rpt rpt rpt rpt
# list = [1,2,6,12,234,"123","12344",(123,3333,11123)]
# ttl = 0
# for i in list:
#     str(i)
#     for j in str(i):
#         try:
#             ttl +=int(j)
#         except:
#             pass  
# print(ttl)


#Problem 43
# new_lst =[]
# lst = [[1,2,3],[4,5],[6]]
# for i in lst:
#     for j in i:
#         new_lst.append(j)
# print(new_lst)      


#Problem 44
# 1 WAY FOR LOOP
# newlst = []
# lst = [1,1,2,3,3,3,4,5,5]
# for i in lst:
#     if i not in newlst:
#         newlst.append(i)
#     else:
#         continue
# print(newlst)


# 2 WAY LIST TO SET AND VICE VERSA
# lst = [1,1,2,3,3,3,4,5,5]
# sett = set(lst)
# print(sett)
# lst = list(sett)
# print(lst)

# 3 WAY Comprehensions 
# lst = [1,1,2,3,3,3,4,5,5]
# sett = {x for x in lst}
# print(sett)
# lst = [x for x in sett]
# print(lst)


#Problem 45

##### 1 WAY
# srt = "111101000101010101110001010000"
# print(srt.count("0"))

##### 2 WAY
# liste = []
# for i in srt:
#     if i == "0":
#         liste.append(i)
# print(len(liste))




#Problem 46
##### ANSWER 1 
# def not_hesaplama(notlar):
#     notlar = notlar[:-1] # alt alta basildiklarinda aralarindaki boslugu silmek icin
#     lst = notlar.split(",") # virgulu target alarak ondan sonrakileri liste olarak ayirdik
#     isim = lst[0]
#     not1 = int(lst[1])
#     not2 = int(lst[2])
#     not3 = int(lst[3])
    
#     not_hesap = 3/10 * not1 + 3/10 * not2 + 4/10 * not3
#     if not_hesap >= 90:
#         harf = "AA"
#     elif not_hesap >= 85:
#         harf = "BA"
#     elif not_hesap >= 80:
#         harf = "BB"
#     elif not_hesap >= 75:
#         harf = "CB"
#     elif not_hesap >= 70:
#         harf = "CC"
#     elif not_hesap >= 65:
#         harf = "DC"
#     elif not_hesap >= 60:
#         harf = "DD"
#     elif not_hesap >= 55:
#         harf = "FD"
#     else:
#         harf = "FF"
#     return isim + "-------------->>>>> " + harf + "\n"

# with open("e:/Udemy Python/ALLCODINGexercises/FileProcessing/dosya.txt", "r", encoding = "utf-8") as file:
#     liste_ekle= []
#     for i in file:
#         liste_ekle.append(not_hesaplama(i))
#     with open("notlar_file_process_experience.txt","w", encoding = "utf-8") as file2:
#         for i in liste_ekle:
#             file2.write(i)




####### ANSWER 2 
# #################  PASSED TXT eq 60 or greater than 60  ############################
# def nothesap(line):
#     line = line[:-1]
#     lst_line = line.split(",")
 
#     name = lst_line [0]
#     note1 = int(lst_line [1])
#     note2 = int(lst_line [2])
#     note3 = int(lst_line [3])
#     calc = (3/10 * note1) + (3/10 * note2) + (4/10 * note3)
#     if calc >= 60:
#         return name + "-------> " + str(calc) + "\n"
#     else:
#         pass
    


# with open("dosya.txt","r", encoding = "utf-8") as file:
#     gecenlst =[]
#     for i in file:
#         gecenlst.append(nothesap(i))
#     with open("passed_txt.txt","w",encoding="utf-8")as file2:
#         for j in gecenlst:
#             try:
#                 file2.write(j)
#             except:
#                 pass

##################  FAILED TXT below 60  ################################
# def calculation(notes):
#     notes = notes[:-1]
#     lst = notes.split(",")
#     name = lst[0]
#     note2 = int(lst[2])
#     note1 = int(lst[1])
#     note3= int(lst[3])
    
#     calc = (3/10 * note1) + (3/10 * note2) + (4/10 * note3)
#     if calc < 60:
#         return name + " -------> " + str(calc) + "\n"

# with open("dosya.txt","r",encoding="utf-8")as file:
#     lst_failed = []
#     for i in file:
#         lst_failed.append(calculation(i))
#     with open("failed_txt.txt","w",encoding = "utf-8") as file2:
#         for j in lst_failed:
#             try:
#                 file2.write(j)
#             except:
#                 pass