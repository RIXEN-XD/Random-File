import os,platform
os.system('git pull')
#exit('\n Wait Working On Tool..!')
RIXEN=platform.architecture()[0]
if RIXEN=="32bit":__import__("Rixen")
elif RIXEN=="64bit":__import__("Rixen")
