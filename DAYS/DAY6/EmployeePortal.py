from abc import ABC,abstractmethod

class Employee(ABC):
    def __init__(self,empid,name):
        self._empid=empid
        self._name=name

    @abstractmethod
    def calculate_gross(self):
        pass

    def __str__(self):
        return f'EMPLOYEE ID= {self._empid}\t \'EMPLOYEE NAME\'={self._name}'

class SalariedEmployee(Employee):
    def __init__(self,empid,name,basic):
        super().__init__(empid,name)
        self._basic=basic

    def calculate_gross(self):
        hra=self._basic*0.4
        da=self._basic*0.12
        return self._basic+hra+da

    def calculate_net(self):
        gross=self.calculate_gross()
        pf=gross*0.12
        return gross-pf


class ContractEmployee(Employee):
    def __init__(self,empid,name,day,rate):
        super().__init__(empid,name)
        self._day=day
        self._rate=rate


    def calculate_gross(self):
        total=self._day*self._rate
        return total

class Manager(SalariedEmployee):
    def __init__(self,empid,name,basic,allowance):
        super().__init__(empid,name,basic)
        self._allowance=allowance

    def calculate_gross(self):
        total=self._allowance+super().calculate_gross()
        return total

#
# emp1=SalariedEmployee(101,"Prati",85000)
# emp2=ContractEmployee(102,"Pranita",1,5000)
# mngr=Manager(103,"Ashish",89000,4500)
#
# print("==========================================================")
# print("SalariedEmployee")
# print(emp1)
# print("GROSS = ",emp1.calculate_gross())
# print("NET = ",mngr.calculate_gross())
#
# print("==========================================================")
# print("ContractEmployee")
# print(emp2)
# print("GROSS = ",emp2.calculate_gross())
#
# print("==========================================================")
# print("Manager")
# print(mngr)
# print("GROSS = ",mngr.calculate_gross())
# print("NET = ",mngr.calculate_net())
# print("==========================================================")