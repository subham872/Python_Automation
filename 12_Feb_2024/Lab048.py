browser = input("Name of my browser\n")
match browser:
    case "Google":
        print("You are using chrome")
    case "Firefox":
        print("You are using Mozzila")
    case _:
        print("No browser")
