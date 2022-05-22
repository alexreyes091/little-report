import platform
import subprocess

def isIpActive(rest, ip):
    
    parameter = '-n' if platform.system().lower()=='windows' else '-c'

    command = ['ping', parameter, '1', ip]
    response = subprocess.call(command)

    if response == 0:
        rest['status'] = 1
    else:
        rest['status'] = 0

        