def common(A,B):

    # calculating lenth each list
    lenA = len(A)
    lenB = len(B)

    # keep result 
    result = [] # empty list

    # pointing first item each array
    p1 = p2 = 0

    # iterate each item following condition
    while p1 < lenA and p2 < lenB:
        if A[p1] == B[p2]:
            result.append(A[p1])

            # increment each pointer
            p1 +=1
            p2 += 1
        elif A[p1] > B[p2]:
            # increment second pointer
            p2 += 1
        else:
            # increment first pointer
            p1 += 1
    

    # return result
    return result

    
    # pass;




# -----------------------------

if __name__ == "__main__":
    A = [1,3,4,6,7,8,9]
    B = [1,2,4,5,9,10]
    print(common(A,B));


