import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 8080

udpsock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

udpsock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = udpsock.recvfrom(1024) # buffer size is 1024 bytes

    udpsock.sendto(data, addr)

    print ("received message:", data.decode("utf-8")) #cn:gb2312

udpsock.close()
