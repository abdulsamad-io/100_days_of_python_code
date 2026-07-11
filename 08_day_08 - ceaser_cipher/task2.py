def calculate_love_score(name1,name2):
    name_merge = name1 + name2
    baseline1 = 'true'
    baseline2 = 'love'

    check1_count = 0
    for letter in name_merge:
        if letter in baseline1:
            check1_count += 1

    check2_count = 0
    for letter in name_merge:
        if letter in baseline2:
            check2_count += 1

    total = str(check1_count) + str(check2_count)
    print (total)

name1 = input('Enter name 1 : ')
name2 = input('Enter name 2 : ')
calculate_love_score(name1,name2)