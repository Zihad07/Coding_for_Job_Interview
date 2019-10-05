
def my_non_reapating_character(mystr):
    result = {}
    for each_character in mystr:
        if each_character not in result:
            result[each_character] = 1
        else:
            result[each_character] +=1
    
    
    for ch in mystr:
        if result[ch] == 1:
            return ch

    return None




if __name__ == "__main__":
    print(my_non_reapating_character('aabcb'))
    print(my_non_reapating_character('xxyz'))
    print(my_non_reapating_character('aabb'))
    

