usernames = {'Sammy': 'sammy-shark', 'Jamie': 'mantisshrimp54'}

while True:
    name = input('Enter a name : ')

    if name in usernames:
        print(f'{usernames[name]} is the username of {name}')
    else:
        print(f"I don't have {name}'s username. What is it??")

        new_username = input('Enter the username please...')

        usernames[name] = new_username

        print('Data Updated')