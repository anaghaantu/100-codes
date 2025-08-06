def remove_adjacent_duplicates(s):
    
    if len(s) <= 1:
        return s
    if s[0] == s[1]:
        i = 1
        while i < len(s) and s[i] == s[0]:
            i += 1
        return remove_adjacent_duplicates(s[i:])
    else:
        rest = remove_adjacent_duplicates(s[1:])
        if rest and rest[0] == s[0]:
            return rest[1:]
        else:
            return s[0] + rest
   
