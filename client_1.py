import socket

host = "127.0.0.1"
port = 9988
         
my_socket = socket.socket()
try:
    my_socket.connect((host,port))
except ConnectionRefusedError:
    print("サーバーが見つかりませんでした。")
    exit()

message = input(" 数値を入力 -> ")
result = 0

while message != "q":#qを押すとストップ
    
    my_socket.send(message.encode())
    data = my_socket.recv(1024).decode()
                 
    print ("足し算の結果は " + str(data))
    
    message = input(" 数値を入力 -> ")
    
my_socket.close()
