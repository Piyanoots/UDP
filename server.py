import socket

localIP     = "127.0.0.1"
localPort   = 20006
bufferSize  = 1024

msgFromServer       = "Hello UDP Client"



UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")
# Listen for incoming datagrams
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    temp="{}".format(message)
    print(clientMsg)
    print(clientIP)
    # Sending a reply to client
    

    num=int(temp)
    factorial = 1
    if num < 0:
       print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
       print("The factorial of 0 is 1")
    else:
       for i in range(1,num + 1):
           factorial = factorial*i
       print("The factorial of",num,"is",factorial)
       print type(clientMsg)

    bytesToSend = str.encode(str(factorial))
    UDPServerSocket.sendto(bytesToSend, address)
