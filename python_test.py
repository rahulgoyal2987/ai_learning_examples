
# Parent class 1
class Father:
    def __init__(self):
        print("hi")
    def __init__(self, name):
        print(f"Father initialized")
    def skills(self):
        print("Father: Gardening, Carpentry")

# Parent class 2
class Mother:
    def __init__(self):
        print("mother initialized")
    def __init__(self, name="Mother"):
        print(f"mother initialized")
    def skills(self):
        print("Mother: Cooking, Painting")

# Child class inheriting from both Father and Mother
class Child(Father, Mother):
    def __init__(self, name="Child"):
        Father.__init__(self, name)  # Initialize Father with name
        Mother.__init__(self, name)  # Initialize Mother with name
        print(f"{name} initialized")
    def skills(self):
        #super().skills()  # Call the skills method from both parents
        super(Child, self).skills()
        # calls mother's skills
        Mother.skills(self)
        # can id Mother.skills(self) using super() as well

Child().skills()