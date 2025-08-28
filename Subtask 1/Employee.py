from random import randint
class Employee:
    def __init__(self, name, family, manager=None):
      self._name = name
      self._id = randint(1000,9999)
      self._family = family.copy()
      self._manager = manager
      self.salary = 2500
    
    @property
    def id(self) -> int:
     return self._id
    @property
    def manager(self):
        return self._manager
    @property
    def family(self) -> dict:
      return dict(self._family)
    
    def apply_raise(self, managed_employee: 'Employee', raise_percent: int):
        if not isinstance(managed_employee,Employee):
            raise ValueError("The target should be an Employee")
        if managed_employee.manager!=self :
            #print(f"{self._name} is not the manager of {managed_employee._name}")
            return f"{self._name} is not the manager of {managed_employee._name}"
        increase = managed_employee.salary*(raise_percent/100)
        managed_employee.salary +=increase
        print(f"New salary for {managed_employee._name}: {managed_employee.salary}")


##### Test code: #####..
if __name__ == '__main__':
  boss = Employee('Jane Redmond', {})
  name = 'John Smith'
  family = {
    'Son': {
      'Insured': True,
      'Age': 16
    },
    'Wife': {
      'Insured': False,
      'Age': 32
    }
  }
  my_employee = Employee(name, family, boss)
  not_boss = Employee('Adam Cater', {})
  # do not change:
  print(id(my_employee.family))
  print(id(my_employee._family)) # should be different
  boss.apply_raise(my_employee, 25)
  print(not_boss.apply_raise(my_employee, 25))