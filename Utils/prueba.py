from paramiko import *

key = PKey('~/.ssh/id_dsa', 'marajade')

ssh = SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy())
try:
    ssh.connect('10.245.10.98', username='root', password='marajad3', timeout=10, pkey=key)
    print "conectado"
    stdin, stdout, stderr = ssh.exec_command("pwd")

    print stdout.read().rstrip()

except AuthenticationException:
    print "hola"