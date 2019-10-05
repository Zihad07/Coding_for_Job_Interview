
# for BIG O(n)
def is_Rotation_my_method(A,B):
    len_A = len(A)

    result = {}

    for i in range(len_A):
        if A[i] not in result:
            result[A[i]]  = 1
        else:
            result[A[i]] += 1
        
        if B[i] not in result:
            result [B[i]] = 1
        else:
            result [B[i]] += 1
    

    # if the diction all item value of sum = len_A*2
    # return true
    # else return false

    myresult = 0

    for key in result.keys():
        myresult += result[key]

    if myresult == (len_A * 2) and len_A == len(result):
        return True
    else:
        return False
# --------------------------------------------------------------

# The Best Solution

def isRotaion(A,B):
    len_A = len(A)
    len_B = len(B)

    if len_A != len_B:
        return False
    
    key = A[0]
    key_index = -1


    for i in range(len_B):
        if key == B[i]:
            key_index = i
            break
    
    if key_index == -1:
        return False
    
    for i in range(len_A):
        j = (key_index + i) % len_A

        if A[i] != B[j]:
            return False
    
    # other wise
    return True # the one array is rotation other array





# Testing my method

if __name__ == '__main__':
    A = [1,2,3,4,5,6,7]
    B = [4,5,6,7,1,2,3]

    print(is_Rotation_my_method(A,B))
    print(isRotaion(A,B))

    A = [1,2,3,4,5,6,7]
    B = [4,8,9,7,1,2,3]
    print(is_Rotation_my_method(A,B))
    print(isRotaion(A,B))

    

