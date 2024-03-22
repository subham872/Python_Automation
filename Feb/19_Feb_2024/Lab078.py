# car - Class
# Objects-Tesla,Lamborgini

class Car:
    name = None
    model = None
    color = None
    speed = None
    engine = None

    def start_engine(self):
        print("Starting engine")

    def drive(self):
        print("Self Driving")

    def car_break(self):
        print("Break")

    def who_is_driving(self):
        print("I am driving" + self.model)


tesla_obj_ref = Car()
lambo_obj_ref = Car()

tesla_obj_ref.name = "Elon Musk"
lambo_obj_ref.name = "Ferrari"
tesla_obj_ref.model="Q5"

tesla_obj_ref.car_break()
tesla_obj_ref.who_is_driving()
lambo_obj_ref.who_is_driving()

