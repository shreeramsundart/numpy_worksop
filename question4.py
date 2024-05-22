#write a program to find the sum of digits of a given number'

n=int(input())
sum = 0
while n != 0:
    sum += n % 10
    n //= 10
print(sum) 
