import pyrogram
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton
import bypasser
import os
import ddl
import requests
import threading

# bot
bot_token = os.environ.get("TOKEN", "")
api_hash = os.environ.get("HASH", "") 
api_id = os.environ.get("ID", "")
app = Client("my_bot",api_id=api_id, api_hash=api_hash,bot_token=bot_token)  

# ENVs
GDTot_Crypt = os.environ.get("CRYPT","COOKIEID")
Laravel_Session = os.environ.get("Laravel_Session","")
XSRF_TOKEN = os.environ.get("XSRF_TOKEN","")
KCRYPT = os.environ.get("KOLOP_CRYPT","")
DCRYPT = os.environ.get("DRIVEFIRE_CRYPT","")
HCRYPT = os.environ.get("HUBDRIVE_CRYPT","")
KATCRYPT = os.environ.get("KATDRIVE_CRYPT","")


# main thread
def mainthread(cmd,message):

    try:
        url = str(message.reply_to_message.text)
    except:
        try:
            url = str(message.text.split(f"{cmd} ")[1])
        except:
            app.send_message(message.chat.id, f"⚠️ Invalid Format, either **reply** to a **link** or use like this -> **{cmd} link**", reply_to_message_id=message.id)
            return


    if cmd == "/dl":
        msg = app.send_message(message.chat.id, "⚡ Generating Direct Link...", reply_to_message_id=message.id)
    elif cmd in ["/ol","/ps"]:
        msg = app.send_message(message.chat.id, "🔎 This Might Take Some Time Kindly Wait...", reply_to_message_id=message.id)
    else:
        msg = app.send_message(message.chat.id, "🔎 Bypassing...", reply_to_message_id=message.id)


    # igg games
    if cmd == "/ig":
        print("You Have Entered igg:",url)
        link = bypasser.igggames(url)

    # ola movies
    if cmd == "/ol":
        print("You Have Entered ola movies:",url) 
        link = bypasser.olamovies(url)
        
    # script links
    elif cmd == "/sc":
        print("You Have Entered script link:",url)
        try:
            link = bypasser.getfirst(url)
        except:
            sess = requests.session()
            link = bypasser.getfinal(f'https://{url.split("/")[-2]}/',url, sess)
        
    # direct download link
    elif cmd == "/dl":
        print("You Have Entered ddl:",url)
        link = ddl.direct_link_generator(url)
        
    # katdrive
    elif cmd == "/kd":
        if KATCRYPT == "":
            app.send_message(message.chat.id, "🚫 You can't use this because **KATDRIVE_CRYPT** ENV not provided", reply_to_message_id=message.id)
            return
        
        print("Entered Link katdrive:",url)
        link = bypasser.katdrive_dl(url, KATCRYPT)
        

    # hubdrive
    elif cmd == "/hd":
        if HCRYPT == "":
            app.send_message(message.chat.id, "🚫 You can't use this because **HUBDRIVE_CRYPT** ENV not provided", reply_to_message_id=message.id)
            return

        print("Entered Link hubdrive:",url)
        link = bypasser.hubdrive_dl(url, HCRYPT)
        

    # drivefire
    elif cmd == "/df":
        if DCRYPT == "":
            app.send_message(message.chat.id, "🚫 You can't use this because **DRIVEFIRE_CRYPT** ENV not provided", reply_to_message_id=message.id)
            return

        print("Entered Link drivefire:",url)
        link = bypasser.drivefire_dl(url, DCRYPT)
        

    # kolop
    elif cmd == "/ko":
        if KCRYPT == "":
            app.send_message(message.chat.id, "🚫 You can't use this because **KOLOP_CRYPT** ENV not provided", reply_to_message_id=message.id)
            return

        print("Entered Link kolop:",url)
        link = bypasser.kolop_dl(url, KCRYPT)
        

    # filecrypt
    elif cmd == "/fc":
        print("You Have Entered filecrypt:",url)
        link = bypasser.filecrypt(url)
        

    # shareus
    elif cmd == "/su":
        print("You Have Entered shareus:",url)
        link = bypasser.shareus(url)
        

    # shortingly
    elif cmd == "/sg":
        print("You Have Entered shortingly:",url)
        link = bypasser.shortlingly(url)
        

    # gyanilinks
    elif cmd == "/gy":
        print("You Have Entered gyanilinks:",url)
        link = bypasser.gyanilinks(url)
        

    # pixl
    elif cmd == "/pi":
        print("You Have Entered pixl:",url)
        link = bypasser.pixl(url)
        

    # shorte
    elif cmd == "/st":
        print("You Have Entered shorte:",url)
        link = bypasser.sh_st_bypass(url)
        

    # psa
    elif cmd == "/ps":
        print("You Have Entered psa:",url)
        link = bypasser.psa_bypasser(url)
        

    # sharer pw
    elif cmd == "/sh":
        if XSRF_TOKEN == "" or Laravel_Session == "":
            app.send_message(message.chat.id, "🚫 You can't use this because **XSRF_TOKEN** and **Laravel_Session** ENV not provided", reply_to_message_id=message.id)
            return

        print("Entered Link sharer:",url)
        link = bypasser.sharer_pw(url, Laravel_Session, XSRF_TOKEN)
        

    # gdtot url
    elif cmd == "/gt":
        print("Entered Link gdtot:",url)
        link = bypasser.gdtot(url,GDTot_Crypt)
        

    # adfly
    elif cmd == "/af":
        print("You Have Entered adfly:",url)
        out = bypasser.adfly(url)
        link = out['bypassed_url']
 
    # gplinks
    elif cmd == "/gp":
        print("Entered Link gplink:",url)
        link = bypasser.gplinks(url)
        
    # droplink
    elif cmd == "/dp":
        print("You Have Entered droplink:",url)
        link = bypasser.droplink(url)
        
    # linkvertise
    elif cmd == "/lv":
        print("You Have Entered linkvertise:",url)
        link = bypasser.linkvertise(url)
        
    # rocklinks
    elif cmd == "/rl":
        print("You Have Entered rocklinks:",url)
        link = bypasser.rocklinks(url)
        
    # ouo
    elif cmd == "/ou":
        print("You Have Entered ouo:",url)
        link = bypasser.ouo(url)

    # gdrive look alike
    elif cmd == "/gd":
        print("You Have Entered gdrive:",url)
        link = bypasser.unified(url)

    # others
    elif cmd == "/ot":
        print("You Have Entered others:",url)
        link = bypasser.others(url)

    # finnaly
    print("bypassed:",link)
    try:
        n = 4096
        split = [link[i:i+n] for i in range(0, len(link), n)]
        for ele in split:
            app.edit_message_text(message.chat.id, msg.id, f'__{ele}__')
    except:
        app.edit_message_text(message.chat.id, msg.id, "__Failed to Bypass__")


# commands
AvailableCommands = ['ol','sc','dl','kd','hd','df','ko','fc','su','sg','gy','pi','st','ps','sh','gt','af','gp','dp','lv','rl','ou','gd','ot','ig']
@app.on_message(filters.command(AvailableCommands))
def receive(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    bypass = threading.Thread(target=lambda:mainthread(message.text.split(" ")[0],message),daemon=True)
    bypass.start()


# start command
@app.on_message(filters.command(["start"]))
def send_start(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    app.send_message(message.chat.id, f"Heylooo, **{message.from_user.mention}**, Welcome to Shit Bypass Bot👀. Kindly use /help to view supported sites list.",


# help command
@app.on_message(filters.command(["help"]))
def send_help(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    app.send_message(message.chat.id, "🔗 **Available Sites** \n\n  \
 /dl - direct download link (/ddllist) \n  \
 /af - adfly \n  \
 /gp - gplinks \n  \
 /dp - droplink \n  \
 /lv - linkvertise \n  \
 /rl - rocklinks \n  \
 /gd - gdrive look-alike (/gdlist) \n  \
 /ot - others (/otlist) \n  \
 /ou - ouo \n  \
 /gt - gdtot \n  \
 /sh - sharer \n  \
 /ps - psa \n  \
 /st - shorte \n  \
 /pi - pixl \n  \
 /gy - gyanilinks \n  \
 /sg - shortingly \n  \
 /su - shareus \n  \
 /fc - filecrypt \n  \
 /ko - kolop \n  \
 /df - drivefire \n  \
 /hd - hubdrive \n  \
 /kd - katdrive \n  \
 /sc - script links \n  \
 /ol - olamovies \n  \
 /ig - igg games \n\n\
Reply to the link with command or use this format /xx link",
reply_to_message_id=message.id)


# gd list
@app.on_message(filters.command(['gdlist']))
def gdlis(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    list = """- appdrive.info \n\
- driveapp.in \n\
- drivehub.in \n\
- gdflix.pro \n\
- drivesharer.in \n\
- drivebit.in \n\
- drivelinks.in \n\
- driveace.in \n\
- drivepro.in \n\
          """
    app.send_message(message.chat.id, list, reply_to_message_id=message.id)


# others list
@app.on_message(filters.command(['otlist']))
def otlis(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    list="""- exe.io/exey.io \n\
- sub2unlock.net/sub2unlock.com \n\
- rekonise.com \n\
- letsboost.net \n\
- ph.apps2app.com \n\
- mboost.me	\n\
- sub4unlock.com \n\
- ytsubme.com \n\
- bit.ly \n\
- social-unlock.com	\n\
- boost.ink	\n\
- goo.gl \n\
- shrto.ml \n\
- t.co \n\
- tinyurl.com
    """
    app.send_message(message.chat.id, list, reply_to_message_id=message.id)    


# ddl list
@app.on_message(filters.command(['ddllist']))
def ddllis(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    list="""- disk.yandex.com \n\
- mediafire.com \n\
- uptobox.com \n\
- osdn.net \n\
- github.com \n\
- hxfile.co \n\
- anonfiles.com \n\
- letsupload.io \n\
- 1drv.ms(onedrive) \n\
- pixeldrain.com \n\
- antfiles.com \n\
- streamtape.com \n\
- bayfiles.com \n\
- racaty.net \n\
- 1fichier.com \n\
- solidfiles.com \n\
- krakenfiles.com \n\
- upload.ee \n\
- mdisk.me \n\
- wetransfer.com \n\
- gofile.io \n\
- dropbox.com \n\
- zippyshare.com \n\
- megaup.net \n\
- fembed.net, fembed.com, femax20.com, fcdn.stream, feurl.com, layarkacaxxi.icu, naniplay.nanime.in, naniplay.nanime.biz, naniplay.com, mm9842.com \n\
- sbembed.com, watchsb.com, streamsb.net, sbplay.org
    """
    app.send_message(message.chat.id, list, reply_to_message_id=message.id)     


# see help
@app.on_message(filters.text)
def short(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    if message.text[0] == "/":
        app.send_message(message.chat.id, "⏩ see /help", reply_to_message_id=message.id)


# server loop
print("bot started")
app.run()
