#entering the purple lights party

import time

#loop so that it repeats itself
while True:
    print("NEW GUEST ARRIVES🤗")
    time.sleep(2)

    print("Welcome to the Purple Lights Party!💜🪩")
    time.sleep(1)

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

 # I decided to not print that⤵️, because I want it to be a loop. (never ending story)
 #   print("Done! Thanks for playing!")
 #   time.sleep(3)
