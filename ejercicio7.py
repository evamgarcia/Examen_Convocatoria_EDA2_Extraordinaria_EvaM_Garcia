import random
import hashlib


lista_armadura = []
for i in range(2000):
    legion = random.choice(["FL", "TF", "TK", "CT", "FN", "FO"])
    code = f"{legion}-{random.randint(100,999)}"
    lista_armadura.append(code)


tabla1_hash = {}
tabla2_hash = {}


for armadura in lista_armadura:
  
    key = armadura[-3:]
    if key in tabla1_hash:
        tabla1_hash[key].append(armadura)
    else:
        tabla1_hash[key] = [armadura]
   
    key = armadura[:2]
    if key in tabla2_hash:
        tabla2_hash[key].append(armadura)
    else:
        tabla2_hash[key] = [armadura]


if "FN-2187" in tabla1_hash["187"] and "FN-2187" in tabla2_hash["FN"]:
    print("FN-2187 está cargado.")
    tabla1_hash["187"].remove("FN-2187")
    tabla2_hash["FN"].remove("FN-2187")
else:
    print("FN-2187 no está cargado.")

armadura718 = tabla1_hash["718"]
print("Armaduras terminados en 718:", armadura718)

armadura537 = tabla1_hash["537"]
print("Armaduras terminados en 537:", armadura537)


armaduraCT = tabla2_hash["CT"]
print("Armaduras de la legión CT para custodiar a Darth Vader en Hoth:", armaduraCT)


armaduraTF = tabla2_hash["TF"]
print("Armaduras de la legión TF para una misión de extrema nación en Endor:", armaduraTF)

