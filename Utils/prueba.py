from paramiko import *
from paramiko_expect import *

key = PKey('~/.ssh/id_dsa', 'marajade')

ssh = SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy())
try:
    ssh.connect('10.245.38.34', username='root', password='marajad3', timeout=10, pkey=key)
    print "conectado"

    sshtransport = ssh.get_transport()

    local_addr = ('10.245.38.34', 22)
    dest_addr = ('192.168.4.50', 22)

    sshchannel = sshtransport.open_channel("direct-tcpip", dest_addr, local_addr)

    sw = SSHClient()
    sw.set_missing_host_key_policy(AutoAddPolicy())
    sw.connect('10.245.38.34', username='admin', password='ceycswtic', sock=sshchannel, timeout=5)

    interact = SSHClientInteraction(sw, timeout=10, display=True)
    interact.expect('DGS-1210-24:admin#')
    print interact.current_output_clean




except AuthenticationException:
    print "No conecta"