# Q1: password quality function:
def check_password(password):

    SQ = False
    num = False
    length = False
    letters = False
    upper = False
    if len(password) >= 6:
        length = True

    for char in password:
        if char in "0123456789":
            num = True
        if char in "!@#$%^&*()?><,./":
            SQ = True
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            upper = True
        if char in "abcdefghijklmnopqrstuvwxyz":
            letters = True

    if SQ and num and length and letters and upper == True:
        return True
    else:
        return False

# password = "Trump@123"
# if check_password(password): # Works when the statement is True in the return
#     print("Nice Password")
# else:
#     print("Bad Password")

# Q2: Make sure the email format is correct
#
# .com@joe      X
# @gmail.Joe    X 