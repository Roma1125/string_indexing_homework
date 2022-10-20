def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if s[0]=='*':
        d=0
    if s[1]=='*':
        d=1
    if s[2]=='*':
        d=2
    if s[3]=='*':
        d=3
    if s[4]=='*':
        d=4
    return d
print(main('asdf*'))
        