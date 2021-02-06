#pylint:disable=E0001
import amino
import time
import os
print("\033[0;31m"+"""  __  __ ___  ___   ___  ___ _    ___ _____ ___ ___ 
 |  \/  / __|/ __| |   \| __| |  | __|_   _| __| _ \ """)
print("\033[0;33m"+""" | |\/| \__ \ (_ | | |) | _|| |__| _|  | | | _||   / """)
print("\033[0;36m"+""" |_|  |_|___/\___| |___/|___|____|___| |_| |___|_|_\ """)
time.sleep(1)
print("\n\n")
print("NOTE:")
print("""this tool can be used for harm uses or for delete the spam message, thank you""")
print("""
YOUTUBE:
	Flame
	DASH&DARK KING(FRANCIS)©®	""")
time.sleep(0.5)
print("\n")
email=input("\033[0;32m"+"YOUR EMAIL: ")
time.sleep(0.5)
print("\n")
password=input("YOUR PASSWORD: ")
time.sleep(0.5)
print("\n")
client=amino.Client() 
client.login(email=email,password=password)
thelink=input("\033[0;37m"+"CHAT LINK: ")
gpid=client.get_from_code(thelink)
chatid=gpid.objectId
comid=gpid.path[1:gpid.path.index("/")]
subclient = amino.SubClient(comId=comid, profile=client.profile)
msgsize=input("\033[0;35m"+"HOW MUCH MESSAGES BOT TAKE(1-100): ")
while True:
    msglist = subclient.get_chat_messages(chatId=chatid, size=msgsize)
    for msgId,msg in zip(msglist.messageId,msglist.content):
    	subclient.delete_message(chatId=chatid,messageId=msgId)
    	print("[DONE] (TO EXIT THE TOOL CLOSE THE PAGE OR: CTRL+C")
    	
		