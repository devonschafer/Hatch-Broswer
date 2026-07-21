import paramiko
from export import Export
from dds import DDS
import os


class ServerSide:

    def surf():
        hostname = Export.host
        username = Export.user
        password = Export.key
        website = Export.url
        command = 'cat /home/hatch/browser/%s' % website

        # Create an SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect to the server
        ssh.connect(hostname, username=username, password=password)

        # Execute the command
        stdin, stdout, stderr = ssh.exec_command(command)

        # Read the output
        Export.virtual_webpage = stdout.read().decode()
        error = stderr.read().decode()

        # Close the connection
        ssh.close()

        Export.refresh = 1

    def publish_page():
        host = Export.host
        port = 22
        username = Export.user
        password = Export.key

        src = "%s" % Export.publish_path
        dst = "/home/hatch/browser/search.dds"
        #print("cwd:", os.getcwd())
        #print("src:", repr(src), "exists:", os.path.isfile(src))
        #print("dst:", repr(dst))
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, port=port, username=username, password=password)
        sftp = ssh.open_sftp()
        sftp.put(src, dst)
        #print(src, dst)
        sftp.close()
        ssh.close()


        
