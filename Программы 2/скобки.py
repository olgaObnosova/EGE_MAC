def check_par(stri):
    c=0
    for a in stri:
        if a=')':
            c-=1
            if c < 0:
                return False
        if a='(':
           c+=1
    return (c==0)
