import ftplib
import os,fnmatch
from time import sleep
from filestack import Client
import glob

sunucu = input("sunucunuzu giriniz : ")
kullanıcı = input("kullanıcı adı giriniz : ")
password = input("şifre giriniz : ")
dosya = input("nereye yüklemek istiyorsunuz : ")
delay = 600000

#files = glob.glob("*.pcap")
while True:
    ftp_server = ftplib.FTP(sunucu, kullanıcı, password)
    ftp_server.encoding = "utf-8"
    ftp_server.cwd(f'/{dosya}')
    #filename = "*.pcap"
    fileOfDirectory = os.listdir('.')
    pattern = "*.pcap"
    for filename in fileOfDirectory:
        if fnmatch.fnmatch(filename, pattern):   
            with open(f'{filename}') as pcap_file:
                ftp_server.storbinary('STOR '+filename,pcap_file)
    ftp_server.dir()
    ftp_server.quit()
    os.system('del "*.pcap"')
    sleep(delay)