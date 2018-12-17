import menu 

from student_function import *


def choose():
    # 選擇
    docs = []  # 此列表用來儲存所有學生訊息
    while True:
        menu.show_menu()
        choose = str(input('選擇功能：'))
        if choose == '1':
            docs += input_stud()
        elif choose == '2':
            output_stud(docs)
        elif choose == '3':
            output_stud(docs)
            modify(docs)
            output_stud(docs)
        elif choose == '4':
            Del_Sort(docs)
        elif choose == '5':
            GradeSort_Big(docs)
        elif choose == '6':
            GradeSort_Samll(docs)
        elif choose == '7':
            AgeSort_Big(docs)
        elif choose == '8':
            AgeSort_Samll(docs)
        elif choose == '9':
            Save_Function(docs)
        elif choose == '10':
            flusho(filename='student.txt')
        elif choose == 'q':
            print('退出')
            break
        else:
            print('重新選擇')


choose()
