
def myfunNotSame(sa,sb,len_a,len_b):

    count_dff = 0
    xa = yb = 0
    while xa < len_a and yb <len_b:
        if sa[xa] == sb[yb]:
            xa += 1
            yb += 1
        else:
            count_dff += 1
            if count_dff == 2:
                return False
            xa += 1
    if count_dff == 0:
        return False
    return True

def myfunSame(sa,sb,len_a):
    
    count_dff = 0
    
    for i in range(len_a):
        if sa[i]!=sb[i]:
            count_dff += 1
            
        if count_dff == 2:
            return False
        
    if count_dff == 0:
        return False
    return True
    
def my_one_way_sting(sa,sb):
    len_a = len(sa)
    len_b = len(sb)

    if len_a == len_b:
        return myfunSame(sa,sb,len_a)
    if len_a > len_b:
        return myfunNotSame(sa,sb,len_a,len_b)
    if len_a < len_b:
        return myfunNotSame(sb,sa,len_b,len_a)




# --------------------------------------

if __name__ == "__main__":
    print(my_one_way_sting('abcde','abfde'))
    print(my_one_way_sting('abcde','abde'))
    print(my_one_way_sting('xyz','xyaz'))
    print(my_one_way_sting('xy','xyaz'))
    print(my_one_way_sting('xay','xyaz'))


