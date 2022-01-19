class Person:
    def __init__(self, age,sex,bmi,children,smoker,region,charges):
        self.age=int(age)
        self.sex=sex
        self.bmi=float(bmi)
        self.children=int(children)
        self.smoker=smoker
        self.region=region
        self.charges=float(charges)
