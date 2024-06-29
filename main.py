with open('body-info.text', mode='r') as file:
    information = file.read()

with open('names.text', mode='r') as names_data:
    names = names_data.readlines()

for name in names:
    file_path = f"letter_container/{name}.text"
    with open(file_path, mode='w') as file:
        person_letter = information.replace("['']", name)
        print(person_letter)
        file.write(person_letter)