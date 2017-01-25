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