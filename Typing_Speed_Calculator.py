from time import *   #by this we can access all the functions of the time module
import random

def mistake(para,userinput):
    error = 0
    for i in range(len(para)):
        try:
            if para[i] != userinput[i]:
                error = error + 1
        except:
            error = error + 1
    return error

#it is used to find typing speed 
def speed_time(time_start, time_end, userinput):
    time_delay = time_end - time_start
    time_roundOff = round(time_delay,2)    #2-> round off upto 2 digit
    speed = len(userinput)/time_roundOff
    return round(speed)

#want to split into 2 parts use this
if __name__=='__main__':
    while True:
        check = input("Ready for test : Yes/No : ")
        if check == "yes":
                #it is used to display the text for typing
            test = ["Text messaging, or simply texting, is the act of composing and sending electronic messages, typically consisting of alphabetic and numeric characters, between two or more users of mobile phones, tablet computers, smartwatches, desktops/laptops, or another type of compatible computer. Text messages may be sent over a cellular network or may also be sent via satellite or Internet connection.",
                    "The term originally referred to messages sent using the Short Message Service (SMS) on mobile devices. It has grown beyond alphanumeric text to include multimedia messages using the Multimedia Messaging Service (MMS) and Rich Communication Services (RCS)",
                    "Which can contain digital images, videos, and sound content, as well as ideograms known as emoji (happy faces, sad faces, and other icons), and on various instant messaging apps. Text messaging has been an extremely popular medium of communication since the turn of the century and has also influenced changes in society."]
            #use to choose 1 line from test
            test1 = random.choices(test)
            print("***** Typing Speed Calculator ******")
            print(test1)
            #line brake
            print()
            print()

            time_1 = time()
            #taking user input
            testinput = input(" Enter : ")
            time_2 = time()

            #calling the functions
            print('Speed : ',speed_time(time_1, time_2, testinput)," Word Per Second")
            print("Error : ",mistake(test1,testinput))
            
        elif "no":
            print("Thank You")
            break
        else:
            print("Wrong Input")
    
