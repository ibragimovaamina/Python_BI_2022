## Task 1

# This function takes unlimited number of functions and a collection of values as input.
# It returns list of results of sequential application of these functions to the collection of values.

def sequential_map(*args):
    *functions, values = [*args]              # unpacking input functions and collection of values
    for function in functions:
        values = map(function, values)
    return list(values)

## Task 2

# This function takes several filters (functions that return True or False) and a collection of values as input.
# It returns list of values that pass every filter.

def consensus_filter(*args):
    *filters, values = [*args]                # unpacking input filters and collection of values
    for filterr in filters:
        values = filter(filterr, values)      # passing to next filter only values that passed current filter
    return list(values)

## Task 3

# conditional_reduce() takes 2 functions and a collection of values.
# First function takes 1 argument and returns True or False (it's a filter).
# Second function takes 2 arguments and returns result (it's a function).
# conditional_reduce() returns 1 value (similar to reduce() function) but only for those values that passed the filter.

def my_reduce(function, values):
    while len(values) > 1:                    #  if 0 or 1 input values, returning values immediately
        values[1] = function(values[0], values[1])
        values = values[1:]
    return values

def conditional_reduce(filterr, function, values):
    filtered_values = list(filter(filterr, values))
    return my_reduce(function, filtered_values)

## Task 4

# func_chain() takes unlimited number of functions as input.
# It returns single function that is a result of a sequential application of them.

def wrapping_function(inner_func, outer_func):
    return lambda x: outer_func(inner_func(x))

def func_chain(*args):
    list_of_functions = [*args]
    while len(list_of_functions) > 1:
        list_of_functions[1] = wrapping_function(list_of_functions[0], list_of_functions[1])
        list_of_functions = list_of_functions[1:]
    return list_of_functions[0]

## Task 4. Additional

# Implementation of Task 1 using func_chain() function.

def sequential_map_new(*args):
    *functions, values = [*args]              # unpacking input functions and list of values
    general_function = func_chain(*functions) # wrapping all input functions into one function
    return general_function(values)

## Extra Task 1

# multiple_partial() works similar to partial() but
# it takes unlimited number of functions and unlimited number of parameters as input and returns a list of "partial" functions.

def multiple_partial(*args, **kwargs):
    list_of_functions = [*args]
    dict_of_parameters = kwargs
    
    list_of_partial_functions = []
    
    for function in list_of_functions:
        def partial_func(function, dict_of_parameters):
            return lambda x: function(x, **dict_of_parameters)
        list_of_partial_functions.append(partial_func(function, dict_of_parameters))
    
    return list_of_partial_functions