a = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
c=''
# Не понравился вариант реализации
# a[1]='05'
# a[8]='+05'
# a.insert(1,'"')
# a.insert(3,'"')
# a.insert(5,'"')
# a.insert(7,'"')
# a.insert(-1,'"')
# a.insert(-3,'"')
#
# text = ''.join(a)
# print(text)
for key,i in enumerate(a):
    if (i[0] == '+'):
        b = i.replace('+','')
        c = '+'
    else:
        b = i
    if(b.isdigit() == True ):
        if (len(b) == 1):
            print('"' + c + '0' + b + '"', end=' ')
        else:
            print('"' + c + b + '"', end=' ')
    else:
        print(b, end=' ')
