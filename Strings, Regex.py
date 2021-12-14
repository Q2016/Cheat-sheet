//regex sub
import re

// string.split("@")
//string.replace("+","")
// string "".join(list) ex: ' '.join(['this', 'is', 'a', 'sentence'])



#Squaring numbers
def square(match):
    number = int(match.group(0))
    return str(number**2)
print re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9")

// regex sub another example
ii = int(input())
for i in range(0,ii):
   txt = input()
   txt = re.sub(r"\ \&\&\ "," and ",txt)
   txt = re.sub(r"\ \|\|\ "," or ",txt)
   txt = re.sub(r"\ \&\&\ "," and ",txt)
   txt = re.sub(r"\ \|\|\ "," or ",txt)
   print(txt)
   
   
   
// if char is alphabet or number lower case or upper case
ord(num) gives the ascii
#a=97 # ascii number
#z=122

#A=65
#Z=90

#0=48
#1=49
#2=50
#9=57   
