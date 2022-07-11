class Geeks: 
     def __init__(self): 
          self._idade = 0
     def get_idade(self): 
         print("Get idade") 
         return self._idade   
     def set_idade(self, a): 
         print("setter idade") 
         self._idade = a 
     def del_idade(self): 
         del self._idade 
     idade = property(get_idade, set_idade, del_idade)    
mark = Geeks()   
mark.idade = 10 
print(mark.idade)