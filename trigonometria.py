#-*- coding: utf-8 -*-#
import math

#ângulo = float(input("Digite o angulo: "))
#seno = math.sin(math.radians(ângulo))
#print("O angulo de {} tem o seno de {:.2f}".format(ângulo, seno))
#cosseno = math.cos(math.radians(ângulo))
#print("O angulo de {} tem o cos de {:.2f}".format(ângulo, cosseno))
#tangente = math.tan(math.radians(ângulo))
#print("O angulo de {} tem a tangente de {:.2f}".format(ângulo, tangente))
print("Use as letras minusculas!")
print("Comandos: ")
print("seno")
print("cosseno")
print("tangente")
sct = str(input(""))
if sct == "seno":
	ang = int(input("Qual o angulo?"))
	anga = math.sin(math.radians(ang))
	oa = str(input("Você quer saber o valor do oposto ou da hipotenusa?"))
	angu = round(anga, 2)
	if oa == "oposto":
		hi = int(input("Qual o valor da hipotenusa?"))
		#seno 0580 = x
		#          = 90
		x = angu * hi
		print("O resultado é: {:.2f}".format(x))
		exit()
	elif oa == "hipotenusa":
		opost = int(input("Qual o valor do oposto?"))
		x = angu/opost
		print("O valor da hipotenusa é: {:.2f}".format(x))
		exit()
if sct == "cosseno":
	#co 45 - a
	#      - h
	ang = int(input("Qual o angulo?"))
	anga = math.cos(math.radians(ang))
	angu = round(anga, 2)
	ah = str(input("Você quer saber o valor da adjacente ou da hipotenusa?"))
	if ah == "adjacente":
		hi = int(input("Qual o valor da hipotenusa?"))
		#co 45 - x
		#      - hi
		x = angu * hi
		print("O valor é: {:.2f}".format(x))
	elif ah == "hipotenusa":
		ad = int(input("Qual o valor da adjacente?"))
		#co 40 - 
		x = angu / ad
		print("O resultado é: {:.2f}".format(x))
	if sct == "tangente":
		ang = int(input("Qual o angulo? "))
		anga = math.tan(math.radians(ang))
		angu = round(anga,2)
		oa = str(input("Você quer saber o valor do oposto ou adjacente? "))
	elif oa == "oposto":
		op = str(input("Qual o valor da adjacente?"))
		x = op * angu
	elif oa == "adjacente":
		ad = int(input("Qual o valor do oposto? "))
		x = ad / angu
		print("A resposta é : {:.2f}".format(x))


