class Grandfather:
    def __init__(self,hobby):
        self.hobby = hobby
class father(Grandfather):  # Parent class
    def __init__(self,name,age,hobby):
        super().__init__(hobby)
        self.name = name
        self.age = age

    def info(self):
        print(self.name,self.age,self.hobby)

class son(father):
    def __init__(self,name,age,job_title,hobby):
        super().__init__(name,age,hobby)
        self.job_title = job_title

    def info(self):
        # Override and extend parent's method
        print(f"Name: {self.name}, Age: {self.age}, Job: {self.job_title}, {self.hobby}")


aharon = father("aharon",10,"run")
amit = son("amit",5,"coding","hi")

aharon.info()
amit.info()

