# Day 3: Register Check

'''TODO'''

'''
Write a function called register_check that checks how many
students are in school. The function takes a dictionary as a
parameter. If the student is in school, the dictionary says 'yes'. If
the student is not in school, the dictionary says 'no'. Your
function should return the number of students in school. Use the
dictionary below. Your function should return 3.
'''
register = {'Michael': 'yes', 'John': 'no',
            'Peter': 'yes', 'Mary': 'yes'}


def register_check(register):
    number_of_students_in_school = []

    for k, v in register.items():
        if v == 'yes':
            number_of_students_in_school.append(k)
            number_total_of_students = len(number_of_students_in_school)
    print(f"  The number of students in school é: {number_total_of_students} and the list of students are {number_of_students_in_school}")

    return number_of_students_in_school


register_check(register)

'''TODO'''

'''
Extra Challenge: Lowercase Names

names = ["kerry", "dickson", "John", "Mary", 
 "carol", "Rose", "adam"]
You are given a list of names above. This list is made up of names 
of lowercase and uppercase letters. Your task is to write a code 
that will return a tuple of all the names in the list that have only
lowercase letters. Your tuple should have names sorted 
alphabetically in descending order. Using the list above, your 
code should return:
('kerry', 'dickson', 'carol', 'adam')

'''
'''
Escrever um código
que retornará uma tupla de todos os nomes da lista que possuem apenas
letras minúsculas. 

'''

try:
    names = ["adam","kerry", "dickson", "John","Mary", 
   "carol", "Rose" ]
   
    def return_lowercase(names):
        letras_minusculas= []
        for l in names:
            if l[0] == l[0].lower():
                letras_minusculas.append(l)
        letras_minusculas.sort()        
        print(tuple(letras_minusculas))
        return  tuple(letras_minusculas)
except:
    raise Exception("Sorry")


return_lowercase(names)