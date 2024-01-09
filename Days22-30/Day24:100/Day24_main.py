REPLACE = "[name]"

with open('Input/Names/invited_names.txt') as names_file:
    names = names_file.readlines()

with open('Input/Letters/starting_letter.txt') as letter_file:
    letter = letter_file.read()

for name in names:
    clean_name = name.strip()
    new_letter = letter.replace(REPLACE, clean_name)
    with open(f'Output/ReadyToSend/letter_for_{clean_name}.txt', mode='w') as finished_letter:
        finished_letter.write(new_letter)




