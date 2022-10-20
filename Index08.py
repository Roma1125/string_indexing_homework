def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if s[0]=='*':
        answer=0
    if s[1]=='*':
        answer=1
    if s[2]=='*':
        answer=2
    if s[3]=='*':
        answer=3
    if s[4]=='*':
        answer=4
    return answer
print(main('asdf*'))
        