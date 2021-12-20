import user as u

action_list = ( 'Create new user',
                'Show users name',
                'Show user info',
                'Deleting user',
                'Change user attribute',
                'Exit program')


def show_action():
    #show menu list
    for i, action in enumerate(action_list, 1):
        print(i, action)

def add_user():
    #adding user
    name        = input('Name: ')
    sex         = input('Sex M/F: ')
    age         = input('Age: ')
    height      = input('Height[cm]: ')
    weight      = input('Weight[kg]: ')

    user        = name
    user        = u.user(name, sex, age, height, weight)
    
    return user

def show_users():
    print('---------------')
    print('Users:')
    print('---------------')
    for instance in u.user.instances:
        print(instance.name)

def choose_user(user_name):
    index = 0
    no_same_name = 0
    for instance in u.user.instances:
        if instance.name == user_name:
            no_same_name = no_same_name + 1
            user_no = index
        index = index + 1

    if no_same_name == 1:
        user_no = user_no
    elif no_same_name > 1:
        print('Number of users with the same name: ' + str(no_same_name))
        print('---------------')
        print('List of users with this name: ')
        for instance in u.user.instances:
            if instance.name == user_name:
                print('Imie: ' + instance.name)
                print('ID: ' + str(instance.id))
                print('Age: ' + str(instance.age))
                print('-------------')
        selected_id = input('Choose user with ID you want: ')
        index = 0
        for instance in u.user.instances:
            if instance.id == int(selected_id):
                user_no = index
            index = index + 1 
    else:
        print('There is no user in this database called: ' + user_name)
    
    return user_no   

def user_info(user_name, user_no):    
    #display user info
    print('---------------')
    print('User : ' + user_name + ' info')
    print('---------------')
    print('Name: ' + u.user.instances[user_no].name)
    print('ID: ' + str(u.user.instances[user_no].id))
    print('Sex: ' + u.user.instances[user_no].sex)
    print('Age: ' + str(u.user.instances[user_no].age))
    print('Height: ' + str(u.user.instances[user_no].height))
    print('Weight: ' + str(u.user.instances[user_no].weight))
    print('-------------')
    
def user_del(user_no):
    #delete user
    u.user.instances.pop(user_no)

    #shifting user id
    for x in range(user_no,len(u.user.instances)):
        u.user.instances[x].id = u.user.instances[x].id - 1


def change_user_attribute(user_no):
    attributs = ('Sex','Age','Height','Weight')

    for i, action in enumerate(attributs, 1):
        print(i, action)

    selected_number = int(input('Choose option: '))

    match selected_number:
        case 1:
            new_variable = input('New value: ')
            u.user.instances[user_no].sex = new_variable
        case 2:
            new_variable = input('New value: ')
            u.user.instances[user_no].age = new_variable
        case 3:
            new_variable = input('New value: ')
            u.user.instances[user_no].height = new_variable
        case 4:
            new_variable = input('New value: ')
            u.user.instances[user_no].weight = new_variable
        case __:
            print('')
            print('The number does not match the menu list!!!')
            print('')