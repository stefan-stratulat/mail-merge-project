#TODO: Create a letter using starting_letter.docx
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []

#read names for from invited_names.txt
with open('input/names/invited_names.txt') as file:
    file_lines = file.readlines()
    for line in file_lines:
        line = line.strip('\n')
        names.append(line)

#Read starting letter
with open('input/letters/starting_letter.docx',) as file:
        content = file.read()

# #Replace the [name] placeholder with the actual name
# for name in names:
#     with open(f'output/readytosend/letter_{name}.docx',mode='w') as letter:
#         letter.write(content)
#         letter.replace('[name]',name)