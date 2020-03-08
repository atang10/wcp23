import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("128.228.79.205",80))
s.listen(5)

while True:
	clt, adr = s.accept()
	print(f"Connection to {adr} established")
	clt.send(bytes("This is the freakin message","utf-8"))
