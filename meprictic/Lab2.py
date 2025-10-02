#from colorsys import yiq_t
#a = 5
#b = 6
#result = 5 == 6
#print(result)
#print(a != b)
#print(a > b)
#print(a < b)
#bool1 = True
#bool2 = False
#print(bool1 == bool2)
#age = 22
#weight = 58
#result = age > 21 and weight == 58
#print(result)
#result = 4 and "w"
#print(result)
from traceback import print_tb

from django.templatetags.i18n import language

#result = 0 and "w"
#print(result)
#age = 22
#isMarried = false
#result = age > 21 or isMarried
#print(result)
#age = 22
#isMarried = False
#print(not age > 21)
#print(not isMarried)
#print(not 4)
#print(not 0)
#message = "hello World!"
#hello = "hello"
#print(hello in message)

#gold = "gold"
#print(gold in message)
#message = "hello World!"
#hello = "hello"
#print(hello not in message)

#gold = "gold"
#print(gold not in message)
#language = "english"
#if language == "english":
    #print("Hello")
#print("End")
#language = "english"
#if language == "english":
    #print("Hello")
    #print("End")
#language = "russian"
#if language == "english":
    #print("Hello")
#else:
    #print("Привет")
#print("End")
#language = "russian"
#if language == "english":
    #print("Hello")
    #print("World")
#else:
#print("Привет")
 #   print("мир")
#language = "german"
#if language == "english":
    #print("Hello")
    #print("World")
#elif language == "german":
    #print("Hallo")
    #print("Welt")
#else:
    #print("Привет")
    #print("мир")
#language = "german"
#if language == "english":
    #print("Hello")
#elif language == "german":
    #print("Hallo")
#elif language == "french":
    #print("Salut")
#else:
    #print("Привет")
#language = "english"
#daytime = "morning"
#if language == "english":
    #print("English")
    #if daytime == "morning":
        #print("Good morning")
    #else:
        #print("Good evening")
#language = "english"
#daytime = "morning"
#if language == "english":
    #print("English")
#if daytime == "morning":
    #print("Good morning")
#else:
   # print("Good evening"
#language = "russian"
#daytime = "morning"
#if language == "english":
    #if daytime == "morning":
        #print("Good morning")
    #else:
        #print("Good evening")
#else:
    #if daytime == "morning":
        #print("Доброе утро")
    #else:
        #print("Добрый вечер")
#y = int(input("2024: "))

#if y % 400 == 0 or y % 4 == 0 and y % 100 != 0:
    #print("2020")
#else:
    #print("1900")
#a = int(input("5 a: "))
#b = int(input("6 b: "))
#if a>b:
    #g=a
#else:
    #g=b
#print("6: ",g)
#a = int(input(" 5 a: "))
#b = int(input(" 6 b: "))
#g =  a if a>b else b
#print(" 6: ",g)
#amount = int(input("25000: "))
#if amount > 0:
    #if amount>25000:
        #discount=amount * 0.3
    #elif amount>15000:
        #discount=amount * 0.2
    #elif amount>5000:
        #discount = amount*0.12
    #else:
        #discount = amount*0.05
    #print("5000: ", discount)
    #print("20000.0 : ", amount-discount)
#else:
    #print("Некорректная сумма")
#while True:
    #num1 = int(input("2: "))
    #num2 = int(input("2: "))
    #print("5: ", num1+num2 )
    #str = input ("Нажмите Y или y для завершения программы: ")
    #if (str =="Y" or str =="y"):  break
#n = 7
#for i in range(0, n):
    #for j in range(0, n):
        #if(i == 0 or i == n-1 or j==i or j == n-i-1): print("*", end="")
        #else: print(" ", end="")
    #print()
#h = 7
#w = h + 2
#m = w //4
#for i in range(1, h+1):
    #if (i <= m):
        #print(" " * (m-i) + "*" * (2*i) + " " * (w-2*i-2*m) + "*" *(2*i) + " " * (m-i))
    #else:
      #print(" " * (i - 2*m+1) + "*" * (w-2*(i-2*m+1)) + " " * (i - 2*m+1))
#n=5
#k=1
#counter=1
#for i in range(n):
    #for j in range(n):
        #if k % 2 == 0:
            #print(counter, end ="  ")
            #counter+=1
        #else: print("*",end="  ")
        #k+=1
    #print()