"""
Задание 5 * (доп.)

Файл имеет вид таблицы: Фамилия Имя Отдел Зарплата (В первой строке заголовки колонок)
•	Посчитайте сколько отделов на фирме
•	Определите максимальную зарплату
•	Определите максимальную зарплату в каждом отделе
•	Выведите «Отдел Макс_Зарплата  Фамилия_человека_с_такой_зарплатой» в новый файл
Подсказка: используйте словари.
"""
if __name__ == "__main__":
    lbase=list()
    employees=list()
    d = dict()
    dict_of_departments = dict()
    with open(r'F:\Git\Homework\Homework6\Task5.txt', encoding='UTF-8', mode='r') as f:
        for line in f:
            if len(lbase) is 0:
                lbase = line.split()
                # print("lbase inside if", lbase)
            else:
                lval = line.split()
                # print("lvalues after split",lval)
                # print(l)
                d ={lbase[i]:lval[i] for i in range(0,len(lbase))}
                employees.append(d)
    # print(employees)
    all_departments=list()
    for element in employees:
        all_departments.append(element[lbase[2]])
    for i in range(len(all_departments)):
        dict_of_departments.update({all_departments[i] : all_departments.count(all_departments[i])})
    # print(d1)
    print("Quantity of departments is", len(dict_of_departments.keys()))
    list_of_salaries=list()
    for element in employees:
        list_of_salaries.append(int(element[lbase[3]]))
    # print(l2)
    print("Max salary in company is", max(list_of_salaries))

    list_of_departments = list(dict_of_departments.keys())
    employees_in_department = {i: list() for i in list_of_departments}
    for department in list_of_departments:
        for item in employees:
            if department in item.values():
                if employees_in_department[department] == []:
                    employees_in_department[department].append(item)
                else:
                    employees_in_department[department].append(item)
    # print(employees_in_department)
    dict_of_salaries_in_dep = {department:list() for department in list_of_departments}
    for department in list_of_departments:
         for employee in employees_in_department[department]:
            dict_of_salaries_in_dep[department].append(int(employee[lbase[3]]))
    # print(dict_of_salaries_in_dep)
    # print(list_of_departments)
    with open(r'F:\Git\Homework\Homework6\result_of_task5.txt', encoding='UTF-8', mode='w') as f:
        for department in list_of_departments:
            max_salary_in_dep = max(dict_of_salaries_in_dep[department])
            print("Max salary in", department, "is", max_salary_in_dep)
            index_of_max_salary = dict_of_salaries_in_dep[department].index(max(dict_of_salaries_in_dep[department]))
            # print(employees_in_department[department])
            name = employees_in_department[department][index_of_max_salary][lbase[0]]
            # print("The winner in", department, "is", name)
            f.write("Department is "+department+". Max salary is " + str(max_salary_in_dep) +". The winner of max salary is " + name + "\n")

