import list_of_actions as loa
import sys

print('---Welcome in fitness program---')

selected_menu_number = 0

while selected_menu_number != 6:
    print('---------------')
    loa.show_action()
    print('---------------')
    selected_menu_number = int(input('Choose option from menu: '))

    match selected_menu_number:
        case 1:
            loa.add_user()
        case 2:
            loa.show_users()
        case 3:
            loa.show_users()
            user_name = input('Type user name: ')
            user_no = loa.choose_user(user_name)
            loa.user_info(user_name, user_no)
        case 4:
            loa.show_users()
            user_name = input('Type user name: ')
            user_no = loa.choose_user(user_name)
            loa.user_del(user_no)
        case 5:
            loa.show_users()
            user_name = input('Type user name: ')
            user_no = loa.choose_user(user_name)
            loa.user_info(user_name, user_no)
            loa.change_user_attribute(user_no)
        case 6:
            sys.exit(0)
        case __:
            print('')
            print('The number does not match the menu list!!!')
            print('Choose again')