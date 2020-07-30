import socket
import time
import select

all_connections = []
all_address = []
Questions=["Q"+str(i) for i in range(1, 52)]
Answers=[i for i in range (2, 53)]
Marks=[0,0,0]
response=[]


# Create a Socket ( for connecting two computers)
def create_socket():
    try:
        global host
        global port
        global s
        host ="" 
        port = input("Enter Port: ") 
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the Port: " + str(port))

        s.bind((host, int(port)))
        s.listen(3)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying")


#Connection of multiple players
#Closing all previous connections
#Basic instructions for players.
def accepting_connections():
    for c in all_connections:
        c.close()

    del all_connections[:]
    del all_address[:]
    j = 0
    while True:
            conn, address = s.accept()
            s.setblocking(1)  #Avoiding timeout
            j = j+1
            all_connections.append(conn)
            all_address.append(address)
            if j < 3:
                print("Connection has been established: Client " + str(j)+" " + address[0])
                conn.send(str.encode("Total questions are 50. First one to reach 5 points wins. First enter yes for buzzer and then answer the question.\nIF YOU DON'T KNOW THE QUESTION JUST DON'T PRESS BUZZER"))
                time.sleep(0.25)
                conn.send(str.encode("You are Player : "+ str(j)))
                time.sleep(0.25)
                conn.send(str.encode("Welcome to the game"))

            else:
                print("Connection has been established :Client " + str(j)+" " + address[0])
                conn.send(str.encode("Total questions are 50. First one to reach 5 points wins. First enter yes for buzzer and then answer the question.\nIF YOU DON'T KNOW THE QUESTION JUST DON'T PRESS BUZZER"))
                print("Maximum Clients Connected")
                time.sleep(0.25)
                conn.send(str.encode("You are Player : "+ str(j)))
                time.sleep(0.25)
                conn.send(str.encode("Welcome to the game"))
                
                
                game_function()
                break
    #return

# Function for handling Marks and questions                
def game_function():
    
    for i in range(len(Questions)):
        for conn in all_connections:
            time.sleep(0.1)
            conn.send(str.encode(Questions[i]+". Do You Know this question: 1+"+str(i+1)))
        response1 = select.select(all_connections,[],[],10)#str(conn.recv(1024),"utf-8")
        if(len(response1[0])>0):
            
            conn_name = response1[0][0];
            b = conn_name.recv(1024)
            b = b.decode("utf-8")
            response1=()
            for conn in all_connections:
                if conn!=conn_name:
                    conn.send(str.encode("Sorry, Player "+str(all_connections.index(conn_name)+1)+ " has pressed the buzzer.\n"))
            for p in range(len(all_connections)):
                    if all_connections[p]==conn_name:
                        t=p;

            b = b.lower()
            if b=='yes' or b=='y':
                        conn_name.send(str.encode("Answer the Question"))
                        answer=str(conn_name.recv(1024),"utf-8")
                        if answer==str(Answers[i]):
                            
                            Marks[t]=Marks[t]+1
                            conn_name.send(str.encode("Correct Answer, You get 1 Point\n"))
                            if Marks[t]>=5:
                                break
                        else:
                            conn_name.send(str.encode("Wrong Answer, You lose 0.5 Points\n"))
                            Marks[t] = Marks[t] - 0.5
                            time.sleep(0.25)
            elif b==str(Answers[i]):
                conn_name.send(str.encode("You didn't press the buzzer before answering.You lose 1 point\n"))
                Marks[t]=Marks[t]-1
                time.sleep(0.25)


        else:
            for c in all_connections:
                c.send(str.encode("\nNobody pressed the buzzer.Moving on to the next question\n"))
    for c in all_connections:
    	c.send(str.encode("bye"))
    	time.sleep(0.25)

#Driver function
def main():
    create_socket()
    bind_socket()
    accepting_connections()
 #   game_function()
    
    y = min(Marks)
    d = 0
    for i in range(len(all_connections)):
        if Marks[i]>y:
            d=i
            y=Marks[i]
    if(y>=5):
	    for c in all_connections:
    	   	if all_connections.index(c)!=d:
    	   	    c.send(str.encode("The winner is Player: " + str(d+1)+" with "+str(y)+" Points" ))
    	   	else:
    	   	    c.send(str.encode("Congratulations! You are the winner with " + str(y)+" Points" ))
    else:
    	for c in all_connections:
    		c.send(str.encode("Reached the end of questions. Game over."))


main()
for c in all_connections:
	c.close()
