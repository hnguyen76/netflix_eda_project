# name = input("enter your favorite food: ")
# with open("ffood.txt", 'w') as file:
#     file.write(name)
# # print('food saved successfully')

# movie = input('Enter your movie name: ')
# with open('movies.txt','a') as file:
#     file.write(movie + '\n')
# print('movie added successfully')

# with open('movies.txt', 'r') as file:
#     movies = file.readlines()
# for movie in movies:
#     print(movie, end='')

# try:
#     with open('books.txt', 'r') as file:
#         books = file.readlines() 
#     for book in books:
#         print(book.strip())
# except FileNotFoundError:
#     print('No books file found')


while True:
    print('1. Add contact')
    print('2. View contact')
    print('3. Delete contact')
    print('4. Quit')
    i=input('Your selection: ')
    if i == '1':
        name=input('What is your name: ')
        phone=input('What is your phone number: ')
        
        with open('contacts.txt','a') as file:
            file.write(f'{name}, {phone}\n')
        
        print('Contact added!')
    elif i =='2':
        try:
            with open('contacts.txt', 'r') as file:
                contacts = file.readlines()
            
            if not contacts:
                print('Empty contact list')
            else:
                for number, contact in enumerate(contacts, 1):
                    print(f'{number}, {contact.strip()}')
                    
        except FileNotFoundError:
            print('Empty contact list!')
    elif i == '4':
        break
    else:
        print('Invalid selection')