def reverse(str):
    n = len(str)
    if n==1:
        return str
    return str[-1] + reverse(str[0:n-1])