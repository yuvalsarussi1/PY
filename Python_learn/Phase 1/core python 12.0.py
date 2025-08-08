import os
class person:
    def __init__(self,name,age,hobby):
        self.name = name
        self.age = age
        self.hobby = hobby
    
    def greet(self):
        print(self.name,self.age,self.hobby)
    
    def save_to_file(self, filepath):
         with open(filepath, "a") as file:
                file.write(f"{self.name},{self.age},{self.hobby}\n")
               



# amit = person("amit",18,"coding")
# shachar = person("shachar",10,"minecraft")

people = []
with open("Python_learn/Phase 1/people.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                name, age, hobby = line.strip().split(",")
                age_int = int(age)
                p = person(name,age_int,hobby)
                people.append(p)

leri = person("leri",30,"running")
leri.save_to_file("Python_learn/Phase 1/people.txt")
people.append(leri)

for i in people:
    i.greet()
