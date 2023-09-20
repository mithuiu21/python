class Human:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o

    def do_work(self):
        if self.occupation == "cricket player":
            print(self.name, "plays cricket")
        elif self.occupation == "actor":
            print(self.name, "shoots film")
    
    def speaks(self):
        print(self.name, "says how are you?")


tom = Human("tom cruise", 'actor')
tom.do_work()
tom.speaks()


sakib = Human("sakib al hasan", "cricket player")
sakib.do_work()
sakib.speaks()
