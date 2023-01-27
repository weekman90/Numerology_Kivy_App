import summdate
def чжп(bday, bmonth, byear):
    try:
        if len(bday) == 1:
            bday = '0' + bday
        if len (bmonth) == 1:
            bmonth = '0' + bmonth
        чжп = int(bday[0]) + int(bday[1]) + int(bmonth[0]) + int(bmonth[1]) +\
              int(byear[0]) + int(byear[1]) + int(byear[2]) + int(byear[3])
        чжп = str(чжп)
        while len(чжп) >= 2:
            if чжп == '11' or чжп == '22' or чжп == '33' or чжп == '44':
                break
            count = 0
            for i in чжп:
                count += int(i)
            чжп = str(count)
            count = 0
        return чжп
    except:
        return 'Введите цифры'

def чжп2(bday, bmonth, byear):
    try:
        if len(bday) == 1:
            bday = '0' + bday
        if len(bmonth) == 1:
            bmonth = '0' + bmonth
        чжп = int(bday[0]) + int(bday[1]) + int(bmonth[0]) + int(bmonth[1]) + \
              int(byear[0]) + int(byear[1]) + int(byear[2]) + int(byear[3])
        чжп = str(чжп)
        while len(чжп) >= 2:
            if чжп == '11' or чжп == '22' or чжп == '33' or чжп == '44':
                break
            count = 0
            for i in чжп:
                count += int(i)
            чжп = str(count)
            count = 0
            break
        return чжп
    except:
        return 'Введите цифры'


def bday0(bday):
    try:
        count = int(bday[0])*2
        return count
    except:
        return 'Введите цифры'

def bday0summ(bday, bmonth, byear):
    try:
        if len(bday) == 1:
            bday = '0' + bday
        if len(bmonth) == 1:
            bmonth = '0' + bmonth
        чжп = int(bday[0]) + int(bday[1]) + int(bmonth[0]) + int(bmonth[1]) \
              + int(byear[0]) + int(byear[1]) + int(byear[2]) + int(byear[3])
        чжп = str(чжп)
        count = int(чжп) - int(bday[0]) * 2
        count = str(count)
        x = 0
        for i in count:
          x += int(i)
        return x
    except:
        return 'Введите цифры'


def First_number_row(bday, bmonth, byear):
    try:
        if len(bday) == 1:
            bday = '0' + bday
        if len(bmonth) == 1:
            bmonth = '0' + bmonth
        чжп = int(bday[0])+int(bday[1])+int(bmonth[0])+int(bmonth[1])+\
              int(byear[0])+int(byear[1])+int(byear[2])+int(byear[3])
        чжп = str(чжп)
        return чжп
    except:
        return 'Введите цифры'






