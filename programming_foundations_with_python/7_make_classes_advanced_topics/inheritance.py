# 5. Class Parent
class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

    # 10. Reusing Methods
    def show_info(self):
        print("Last Name: " + self.last_name)
        print("Eye Color: " + self.eye_color)

# 7. Class Child
class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor Called")

        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys
    # 11. Methods Overriding
    def show_info(self):
        print("Last_name: " + self.last_name)
        print("Eye Color: " + self.eye_color)
        print("Number of Toys: " + str(self.number_of_toys))

billy_cyurs = Parent("Cyrus", "blue")
# billy_cyurs.show_info()

miley_cyurs = Child("Cyrus", "blue", 5)
miley_cyurs.show_info()
