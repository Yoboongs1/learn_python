def binary_search(x, y):
    "Peform binary search on x to find y. If found returns position, otherwise returns None."

    # Intialise end point indices
    lower, upper = 0, len(x) - 1

    # If value is outside of interval, return None 
    if y < x[lower] or y > x[upper]:
        return None

    # Perform binary search
    while True:
                
        # Compute midpoint index (integer division)
        midpoint = (upper + lower)//2

        # Check which side of x[midpoint] y lies, and update midpoint accordingly
        if y < x[midpoint]:
            upper = midpoint - 1
        elif y > x[midpoint]:
            lower = midpoint + 1
        elif y == x[midpoint]:  # found, so return
            return midpoint
       
        # In this case val is not in list (return None)
        if upper < lower:
            return None

mylist = [1,5,3,45,23,8]
mylist.sort()

print(binary_search(mylist, 45))
print(binary_search(mylist, 8))