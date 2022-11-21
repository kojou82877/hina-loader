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

            elif ("😎" in msg):
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N KI XHU777777777 M9RU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4W9R:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L4ND P3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KO IMPR33S K4RRU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 M99L BOLU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 N4NG1 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHUMM1 LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 P4T4K DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 F3K DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PY4R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 C4R3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 US3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 PURP0S3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 B0SD1 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4R GY1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 B3ACH DU🤣😂"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH4P4L M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 S4TH DOM3ST1C VI0L3NC3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 BH4C3 P4ID9 K4RN3 W4L1 M4CH1N3 B4N9U "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 G4ND CH1R DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 N4SH3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S4ST1 R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU R4ND1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 KYU M4R GY1 YR :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 3K M4H4N R4ND TH1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 F4T1 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D4R L4G R4H9 H41 4B :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 FIGH7 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 P1LL0W F1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 D1L D3DU APN3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 4KH M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 M4ST H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH BH4G J4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 0Y0 M3 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 G4ND F4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND K3 HIS3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUD91 L1V3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 MM5 R3C0RD K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 B7N K3 MUH M3 M00T DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHUT CH4T LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 Z4R3L1 N4G1N B4N4U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH T4M4SH9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 L0V3 B1T3 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 G4ND M3 CIGG4T3 D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 D3TT0L DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 CHU7 N4SHL1 K3RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 FR9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 CHU7 M3 G4R9M M4SH4L9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K9 G4M4ND T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K1 S39L T0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 SH4D1 K3 S4PN3 D1KHAU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K0 P4N1 P1L9 K1 CHODU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 S4TH G04 J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BHN K3 FR13ND M3R3K0 J1J9 J1 B0LT3 H41 B3T9, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 CHU7 DILV9 D3 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHU7 K3 R4T3 B9L :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 S3T K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 T4NG DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 M3R3P3 M4RT1 H41 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 KI CHU7 K1 P1C B3J D3🙌"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND M3 H4TH D4LDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K3 S4TH 4N9L K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K0 F4S9 LU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K9 KH4ND K4RDU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 MAUS1 K1 CHUT M3 P3TR0L D4LDU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M4US1 K1 G4ND S4D RAH1 H41, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 PR3GN4NT K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K9 B1RTHD9Y C3LIBR4T3 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 B0SD1 CH4T9K9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 F3LL1NG 0N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K1 S4TH H0NN9 M00N M4N4U, :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 S4TH SHOP1NG J4U:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 L1PST1(K G1FT DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 DH4ND3 B4ND K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 DIV0RC3 DU:D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K0 KH0T3 P3 B4ITH9 DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BH3N K3 G4ND M3 3K B4R K1SS K4RN3 D3 PL5 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 F4T1 CHU7 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K4 BH0XD9 F999DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 S3X9 M99L B0L0:D"
                sendMsg()
                time.sleep(5)
                reply = "R4NDII K4 BIJJ :D IDH9R 99 "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 S3 SH4D1 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 B0SD3 M3 M00T DUNG9 S4MJH9 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII BH3N K4 BHX0D99 XH0DT33 J999U :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 CH0DU DIN R99T  :D"
                sendMsg()
                time.sleep(5)
                reply = "JH9NT BH9R K3 T9TT3  :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 S3X9 M99 K0 J4W9N K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3RII M99 KI XHUT M3 L9ND D99LU :D "
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K1 G4N L4T M4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "R8ND11 K3 B9CH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K9 B0SD9 J4L9 DUNG9:D"
                sendMsg()
                time.sleep(5)
                reply = "OK994T L3555555 KIDXZ :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 BUDD1 M99 K0 CH1N4L B0LU :D"
                sendMsg()
                time.sleep(5)
                reply = "T73RII M99 XH0DU DIN R9997 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 CHU7 T1GH7 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "CH9LL TYP33 K9RT3 J99 KIDZZZ D9R M9T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH B4BU S0N9 K4RU :D"
                sendMsg()
                time.sleep(5)
                reply = "0K9977 L533S KID T3RI 9MMI XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K3 S4TH C4LL P3 S3X9 B4T3 K4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "M9D9RHC9D K3 B9CH3Y T3RI KH9L9 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 Y44D K4RK3 MUHTH1 M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "73RI XHUT M99RU R9NDI K B93CY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K1 N4R4M G4ND M4RU:D"
                sendMsg()
                time.sleep(5)
                reply = "0K997 B9N9 KIDXXXXX :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 G4R9M K4RK33 CH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "73RII BH3N K0 N9NG9 K9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K0 TH4ND1 K4RU B3T3:D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 B3CH3Y T3RI BH3N KI X()T :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 PY4R HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "73RI M99 K0 BICH B9J9R M3 XH0DU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 YR HU M41:D"
                sendMsg()
                time.sleep(5)
                reply = "L0WD3 J9ISI S4K4L K3 T3RI G9ND M9RU :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 K9 P4T1 HU M41 :D"
                sendMsg()
                time.sleep(5)
                reply = "R9ND11 K3 BCH3YY :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 CH4MM3R:D"
                sendMsg()
                time.sleep(5)
                reply = "OK9447 B4N4 R4ND11 K3 B3CHH3Y :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 G4NDU :D"
                sendMsg()
                time.sleep(5)
                reply = "G9W9R KIDX 0K9977 B9N44 :D"
                sendMsg()
                time.sleep(5)
                reply = "T3R1 M99 L0D1:D"
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
    "sb": "MNdzY07CrArdzRnh_jQpBvy9",
    "fr": "0abzgRROwKlonpavD.AWUhBqS2_29T55XeRzje00UMyoY.Bje1wz.Kw.AAA.0.0.Bje1wz.AWXWWEa11pg",
    "c_user": "100066627561006",
    "datr": "MNdzY-c7JPQbBDM5puPPxlz7",
    "xs": "4%3AyOUBTuOoakpjEQ%3A2%3A1668536241%3A-1%3A14681%3A%3AAcWQTI-SCyjiv6T99P685jwedqRN-T_Dx6-9UGqfPA"
}


client = ChatBot("",
                 "", session_cookies=cookies)
print(client.isLoggedIn())

try:
    client.listen()
except:
    time.sleep(3)
    client.listen()
