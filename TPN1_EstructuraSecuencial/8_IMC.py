#Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo:
#𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 / (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)**2

peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura en metros: "))

IMC = peso / (altura**2)

print(f"Su IMC es de: {IMC}" )