import itchat
import time
itchat.login(enableCmdQR=2)
users = itchat.search_friends(name='vector')
print users
userName =users[0]['UserName']
var=1
while var == 1:
	itchat.send("hello",toUserName = userName)
#	time.sleep(1)
