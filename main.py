import random
from math import trunc
from random import randint
import time
import keyboard

guessSeconds = 0
userSentence = ""
percent = 0.0
sentences = []
chosenSentence = ""


def titleScreen():
    choice = input("Ready to test your typing speed? 1) Go")
    if choice == "1":
        type()


def type():
    global sentences
    global userSentence
    global chosenSentence

    sen1 = "He had a vague sense that trees gave birth to dinosaurs."
    sen2 = "The door slammed on the watermelon."
    sen3 = "She let the balloon float up into the air with her hopes and dreams."
    sen4 = "I ate a sock because people on the Internet told me to."
    sen5 = "Today is the day I'll finally know what brick tastes like."

    sentences.append(sen1)
    sentences.append(sen2)
    sentences.append(sen3)
    sentences.append(sen4)
    sentences.append(sen5)

    chosenSentence = random.choice(sentences)

    print("-------------------------------------------------------------------")
    timeStart = time.time()
    print("Copy the sentence:")
    userSentence = input(chosenSentence)

    timeEnd = time.time()

    timeSpent = timeEnd - timeStart

    checkAccuracy()
    timeConvertToMakePretty(timeSpent)


def checkAccuracy():
    global percent
    global userSentence
    global chosenSentence
    num = 0
    for x in range (0, len(userSentence)):
        if userSentence[x] == chosenSentence[x]:
            num += 1

    percent = round(num / len(userSentence), 2)


def timeConvertToMakePretty(time):
    global percent
    print("-------------------------------------------------------------------")
    print("You typed the sentence at " + str(round(time, 2)) + " seconds with an accuracy of " + str(percent))
    print("-------------------------------------------------------------------")
    titleScreen()


titleScreen()
