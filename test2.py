__author__ = 'Bog'
import bftplib

print "trying"
file = open("C:\\Stuff3\\dev\\py\\xxx.txt", "rb")
ftp = bftplib.FTP("192.168.154.172", 2121)
#ftp.setStorePort(1111)
#ftp.set_pasv(False)
ftp.login("z")
ftp.storbinary("STOR e.txt", file)
ftp.quit()
print "done"