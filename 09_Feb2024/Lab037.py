#Wreite a program that calculate and dispaly the grades between A to F #You have to use if ,elif ,else

marks = int(input("Enter your number"))

if marks >=90 and marks <= 100:
    print("Yoy got A grade")
elif marks >=80 and marks<= 89:
    print("You got a B grade")
elif marks >=70 and marks<= 79:
    print("You got a C grade")
elif marks >= 60 and marks<= 69:
    print("You got a D grade")
elif marks >= 0 and marks<=59:
    print("You have been failed")
else:
    print("Out of Marks")