#there was confusion in this question that i have to check input no is prime or i have to check each factor no is prime , so i coded both situation program :


#situation first , check input no is prime and print all factors :





def prime_and_factor(user_inp):

    factors=[]
    for i in range(2,user_inp+1):
        if user_inp%i==0:
            factors.append(i)
    if len(factors)==1:
        return "it's a prime no : {}".format(factors[0])
    else:
        return "it's not a prime no and factors are : {} ".format(factors)
        
        
        
        
        
        
#situation second , find all factors of number and check each factor is prime or not.




def prime_and_factor(user_inp):

    factors=[]
    for i in range(2,user_inp+1):
        if user_inp%i==0:
            factors.append(i)

    return factors

input_query=int(input(''))

if len(prime_and_factor(input_query))==1:
    "it's not a prime no and factors are : {} ".format(prime_and_factor(input_query))
else:
    print(prime_and_factor(input_query))
    for i in prime_and_factor(input_query):
        if len(prime_and_factor(i))==1:
            print('prime no',i)
        else:
            print('Not prime no',i)
