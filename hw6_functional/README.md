- **sequential_map()** takes unlimited number of functions and a collection of values as input. \
It returns list of results of sequential application of these functions to the collection of values.

- **consensus_filter()** takes several filters (functions that return True or False) and a collection of values as input. \
It returns list of values that pass every filter.

- **conditional_reduce()** takes 2 functions and a collection of values. \
First function takes 1 argument and returns True or False (it's a filter). \
Second function takes 2 arguments and returns result (it's a function). \
conditional_reduce() returns 1 value (similar to reduce() function) but only for those values that passed the filter.

- **func_chain()** takes unlimited number of functions as input. \
It returns single function that is a result of a sequential application of them.

- **sequential_map_new()** is a sequential_map() implemented using func_chain() function.

- **multiple_partial()** works similar to partial() but it takes unlimited number of functions and unlimited number of parameters as input and returns a list of "partial" functions.
