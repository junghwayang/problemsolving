def timeConversion(s):
    if s[-2:] == 'AM' and s[:2] == '12':
        return '00' + s[2:8]
    elif s[-2:] == 'PM' and s[:2] != '12':
        return str(int(s[:2]) + 12) + s[2:8]
    else:
        return s[:8]