from wxpy import *
bot = Bot()

tuling = Tuling(api_key='69f16f563d124ccfb7635de6c84b1f5e')


@bot.register(msg_types=TEXT)
def auto_reply_all(msg):
	tuling.do_reply(msg)
bot.join()
