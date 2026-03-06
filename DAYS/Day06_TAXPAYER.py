from abc import ABC,abstractmethod


class TaxPayer(ABC):
    def __init__(self,pan):
        self._pan=pan

    @abstractmethod
    def calculate_tax(self):
        pass

    def __str__(self):
        return f'{self._pan}'
#------------------------------------------------------------------------------
class Employee(ABC):
    def __init__(self,empid,name):
        self._empid=empid
        self._name=name

    @abstractmethod
    def calculate_gross(self):
        pass

    def __str__(self):
        return f'EMPLOYEE ID= {self._empid}\t \'EMPLOYEE NAME\'={self._name}'
#------------------------------------------------------------------------------
class SalariedEmployee(Employee,TaxPayer):
    def __init__(self,empid,name,basic,pan):
        # super().__init__(empid,name)
        # super().__init__(pan)
        Employee.__init__(self, empid, name)
        TaxPayer.__init__(self,pan)
        self._basic=basic

    def calculate_gross(self):
        hra=self._basic*0.4
        da=self._basic*0.12
        return self._basic+hra+da

    def calculate_net(self):
        gross=self.calculate_gross()
        pf=gross*0.12
        return gross-pf

    def calculate_tax(self):
        pass

#------------------------------------------------------------------------------
class ContractEmployee(Employee,TaxPayer):
    def __init__(self,empid,name,day,rate,pan):
        # super().__init__(empid,name)
        # super().__init__(pan)
        Employee.__init__(self, empid, name)
        TaxPayer.__init__(self, pan)
        self._day=day
        self._rate=rate


    def calculate_gross(self):
        total=self._day*self._rate
        return total

    def calculate_tax(self):
        pass
#------------------------------------------------------------------------------
class Manager(SalariedEmployee):
    def __init__(self,empid,name,basic,allowance,pan):
        super().__init__(empid,name,basic,pan)
        self._allowance=allowance


    def calculate_gross(self):
        total=self._allowance+super().calculate_gross()
        return total

    def calculate_tax(self):
        pass
#------------------------------------------------------------------------------
emp1=SalariedEmployee(101,"Prati",85000,"AHHB9098J")
emp2=ContractEmployee(102,"Pranita",1,5000,'fgfha787j')
mngr=Manager(103,"Ashish",89000,4500,"fgdhasd765j")
#------------------------------------------------------------------------------
print("==========================================================")
print("SalariedEmployee")
print(emp1)
print("GROSS = ",emp1.calculate_gross())
print("NET = ",mngr.calculate_gross())

print("==================@========================================")
print("ContractEmployee")
print(emp2)
print("GROSS = ",emp2.calculate_gross())

print("==========================================================")
print("Manager")
print(mngr)
print("GROSS = ",mngr.calculate_gross())
print("NET = ",mngr.calculate_net())
print("==========================================================")