def block(string) :
    import time
    from datetime import datetime as dt
    #Windows host file path
    hostsPath=r"C:/Windows/System32/drivers/etc/hosts"
    redirect="127.0.0.1"
    #Add the website you want to block, in this list
    websites=string
    with open(hostsPath,'r+') as file:
        content = file.read()
        if websites in content:
            pass
        else:
            file.write(redirect+" "+websites+"\n")



    