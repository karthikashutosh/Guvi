num = int(input("Enter a number: "))  
result = 0  
temp = num  
  
while temp > 0:  
   digit = temp % 10  
   result += digit ** 3  
   temp //= 10  
  
if num == result:  
   print(num,"is an Armstrong number")  
else:  
   print(num,"is not an Armstrong number")  
