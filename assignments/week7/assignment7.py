#entering the purple lights party
import os
import time
import csv
import random

DEBUG = True

if not os.path.exists("record.csv"): #help through included AI because I don't want the headings to be written everytime
    with open("record.csv", "a") as record: #opening file
        writer = csv.writer(record)
        writer.writerow(["Name", "Age", "Choice", "Outfit", "Duration"])

#loop so that it repeats itself
if DEBUG == False:
    while True:
        print("NEW GUEST ARRIVES🤗")
        time.sleep(2)

        print("Welcome to the Purple Lights Party!💜🪩")
        time.sleep(1)

        timerstart = time.time() #take the time when the program starts
    #name
        name = input("First things first. What's your name?")

    #boss check
        if name.lower() == "boss":
            print("You're the boss! Go wherever you want!")
            time.sleep(2)
            continue
        print(f"Checking the guest list for {name}...")
        time.sleep(2)

    #age
        while True:
            #try except requirement to make sure that the input is a number
            try:
                age = int(input("How old are you?"))
                if 18 <= age <= 99:
                    print (f"Okay, {name}, you're old enough to enter.")
                    time.sleep(2)
                    break
                else:
                    print("Nice try, but you're not old enough to enter.")
            except ValueError:
                print( "That's not even a number. Try again.")

    #choosing between VIP or dancing floor

        choice = input ("Ok, are you here for the [VIP] or the [dancefloor]?").lower()
        outfit = ""
        if choice == "vip":
            outfit = input("VIP has a dress code! Are you dressed [Chic] or [Casual]?").lower()
            if outfit == "chic":
                print("You're dressed up perfectly for the VIP lounge! Have fun!")
                time.sleep(3)
            elif outfit == "casual":
                print("You're not dressed up for the VIP lounge, but you can still have fun on the dancefloor!")
                time.sleep(3)
        elif choice == "dancefloor":
            print ("Have fun! The music is great and the dancers are amazing!")
            print ("🪩🕺🏼💃🏼")
            time.sleep(4)
        else:
                print("Sorry, I don't understand. Please try again.")
        timerend = time.time()
        duration = timerend - timerstart

        with open("record.csv", "a") as record:
            writer = csv.writer(record)
            writer.writerow([name, age, choice, outfit, f"{float(duration):.2f}"])

        goon=input("Do you want to go on? (yes/no)").lower()
        if goon == "no":
            break

else:
    while True:
        #try except requirement to make sure that there is a name
        try:
            name = input("What's your name? ")

            if name == "":
                raise ValueError
            break

        except ValueError:
            print("Please enter a real name.")

    age = random.randint(18, 99)
    choice = random.choice(["vip", "dancefloor"])
    if choice == "vip":
        outfit = random.choice(["chic", "casual"])
    else:
        outfit = ""

    duration = random.uniform(15, 30)

    with open("record.csv", "a") as record:
        writer = csv.writer(record)
        writer.writerow([name, age, choice, outfit, f"{float(duration):.2f}"])

with open("record.csv", "r") as record:
    for row in csv.reader(record):
        name = row[0]
        age = row[1]
        choice = row[2]
        outfit = row[3]
        duration = row[4]
        print(f"{name:8s} | {age:5s} | {choice:10s} | {outfit:10s} | {duration:10s}")