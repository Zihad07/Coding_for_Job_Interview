
# defin funtion that return 
# most frequent occurnint number in a list or arrat

def most_frequent(given_array):

    max_count = -1
    max_item = None

    # empty dictionary
    count = {}

    for item in given_array:
        if item not in count:
            count[item] = 1
        else:
            count[item] += 1
        
        # max determint

        if count[item] > max_count:
            max_count = count[item]
            max_item = item
        
    return str(max_item) + " has " + str(max_count) + "times."

# -------------------------------------------------------------

print(most_frequent([1,3,1,3,2,1])) 
print(most_frequent([1,3,1,3,2,1,4,5,4,6,4,])) 
print(most_frequent([1,3,0,3,2,1,0,2,0])) 
print(most_frequent([1,3,1,3,2,1,3])) 