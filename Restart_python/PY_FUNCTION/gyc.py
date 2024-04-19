class Perent:
    def Kinal(self):
        print("Perent")
class Child(Perent):
    def Kinal(self):

        super().Kinal()
p=Child()
print(p.Kinal())

    