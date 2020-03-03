from socket import *
import base64
msg = "\r\n I love Computer Networks"
endmsg = "\r\n.\r\n"
mailserver = ("mail.smtp2go.com", 2525)
# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
recv = clientSocket.recv(1024)
print(recv.decode())
if recv[:3] != '220':
 print('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'EHLO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
 print('250 reply not received from server.')
#Information: username and password
username = "manavahlawat95@gmail.com"
password = "rB9sf4brIUbI"
base64_str = ("\x00"+username+"\x00"+password).encode()
base64_str = base64.b64encode(base64_str)
auth = "AUTH PLAIN ".encode()+base64_str+"\r\n".encode()
clientSocket.send(auth)
recvauth = clientSocket.recv(1024).decode()
print(recvauth)
if recvauth[:3] != '250':
 print('250 reply not received from server.')
# Send MAIL FROM command and print server response.
mailFrom = "MAIL FROM: <manavahlawat95@gmail.com> \r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
 print('250 reply not received from server.')
# Send RCPT TO command and print server response.
rcptTo = "RCPT TO: <ma5169@nyu.edu> \r\n"
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
 print('250 reply not received from server.')
# Send DATA command and print server response.
data = "DATA\r\n"
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '250':
 print('250 reply not received from server.')
# Send message data.
subject = "Subject: SMTP Test \r\n\r\n"
clientSocket.send(subject.encode())
message = input("Enter the message: \r\n")
clientSocket.send(message.encode())
clientSocket.send(endmsg.encode())
receive_message = clientSocket.recv(1024).decode()
print(receive_message)
if receive_message[:3] != '250':
 print('250 reply not received from server.')
# Send QUIT command and get server response.
clientSocket.send("QUIT\r\n".encode())
message=clientSocket.recv(1024).decode()
print (message)
clientSocket.close()