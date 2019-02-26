donors = [[], [], [], [], []]
donors[0].append((input('Name:')))
donors[0].append(input('Phone:'))
donors[0].append(input('Donation Amount:'))
donors[1].append((input('Name:')))
donors[1].append(input('Phone:'))
donors[1].append(input('Donation Amount:'))
donors[2].append(input('Name:'))
donors[2].append(input('Phone:'))
donors[2].append(input('Donation Amount:'))
donors[3].append(input('Name:'))
donors[3].append(input('Phone:'))
donors[3].append(input('Donation Amount:'))
donors[4].append(input('Name:'))
donors[4].append(input('Phone:'))
donors[4].append(input('Donation Amount:'))
donors[1][0] = 'Here we demonstrate the ability to access and edit our list of lists.'

for i in range(5):
    for j in range(3):
        print(donors[i][j])
