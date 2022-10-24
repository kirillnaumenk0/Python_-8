import csv


def write_students():
    surnames = []
    names = []
    patronymics = []
    phones = []
    emails = []
    specializations = []
    form_of_trainings = []
    groups = []
    while True:
        surname = input('Введите фамилию, или команду (end) для завершения ')
        if surname == 'end':
            break
        name = input('Имя: ')
        patronymic = input('Отчество: ')
        phone = input('Номер телефона: ')
        email = input('Email: ')
        specialization = input('Специальность: ')
        form_of_training = input('Форма обучения: ')
        group = input('Введите группу: ')
        surnames.append(surname)
        names.append(name)
        patronymics.append(patronymic)
        phones.append(phone)
        emails.append(email)
        specializations.append(specialization)
        form_of_trainings.append(form_of_training)
        groups.append(group)

    students_list = {}
    for i in range(len(surnames)):
        key = i + 1
        students_list[key] = []
        students_list[key].append(surnames[i])
        students_list[key].append(names[i])
        students_list[key].append(patronymics[i])
        students_list[key].append(phones[i])
        students_list[key].append(emails[i])
        students_list[key].append(specializations[i])
        students_list[key].append(form_of_trainings[i])
        students_list[key].append(groups[i])

    return students_list


def writing_csv():
    with open("data1.csv", "a", newline='') as file:
        book = write_students()
        for value in book.values():
            writer = csv.writer(file, delimiter=';', quotechar='"')
            writer.writerow(value)


def reading_csv():
    with open("data1.csv", "r") as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            print(row)



        