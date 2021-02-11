a = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for key, i in enumerate(a):
    parts = i.split(' ')
    name = list(reversed(parts))
    print('Привет, ' + name[0].title() + '!')