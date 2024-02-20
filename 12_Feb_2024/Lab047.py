#Match case
#switch case

number = int(input("Enter a number\n"))

match number:
    case 1:
        print("you have entered 1")
    case 2:
        print("you have entered two")
    case 3:
        print("you have entered 3")
    case _:
      print("Outside the case statemnet")