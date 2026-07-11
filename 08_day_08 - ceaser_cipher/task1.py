def greeting_with_location(name,location):
    print (f'Welcome {name}!')
    print (f'What is it like in {location}?')

'''
names = ['Michael', 'David', 'Susan']
locations = ['New York', 'Los Angeles', 'San Diego']
location = 0
for name in names:
    greeting_with_location(name,locations[location])
    location += 1
'''

my_name = input('Enter your name: ')
my_location = input('Enter your location: ')
greeting_with_location(location=my_location,name=my_name)

