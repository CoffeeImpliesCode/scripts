import subprocess as sp
from subprocess import PIPE
import json

def rofi_menu(title, choices, sep=';'):
    proc = sp.Popen(['rofi', '-sep', sep, '-dmenu', '-p', title], stdout=PIPE, stdin=PIPE)
    stdout, _ = proc.communicate(input=choices.encode())
    return stdout.decode()

def pw_dump():
    stdout, _ = sp.Popen(["pw-dump"], stdout=PIPE).communicate()
    return json.loads(stdout)

def pw_set_default(new_default_id):
    sp.Popen(["wpctl", "set-default", str(new_default_id)]).communicate()





