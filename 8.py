import itchat

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
	print msg['Text']
	itchat.send(msg['Text'], 'filehelper')
#	return msg['Text']


@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def text_reply(msg):
	print msg['ActualNickName']
	print msg['Text']

itchat.auto_login()
itchat.run()
