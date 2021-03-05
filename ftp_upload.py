#-----------------------------------------------------------------------
# This script  allows to upload to Fileserve with FTP various files at the same time
#
from ftplib import FTP
import sys
import osf
import glob

########### MODIFY ########################

USER = 'Administrator'
PASS = '@dm!n.3nergy@2021'

########### MODIFY IF YOU WANT ############

SERVER = 'LGBU-INT-SVR-02'
PORT = 21
BINARY_STORE = False # if False then line store (not valid for binary files (videos, music, photos...))

###########################################

def print_line(result):
    print(result)

def connect_ftp():
    #Connect to the server
    ftp = FTP()
    ftp.connect(SERVER, PORT)
    ftp.login(USER, PASS)
    
    return ftp

def upload_file(ftp_connetion, upload_file_path):

    #Open the file
    try:
        upload_file = open(upload_file_path, 'r')
        #get the name of file
        path_split = upload_file_path.split('/')
        final_file_name = path_split[len(path_split)-1]
        path_split = upload_file_path.split('\\')
        final_file_name = path_split[len(path_split)-1]
        print(final_file_name)
        #transfer the file
        print('Uploading ' + final_file_name + '...')

        if BINARY_STORE:
            ftp_connetion.storbinary('STOR '+ final_file_name, upload_file)
        else:
            #ftp_connetion.storlines('STOR ' + final_file_name, upload_file, print_line)
            ftp_connetion.storlines('STOR '+ final_file_name, upload_file)
            
        print('Upload finished.')
        
    except IOError:
        print ("No such file or directory... passing to next file")

    
#Take all the files and upload all
ftp_conn = connect_ftp()

#Access file folder and retrieve all files
x=glob.glob("../Desktop/DataLogger/*.wdf")
print(len(x))
for i in range(len(x)+1):
    upload_file(ftp_conn, x[i])