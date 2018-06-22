import socketserver
from pprint import pprint
from datetime import datetime

BUFFER = 4096
PORT = 9988

class ServerProg(socketserver.StreamRequestHandler):
    res = 0    
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
            
            try:
                self.res += float(data)    
            except ValueError:
                pass

            if len(data) == 0:
                now2 = datetime.now()
                diff = round((now2 - now1).total_seconds(),2)
                print("接続時間は " + str(diff) + " 秒です")             
                with open("log.txt", "a") as file:
                    pprint("接続時間は " + str(diff) + " 秒です．", stream=file)                    
                break
                
            client_sum = str(self.res).encode()
            self.request.send(client_sum)#結果の渡し方

        self.request.close()

        with open("log.txt", "a") as file:
            pprint("計算の合計は " + str(self.res), stream=file) 

server = socketserver.ThreadingTCPServer(("",PORT),ServerProg)
print("listening: " + str(server.socket.getsockname()))
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("Ctrl + C が入力されました")
