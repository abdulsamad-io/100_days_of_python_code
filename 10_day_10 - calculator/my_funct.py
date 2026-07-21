def my_funct(f_name, l_name):
    if f_name == '' and l_name == '':
        return
    f_name_tcase = f_name.title()
    l_name_tcase = l_name.title()
    return f'{f_name_tcase} {l_name_tcase}'



f_name = input('Enter your first name: ')
l_name = input('Enter your last name: ')

print(my_funct(f_name=f_name, l_name=l_name))

#  print (output)


