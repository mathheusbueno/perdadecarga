# Moody 
def eqMoody(rugosidade, diametro, reynolds):
    fatordeatrito = 0.0055 * (1 + math.pow((20000 * rugosidade / diametro) + (1000000 / reynolds), 1 / 3))
    return fatordeatrito
    
# Wood
def eqWood(rugosidade, diametro, reynolds):
	B = 1.62*(math.pow((rugosidade/diametro),0.134))
	fatordeatrito = ((0.094*math.pow((rugosidade/diametro),0.225)) + (0.53*(rugosidade/diametro)) + ((88*math.pow((rugosidade/diametro),0.4))*(math.pow(reynolds,-B))))
	return fatordeatrito
	
# Eck
def eqEck(rugosidade, diametro, reynolds):
	fatordeatrito = 1/(math.pow((-2*math.log10((rugosidade/(3.715*diametro))+(15/reynolds))),2))
	return fatordeatrito
	
# Swamee and Jain
def eqJain(rugosidade, diametro, reynolds):
	fatordeatrito = 1/(math.pow(-2*math.log10((math.pow((rugosidade/(3.7*diametro)),1.11))+(5.74/(math.pow(reynolds,0.9)))),2))
	return fatordeatrito
	
# Churchill
def eqChurchill(rugosidade, diametro, reynolds):
	A = (math.pow((2.457*math.log((1)/((math.pow((7/reynolds),0.9))+((0.27*rugosidade)/(diametro))))),16))
	B = (math.pow((37530/reynolds),16))
	fatordeatrito = 8*(math.pow(((math.pow((8/reynolds),12))+((1)/(math.pow((A+B),3/2)))),1/12))
	return fatordeatrito
	
# Chen
def eqChen(rugosidade, diametro, reynolds):
	fatordeatrito = (1)/(math.pow((-2*math.log10((rugosidade/(3.7065*diametro)-((5.0452/reynolds)*math.log10((1/2.8257)*(math.pow((rugosidade/diametro),1.1098))+(5.8506/(math.pow(reynolds,0.8981)))))))),2))
	return fatordeatrito

# Shacham
def eqShacham(rugosidade, diametro, reynolds):
	fatordeatrito = 1/(math.pow((-2)*math.log10((rugosidade/(3.7*diametro)) - ((5.02/reynolds)*(math.log10((rugosidade/(3.7*diametro)) + (14.5/reynolds))))),2))
	return fatordeatrito

# Round
def eqRound(rugosidade, diametro, reynolds):
	fatordeatrito = 1/(math.pow(1.8*math.log10(reynolds/((0.135*reynolds*(rugosidade/diametro)) + 6.5)),2))
	return fatordeatrito

# Zigrang and Sylverter
def eqSylverter(rugosidade, diametro, reynolds):
	fatordeatrito = (1)/(math.pow(-2*(math.log10((rugosidade/(3.7*diametro)) - ((5.02/reynolds)*math.log10((rugosidade/(3.7*diametro)) + (13/reynolds))))),2))
	return fatordeatrito

# Romeo, Royo and Monzon
def eqRomeo(rugosidade, diametro, reynolds):
	fatordeatrito = 1/(math.pow(-2*(math.log10(((rugosidade/diametro)/3.7065) - ((5.0272/reynolds)*math.log10(((rugosidade/diametro)/3.827))) - ((4.567/reynolds)*math.log10((math.pow(((rugosidade/diametro)/7.7918),0.9924)) + (math.pow(5.3326/(208.815 + reynolds),0.9345)))))),2))
	return fatordeatrito

# Haaland
def eqHaaland(rugosidade, diametro, reynolds):
	fatordeatrito = (1)/(math.pow((-1.8*math.log10((math.pow((rugosidade/(3.7*diametro)),1.11))+(6.9/reynolds))),2))
	return fatordeatrito

# Manadilli
def eqManadilli(rugosidade, diametro, reynolds):
	fatordeatrito = 1/(math.pow((-2*math.log10((rugosidade/(3.70*diametro)) + (95/(math.pow(reynolds,0.983))) - (96.82/reynolds))),2))
	return fatordeatrito

# Sonnad and Goudar
def eqSonnad(rugosidade, diametro, reynolds):
	S = 0.124*reynolds*(rugosidade/diametro)+math.log(0.4587*reynolds)
	fatordeatrito = 1/(math.pow((0.8686*math.log((0.4587*reynolds)/(math.pow(S,(S/(S+1)))))),2))
	return fatordeatrito

# Vantankhah and Kouchakzadeh
def eqVantankhah1(rugosidade, diametro, reynolds):
	S = 0.124*reynolds*(rugosidade/diametro)+math.log(0.4587*reynolds)
	fatordeatrito = (1)/(math.pow((0.8686*math.log((0.4587*reynolds)/(math.pow((S-0.31),((S)/(S+0.9633)))))),2))
	return fatordeatrito

# Buzzelli
def eqBuzzelli(rugosidade, diametro, reynolds):
	A = (((0.774*math.log(reynolds)) - 1.41)/(1 + (1.32*math.sqrt(rugosidade/diametro))))
	B = (((rugosidade*reynolds)/(3.7*diametro)) + (2.51*A))
	fatordeatrito = 1/(math.pow((A - ((A + 2*math.log10(B/reynolds))/(1 + (2.18/B)))),2))
	return fatordeatrito

# Fang , Xu and Zhou
def eqFang(rugosidade, diametro, reynolds):
	fatordeatrito = (1.613*(math.pow((math.log((0.234*(math.pow((rugosidade/diametro),1.1007)))-((60.525)/(math.pow((reynolds),1.1105)))+((56.291)/(math.pow((reynolds),1.0712))))),-2)))
	return fatordeatrito

# Offor and Alabi
def eqOffor(rugosidade, diametro, reynolds):
	fatordeatrito = 1/(math.pow((-2*math.log10((rugosidade/(3.71*diametro)) - ((1.975/reynolds)*(math.log((math.pow((rugosidade/(3.93*diametro)),1.092)) + (7.627/(reynolds + 395.9))))))),2))
	return fatordeatrito

# Ghanbari, Farshad and Rieke
def eqGhanbari(rugosidade, diametro, reynolds):
	fatordeatrito = (math.pow((-1.52*math.log10((math.pow(((rugosidade/diametro)/(7.21)),1.042))+(math.pow((2.731)/(reynolds),0.9152)))),-2.169))
	return fatordeatrito

# Vantankhah2
def eqVantankhah2(rugosidade, diametro, reynolds):
	G = (0.124*reynolds*(rugosidade/diametro)) + math.log(0.4599*reynolds)
	fatordeatrito = 1/(math.pow((0.8686*math.log((0.4599*reynolds)/(math.pow((G - 0.2753),(G/(G+0.9741)))))),2))
	return fatordeatrito

# Vantankhah3
def eqVantankhah3(rugosidade, diametro, reynolds):
	DEL = (((6.0173)/(reynolds*math.pow((0.07*(rugosidade/diametro)+math.pow((reynolds),-0.885)),0.109)))+((rugosidade/diametro)/3.71))
	fatordeatrito = (math.pow((((2.51/reynolds)+1.1513*DEL)/((DEL)-((rugosidade/diametro)/3.71)-(2.3026*DEL*math.log10(DEL)))),2))
	return fatordeatrito

# Samadianfard
def eqSamadianfard(rugosidade, diametro, reynolds):
	fatordeatrito= ((((math.pow(reynolds,(rugosidade/diametro)))-(0.6315093))/((math.pow(reynolds,1/3))+(reynolds*(rugosidade/diametro))))+(0.0275308*(math.pow(((6.929841/reynolds)+(rugosidade/diametro)),1/9)))+(((math.pow(10,(rugosidade/diametro)))/((rugosidade/diametro)+(4.781616)))*((math.sqrt((rugosidade/diametro)))+(9.99701/reynolds))))
	return fatordeatrito

# Samadianfard,Taghi, Kisi and Kazemi
def eqKisi(rugosidade, diametro, reynolds):
	fatordeatrito = (152.137*math.pow((rugosidade/diametro),3))+(1223*math.pow((rugosidade/diametro),4))+((9.96213+reynolds)/(math.pow(reynolds,2)))+(math.atan(-(8.79056*(math.pow((rugosidade/diametro),2))*(reynolds-9.72464))/(9.72464+reynolds)))+((0.0834528*(math.pow(((rugosidade/diametro)*(math.sqrt(reynolds))),2/3)))/(math.pow(math.log(math.pow((rugosidade/diametro),3)),2)))+((math.pow(math.atan(8.3663*(rugosidade/diametro)*math.sqrt(reynolds)),2))/(math.pow(math.log(math.pow((rugosidade/diametro),3)),2)))+((math.pow(math.atan((math.sqrt(reynolds)*math.sin((rugosidade/diametro)))),2))/(math.pow(math.log(math.pow((rugosidade/diametro),3)),2)))+((math.log((reynolds)/((rugosidade/diametro))))/(reynolds-9.96213))+(math.atan((rugosidade/diametro)*(math.sin((math.atan((0.447021)/((rugosidade/diametro))))/((rugosidade/diametro)*reynolds)))))+(math.sin((rugosidade/diametro)*(math.atan((math.atan((2.70969)/((rugosidade/diametro))))/((rugosidade/diametro)*reynolds)))))-(2*math.sin(((rugosidade/diametro))-((math.atan(math.atan((rugosidade/diametro))))/(math.atan(math.atan(reynolds))))))+(math.pow((math.sin((math.atan((0.488525)/((rugosidade/diametro))))/(9.98978+math.log(reynolds)))),2))
	return fatordeatrito
    
