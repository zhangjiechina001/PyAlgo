from abc import ABCMeta,abstractmethod

class Plane(object):
    def __init__(self):
        self.color='black'
        self.lift_left=100

    def fire(self):
        pass

    @abstractmethod
    def trun(self,direction):
        print('base turn')

class Plane1(Plane):
    def __init__(self):
        Plane.__init__(self)

    def trun(self,direction):
        print('Plane1 turn')


if(__name__=='__main__'):
    p=Plane1()
    p.trun(None)
    p=Plane()
    p.trun(None)