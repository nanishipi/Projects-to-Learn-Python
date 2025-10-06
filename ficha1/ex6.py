mathematics = {'João': 3, 'Diogo': 4, 'Ana': 4, 'Catarina': 4, 'Francisco': 3, 'Joana': 5, 'Filipe': 2,
'Manuel': 5}

def query_grades(d, n):
    result = []
    grades = []
    
    for element in d.values():
        grades.append(element)

    i = -1
    for element in d:
        i += 1
        if element and grades[i] == n:
            result.append(element)
    return result
        
print(query_grades(mathematics, 5))        
