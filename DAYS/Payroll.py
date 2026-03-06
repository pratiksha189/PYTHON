from EmployeePortal import (Employee, SalariedEmployee, Manager)
class Payroll:
    @staticmethod
    def display_gross(employee:Employee):
        print(employee.calculate_gross())


    @staticmethod
    def display_net(employee:SalariedEmployee):
        print(employee.calculate_net())

se=SalariedEmployee(654,"prati",80000)
me=Manager(786,"pranita",98767,"HGGD9783J")


print(se)
Payroll.display_gross(se)
Payroll.display_net(se)