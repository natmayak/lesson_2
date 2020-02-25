age = int(input('How old are you? '))
gender = str(input('Are you male of female? '))

def ageist_function(age, gender):
    if age < 0:
        raise ValueError("You are in your parents' plans")
    elif 0 <= age <= 6:
        print('You are having fun in the kindergarden')
    elif 6 < age <= 16:
        print('Wasting best years at school')
    elif 16 < age <= 21:
        print('Getting the best of alma mater')
    elif 21 < age < 60:
        print('Getting the job done most of their time')
    elif 60 <= age <= 65 and gender == "male":
        print('Getting the job done most of their time')
    elif 60 < age <= 65 and not gender:
        print("You are probably retired but it depends on gender")
    elif 60 < age <= 65 and gender != "male" and gender != "female":
        print("You are probably retired but it depends on gender")
    else:
        print('Sharing wisdom with others')

ageist_function(age, gender)







