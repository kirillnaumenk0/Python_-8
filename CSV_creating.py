import csv

students = [
    "Surname", "Name", "Patronymic", "Phone", "Email", "Specialization", "Form of training", "Group"
]


def creating_cap():
    with open("data1.csv", "w") as file:
        write = csv.writer(file, delimiter=";")
        write.writerow(students)
    



