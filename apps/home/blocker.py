def block(string):
    import time
    from datetime import datetime as dt
    #Windows host file path
    hostsPath=r"C:/Windows/System32/drivers/etc/hosts"
    redirect="127.0.0.1"
    #Add the website you want to block, in this list
    websites=string
    #Duration during which, website blocker will work is from 9 am to 6 pm
    with open(hostsPath,'r+') as file:
            content = file.read()
            if websites in content:
                pass
            else:
                file.write(redirect+" "+websites+"\n")