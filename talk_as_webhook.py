#if module not installed then install
try:
    import webbrowser
    import fade
    import requests
    import os
    import colorama
    from colorama import Fore
    import time
except ModuleNotFoundError:
    os.system("pip install fade")
    os.system("pip install requests")
    os.system("pip install colorama")
    os.system("python talk_as_webhook.py")#re open file after modules are installed

colorama.init(autoreset=True)# make oclors show in terminal/console
#open links
webbrowser.open("https://www.youtube.com/channel/UCN8LRd8JnX2FkelKfnfRRfg")
webbrowser.open("discord.gg/jnn")


title = fade.purplepink(f"""
████████╗ █████╗ ██╗    ██╗    ██╗   ██╗     ██╗    ██████╗ 
╚══██╔══╝██╔══██╗██║    ██║    ██║   ██║    ███║   ██╔═████╗
   ██║   ███████║██║ █╗ ██║    ██║   ██║    ╚██║   ██║██╔██║
   ██║   ██╔══██║██║███╗██║    ╚██╗ ██╔╝     ██║   ████╔╝██║
   ██║   ██║  ██║╚███╔███╔╝     ╚████╔╝      ██║██╗╚██████╔╝
   ╚═╝   ╚═╝  ╚═╝ ╚══╝╚══╝       ╚═══╝       ╚═╝╚═╝ ╚═════╝ 
  Talk     As     Webhook   |    discord.gg/jnn | @jnnlol                   
""")
print(title)
print(Fore.RED+"This is NOT an efficient way to spam webhooks. Instead use my webhook spammer at: https://github.com/jnnlol/discord-webhook-spammer")
webhook = input(Fore.MAGENTA+"Enter Webhook: ")
set_webhook = "IF YOU WANT UR WEBHOOK SET AUTOMATICALLY SET IT HERE"

while True:
    message = input(Fore.MAGENTA+"Enter webhook message (Message to send): ")
    requests.post(webhook, json={"content": message})
    #requests.post(requests.post(set_webhook, json={"content": message}))
    #REMOVE THE # FROM THE LINE ABOVE IF YOU HAVE THE WEBHOOK SET IN THE PROGRAM ALREADY (if you edit the source code)
    print(Fore.BLUE+f"Sent {message}")
    os.system("cls")
    print(title)