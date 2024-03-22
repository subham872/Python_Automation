# constructor
class Car:
    name = None
    make = None
    model = None

    def __init__(self, o_name, o_make, o_model):
        self.name=o_name
        self.make=o_make
        self.model=o_model

    def start_engine(self):
        print("Starting car with the name" + self.name)
        print("Starting car with the name" + self.make)
        print("Starting car with the name" + self.model)


lambo = Car("gini", "V2", "2024")
lambo.start_engine()

mahindra=Car("XUV","700","2023")
mahindra.start_engine()