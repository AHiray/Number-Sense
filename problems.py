import random
import time

#Import time library
def countdown(t):
    while t: # while t > 0 for clarity 
      mins = t // 60
      secs = t % 60
      timer = '{:02d}:{:02d}'.format(mins, secs)
      print(timer, end="\r") # overwrite previous line 
      time.sleep(1)
      t -= 1
    print('Times Up')
t = input("Enter the time in seconds: ") 


def reverseInt(x):
    x = str(x)
    lst = list(x)
    lst.reverse()
    x = "".join(lst)
    x = int(x)
    return x


def SubRev3Digit():
    a = random.randint(100,999)
    b = reverseInt(a)
    return str(a) + " - " + str(b), a - b

def SubRev4Digit():
    a = random.randint(1000,9999)
    b = str(a)
    lst = list(b)
    lst[0], lst[3] = lst[3], lst[0]
    b = "".join(lst)
    b = int(b)
    return str(a) + " - " + str(b), a - b

def Mult25():
    a = str(random.randint(1,9)) + '5'
    b = str(random.randint (1,9)) + '5'
    return a + ' *  ' +  b, int(a) * int(b)

def Mult12():
    a = str(random.randint(10,100))
    return a + ' * 12', int(a) * 12

def Mult125():
    a = str(random.randint(1,100))
    return a + ' * 125', int(a) * 125

for i in range(10):
        question, answer = Mult125()
        print(question)
        #countdown(15)
        givAnswer = input( 'Answer: ')
        if answer == int(givAnswer):
            print("Correct")
        else:
            print("Incorrect, the answer is " + str(answer))
