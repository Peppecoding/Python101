class Employee:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def show_deatils(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Email: {self.email}")


class Programmer(Employee):
    def __init__ (self, name, email, programming_languagues):
        super().__init__(name,email)
        self.programming_lenaguages = programming_languagues

    def show_deatils(self):
        super().show_deatils()
        print(f"Programming languages: {self.programming_lenaguages}")

    def get_programming_languages(self):
        return self.programming_lenaguages
    
    def set_programming_languages(self, programming_languages):
        self.programming_lenaguages = programming_languages
        

programmer = Programmer("Peppe", "pepepeppe@gmail.com", ["Python", "Java"])

print("\n|-----( Before update )-----|\n")
programmer.show_deatils()

programmer.set_programming_languages(["Python", "Java","C++","C#"])
print('\n|------( After update )-----|\n')
programmer.show_deatils()


