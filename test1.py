__author__ = 'Bog'
import bftplib

print "trying"
file = open("C:\\Users\\Bog\\Desktop\\xxx.txt", "rb")
ftp = bftplib.FTP("127.0.0.1", 2121)
ftp.connect()
#ftp.setStorePort(1111)
#ftp.set_pasv(False)
ftp.login("z")
ftp.storbinary("STOR e.txt", file)
ftp.quit()
print "done"