class Agile:
    def create(self):
        print("Forming class Agile")

class Dev(Agile):
    def create(self):
        print("Forming class Dev")

class QA(Agile):
    def create(self):
        print("Forming class QA")

class Sprint(QA, Dev):
    pass

sprint = Sprint()
sprint.create()