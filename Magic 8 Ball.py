import random
import time
import os
clear = lambda: os.system('cls')

while True:
    print("Welcome to Magic 8 Ball")
    question = input("Please enter your question here.\n")

    ans = [
        #Affirmative
        "It is certain\n",
        "Absolutely true\n",
        "Affirmative\n",
        "Unequivically Correct\n",
        "Yes\n\n",

        #Vague
        "Ask again later\n",
        "Ask something else\n",
        "My vision is clouded currently\n",
        "Unsure at the moment\n",
        "Please try again\n",

        
        #Negative
        "Never\n",
        "Not likely\n",
        "Not on your life\n",
        "No\n",
        "It is unlikely\n"

    ]
    print(random.choice(ans))
    time.sleep(5)

    clear()
