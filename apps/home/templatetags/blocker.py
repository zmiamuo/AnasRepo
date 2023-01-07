import time
import sys
import platform

#function to fetch the URLs that have been saved in urllist.txt for blocking


#fetching the URLs, defining the redirection to localhost 127.0.0.1

redirect = "127.0.0.1"

#identifying the underlying Operating System to decide the directory the hosts file resides in
#Currently working for Microsoft Windows, Linux Distributions and MacOS
if platform.system() == 'Windows':
    host_file = r"C:\Windows\System32\drivers\etc\hosts"
elif platform.system() == "Linux" or platform.system() == "darwin":
    host_file = "/etc/hosts"
else:
    print("Expected your OS to be Windows, Linux or MacOS but found something else, hence quitting...")
    sys.exit(1)

#function that will block or remove blocking based on user request
def block(string):
	while True:
		with open(host_file, 'r+') as hostentry:
			hosts = hostentry.read() #reading the host entries to confirm if the required URLs are present or not
			#adding the urls from DB in hosts file and adding redirection to localhost to make them inaccessible
			for url in [string]:
				if url not in hosts:
					hostentry.write(redirect+' '+url+'\n')
		try:
			time.sleep(50)
		except KeyboardInterrupt:
			#catching the ctrl + c (quit) from user, asking for confirmation
			quitting = input("Do you really want to disable content blocking?[Y/y or N/n]")
			if (quitting == "Y" or quitting == "y"):
				#clearing the entries made during blocking phase
				with open(host_file, 'r+') as hostentry:
					hosts = hostentry.readlines()
					hostentry.seek(0)
					for host in hosts:
						if not any(url in host for url in [string]):
							hostentry.write(host)
					hostentry.truncate()
				print("Cool!!\nhave a great time!")
				sys.exit(1)
			else:
				continue

