class Physicist:
    def __init__(self,name,iq=120,looks='handsom',subject='physics'):
        self.name=name
        self.iq=iq
        self.looks=looks
        self.subject=subject

    def research(self,field):
        print("{0} research {1}".format(self.name,field))

    def speak(self):
        print("My name is ",self.name)
        print("I am ",self.looks)
        print("Intelligence is ",self.iq)
        print("I like ",self.subject)

class ExpermentalPhysicist(Physicist):
    def __init__(self,main_study,name,iq=120,looks='handsom',subject='physics'):
        self.main_study=main_study
        super().__init__(name,iq,looks,subject)

    def experiment(self):
        print("{0} is in Physics Lab.".format(self.name))

class TheoreticalPhysicist(Physicist):
    def __init__(self,theory,name,iq=120,looks='handsom',subject='physics'):
        self.theory=theory
        super().__init__(name,iq,looks,subject)

    def research(self,field,base):
        super().research(field)
        print("My theory is {},it is based on {}".format(self.theory,base))


einstein=TheoreticalPhysicist('Belativity','Albert_einstein',iq=160,looks='Hair is prety')