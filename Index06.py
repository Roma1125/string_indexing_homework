def main(s):
    """
    A string variable consisting of several characters is given. Add and return the first and last character.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    answer=f'{s[0]+s[-1]}'
    return answer
print(main('aaadadsdsf'))