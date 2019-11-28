def minimumNumber(n, password):
    cnt = 0    
    if not any(p.isdigit() for p in password):
        cnt += 1
    if not any(p.islower() for p in password):
        cnt += 1
    if not any(p.isupper() for p in password):
        cnt += 1
    if not any(p in '!@#$%^&*()-+' for p in password):
        cnt += 1
    return max(cnt, 6 - n)