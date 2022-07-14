class Human:
    def __init__(self, n, o):
    #properties of class Human
        self.name = n               
        self.occupation = o 
    #Methods of class Human
    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name,"plays tennis.")
        elif self.occupation == "actor":
            print(self.name,"acts on films.")
    def speaks(self):
        print(self.name,"says how are you?")
    
tom = Human("Tom Cruise","actor")
tom.do_work()
tom.speaks()

john = Human("John Isner","tennis player")
john.do_work()
john.speaks()