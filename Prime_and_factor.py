#there was confusion in this question that i have to check input no is prime or i have to check each factor no is prime , so i coded both situation program :


#situation first , check input no is prime and print all factors :






inpu_query=int(input())
def prime_and_factor(user_inp):

    factors=[]
    for i in range(2,user_inp+1):
        if user_inp%i==0:
            factors.append(i)
    if len(factors)==1:
        return "it's a prime no : {}".format(factors[0])
    else:
        return "it's not a prime no and factors are : {} ".format(factors)



print(prime_and_factor(inpu_query))


#sample


# 192
# it's not a prime no and factors are : [2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 192] 

# 71
# it's a prime no : 71
        
        
        
        
        
        
#situation second , find all factors of number and check each factor is prime or not.




def prime_and_factor(user_inp):

    factors=[]
    for i in range(2,user_inp+1):
        if user_inp%i==0:
            factors.append(i)

    return factors



while True:
    input_query = int(input('Inter any no less than 100000'))

    if input_query<100000:
        break

    else:
        print 'please input valid no'

if len(prime_and_factor(input_query))==1:
    print("it's not a prime no and factors are : {} ".format(prime_and_factor(input_query)))
else:
    print('factors are',prime_and_factor(input_query))
    for i in prime_and_factor(input_query):
        if len(prime_and_factor(i))==1:
            print('prime no',i)
        else:
            print('Not prime no',i)
            
            
            
#sample

# Inter any no less than 100000  192
# ('factors are', [2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 192])
# ('prime no', 2)
# ('prime no', 3)
# ('Not prime no', 4)
# ('Not prime no', 6)
# ('Not prime no', 8)
# ('Not prime no', 12)
# ('Not prime no', 16)
# ('Not prime no', 24)
# ('Not prime no', 32)
# ('Not prime no', 48)
# ('Not prime no', 64)
# ('Not prime no', 96)
# ('Not prime no', 192)
