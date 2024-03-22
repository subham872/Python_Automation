#Custom Exception
class XYZ:
    def f1(self):
        try:
            a= int(input("Enter number one\n"))
        except Exception as e :
            print("Enter int value of a")
        else:
            print(a)
        finally:
            print("Anyhow i will be printed")


x = XYZ()
x.f1()