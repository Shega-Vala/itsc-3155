class Person: #class named Person
    
    def __init__(self, name): # The __init__ method is roughly what represents a constructor in Python 
        self.name = name
        
p1 = Person("John") #first person is John
p2 = Person("Bob")  #second person is John
print(p1.name) #call first person
print(p2.name) #call second person 