
class Person:
    def __init__(self,first_name,last_name,birth_date):
        self.first_name=first_name
        self.last_name=last_name
        self.birth_date=birth_date
        
    def get_age(self):
        age=2022-self.birth_date
        return age
    
    def get_full_name(self):
        full_name = self.first_name + ' ' +self.last_name
        return full_name
    def get_last_name(self):
        last_name=self.last_name
        return last_name

      
      
a=Person('Ravshan','Abdulrakhman',1950)
print(a.get_age())
print(a.get_last_name())

