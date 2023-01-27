summ=0


def summ(x):
    try:
        count=0
        while len(x) >= 2:
            for i in x:
                count += int(i)
                x = str(count)
            count = 0
        return x
    except:
        return 'Введите цифры'


def summwith(x):
    try:
        count=0
        while len(x) >= 2:
            if count == '11' or count == '22' or count == '13' or count == '14' or count == '16' or count == '19' or count == '21':
                return x
                break
            else:
                for i in x:
                    count += int(i)
                x = str(count)
                count = 0
        return x
    except:
        return 'Введите цифры'

