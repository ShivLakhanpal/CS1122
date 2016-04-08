#Homework 7
#svl238
#Shiv Lakhanpal


import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("gnarlygno.me",8888))
s.settimeout(200)
stri = s.recv(2048)
print(stri)
while True:
	gg = s.recv(1024)
	while gg == "\n":
		gg = s.recv(1024)
		
	if(gg.startswith("Convert")):
		num = gg.find("(",0,len(gg))
		sec = gg.find(")")
		conFactor = gg.rfind("(",0,len(gg))
		conFactor2 =gg.rfind(")",0,len(gg))

		toChange = int(gg[(num+1):sec])
		factor = int(gg[(conFactor+1):conFactor2])

		print(gg)

		if factor == 10:
			s.send(str(toChange)+"\n")
			print("After the conversion", toChange," is ",toChange)



		if factor == 16:
			s.send(hex(toChange)+"\n")
			print("After the conversion ", toChange," is ",hex(toChange))



		if factor == 2:
			s.send(bin(toChange)+"\n")
			print("After the conversion ", toChange," is ",bin(toChange))
	if gg.startswith("Phase"):
		break

print (gg)
while not gg.startswith("How"):
	gg = s.recv(1024)


print(gg) 
print("Why not salsaman")
s.send("Salsaman\n")
print("Salsaman")
gg = s.recv(1024) 
print(gg)
gg = s.recv(1024)
print(gg)

print(gg)
