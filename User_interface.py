from File_completion import writing_csv as wrc
from File_completion import reading_csv as rec


def choice():
    while True:
         print('Выберите дейстиве \n 1: Запись студента \n 2: Просмотр списка \n 3: Закрыть')
         choices = input("Ввод: ")
         if choices == '1':
            wrc()
         elif choices == '2':
            rec()
         elif choices == '3':
            break
         elif choices != '1' or '2' or '3':
            print('Error')  
         
