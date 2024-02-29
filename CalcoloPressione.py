#python 3.7.1
# Calcolo pressione osmotica
# Costante universale dei gas 0.0821 L atm / mol K
import os
import time
import sys

os.system('clear')
print("\033[1;32;40mProgramma per il calcolo della presione osmotica secondo la formula \nP\033[1;31;40m(atm)\033[1;32;40m = M\033[1;31;40m(mol/L)\033[1;32;40m * R\033[1;31;40m(costante universale gas 0.082)\033[1;32;40m * T\033[1;31;40m(Kelvin)\033[1;32;40m * i\033[1;31;40m(coefficiente di van't Hoff) \033[1;32;40m")
print("\n\t\t \033[1;31;47mP = M * R * T * i\33[1;0m\n")
print("\n\t\t\033[1;31;47mM = P / (R * T * i)\33[1;0m\n")
ciclo=3
R=0.082
kKC=273.15 # 0°C in gradi Kelvin
# gradi Kelvin 0° K = -273.15° C || 0° C = 273.15° K

print("Mi riscaldo")
for i in range(ciclo):
    time.sleep(0.5)
    sys.stdout.write(".")
    sys.stdout.flush()

#print("\033[5mBlinking \033[0m Not Blinking")

loopS=0
while (loopS!=1):	

	rispS=0
	while (rispS!=1):
		print("\n\nCosa vuoi calcolare?")
		print("[1] Presione osmotica")
		print("[2] Molarità")
		sceltaS=str(input("\nScelta: [1]/[2]\n"))
		if sceltaS.isdigit():
			scelta=int(sceltaS)

		else:
			print("Scelta sbagliata!")
			scelta=0

		if scelta == 1:
			risp=0
			print()
			while (risp != 1):
				AnsT=str(input("\nVuoi usare i gradi centigradi?(\033[1;37;46mS,s,Sì,sì,Y,y/N,n\033[1;0m): \n"))

				if AnsT in ['S', 's', 'Sì', 'sì', 'y', 'Y', 'yes', 'Yes', 'YES']:
					T=float(input("Inserisci la temperatura in gradi centigradi (T): "))
					TK=T+kKC
					risp=1
				elif AnsT in ['N','n']:
					TK=float(input("Inserisci la temperatura in gradi Kelvin (T): "))
					risp=1
				else:
					print("Risposta non riconosciuta!")
					time.sleep(0.5)
					os.system('clear')
					print("\033[1;32;40mProgramma per il calcolo della presione osmotica secondo la formula \nP\033[1;31;40m(atm)\033[1;32;40m = M\033[1;31;40m(mol/L)\033[1;32;40m * R\033[1;31;40m(costante universale gas 0.082)\033[1;32;40m * T\033[1;31;40m(Kelvin)\033[1;32;40m * i\033[1;31;40m(coefficiente di van't Hoff) \033[1;32;40m")
					print("\n\t\t\033[1;31;47mP = M * R * T * i\33[1;0m\n")
					risp=0
				time.sleep(0.5)
			#T=283.16
			# indice di van't Hoff
			i=int(input("Inserisci il coefficiente di van't Hoff (i): "))
			#i=1
			# Molarità soluzione
			M=float(input("Inserisci la molarità della soluzione (M): "))
			#M=1
			# Pressione osmotica
			P=M*R*TK*i
			#PS=str(P)
			PHpas=float(P*1013.25)
			print ("La pressione osmotica è di \033[1;31;40m%.2f\033[1;0m atmosfere o \033[1;31;40m%.2f\033[1;0m hPa." %(P, PHpas))
			rispS=1

		elif scelta==2:
			risp=0
			print()
			while (risp != 1):
				AnsT=str(input("\nVuoi usare i gradi centigradi?(\033[1;37;46mS,s,Sì,sì,Y,y/N,n\033[1;0m): \n"))

				if AnsT in ['S', 's', 'Sì', 'sì', 'y', 'Y', 'yes', 'Yes', 'YES']:
					T=float(input("Inserisci la temperatura in gradi centigradi (T): "))
					TK=T+kKC
					risp=1
				elif AnsT in ['N','n']:
					TK=float(input("Inserisci la temperatura in gradi Kelvin (T): "))
					risp=1
				else:
					print("Risposta non riconosciuta!")
					time.sleep(0.5)
					os.system('clear')
					print("\033[1;32;40mProgramma per il calcolo della presione osmotica secondo la formula \nP\033[1;31;40m(atm)\033[1;32;40m = M\033[1;31;40m(mol/L)\033[1;32;40m * R\033[1;31;40m(costante universale gas 0.082)\033[1;32;40m * T\033[1;31;40m(Kelvin)\033[1;32;40m * i\033[1;31;40m(coefficiente di van't Hoff) \033[1;32;40m")
					print("\n\t\t\033[1;31;47mP = M * R * T * i\33[1;0m\n")
					risp=0
				time.sleep(0.5)
			# indice di van't Hoff
			i=int(input("Inserisci il coefficiente di van't Hoff (i): "))
			#i=1
			# indice di van't Hoff
			P=float(input("Inserisci la pressione osmotica in atmosfere (P): "))
			#i=1

			M=P/(R*TK*i)
			print("La Molarità è di \033[1;31;40m%.2f\033[1;0m moli/L." %M)
			rispS=1
		else:
			os.system('clear')
			rispS=0

	loopSX=str(input("Vuoi fare altri calcoli?(\033[1;37;46mS,s,Sì,sì,Y,y/N,n\033[1;0m): \n"))
	if loopSX in ['S', 's', 'Sì', 'sì', 'y', 'Y', 'yes', 'Yes', 'YES']:
		loopS=0
		rispS=0
		os.system("clear")
	else:
		loopS=1

print("\nCiao!")





