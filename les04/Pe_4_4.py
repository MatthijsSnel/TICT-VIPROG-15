def new_password(oldpassword, newpassword):
    if len(newpassword) > 5 and oldpassword != newpassword:
        return True
    else:
        return False



new_password('randompass1', 'randompass2')