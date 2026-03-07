from DAYS.DAY6.Day06_TAXPAYER import SalariedEmployee,ContractEmployee,Manager
import pickle
emp1=SalariedEmployee(101,"Prati",85000,"AHHB9098J")
emp2=ContractEmployee(102,"Pranita",1,5000,'fgfha787j')
mngr=Manager(103,"Ashish",89000,4500,"fgdhasd765j")
employees=[emp1,emp2,mngr]

with open('Day06_TAXPAYER.pkl','wb') as fw:

        try:
            for employee in employees:
                pickle.dump(employee,fw)
                print("data written")
        except IOError  as  e:
            print(e)


with open('Day06_TAXPAYER.pkl','wb') as fr:
    while True:
        try:
            data=pickle.load(fr)
            employee_data.append(data)


