glasnie = ['а', 'у', 'о', 'ы', 'э', 'е', 'ё', 'и',
           'ю', 'я', 'a', 'e', 'i', 'o', 'u', 'y']

soglasnie = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к',
             'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф',
             'х', 'ц', 'ч', 'ш', 'щ', 'b', 'c', 'd',
             'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
             'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

simbols = {1: ['а', 'и', 'с', 'ъ', 'a', 'j', 's'],
               2: ['б', 'й', 'т', 'ы', 'b', 'k', 't'],
               3: ['в', 'к', 'у', 'ь', 'c', 'l', 'u'],
               4: ['г', 'л', 'ф', 'э', 'd', 'm', 'v'],
               5: ['д', 'м', 'х', 'ю', 'e', 'n', 'w'],
               6: ['е', 'н', 'ц', 'я', 'f', 'o', 'x'],
               7: ['ё', 'о', 'ч', 'g', 'p', 'y'],
               8: ['ж', 'п', 'ш', 'h', 'q', 'z'],
               9: ['з', 'р', 'щ', 'i', 'r']}


def glassn(firstname, lastname, secondname):
    total = firstname + lastname + secondname
    count = ''
    for i in total:
        if i in glasnie:
            count += i
    total = count
    count = 0
    for i in simbols:
        for j in simbols.get(i):
            for n in total:
                if j == n:
                    count += i
    count=str(count)
    if count == '11' or count == '22' or count == '13' or count == '14' or count == '16' or count == '19':
        return count
    else:
        while len(count) >= 2:
            x = 0
            for i in count:
                x += int(i)
            count = str(x)
            x = 0
        return count


def soglas(firstname, lastname, secondname):
    total = firstname + lastname + secondname
    count = ''
    for i in total:
        if i in soglasnie:
            count += i
    total = count
    count = 0
    for i in simbols:
        for j in simbols.get(i):
            for n in total:
                if j == n:
                    count += i
    count = str(count)
    if count == '11' or count == '22' or count == '13' or count == '14' or count == '16' or count == '19':
        return count
    else:
        while len(count) >= 2:
            x = 0
            for i in count:
                x += int(i)
            count = str(x)
            x = 0
        return count




#def soglasnie(firstname,lastname,secondname):
#    total = firstname + lastname + secondname
#    count=0