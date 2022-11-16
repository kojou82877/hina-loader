from fbchat import Client, log, _graphql
from fbchat.models import *
import json
import random
import wolframalpha
import requests
import time
import math
import sqlite3
from bs4 import BeautifulSoup
import os
import concurrent.futures
from difflib import SequenceMatcher, get_close_matches



class ChatBot(Client):

    def onMessage(self, mid=None, author_id=None, message_object=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
        try:
            msg = str(message_object).split(",")[15][14:-1]

            if ("//video.xx.fbcdn" in msg):
                msg = msg

            else:
                msg = str(message_object).split(",")[19][20:-1]
        except:
            try:
                msg = (message_object.text).lower()
                print(msg)
            except:
                pass
        def sendMsg():
            if (author_id != self.uid):
                self.send(Message(text=reply), thread_id=thread_id,
                          thread_type=thread_type)

        def sendQuery():
            self.send(Message(text=reply), thread_id=thread_id,
                      thread_type=thread_type)
        if(author_id == self.uid):
            pass
        else:
            try:
                conn = sqlite3.connect("messages.db")
                c = conn.cursor()
                c.execute("""
                CREATE TABLE IF NOT EXISTS "{}" (
                    mid text PRIMARY KEY,
                    message text NOT NULL
                );
                """.format(str(author_id).replace('"', '""')))

                c.execute("""
                INSERT INTO "{}" VALUES (?, ?)
                """.format(str(author_id).replace('"', '""')), (str(mid), msg))
                conn.commit()
                conn.close()
            except:
                pass
       
        try:
            if("search pdfiiixxd" in msg):
                searchFiles(self)
            elif "weakojouther okojouf" in msg:
                indx = msg.index("weathkojouer okojouf")
                query = msg[indx+11:]
                reply = weather(query)
                sendQuery()

            elif("mkojouute convekojoursation" in msg):
                try:
                    self.muteThread(mute_time=-1, thread_id=author_id)
                    reply = "xd 🔕"
                    sendQuery()
                except:
                    pass

            elif ("🙃" in msg):
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                time.sleep(30)
                reply = "<K><S> (^^) ((^^)) (Y) (^^)|3 🦈 ((^^)) (Y) 3((^^)) (Y) || (Y) ((^^^)) (Y) | 😈 ((^^)) (Y) ((^^^)) 😈 | (Y) ((^^)) 3 😃 ((^^)) || 😃 (Y) ((^^)) 🦈 ((^^)) || (Y) @ (Y) ((^)) J 🦈 || ((^)) T (Y) )^))^) (+) U 🙂 (Y) W (^^) (^) A )(()) (y) (^^)) ^,^ 😈 😃 (Y) 😊) ♥ #_IDH_BH9NGII__KI_MKC_M_L||ND (^) 😃 (Y) ( 🦈 ) #__TH3__L3G3ND__N0NXT0P3R ❤ ( 🦈 ) 😈 #M9RK__H3R3 (Y) (Y) ♥"
                sendMsg()
                time.sleep(60)
                reply = "APNE BAAP MARK KI NP COPY KARKE SHABIT KAR DIYA KI TUMHARI AMMI MUJHSE HI XHUDTI HAI DAILY 😂😂🤘 KEEP FEEL MY LAND KIDXXX ABHI TO MAJARK KAR RHA HUN TUMHARE SAATH FYT SAMJHNE KI BHUL NA KARO AGAR FYT PAR AA GAYA TO TUMHARI AMMI LE JAAUNGA OYO ME AUR WAHI PAR CH0DUNGA 😂✌❤"
                sendMsg()
                time.sleep(30)
                reply = "7 😃 ((^)) ❤ 😎 😳 #___B4ND3__H4II__H4M__USK33 8|^^^<) 😃 ((^)) ❤ 😎 >> 🤓 <33 __> [[ #H4M__P3__KI5K4_J0R 😎 🦈 😳 😛 #M9__CH0D__D3NG3__U4SKI__J0_D3KH0__H4M4RI__0R 😃 ((^)) ❤ 😎 __________#M9RK H3R3 :D <3"
                sendMsg()
                
                



        except Exception as e:
            print(e)

        self.markAsDelivered(author_id, thread_id)

    def onMessageUnsent(self, mid=None, author_id=None, thread_id=None, thread_type=None, ts=None, msg=None):

        if(author_id == self.uid):
            pass
        else:
            try:
                conn = sqlite3.connect("messages.db")
                c = conn.cursor()
                c.execute("""
                SELECT * FROM "{}" WHERE mid = "{}"
                """.format(str(author_id).replace('"', '""'), mid.replace('"', '""')))

                fetched_msg = c.fetchall()
                conn.commit()
                conn.close()
                unsent_msg = fetched_msg[0][1]

                if("//video.xx.fbcdn" in unsent_msg):

                    if(thread_type == ThreadType.USER):
                        
                        self.send(Message(text=reply), thread_id=thread_id,
                                  thread_type=thread_type)
                        self.sendRemoteFiles(
                            file_urls=unsent_msg, message=None, thread_id=thread_id, thread_type=ThreadType.USER)
                    elif(thread_type == ThreadType.GROUP):
                        user = self.fetchUserInfo(f"{author_id}")[
                            f"{author_id}"]
                        username = user.name.split()[0]
                        #reply = f"{username} just unsent a video"
                        self.send(Message(text=reply), thread_id=thread_id,
                                  thread_type=thread_type)
                        self.sendRemoteFiles(
                            file_urls=unsent_msg, message=None, thread_id=thread_id, thread_type=ThreadType.GROUP)
                elif("//scontent.xx.fbc" in unsent_msg):

                    if(thread_type == ThreadType.USER):
                        
                        self.send(Message(text=reply), thread_id=thread_id,
                                  thread_type=thread_type)
                        self.sendRemoteFiles(
                            file_urls=unsent_msg, message=None, thread_id=thread_id, thread_type=ThreadType.USER)
                    elif(thread_type == ThreadType.GROUP):
                        user = self.fetchUserInfo(f"{author_id}")[
                            f"{author_id}"]
                        username = user.name.split()[0]
                        #reply = f"{username} just unsent an image"
                        self.send(Message(text=reply), thread_id=thread_id,
                                  thread_type=thread_type)
                        self.sendRemoteFiles(
                            file_urls=unsent_msg, message=None, thread_id=thread_id, thread_type=ThreadType.GROUP)

            except:
                pass


cookies = {
    "sb": "xasyYmAoy1tRpMGYvLxgkHBF",
    "fr": "0NxayJuewRHQ30OX3.AWVJwIYNh0Tt8AJv6kSwDamhkoM.BiMrVd.Iu.AAA.0.0.BiMtVZ.AWXMVaiHrpQ",
    "c_user": "100062003664357",
    "datr": "xasyYs51GC0Lq5H5lvXTl5zA",
    "xs": "27%3Am-qBrOpI2Xr_5g%3A2%3A1668531198%3A-1%3A5095%3A%3AAcWEYSIqcQxkcOkMGkqoB6hn8UoRm67RyjH6Y5EMWQ"
}


client = ChatBot("",
                 "", session_cookies=cookies)
print(client.isLoggedIn())

try:
    client.listen()
except:
    time.sleep(3)
    client.listen()
