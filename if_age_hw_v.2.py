age = int(input("How old are you? "))

def ageist_function(age):
    if age <= 0:
        raise ValueError("You are in your parents' plans")
    elif 0 < age <= 6:
        print('Having fun at nursery')
    elif 6 < age <= 16:
        print('Wasting best years at school')
    elif 16 < age <= 21:
        print('Getting the best of alma mater')
    elif 21 < age < 60:
        print('Working hard most of their time (probably)')
    elif 60 <= age <= 65:
        print('Are you male of female?')
        gender = str(input())
        if gender == 'male':
            print('Working hard most of their time (probably)')
        elif gender == 'female':
            print('Sharing wisdom with others')
        elif gender != 'female' or gender != 'male' or not gender:
            print("You are probably retired but it depends on gender")
        #else:
        #print("You are probably retired but it depends on gender")
    else:
        print('Sharing wisdom with others')

ageist_function(age)







