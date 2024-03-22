class GF:
    def car(self):
        return "Ambassador"

class Father(GF):
    def car(self):
        return "Alto"

class Son(Father):
    def car(self):
        return "Tiago"

subham=Son()
print(subham.car())