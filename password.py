
from random import sample
from string import ascii_lowercase as al, ascii_uppercase as au

password=''.join(sample('_*&!?;:$%^-/.,1234567890'+au+al,8))
print('password:  ', password)



# code by Vazgen Gasparyan
# Facebook: https://bit.ly/3zhk3PO

# Thank you!
