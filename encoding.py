i=0
new=[]

#Salut les amis !!
with open("catalogue.sql",encoding = "utf-8") as f:
	f=f.readlines()
	for line in f:
		line=line.replace("Ã©","é")
		line=line.replace("ÃƒÂ©","é")
		line=line.replace("Ã¨","è")
		line=line.replace("\\","")
		line=line.replace("Ã§","ç")
		line=line.replace("Ãª","è")
		line=line.replace("â€“","-")
		line=line.replace("Å“","œ")
		line=line.replace("Â°","°")
		line=line.replace("Ãˆ","È") 
		line=line.replace("Ã‰","É")
		line=line.replace("Ã¼","ü")
		line=line.replace("ÃŒ","Ì")
		line=line.replace("ÃŽ","Î")
		line=line.replace("Ã¶","ö")
		line=line.replace("ÃŸ","ß")
		line=line.replace("Ã¡","á")
		line=line.replace("Ã¢","â")
		line=line.replace("Ã¤","ä")
		line=line.replace("Ãª","ê")
		line=line.replace("Ã«","ë")
		line=line.replace("Ã®","î")
		line=line.replace("Ã¯","ï")
		line=line.replace("Ã´","ô")
		line=line.replace("Ã¸","ø")
		line=line.replace("Ã¹","ù")
		line=line.replace("Ã»","û")
		line=line.replace("Ã¼","ü")
		line=line.replace("Ã","à")
		line=line.replace("Ã","Í")
		line=line.replace("Ã","Ð")
		line=line.replace("Ã","Á")
		line=line.replace("Ã","Ï")
		line=line.replace("Ã","Ý")
		new.append(line)
		# i+=1
		# if i==6895:
			# print(line)

with open("catalogue2.sql","w",encoding = "utf-8") as g:
	for i in new:
		g.write(i)



