import telnetlib
import socks
import sys

#
#
#
#
#
#
#
#
#
#
#created by Art3m1sF0wl
#all rights reserved
#not for distribution (as it contains personal info kek)
#edit: removed personal info for the interwebs topkek
#usage
#linux: base64 -w 0 file.txt | python3 script_tor.py
#or :python3 script_tor.py <message>
#windows (untested): certutil -encode -f "file.txt" "file_wncoded.txt" and then idk 
#
#
#
#
#

# SOCKS proxy configuration
proxy_host = 'localhost'
proxy_port = 1234  # Change this to your proxy's port
target_host = 'asd.onion'  # Replace with the target hostname or IP
target_port = 5678  # Change this to the port you want to connect to
timeout = 10  # Adjust as needed

def quine():
    command = "QUINE\r\n"
    print(command)
    tn.write(command.encode())
    #print("ho mandato e ora sto aspettando la risposta\n")

    #response = tn.read_until(b'.', timeout).decode('utf-8')
    response = ""
    while True:
        line = tn.read_until(b'\n', timeout).decode('utf-8')
        response += line
        #print(line, end='')  # Print the line without an extra newline
        if line.strip() == ".":
            break
    #print("Response from server:")
    print(response)
def rand(n):
    command = "RAND "+str(n)+"\r\n"
    print(command)
    tn.write(command.encode())
    #print("ho mandato e ora sto aspettando la risposta\n")

    #response = tn.read_until(b'.', timeout).decode('utf-8')
    response = ""
    while True:
        line = tn.read_until(b'\n', timeout).decode('utf-8')
        response += line
        #print(line, end='')  # Print the line without an extra newline
        if line.strip() == ".":
            break
    #print("Response from server:")
    print(response)

def koan():
    command = "KOAN\r\n"
    print(command)
    tn.write(command.encode())
    #print("ho mandato e ora sto aspettando la risposta\n")

    #response = tn.read_until(b'.', timeout).decode('utf-8')
    response = ""
    while True:
        line = tn.read_until(b'\n', timeout).decode('utf-8')
        response += line
        #print(line, end='')  # Print the line without an extra newline
        if line.strip() == ".":
            break
    #print("Response from server:")
    print(response)

def goodbye():
    command = "GOODBYE\r\n"
    print(command)
    tn.write(command.encode())

    response = tn.read_until(b'\n', timeout).decode('utf-8')
    #print("Response from server:")
    print(response)
def next(string):
    command = "NEXT\r\n"
    print(command)
    tn.write(command.encode())

    response = tn.read_until(b'\n', timeout).decode('utf-8')
    #print("Response from server:")
    print(response)
    command = string+"\r\n"+"."+"\r\n"
    print(command)
    tn.write(command.encode())
    response = tn.read_until(b'\n', timeout).decode('utf-8')
    #print("Response from server:")
    print(response)

def base29(n):
    command = "BASE29 "+str(n)+"\r\n"
    print(command)
    tn.write(command.encode())

    response = tn.read_until(b'\n', timeout).decode('utf-8')
    #print("Response from server:")
    print(response)
def dh(n,k):
    command = "DH "+str(n)+"\r\n"
    print(command)
    tn.write(command.encode())

    response = tn.read_until(b'\n', timeout).decode('utf-8')
    #print("Response from server:")
    print(response)
    command = str(k)+"\r\n"
    print(command)
    tn.write(command.encode())
    response = tn.read_until(b'\n', timeout).decode('utf-8')
    #print("Response from server:")
    print(response)

if len(sys.argv) > 1:
   message=sys.argv[1]
else:
   message=sys.stdin.read()

try:
    # Create a SOCKS proxy connection
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, proxy_host, proxy_port)
    socket = socks.socksocket()
    
    # Enable verbose mode
    #socket.set_proxy(verbose=True)

    # Perform DNS lookup at the proxy's end
    socket.connect((target_host, target_port))

    # Create a Telnet connection
    tn = telnetlib.Telnet()
    tn.sock = socket

    #Read and print the response
    response = tn.read_until(b'\n', timeout).decode('utf-8')
    #print("Response from server:")
    print(response)

    #n=45
    #k=13
    #message="test message"
    #quine()
    #koan()
    #base29(n)
    #rand(n)
    #dh(n,k)
    next(message)

    #Close the Telnet connection
    #tn.close()
    goodbye()

except Exception as e:
    print(f"Error: {str(e)}")

finally:
    # Reset the socket settings
    socket.close()
