def summkod(x,y,z):
    x=x+y+z
    summ=0

    simbols = {1: ['а', 'и', 'с', 'ъ', 'a', 'j', 's'],
               2: ['б', 'й', 'т', 'ы', 'b', 'k', 't'],
               3: ['в', 'к', 'у', 'ь', 'c', 'l', 'u'],
               4: ['г', 'л', 'ф', 'э', 'd', 'm', 'v'],
               5: ['д', 'м', 'х', 'ю', 'e', 'n', 'w'],
               6: ['е', 'н', 'ц', 'я', 'f', 'o', 'x'],
               7: ['ё', 'о', 'ч', 'g', 'p', 'y'],
               8: ['ж', 'п', 'ш', 'h', 'q', 'z'],
               9: ['з', 'р', 'щ', 'i', 'r']}
    for i in simbols:
        for j in simbols.get(i):
            for n in x:
                if j == n:
                    summ+=i
        a=str(summ)
        b=0
        while len (a)>=2:
            for i in a:
                b+=int(i)
            a=str(b)
            b=0
    a=int(a)
    return (a)