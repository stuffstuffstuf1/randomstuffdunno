print('welcome to the stuff industries recruitment quiz')
name = input('your name is ')
print('hello, ' + name + '.')
print('are you male of female')
gender = input()
if gender == 'female':
    pass
elif gender == 'Female':
    pass
elif gender == 'male':
    pass
elif gender == 'Male':
    pass
else:
    print('that is not a gender')
age = input ('Aged ')
if age < '18':
    print('sorry, you are underaged to join stuff industries')
if age > '18':
    print('have you finished school?')
    school = input()
    if school == 'yes':
        print('do you have any special departments you want to work in?')
        special_departments = input()
        if special_departments == 'no':
            print('ok, we will try and find a spot for you in stuff industries')
        if special_departments == 'yes':
            print('what are they?')
            special_departments2 = input()
            print('we might have a spot for you in ' + special_departments2 + '.')
        else:
            print('good choice, we might have a spot for you in ' + special_departments + '.')
    elif school == 'no':
        print('you need to have finished school to join stuff industries')
    if school == 'Yes':
        print('do you have any special departments you want to work in? if you do, please list them below')
        special_departments = input()
        pass
    elif school == 'No':
        print('thank you for taking the stuff industries recruitment quiz')
        pass