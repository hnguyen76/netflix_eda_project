# name = input("What is your name? ")
# print('Hello', name)
# # print('Your name has ', len(name), 'letter')
# print(f'Your name has {len(name)} letters')
# print('Your name uppercase is', name.upper())

# sen = input("Give me a sentence: ")
# print('Lowercase:', sen.lower())
# print('Uppercase:', sen.upper())
# print(f'that sentence has: {len(sen)} words')
# print(f'that sentence has cut space: {sen.strip()}')

# if sen == sen.lower():
#     print('That is uppercase')
# else: 
#     sen == sen.upper(), print('that is lowercase')
# print(f'that sentence has: {len(sen)} words')
# print(f'that sentence has cut space: {sen.strip()}')

# word = input('word input: ')
# if len(word) > 5:
#     print('Long word')
# else:
#     print('Short word')

# fruits = ['apple', 'banana', 'orange']
# for fruit in fruits:
#     if fruit == 'banana':
#         print('I like banana')
#     else:
#         print(fruit)

# names=['tom','trrdfd']
# n=input('please input: ')
# names.append(n)
#     print("dafsaf")
# print(names)

# print(names.append(n)) # to print name

# names=[]
# while True:
#     n=input('please input any thing except "q" for quit: ')
#     if n == 'q':
#         break
#     names.append(n)
# if not names: 
#     print('Empty list')
# else: 
#     print(names)
        
contacts = []
while True:
    print('1. Add contact')
    print('2. View contact')
    print('3. Quit')
    i=input('Your selsection: ')
    if i == '1':
        s=input('What is your name: ')
        contacts.append(s)
    elif i == '2':
        if not contacts:
            print('Empty contact list')
        else:
            for con in contacts:
                print(con) 
                #print with orderly number 
    elif i == '3':
        break
    else:
        print('Invalid Selection')
    
        


