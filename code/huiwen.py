while 1:
    s = raw_input()
    if s != " ":
        i, j, end = 0, len(s)-1, len(s)-1
        while i <= j:
            if s[i] == s[j]: 
                i += 1
                j -= 1
            else:
                i, j, end = 0, end-1, end-1
        print (end+1)
    else:
        break
