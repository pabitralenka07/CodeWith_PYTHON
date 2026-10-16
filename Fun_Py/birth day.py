import pyfiglet     
import time
import pyttsx3 
from random import randint
for i in range(1,70):
    print(' ')
space=' '
for i in range(1,30):
    count=randint(1,100)
    while(count>0):
        space+=' '
        count-=1

    if(i%10==0):
        print(space+'🎂Happy Birthday to you!')
    elif(i%9==0):
        print(space+"🎈")
    elif(i%5==0):
        print(space+"💖")
    elif(i%8==0):
        print(space+"🎉")
    elif(i%7==0):
        print(space+"👑")
    elif(i%6==0):
        print(space+"Happy Birthday Pabitra!💖")
    else:
        print(space+"💥")
    space=' '
    time.sleep(0.2)

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__=="__main__":
    speak("Happy birthday pabitra lenka ,many many happy returns of day.and i want to say few words for you that hope your special day brings you all that your desires!")



for i in range(1,30):
    count=randint(1,100)
    while(count>0):
        space+=' '
        count-=1

    if(i%10==0):
        print(space+'🎂Happy Birthday to you!')
    elif(i%9==0):
        print(space+"🎈")
    elif(i%5==0):
        print(space+"💖")
    elif(i%8==0):
        print(space+"🎉")
    elif(i%7==0):
        print(space+"👑")
    elif(i%6==0):
        print(space+"Happy Birthday Pabitra!💖")
    else:
        print(space+"💥")
    space=' '
    time.sleep(0.2)

def print_with_typewriter_effect(string):
    for char in string:
        print(char,end='',flush=True)
        time.sleep(0.5)



font_style=pyfiglet.figlet_format("HAPPY BIRTHDAY      TO PABITRA")
#font_style=pyfiglet.figlet_format("TO PABITRA")

lines=font_style.split('\n')



max_line_lentgh=max(len(line) for line in lines)
padding=(80-max_line_lentgh)//2

for line in lines:
    print(' '*padding+line)
    time.sleep(0.5)

print("\n           Dil se chahat hai meri:")
print("---"*2)

print_with_typewriter_effect("           Ap khub unchai chuinye\n")
print_with_typewriter_effect("   💖     Bahut tarraki kijiye\n")
print_with_typewriter_effect("           Sb logon ki madad kijiye\n")
print_with_typewriter_effect("     🎂       Par bs itna hi dukh hai\n")
print_with_typewriter_effect("            ki aap ese hi aaj tak single ho:😁\n")
print_with_typewriter_effect("        🎈      Aur aap ese hi rohoge : \n")
