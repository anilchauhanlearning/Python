#take number from user and perform some operations like additional multiplication etc check peration resut is prime or not 
num_prime = int(input("Enter your number: "))
num_secPrime = int(input("Enter your 2nd number: "))
perform_operation = input("What you want to peform: +, -, %, * ")
if perform_operation == "+":
    output = num_prime+num_secPrime
elif perform_operation =="-":
    output =num_prime-num_secPrime
elif perform_operation == "*":
    output = num_prime*num_secPrime
elif perform_operation =="%":
    if num_prime >1:
        if num_secPrime>0:
            output = num_prime %num_secPrime
        else:
            print("Its not a valid option")
elif perform_operation == "/":
    if num_secPrime>1:
        output = num_secPrime/num_secPrime
    else:
        print('Output is zero')
else:
    output ="You didn't make a great choice"
#
if output >1:
    for i in range(2, output):
        if output % 2==0:
            print(f"{output} is not a primary number")
            break
        else:
            print(f"{output} is a prime number")
else:
    print("All task done")
    
for i in output:
    if i >0:
        print("Good")
         

    
        
            
    
    
    