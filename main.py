#Python program to generate strong passwords upto 70 characters

import random
lower= "abcdefghijklmnopqrstuvwxyz"
upper= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeral= "0123456789"
symbols="@#*&/$~!"
case=lower+upper+numeral+symbols

try:
   length=int(input("Enter the number of required characters (max=70) : "))

   if 4<= length <=70:
     passcode="".join(random.sample(case, length))
     print("Your new passcode is: " + passcode)
   elif length <4:
     print("The minimum character length must be greater than or equal to 4.")
   else:
     print("Character Length too large!")
except ValueError:
    print("Only integral input is valid.")

#End of the program
