# find if the given number is a palindrome or not?

Check=int(input("Enter the Number to Check:"))
check_Str=str(Check)

if check_Str==check_Str[::-1]:
    print("It is Palidrome")
else:
    print("Not Palidrome")
