
from random import sample
from string import ascii_lowercase as al, ascii_uppercase as au

lens = int(input("\nWhat is the length of the password: "))

for pas in range(0 , 5):
  password=''.join(sample('_*&!?;:$%^-/.,1234567890'+au+al,lens))
  print('password:  ', password)

    

# code by Vazgen Gasparyan
# Facebook: https://bit.ly/3zhk3PO

# Thank you!
