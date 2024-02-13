# Lists (muttable)

list1 = [1, 2, 3]

list1.append(4)
list1.pop(2)

print("lista 1 " + str(list1))

# Tupples (immutable)

tuple1 = (1, 2, 3)

print("tupla 1 " + str(tuple1))

# Setts (no order)

set1 = {1, 2, 3}
set2 = {1, 3 , 4}

set1.add(5)
set1.remove(2)

set3 = set1 & set2
set4 = set1.union(set2)

list1Set = set(list1)


print("set 4 " + str(set4))
print(set4.issuperset(set3))
print(set4.issubset(set3))

# Dictionaries (keys and values)

dict1 = {
    "nome": "Lucas",
    "idade": 20
}

dict1["peso"] = 74
del(dict1["idade"])

print("dict 1 " + str(dict1))
