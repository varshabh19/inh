class father:
    def __init__(self, surname, name):
        self.surname = surname
        self.father_name = name

    def display_surname(self):
        print("Surname is:", self.surname)

    def display_father_name(self):
        print("Father name is:", self.father_name)


class mother:
    def __init__(self, eye_color, name):
        self.eye_color = eye_color
        self.mother_name = name

    def display_eye_color(self):
        print("Eye color is:", self.eye_color)

    def display_mother_name(self):
        print("Mother name is:", self.mother_name)


class son(father, mother):
    def __init__(self, name, surname, father_name, eye_color, mother_name):
        self.name = name
        father.__init__(self, surname, father_name)
        mother.__init__(self, eye_color, mother_name)

    def display_name(self):
        print("Name is:", self.name)

son_obj = son("rajesh", "k", "Rajesh", "blue", "rani")
son_obj.display_surname()
son_obj.display_father_name()
son_obj.display_eye_color()
son_obj.display_mother_name()
son_obj.display_name()

