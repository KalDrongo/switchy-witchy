import getpass
import pexpect

secret_phrase = str(getpass.getpass())

invoker = pexpect.spawn("scp -o KexAlgorithms=+diffie-hellman-group14-sha1 manager@128.111.111.20:/cfg/running-config .")
invoker.expect("password:")
invoker.sendline(secret_phrase)
invoker.expect(pexpect.EOF)
