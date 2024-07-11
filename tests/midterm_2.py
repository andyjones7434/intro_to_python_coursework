import random
def readysetgo():

        arr = ["1", "2", "3", "4"]

        random.shuffle(arr)

        print(arr)

        return arr


def main():
    balance = 200
    end = False

    print("Welcome to horse betting!\n")

    '''print(" Exacta.Takes as input a two element array (for Python use list) with their bets, a four element array of the "
          "winning sequence,\n and returns true if they win the exacta\n\n Exactabox.  Takes as input a two element array "
          "(for Python use list) with their bets, a four element array of the winning sequence,\n and returns true if they "
          "win the exacta box\n\n Trifecta.  Takes as input a three element array (for Python use list) with their bets, a "
          "four element array of the winning sequence,\n and returns true if they win the trifecta\n\n Trifectabox.  "
          "Takes as input a three element array (for Python use list) with their bets, a four element array of the winning "
          "sequence,\n and returns true if they win the trifecta box\n")'''

    while end == False:

        horses = readysetgo()

        choice = input("please select bet type from the following options 1-6:\n 1) Place an EXACTA bet = Price: 15 USD\n "
                       "2) Place an EXACTABOX bet = Price: 10 USD\n 3) Place a TRIFECTA bet = Price: 20 USD\n 4) Place a "
                       "TRIFECTABOX bet = Price: 18 USD\n 5) BALANCE\n 6) EXIT\n Please enter type of bet no spaces:\n").upper()

        if choice == "EXACTA":

            horse = input("Please enter two horses below seperated by a space:\n")
            horse = horse.split()

            if (horse[0] == horses[0]) and (horse[1] == horses[1]):
                balance = balance + 150
                print("balance =", end=" ")
                print(balance, end=" ")
                print("USD")
                print("You are the winner!")
            else:
                balance = balance - 15
                print("Sorry you lost")
                print("balance =", end=" ")
                print(balance, end=" ")
                print("USD")

        elif choice == "EXACTABOX":

            horse = input("Please enter two horses below seperated by a space:\n")
            horse = horse.split()

            if ((horse[0] == horses[0]) or (horse[0] == horses[1])) and ((horse[1] == horses[0]) or (horse[1] == horses[1])):
                balance = balance + 100
                print("balance =", end=" ")
                print(balance, end=" ")
                print("USD")
                print("You are the winner!")
            else:
                balance = balance - 10
                print("Sorry you lost")
                print("balance =", end=" ")
                print(balance, end=" ")
                print("USD")

        elif choice == "TRIFECTA":

            horse = input("Please enter three horses below seperated by a space:\n")
            horse = horse.split()

            if (horse[0] == horses[0]) and (horse[1] == horses[1]) and (horse[2] == horses[2]):
                balance = balance + 250
                print("balance =", end=" ")
                print(balance, end=" ")
                print("USD")
                print("You are the winner!")
            else:
                balance = balance - 20
                print("Sorry you lost")
                print("balance =", end=" ")
                print(balance, end=" ")
                print("USD")

        elif choice == "TRIFECTABOX":

            horse = input("Please enter three horses below seperated by a space:\n")
            horse = horse.split()

            if (((horse[0] == horses[0]) or (horse[0] == horses[1]) or (horse[0] == horses[2])) and
                    ((horse[1] == horses[0]) or (horse[1] == horses[1]) or (horse[1] == horses[2])) and
                    ((horse[2] == horses[0]) or (horse[2] == horses[1]) or (horse[2] == horses[2]))):
                balance = balance + 180
                print("balance =", end=" ")
                print(balance, end=" ")
                print("USD")
                print("You are the winner!")

            else:
                balance = balance - 18
                print("Sorry you lost")
                print("balance =", end=" ")
                print(balance, end=" ")
                print("USD")

        elif choice == "BALANCE":
            print("balance =", end=" ")
            print(balance, end=" ")
            print("USD\n")

        elif choice == "EXIT":
            end=True


main()
