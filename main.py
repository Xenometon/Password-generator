#Python program to generate strong passwords of upto 8 characters.

import random
lower= "abcdefghijklmnopqrstuvwxyz"
upper= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeral= "123456789"
notation="αβΔπλΨΩ"
symbols="@#%*&/"
case=lower+upper+numeral+notation+symbols
length=8
passcode="".join(random.sample(case, length))
print("Your new passcode is: " + passcode)

