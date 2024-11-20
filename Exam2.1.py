with open('Exam Two Names.txt', 'r') as file:
    lines = file.readlines()
boys_names = []
girls_names = []
for line in lines:
    parts = line.strip().split(',')
    if len(parts) == 2:
        boy_name = parts[0].strip()
        girl_name = parts[1].strip()
        boys_names.append(boy_name)
        girls_names.append(girl_name)
while True:
    user_input = input("Enter a Name: ").strip()
    if user_input.lower() == 'q':
        break
    formatted_name = user_input.capitalize()
    boy_rank = None
    girl_rank = None
    for i in range(len(boys_names)):
        if boys_names[i].lower() == formatted_name.lower():
            boy_rank = i + 1
            break
    for i in range(len(girls_names)):
        if girls_names[i].lower() == formatted_name.lower():
            girl_rank = i + 1
            break
    if boy_rank:
        print(f"Boy's Name - Rank: {boy_rank}")
    elif girl_rank:
        print(f"Girl's Name - Rank: {girl_rank}")
    else:
        print("Name Not Found")