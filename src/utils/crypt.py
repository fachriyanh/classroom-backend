
def enkripsi(password) :
    enkrps = []
    word = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+'
    for i in password :
        for j, x in enumerate (word) :
            if i == x :
                enkrps.append(word[(j+3)%(len(word))])
    string = ''.join(enkrps)
    return string

def dekripsi(enkripted) :
    dkrps = []
    word = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+'
    for i in enkripted :
        for j, x in enumerate (word) :
            if i == x :
                dkrps.append(word[(j-3)%(len(word))])
    string = ''.join(dkrps)
    return string