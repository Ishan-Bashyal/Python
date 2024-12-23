'''
Accept the age, gender ('M', 'F'), and show type ('Matinee', 'Evening'):
Age < 12:
    Male or Female:
        Matinee: Ticket = Rs500
        Evening: Ticket = Rs700
Age >= 12 and < 60:
    Male:
        Matinee: Ticket = Rs800
        Evening: Ticket = Rs100
    Female:
        Matinee: Ticket = Rs700
        Evening: Ticket = Rs900
Age >= 60:
    Male or Female: Ticket = Rs600
'''
age = int(input("Enter your age: "))
gender = input("Enter your gender ('M' for Male, 'F' for Female): ").upper()
show_type = input("Enter the show type ('Matinee' or 'Evening'): ").capitalize()

if age < 12:
    if show_type == 'Matinee':
        ticket_price = 500
    else:
        ticket_price = 700
elif 12 <= age < 60:
    if gender == 'M':
        if show_type == 'Matinee':
            ticket_price = 800
        else:
            ticket_price = 100
    elif gender == 'F':
        if show_type == 'Matinee':
            ticket_price = 700
        else:
            ticket_price = 900
else:
    ticket_price = 600

print(f"The ticket price is Rs{ticket_price}")