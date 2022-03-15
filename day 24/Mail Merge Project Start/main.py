with open("/Users/rasi/Downloads/Mail Merge Project Start/Input/Names/invited_names.txt") as names:
    names_list = names.readlines()

with open("/Users/rasi/Downloads/Mail Merge Project Start/Input/Letters/starting_letter.txt") as start_content:
    start_content_txt = start_content.read()
    for name in names_list:
        name1 = name.strip()
        end_content_txt = start_content_txt.replace("[name]", name1)
        with open(f"/Users/rasi/Downloads/Mail Merge Project Start/Output/ReadyToSend/letter_for_{name1}.txt", mode="w") as completed_content:
            completed_content.write(end_content_txt)






