'''
A decorator lays out a way in which a function can be enhanced
'''

def kerala():
    print("God's own country Kerala")


def welcome_decorator(place_function):
    def wrapper():
        print("Welcome to")
        place_function()
    return wrapper   # wrapper is a function, which is an object, so it is fine to not call it

welcome_decorator(kerala)  # returns the wrapper object
welcome_decorator(kerala)()  # calls the wrapper, so wrapper acts a function and execute


def colwyn_bay():
    print("Old colwyn, Colwyn bay")


welcome_decorator(colwyn_bay)()

'''
Decorator syntax
In the above example we saw how we have to define a function, then pass it as an
argument object to the decorator and then call the function that the decorator returns. This
is a lot of work! So we can condense it by using a compact syntax, which enables us to sort of
like just 'mention - @' the decorator and move on with our life - the '@' takes care of calling
the decorator by passing on the function we want to enhance as an argument and then also call 
the wrapper that is returned by the decorator. All we have to do is just call our function!
'''

@welcome_decorator
def karunagappally():
    print("Karunagappally, the land of the mosque of black snakes!")

karunagappally()

'''
A decorator is a higher order function
RECAP: A function is higher-order if it takes in another function as an argument, has another
function within its body or returns a function
A decorator does all three mostly. Therefore it is a higher-order function
'''

'''
'''

def greeting_decorator(function):
    def wrapper(*args, **kwargs):
        print("Hi,")
        function(*args, **kwargs)
    return wrapper

@greeting_decorator
def my_age(age):
    print(f"I am {age} years old")

my_age(24)