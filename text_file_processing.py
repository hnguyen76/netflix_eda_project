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

def add_contact():
    name=input('\nWhat is your name: ')
    phone=input('\nWhat is your phone number: ')
     
    with open('contacts.txt','a') as file:
        file.write(f'{name}, {phone}\n')
        
    print('✅Contact added!\n')    

def view_contacts():
    try:
        with open('contacts.txt', 'r') as file:
            contacts = file.readlines()
        
        if not contacts:
            print('\nEmpty contact list\n')
        else:
            for number, contact in enumerate(contacts, 1):
                print(f'{number}. {contact.strip()}')
        print('\n')
                
    except FileNotFoundError:
        print('\nEmpty contact list!')

def delete_contact():
    try:
        with open('contacts.txt', 'r') as file:
            contacts = file.readlines()
        if not contacts:
            print('\nEmpty contact list\n')
        else:
            for number, contact in enumerate(contacts, 1):
                print(f'{number}. {contact.strip()}')
            try:
                delete_number = int(input('\nWhich contact number do you want to delete?: '))
                if delete_number < 1 or delete_number > len(contacts):
                    print('\nThat contact numver does not exist.\n')
                else:
                    deleted_contact = contacts.pop(delete_number - 1)
                
                    with open('contacts.txt', 'w') as file:
                        file.writelines(contacts)
                    
                    print(f'\n✅Deleted: {deleted_contact.strip()}\n')
            except ValueError:
                print('\nPlease enter a valid number.\n')
            # except IndexError:
            #     print('\nThat contact number does not exist.\n')
    except FileNotFoundError:
        print('\nEmpty contact list!')


def search_contact():
    try:
        with open('contacts.txt', 'r') as file:
            contacts = file.readlines()
            
        if not contacts:
            print('\nEmpty contact list')
        else:
            search_name = input('\nEnter name to search: ')
            found = False
            for contact in contacts:
                if search_name.lower() in contact.lower():
                    print(f'Found: {contact.strip()}')
                    found = True
            if not found:
                print('\nNo contact found\n')
                
    except FileNotFoundError:
        print('\nEmpty contact list!\n')
        
def main():
    while True:
        print('1. Add contact')
        print('2. View contact')
        print('3. Delete contact')
        print('4. Search contact')
        print('5. Quit')
        
        i=input('Your selection: ')
        
        if i == '1':
            add_contact()
            
        elif i =='2':
            view_contacts()
        
        elif i == '3':
            delete_contact()
            
        elif i =='4':
            search_contact()
            
        elif i == '5':
            print('\nGoodbye!\n')
            break
        else:
            print('\nInvalid selection\n')
            
if __name__ == "__main__":
    main()