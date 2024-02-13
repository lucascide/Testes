string = "lucas marcio lucas"

def qtdLucas(string, *passedKeys):
    words = string.split()
    dict = {}
    for key in passedKey:
        dict[key] = 0

        for w in words:
            if w.lower() == key:            
                dict[key] = dict[key] + 1
    return dict


print(qtdLucas(string, "lucas", "marcio"))