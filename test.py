"""
VERSJA 1
import weakref

class A:
    instances = []
    def __init__(self, name, age):
        self.__class__.instances.append(weakref.proxy(self))
        self.name = name
        self.age = age

a1 = A('a1',18)
a2 = A('a2',22)

for instance in A.instances:
    print(instance.age)
"""

class A:
    instances = []
    def __init__(self, name, age):
        self.index = len(A.instances)
        self.__class__.instances.append(self)
        self.name = name
        self.age = age

a1 = A('Marek',18)
a2 = A('Jarek',22)


#print(A.instances[1].name)
#print(A.instances[1].index)
select_name = 'Jarek'

for instance in A.instances:
    if instance.name == select_name:
        #print(instance.name)
        #print(type(instance.index))
        #print(instance.index)
        user_no = instance.index
print('user index: ' + str(user_no))

print('Name: ' + str(A.instances[user_no].name))
print('Age: ' + str(A.instances[user_no].age))
'''
import user
import sys

def str_to_class(user):
    return getattr(sys.modules[__name__], user)

kamil = user.user('Kamil', 'M', 22, 185, 85)
Mati = user.user('Mateusz', 'F', 24, 220, 115)

imie = input('podaj imie: ')
#imie = str_to_class(imie)
imie = getattr(user.user, imie)
print(type(imie))
print(imie.name)
'''

'''
#wyswietl wszyskich uzytkownikow - imiona
for instance in A.instances:
    print(instance.name)
'''


'''
select_name = 'a1'

for instance in A.instances:
    if instance.name == select_name:
        print('dzien dobry '+ instance.name)
        print('Masz '+ str(instance.age) + ' lata')
'''