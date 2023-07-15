
# 1
"""
Write a decorator that:
- ensures a function is only called by users with a specific role.
- Each function should have an user_type with a string type in kwargs.
"""


customer_receipt = {"receipt_id": 123456,
                    "client_name": "Big Lebowski",
                    "med_name": "Adderall"}      


def is_admin(func):
    def wrapper(*args, **kwargs):
        try:
            user_type = kwargs.get('user_type')
            if user_type == 'admin':    
                return func(*args, **kwargs)
            else:
                raise ValueError("Permission denied")
        except ValueError as ve:
            print(f"ValueError occurred: {ve}")
          
    return wrapper

# Test block
@is_admin
def show_customer_receipt(user_type: str):
    return print(customer_receipt)


# 2
'''
Write a decorator that:
- wraps a function in a try-except block 
- and prints an error if any type of error has happened.
'''


def catch_errors(func):
    def wrapper(*args, **kwargs):
        try: 
            return func(*args, **kwargs)
        except Exception as ex:
            return f"""Found error during execution of your function: 
            ---{type(ex).__name__}: {str(ex)}---
            Your arguments {args}
            
            ---"""
    return wrapper

# Test block
@catch_errors
def some_function_with_risky_operation(data):
    return(data['key'])

assert some_function_with_risky_operation({'foo': 'bar'}) != "bar"
assert some_function_with_risky_operation({'key': 'bar'}) == "bar"

# 3
"""
Optional: Create a decorator that:
- will check types. 
	- It should take a function with arguments 
	- -> validate inputs with annotations. 
- It should work for all possible functions. 

Don`t forget to check the return type as well
"""

def check_types(func):
    def wrapper(*args, **kwargs):
        try: 
            annotations_key_value = [{key: value} for key, value in func.__annotations__.items()]
            for i in range(len(annotations_key_value)):
                ann_var_name = list(annotations_key_value[i].keys())[0]
                ann_type = list(annotations_key_value[i].values())[0]
                #check type result type
                if i==len(annotations_key_value)-1:
                    func_result = func(*args, **kwargs)
                    result_type = type(func_result).__name__
                    if result_type != ann_type:
                        raise TypeError(f"TypeError: Result ' {func_result} ' must be '{ann_type}', not '{args_type}' *-* ")
                    else: 
                        return func_result

                #check type arguments type
                args_type = type(args[i]).__name__    
                if args_type != ann_type:
                    raise TypeError(f"TypeError: Argument '{ann_var_name}' must be '{ann_type}', not '{args_type}'. *-*")
            
        except TypeError as type_er:
            return type_er

    return wrapper

############################################
# Test block
@check_types
def add(a: "int", b: "int") -> "str":
    return a + b

############################################

# 4

"""
Optional: Create a function that 
- caches the result of a function, 
		- so that if it is called with the same argument multiple times, 
		- > it returns the cached result first instead of re-executing the function.
"""

"""
Using `@wraps` is a recommended practice to ensure the decorated function retains the original function's metadata.
If you choose not to use `@wraps`: 
- you would need to manually update the attributes of the `wrapper` function to match those of the original function.
This includes setting the `__name__`, `__doc__`, and other attributes.
"""
from functools import wraps


def cache_result(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = args + tuple(kwargs.items())
        if key in cache:
            return cache[key]
        else:
            result = func(*args, **kwargs)
            cache[key] = result
            return result

    return wrapper

@cache_result
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

#### Test

####



# 5

"""
Optional: Write a decorator that:
- adds a rate-limiter to a function:
	- it can only be called a certain amount of times per minute
"""


import time


def rate_limiter(max_calls, interval):

    def decorator(func):
        func_count = 0
        get_time = time.time()
        inter_end_time = get_time + interval

        def wrapper(*args, **kwargs):
            nonlocal func_count, inter_end_time
            get_time = time.time()
            if get_time > inter_end_time:
                print("Interval refreshed")
                func_count = 0
                inter_end_time += interval

            if func_count >= max_calls:
                raise Exception(f"Rate limit exceeded. Maximum {max_calls} calls allowed within {interval} seconds.")
            
            func_count += 1
            return func(*args, **kwargs)

        return wrapper

    return decorator


@rate_limiter(max_calls=3, interval=3.01)
def my_function():
    time.sleep(1)
    print("Hello, rate-limited world!")
    print("-----")



###
# Test the rate-limited function
def test_my_function(func):
    for i in range(100):
        try:
            func()
        except Exception as ex:
            print(ex)
###          






if __name__ == "__main__":
    pass
    # Task 1
    # show_customer_receipt('user', customer_receipt)
    # show_customer_receipt(user_type='user')  # Raises ValueError: Permission denied
    # show_customer_receipt(user_type='admin') 

    # Task 2
    # print(some_function_with_risky_operation({'foo': 'bar'}))
    # print(some_function_with_risky_operation({'key': 'bar'}))

    # Task 3
    # print(add(1, 2))  # TypeError: Result ' 3 ' must be 'str', not 'int'
    # print(add("1", "2"))  # TypeError: Argument 'a' must be 'int', not 'str'

    # Task 4
    # print(fibonacci(100))

    # Task 5
    test_my_function(my_function)


