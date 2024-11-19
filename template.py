#!/usr/bin/env python3

'''
    author: {{author}}
    time: {{time}}
'''
from pwn import *

filename = "{{filename}}"
libcname = "{{libcname}}"
host = "{{host}}"
port = {{port}}
e = context.binary = ELF(filename)
context.terminal=["tmux","split","-h"]
if libcname:
    libc = ELF(libcname)
gs = '''
b main
{% if debug_file_directory %}set debug-file-directory {{debug_file_directory}}{%endif%}
{% if source_dircetory %}set directories {{source_dircetory}}{%endif%}
'''

def start():
    if args.GDB:
        return gdb.debug(e.path, gdbscript = gs)
    elif args.REMOTE:
        return remote(host, port)
    else:
        return process(e.path)

p = start()

# Your exploit here

p.interactive()
