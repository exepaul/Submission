#Write a function that accepts a list of strings from stdin, and sorts it based on length of those strings. The output is the sorted list of strings.


#I tried with two methods :

#by Pure algorithm method :

user_input=[i for i in raw_input().split()]

def sort_by_length(string_list):

    if len(string_list)>0:
        determiner = len(string_list[0])
        left=[]
        right=[]
        equal=[]
        for j,i in enumerate(string_list):
            if len(i) > determiner:
                left.append(i)

            elif len(i) < determiner:
                right.append(i)
            elif len(i) == determiner:
                equal.append(i)
        return sort_by_length(right)+equal+sort_by_length(left)
    else:
        return string_list

print sort_by_length(user_input)


#sample input
# ni nikichatbot chat c niki nikichatbotartificial
#output:
#['c', 'ni', 'chat', 'niki', 'nikichatbot', 'nikichatbotartificial']




#by In-built method 

print list(map(lambda x:user_input[x[1]],sorted([(len(i),j) for j,i in enumerate(user_input)])))

#['c', 'ni', 'chat', 'niki', 'nikichatbot', 'nikichatbotartificial']







