
first_name = str(input("Please enter your first name: "))
nick_name = str(input("Please enter your nick name: "))
last_name = str(input("Please enter your last name: "))

first_name = first_name.capitalize()
nick_name = nick_name.capitalize()
last_name = last_name.capitalize()

name_format = "{first} {middle:.1s}. {last}"
print(name_format.format(first = first_name, middle = nick_name, last = last_name))