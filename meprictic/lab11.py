#class Cat:

   # def __init__(self, name):
       # self.name = name
       # self.value = "Мяу"

#class dog:

    #def __init__(self,name):
       # self.name = name
        #self.value = "Гав"

#cat = Cat("шаурма")
#dog = dog("бобик")

#print()

"""import  message
print(message.hello)
message.print_message("Hello world")"""


#myfile = open("hello.txt", "w")
import os
from fileinput import filename
from imghdr import tests
from turtledemo.penrose import start

from django.utils.lorem_ipsum import words


#def get_words(filename):
   # with open(filename, encoding="utf8") as file:
       # text = file.read()
    #text = text.replace("\n", " ")
    #text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    #text = text.lower()
   # words = text.split()
    #words.sort()
    #return words


#def get_words_dict(words):
    #words_dict = dict()

   # for word in words:
      #  if word in words_dict:
       #     words_dict[word] = words_dict[word] + 1
       # else:
      #      words_dict[word] = 1
    #return words_dict


#def main():
   # filename = input("Введите путь к файлу: ")
   # if not os.path.exists(filename):
      #  print("Указанный файл не существует")
   # else:
        #words = get_words(filename)
        #words_dict = get_words_dict(words)
        #print(f"Кол-во слов: {len(words)}")
        #print(f"Кол-во уникальных слов: {len(words_dict)}")
       # print("Все использованные слова:")
       # for word in words_dict:
          #  print(word.ljust(20), words_dict[word])

#if __name__ == "__main__":
   # main()

#file = open("number.txt", "w")
#import random
#for i in range(100):
 #print(random.randint(0, 101))
#file.close()
#print("")