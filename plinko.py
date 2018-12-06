import random
import time
user_selection = 0


slot_prize_money = {2 : 100, 4 : 500, 6 : 1000, 8 : 0, 10 : 10000, 12 : 0, 14 : 1000, 16 : 500, 18 : 100}

def plinko():
  chip_count = 1
  wallet_amount = 0

  print("Welcome to the Plinko Simulator! Here's a free plinko chip to get started! Enter 3 to see options")

  while (True):
    user_selection = int(input("Enter selection now: "))

    if (user_selection == 3):
      print("Menu: Please select one of the following options: ")
      print("1 - Purchase more chips")
      print("2 - Drop a single chip")
      print("3 - Show options menu")
      print("4 - Quit the program")

    elif (user_selection == 4):
      print(f"You finished with ${wallet_amount}. Thanks for playing!")
      return False

    elif (user_selection == 1):
      new_chips = int(input("Chips are $800 each.  How many would you like?"))
      chip_count += new_chips
      wallet_amount -= (new_chips * 800)
      print(f"Great! That will be ${new_chips * 800} dollars. Your current balance is now ${wallet_amount} dollars and you have {chip_count} total chips. Enjoy your game!")
    
    elif (user_selection == 2):
      if (chip_count == 0):
        print("You need chips! Press 1 to buy more!")
      else:
        print("*** Drop single chip with visual! ***")
        chip_count -= 1
        start_slot = int(input("Which slot would you like to drop your chip into? (1-9)"))
        start_slot = (start_slot + 1) * 2 - 3
        if (start_slot > 17 or start_slot < 1):
          print("Invalid slot choice")
        else:
          board_size = 12
          wait_time = .04
          current_slot = float(start_slot)
          print("Path:")
          for x in range(0, board_size):            
            if (x % 2 == 0):
              row_list = "/ . . . . . . . . \\"
            else:
              row_list = "\. . . . . . . . ./"
            row_list = row_list[0:int(current_slot)] + 'O' + row_list[int(current_slot + 1):]
            if (x < board_size - 1):
              if (current_slot == 17):
                current_slot -= 1
              elif (current_slot == 1):
                current_slot += 1
              else:
                num = random.randint(1, 2) % 2
                if (num == 1):
                  current_slot += 1
                else:
                  current_slot -= 1
            print(row_list)
            time.sleep((random.randint(1, 10) / 10))
            # time.sleep(wait_time)


          mid_bottom_str = ".| | | | | | | | |."
          bottom_str = ".|_|_|_|_|_|_|_|_|."
          mid_bottom_str = mid_bottom_str[:int(current_slot)] + 'O' + mid_bottom_str[int(current_slot + 1):]
          bottom_str = bottom_str[:int(current_slot)] + 'O' + bottom_str[int(current_slot + 1):]
          print(mid_bottom_str)
          time.sleep(wait_time)
          print(bottom_str)
          time.sleep(wait_time)


          print(f"Winnings: ${slot_prize_money.get(current_slot)}") 
          wallet_amount += slot_prize_money.get(current_slot)
          print(f"Congrats! Your wallet now holds ${wallet_amount}!")  

    else:
      print("Invalid selection. Enter 3 to see options.")

plinko()
 