import socket

host = "127.0.0.1"
port = 9988
         
my_socket = socket.socket()
my_socket.connect((host,port))
         
message = input(" 数値を入力 -> ")
result = 0         

while message != "q":#qを押すとストップ
    
    my_socket.send(message.encode())
    data = my_socket.recv(1024).decode()
                 
    #print (str(data) + " がサーバーから送り返されました．")
    
    try:
        result += float(data)
    except ValueError:
        pass
    finally:
        message = input(" 数値を入力 -> ")
    

else:
    print("合計は " + str(result)) 
  
my_socket.close()
