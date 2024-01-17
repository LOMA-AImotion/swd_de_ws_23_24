class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print(f"***** Hi, my name is {self.name}")

class Student(Person):
   def __init__(self, name, matriculation_id):
    super().__init__(name)
    self.matriculation_id = matriculation_id
  
   def greet(self):
     super().greet()
     print(f"and my mat id is {self.matriculation_id}")

p = Person("Caroline")
p.greet()
p2 = Person("Johann")
p2.greet()

s = Student("Francis", 14483)
s.greet()
