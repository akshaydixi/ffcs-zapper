import daemon
import urllib2
import sys
import os
from emailclient import SMTPClient
"""
    Basically used to create daemon processes to run in the backend
    This improves speed of response, as the work is done asynchronously
    So PHP can get back control as soon as possible
    

FORMAT:
======
	python daemonize.py <controller> <arguments>

where the function corresponding to the <controller> needs to be implemented
and checked in the function run()

"""

def sendMessage(args):
    command = 'python /opt/lampp/htdocs/pribeta/script/fbchat.py '+args[0]+' '+args[1]+' '+args[2]+' '+args[3]+' '+args[4]+' "'+args[5]+'"'
    with open('/tmp/result.txt','w') as f:
        f.write(command)
    os.system(command)

def sendMailNew(args):
    recipient = args[0]
    subject = args[1]
    message = args[2]
    client = SMTPClient(recipient,subject,message)

def updateMongo():
	command = 'python /opt/lampp/htdocs/pribeta/script/updateMongo.py'
	os.system(command)
	with open('test.txt','w') as f:
		f.write('successfull')

def updateMongoById(args):
	command = 'python /opt/lampp/htdocs/pribeta/script/updateMongoById.py '+str(args[0])
	os.system(command)

def syncFBConnections(args):
	command = 'python /opt/lampp/htdocs/pribeta/script/neo4jAccess.py '+str(args[0])+' "'+str(args[1])+'"'
	with open('/tmp/temp.txt','w') as f:
		f.write(command)
	os.system(command)
	with open('/tmp/temp.txt','w') as f:
	    f.write('done')

def newSyncFBConnections(args):
	command = 'python /opt/lampp/htdocs/pribeta/script/syncFBConnections.py '+str(args[0])+' '+str(args[1])
	with open('/tmp/test.txt','w') as f:
		f.write(command)
	os.system(command)

def updateQRTrack(args):
	command = 'python /opt/lampp/htdocs/pribeta/script/qr_tracker.py '+str(args[0])+' '+str(args[1])
	with open('/tmp/test.txt','w') as f:
		f.write(command+' is executing :)')
	os.system(command)

def run(controller,args):
    if controller == 'FBChatMessage':
        with daemon.DaemonContext():
            sendMessage(args)
    if controller == 'sendMail':
        with daemon.DaemonContext():
            sendMailNew(args)
    if controller == 'updateMongo':
	with daemon.DaemonContext():
	    updateMongo()
    if controller == 'updateMongoById':
	with daemon.DaemonContext():
	    updateMongoById(args)  	
    if controller == 'syncFBConnections':
	with daemon.DaemonContext():
	     newSyncFBConnections(args)  
    if controller == 'updateQRTrack':
	with daemon.DaemonContext():
	    updateQRTrack(args)
 
if __name__ == '__main__':
    controller = sys.argv[1]
    args = sys.argv[2:]
    run(controller,args)
