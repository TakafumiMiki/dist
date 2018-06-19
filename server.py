import socketserver
import os
from pprint import pprint
from datetime import datetime

BUFFER = 4096
PORT = 9988
class ServerProg(socketserver.StreamRequestHandler):    
    def handle(self):
        print(str(self.client_address) + " から接続されました．")
        now1 = datetime.now()      
        print("接続された時間は " + str(now1.time()) + " です．")
        with open("log.txt", "w") as file:
                pprint("接続された時間は " + str(datetime.now().time()), stream=file)      
         
        while True:
            data = self.request.recv(BUFFER)          
            with open("log.txt", "a") as file:
                pprint(data.decode(), stream=file)      
                
            if len(data) <= 0:
                now2 = datetime.now()
                diff = (now2 - now1).total_seconds()                
                with open("log.txt", "a") as file:
                    pprint("接続時間は " + str(diff) + " 秒です．", stream=file)                    
                break
            self.request.send(data)       
        self.request.close()

server = socketserver.ThreadingTCPServer(("",PORT),ServerProg)
print("listening: " + str(server.socket.getsockname()))
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("Ctrl + C が入力されました")
