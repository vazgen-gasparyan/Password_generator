
from random import sample
from string import ascii_lowercase as al, ascii_uppercase as au

for i in range(5):
    while True:
        length = input('\nEnter 8-32 for length password -  ')
        try:
            while int(length)<8 or int(length)>32:
                length = input('\nInvalid length for password\nPlease enter 8-32 for length password -  ')
        except ValueError: continue
        if int(length)>=8 or int(length)<=32:
            print('password: ', ''.join(sample('_*&!?;:$%^-/.,1234567890'+au+al,int(length))))
            break
