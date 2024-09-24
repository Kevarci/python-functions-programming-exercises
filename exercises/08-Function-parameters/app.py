# Your code goes here:
def render_person(name, birth_date, eyecolor, age, gender):
    return name + " is a" + str(age) + " year old " + gender + " born in " + birth_date + " with " + eyecolor


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))