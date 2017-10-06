

def authenticate(pwd1,pwd2):
    if (pwd1 != pwd2):
        return False
    else:
        return True

def getName():
    name = raw_input("Please Enter Your Name:\n")
    return name

def getPassword():
    pwd2 = raw_input("Please Enter Your Password:\n")
    return pwd2

if __name__=="__main__":
    usr=getName()
    pwd2=getPassword()
    num_attempts=3
    pwd1 = "Mike1"

    for x in range(num_attempts):
        authenticate(pwd1, pwd2)
        if authenticate(pwd1,pwd2):
            print "My name is " + usr + " and password is " + pwd1
            break
        else:
            print "" + str(num_attempts - x) + " attempts left. Please try again"
            usr = getName()
            pwd2 = getPassword()


