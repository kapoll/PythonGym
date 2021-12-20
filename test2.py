##program to testing


class A:
    instances = []
    def __init__(self, name, age):
        self.__class__.instances.append(self)
        self.id = len(A.instances)
        self.name = name
        self.age = age

a1 = A('Marek',18)
a2 = A('Jarek',22)
a3 = A('Darek',24)
a4 = A('Marek',44)


#change user attribute
def choose_user(select_name):
    no_same_name = 0
    index = 0
    for instance in A.instances:
        if instance.name == select_name:
            no_same_name = no_same_name + 1
            user_no = index
        index = index + 1

    if no_same_name == 1:
        user_no = user_no
    elif no_same_name > 1:
        print('Ilosc uzytkowników o takim imieniu: ' + str(no_same_name))
        print('---------------')
        print('Uzytkownicy o takim samym imieniu: ')
        for instance in A.instances:
            if instance.name == select_name:
                print('Imie: ' + instance.name)
                print('ID: ' + str(instance.id))
                print('Age: ' + str(instance.age))
                print('-------------')
        selected_id = input('Wybierz interesujące Cię ID uzytkownika: ')
        index = 0
        for instance in A.instances:
            if instance.id == int(selected_id):
                user_no = index
            index = index + 1
    else:
        print('Nie ma takiego chopa')
    
    return user_no

name = 'Marek'
user_no = choose_user(name)


print('-------------')
print('user: ' + name)
print('-------------')
print('ID: ' + str(A.instances[user_no].id))
print('Name: ' + A.instances[user_no].name)
print('Age: ' + str(A.instances[user_no].age))
print('-------------')

attributs = ('name','age')

for i, action in enumerate(attributs, 1):
    print(i, action)

selected_number = int(input('Choose option: '))

match selected_number:
    case 1:
        new_variable = input('nowa wartosc: ')
        A.instances[user_no].name = new_variable
    case 2:
        new_variable = input('nowa wartosc: ')
        A.instances[user_no].age = new_variable
    case __:
        print('')
        print('The number does not match the menu list!!!')
        print('')

print('user po zmianie: ' + name)
print('-------------')
print('ID: ' + str(A.instances[user_no].id))
print('Name: ' + A.instances[user_no].name)
print('Age: ' + str(A.instances[user_no].age))
'''
#deleting user tests
select_name = 'Marek'
no_same_name = 0
index = 0
for instance in A.instances:
    if instance.name == select_name:
        no_same_name = no_same_name + 1
        user_no = index
    index = index + 1

if no_same_name == 1:
    user_no = user_no
elif no_same_name > 1:
    print('Ilosc uzytkowników o takim imieniu: ' + str(no_same_name))
    print('---------------')
    print('Uzytkownicy o takim samym imieniu: ')
    for instance in A.instances:
        if instance.name == select_name:
            print('Imie: ' + instance.name)
            print('ID: ' + str(instance.id))
            print('Age: ' + str(instance.age))
            print('-------------')
    selected_id = input('Wybierz interesujące Cię ID uzytkownika: ')
    index = 0
    for instance in A.instances:
        if instance.id == int(selected_id):
            user_no = index
        index = index + 1
else:
    print('Nie ma takiego chopa')

A.instances.pop(user_no)

for x in range(user_no,len(A.instances)):
    A.instances[x].id = A.instances[x].id - 1
    

print('---------------')
print('Users:')
print('---------------')
for instance in A.instances:
    print(instance.name)
    print(instance.id)
    print('------------')
'''


'''
#/////user info tests/////
select_name = 'Marek'
index = 0
no_same_name = 0
for instance in A.instances:
    if instance.name == select_name:
        no_same_name = no_same_name + 1
        user_no = index
    index = index + 1

#print('user index: ' + str(user_no))

if no_same_name == 1:
    print('ID: ' + str(A.instances[user_no].id))
    print('Name: ' + A.instances[user_no].name)
    print('Age: ' + str(A.instances[user_no].age))
elif no_same_name > 1:
    print('Ilosc uzytkowników o takim imieniu: ' + str(no_same_name))
    print('---------------')
    print('Uzytkownicy o takim samym imieniu: ')
    for instance in A.instances:
        if instance.name == select_name:
            print('Imie: ' + instance.name)
            print('ID: ' + str(instance.id))
            print('Age: ' + str(instance.age))
            print('-------------')
    selected_id = input('Wybierz interesujące Cię ID uzytkownika: ')
    index = 0
    for instance in A.instances:
        if instance.id == int(selected_id):
            user_no = index
        index = index + 1
    print('ID: ' + str(A.instances[user_no].id))
    print('Name: ' + A.instances[user_no].name)
    print('Age: ' + str(A.instances[user_no].age))
else:
    print('Nie ma takiego chopa')
'''
