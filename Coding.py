def main():
     yourAnswer=input("Welcome to a story book adventure based on your choices, Please enter Yes to start ")
     if yourAnswer == "Yes":
         print("At any time press Enter to quit ")
         print("You wake up in laying on the side of the road, you see two paths to take one labelled Lerwick and one labelled Brickelwhyte, which road do you take? ") 
         print()
         print("1. Lerwick")
         print("2. Brickelwhyte")
         yourStart = input("Make your choice: ")
         print()
         if yourStart == "1":
              print("You see a old lady gestures for you to come over, do you? ") 
              print()
              print("1. Yes")
              print("2. No")
              yourOption= input("Make your choice: ")
              print()
              if yourOption == "1":
                   print("'Welcome,You seem lost, here take a weapon on the house to venture on' She spits out ") 
                   print("You see")
                   weaponsList = ['A Sword','Pair of Daggers', 'A Greatsword', 'A Axe']
                   print (', '.join(weaponsList))
                   print()
                   print("1. Sword")
                   print("2. Pair of Daggers")
                   print("3. Greatsword")
                   print("4. Axe")
                   yourWeapon= input("Make your choice: ")
                   print("'Hope you made the right choice' She crackles")
                   print()
               
         else:
              print("You see a chest, do you open it? ") 
              print("You slowly open the chest ") 
              print("You see")
              weaponsList = ['A Sword', 'Pair of Daggers', 'A Greatsword', 'A Axe']
              print (', '.join(weaponsList))
              print()
              print("1. Sword")
              print("2. Pair of Daggers")
              print("3. Greatsword")
              print("4. Axe")
              yourWeapon= input("Make your choice: ")
              print("'You hear the chest slam as you walk away")
              print()
         if yourWeapon == "1":
             print("Would you like to name your Sword?")
             print()
             print("1. Yes")
             print("2. No")
             option= input("Make your choice: ")
             if option == "1":
                  print()
                  yourWeaponName = input("Type in your weapon's name: ")
                  print("And so you begin your adventure you look at your Sword named {} ready to face the world".format(yourWeaponName))
             else:
                  print("And so you begin your adventure you look at your Sword ready to face the world")             
         elif yourWeapon == "2":
             print("Would you like to name your Pair of Daggers?")
             print()
             print("1. Yes")
             print("2. No")
             option= input("Make your choice: ")
             if option == "1":
                  print()
                  yourWeaponName = input("Type in your weapon's name: ")
                  print("And so you begin your adventure you look at your Pair of Daggers named {} ready to face the world".format(yourWeaponName))
             else:
                  print("And so you begin your adventure you look at your Pair of Daggers ready to face the world")
         elif yourWeapon == "3":
             print("Would you like to name your Greatsword?")
             print()
             print("1. Yes")
             print("2. No")
             option= input("Make your choice: ")
             if option == "1":
                  print()
                  yourWeaponName = input("Type in your weapon's name: ")
                  print("And so you begin your adventure you look at your Greatsword named {} ready to face the world".format(yourWeaponName))
             else:
                  print("And so you begin your adventure you look at your Greatsword ready to face the world")

         elif yourWeapon == "4":
             print("Would you like to name your Axe?")
             print()
             print("1. Yes")
             print("2. No")
             option= input("Make your choice: ")
             if option == "1":
                  print()
                  yourWeaponName = input("Type in your weapon's name: ")
                  print("And so you begin your adventure you look at your Axe named {} ready to face the world".format(yourWeaponName))
             else:
                  print("And so you begin your adventure you look at your Axe ready to face the world")
     else:
         print("The End")
main()



