import time


def input_stud():
    # 登入學生訊息
    L = []
    while True:
        n = str(input('輸入姓名:'))
        if not n:
            break
        a = str(input('輸入年齡:'))
        g = str(input('輸入成績:'))
        stud = {}
        stud['name'] = n
        stud['age'] = a
        stud['grade'] = g
        L.append(stud)
    return L


def output_stud(L):
    # 顯示學生訊息
    print('+------------+-------+-------+\n')
    print('|    name    |  age  | grade |\n')
    print('+------------+-------+-------+\n')
    for stud in L:
        t = (stud['name'].center(12),
             str(stud['age']).center(7),
             str(stud['grade']).center(7))
        line = "|%s|%s|%s|" % t
        print(line+'\n')
    print('+------------+-------+-------+\n')
    time.sleep(1)


def modify(lst):
    # 修改
    name = str(input('修改學生姓名：'))
    for d in lst:
        if d['name'] == name:
            age = int(input('輸入新年齡:'))
            d['age'] = age
            grade = int(input('輸入新成績:'))
            d['grade'] = grade
        else:
            print('沒找到', name)


def Del_Sort(lst):
    # 刪除學生訊息
    name = str(input('要刪除學生姓名：'))
    for x in range(len(lst)):
        if lst[x]['name'] == name:
            del lst[x]
            print('成功刪除：', name, '的訊息')
            return True
    else:
        print('查無此學生')


def GradeSort_Big(L):
    # 成績高到低
    L = sorted(L, key=lambda d: d['grade'], reverse=True)
    output_stud(L)


def GradeSort_Samll(L):
    # 成績低到高
    L = sorted(L, key=lambda d: d['grade'])
    output_stud(L)


def AgeSort_Big(L):
    # 成績高到低
    L = sorted(L, key=lambda d: d['age'], reverse=True)
    output_stud(L)


def AgeSort_Samll(L):
    # 成績低到高
    L = sorted(L, key=lambda d: d['age'])
    output_stud(L)


def Save_Function(lst, filename='student.txt'):
    try:
        f = open(filename,'w') #打開文件
        f.write('+------------+-------+-------+\n')
        f.write('|    name    |  age  | grade |\n')
        f.write('+------------+-------+-------+\n')
        for x in lst:
            t = (x['name'].center(12),
                str(x['age']).center(7),
                str(x['grade']).center(7))
            line = "|%s|%s|%s|" % t
            f.write(line+'\n')
        f.write('+------------+-------+-------+\n')
        print('寫入成功')
    except:
    	print('寫入失敗')
    f.close() #關閉文件



def flusho(filename='student.txt'):
	try:
		f = open(filename,'r')
		for x in f: # x綁定末尾到'\n'的字串
			n = str(x.rstrip()) #把n轉成字串 去掉'\n'
			print(n)
		f.close()
	except:
		print('失敗')
