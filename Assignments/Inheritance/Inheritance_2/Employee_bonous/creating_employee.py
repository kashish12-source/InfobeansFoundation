from employee import Developer ,Intern ,Manager
from storage import store_data,fetch_data

dev = Developer("kashish",101,2000000)
man= Manager("Piyush",102,3000000)
inte = Intern("koshiki",103,200000)

employees = [dev,man,inte]

store_data(employees)
emp = fetch_data()

print(emp)
