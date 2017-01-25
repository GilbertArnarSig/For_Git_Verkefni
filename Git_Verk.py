# Gilbert Arnar Sigurðsson
# 25.01.17
# Git verkefni

# Dæmi 1
#Hér fyrir neðan er forrit sem tekkur tvær tölur frá notanda og legur þær saman og margfaldar þær

tala = int(input("Veldu tölu ")) # Byður notanda um tölu
tala2 = int(input("Veldu aðra tölu "))# Byður notanda um aðra tölu
samanlagt = tala + tala2 # legur saman tölu1 og tölu2
margfoldun = tala * tala2 # margfaldar tölu1 og tölu2 saman

print(tala,"+",tala2,"=",samanlagt) # byrtir reikning fyrir samanlagningu
print(tala,"*",tala2,"=",margfoldun)# byrtir margföldunar reikningiginn
print("") # noitað fyrir bil

# Dæmi 2
# Hér fyrir neðan er forrit sem byður notanda um fornanf og eftirnafn

nafn = input("Hvað er fornafn þitt? ") # Byður notanda um fornafn
eftirNafn = input("Hvað er eftirnafn þitt? ") # Byður notanda um eftirnafn

print("Halló",nafn,eftirNafn) # Byrtir "Halló Nafn notadna"
print("") # gert fyrir bil

#Dæmi 3
# Hér fyrir neðan er forrit sem byður notanda um texta og segir svo hvað eru margir hástafir/lástfir í honum

texti = input("Sláðu inn texta: ") # byður notanda um texta
teljariLaEftirHa = 0 # Breyta fyrir Teljara lástafi eftie hástafi
teljariHa = 0 # Breyta fyrir teljara hástafa
teljariLa = 0 # Breyta fyrir teljara lástafa

for x in range(len(texti)):
    if(texti[x].isalpha()) and (texti[x].isupper()):
        teljariHa += 1
        if(texti[x+1].islower()):
            teljariLaEftirHa += 1
    if(texti[x].isalpha()) and (texti[x].islower()):
        teljariLa += 1


print("Textin er: ",texti) # Byrtir textan fyrir notanda
print("Í þessum texta eru ",teljariHa," hástafir, ",teljariLa," lágstafir og ",teljariLaEftirHa, "lágstafir koma strax á eftir hástaf.")
# Hér fyrir ofan sýnir textin hvað voru margir hástafir/lástafir og hvað komu margir lástafir eftir hástaf