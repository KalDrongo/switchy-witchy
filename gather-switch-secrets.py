import getpass
import pexpect
import json
import os

#Get manager's password
secret_phrase = str(getpass.getpass())

# Opening JSON switch_file
switch_file = open('switches.json',)
# returns JSON object as a dictionary
book_of_switches = json.load(switch_file)

for switch in book_of_switches:
  print("Trying to connect to: " + switch["NAME"])
  invoker = pexpect.spawn("scp -o KexAlgorithms=+diffie-hellman-group14-sha1 manager@" + switch["IP"] + ":/cfg/running-config .")
  invoker.expect("password:")
  invoker.sendline(secret_phrase)
  invoker.expect(pexpect.EOF)
  os.system("mv running-config configs/" + switch["NAME"] + "-config")

# Closing JSON switch_file
switch_file.close()
