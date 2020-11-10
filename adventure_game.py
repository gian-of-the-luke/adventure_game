#Introduction
import sys

print("Hello, and welcome to Gianluca's first game!")

#ask user their name, age, and make them agree to be nice
user_name = input("So, what's your name, friend? ")
user_age = int(input("Hi {}! Also, how old are you? ".format(user_name)))
if user_age >= 18:
    print("{}, you're old enough to play, but let's keep \
things church, aight?".format(user_name))
    agree = input("Please choose the appropriate response:\n\n Fo' sho\n Nah mayne\n response: ")
    if agree == "Fo' sho":
        print("\nLet's start.")
    elif agree == "Nah mayne":
        print("*points piece* {}".format("BANG"*10))
    else:
        print("Please speak TRUE mein bruder.")
else:
    print("{}, you're basically a walking-fetus! You can't play, bye.".format(user_name))

#Prologue

if agree == "Fo' sho":
    print("\nWelcome to the land of coffee-stan, an unfair place. \
    \nBean people are regularly bought and sold to the highest bidder,\n\
and shipped off to work.\
    \nNicknamed; 'The Grinder', it consumes countless lives.\
    \nOne bean wants to change that. \n'Arabica!', called his Mother")

    #Divert to ignore Mom
    q1 = input("\nRespond: Yeah Mom? vs. Ignore her\n")
    if q1 == "Yeah Mom?":
        print("Come down, your Father and I need to speak with you.")
    elif q1 == "Ignore her":
        print("Arabica!\n")
        q1_1 = input("\nRespond: Yeah Mom? vs. Ignore her\n")
        if q1_1 == "Ignore her":
            print("Arabica!\n")
            q1_2 = input("Respond: Yeah Mom? vs. Ignore her\n")
            if q1_2 == "Ignore her":
                print("Arabica never learns the truth of The Grinder.\n\nYou lose!")
                sys.exit()
        #Continue linear path.
    if q1 or q1_1 or q1_2 == "Yeah Mom?":
        print("\nArabica runs to meet his parents.\n\
His Father looked at him with sunken eyes while holding his \
Mother's hand.\n\
'Son, your Mother's time has come. She's due for the grinder.'")
        q2 = input("\nPick one of the following:\n\
You're right.\nNo, it can't be!\n").lower()

    if q2 == "you're right.":
        print("Father: 'Yes, that's right, now help me take her there.\n")
    else:
        print("Maybe you're the one due for the grinder...\n")
        sys.exit()

            #Continue linear path

    if q2 == "You're right." or "No it's can't be!" or "What's the grinder?":
        print("Arabica and his Father take his Mother to the grinder.\n\
There, a cabal of beans surround the machine, ready to accept his Mama.")
        q3 = input("Let Mama join the Grind?\n\
or\n\
Stop this madness!\n")

    if q3 == "Let Mama join the Grind":
        print("Off she goes, through a hole. Moments later the machine awakens,\n\
A sickening roar of metal and blade erupts over the chants of the bean people. \n\
Mama has come home.")
    else:
        print("Arabica heroically pummels the caffienated shamans and declares: \n\
        'Not one more bean will serve this monster.'\n\
        'Today, we are masters of our own brew.\n\n\
        'What matters is not the color of our roast \n\
        but the decisions we make'.")
        q4 = input("\nDo you agree?  Yes // No\n")

        if q4 == "Yes":
            print("Well {}, if you truly believe that, \n\
    then start living your life like that. The line\n\
    between good and evil cuts through the heart of\n\
    all, human or bean.\n\
            Good ending".format(user_name))
        elif q4 == "No":
            print("Despair!\n\
            Bad ending")
        else:
            print("You are madness.\n Chaotic Neutral ending.")
