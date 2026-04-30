# from datetime import datetime

# now = datetime.now()

# print(now.strftime("%A, %B %d, %Y"))
# print(now.strftime("%I:%M %p"))

# from datetime import datetime, timedelta

# today = datetime.now()
# next_7days = today + timedelta(days=7)
# last_3days = today - timedelta(days=3)

# print(next_7days.strftime("%Y-%m-%d"))
# print(last_3days.strftime("%Y-%m-%d"))

# from datetime import datetime
# def add_contact():
#     name = input('Enter your contact name: ')
#     phone = input('Enter your number: ')
#     created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
#     with open('contacts.txt', 'a') as file:
#         file.write(f'{name}, {phone}, {created_at}\n')
#     print('Contact added!')
    
    
from datetime import datetime, timedelta
while True:
    try:
        task = input('Task name: ')
        deadline = int(input('due date (number only no negative number): '))

        if deadline < 0:
           print('Please enter a non-negative number.')
           continue
        
        due_date = datetime.now() + timedelta(days=deadline)

        print(f'Task: {task}')
        print(f'Due date: {due_date.strftime("%Y-%m-%d")}') 
        break
    
    except ValueError:
        print('Please enter a valid number. ')
