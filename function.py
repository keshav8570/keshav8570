#function even
def is_even(number):
    """
    this fucntion tells which number is even or odd
    created by keshav 

    """
    if number%2==0:
       return "even"
    else:
        return "odd"

for i in range(1,11):
     print(is_even(i))



        
