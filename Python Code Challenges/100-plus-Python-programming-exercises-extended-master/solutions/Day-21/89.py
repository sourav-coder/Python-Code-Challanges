class person(object):
    def getGender(self):
        pass



class male(person):
    
    def getGender(self):
        
        print('Male')

class female(person):
    
    def getGender(self):
        print('Female')


x=male()
x.getGender()
