class Team:
    def show_Team(self):
        print("This is our team")

# Testing class inherited from Team
class Testing(Team):
    TestingName = ""

    def show_Testing(self):
        print(self.TestingName)

# Dev class inherited from Team
class Dev(Team):
    DevName = ""

    def show_Dev(self):
        print(self.DevName)

# Sprint class inherited from Testing and Dev classes
class Sprint(Testing, Dev):
    def show_parent(self):
        print("Testing: ",self.TestingName)
        print("Dev: ",self.DevName)

s1 = Sprint()
s1.TestingName = "James"
s1.DevName = "Barter"
s1.show_Team()
s1.show_parent()