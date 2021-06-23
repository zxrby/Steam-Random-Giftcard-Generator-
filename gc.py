import random
import string
import pathlib
import requests, os, threading, sys, time, random, ctypes, webbrowser,re, hashlib, datetime, os.path, tkinter
import colorama
from colorama import Fore, init, Style, Back
from datetime import date
import getpass

os.system("title Module : [STEAM] GiftCard Generator - zxrby#1234")
def Spinner():
	l = ['+', '-', '+', '-']
	for i in l+l+l:
		sys.stdout.write('\r' + Style.BRIGHT + Fore.YELLOW + Back.BLACK +'[+] Loading Modules. '+i)
		sys.stdout.flush()
		time.sleep(0.2)

Spinner()

count = 0
current_path = os.path.dirname(os.path.realpath(__file__))

os.system("cls")
username = getpass.getuser()
print ("Welcome back ") 
print(username)
print(""+Fore.BLUE+"                                                                           ")
print("░██████╗████████╗███████╗░█████╗░███╗░░░███╗  ██╗░░██╗███████╗██╗░░░██╗    ")
print("██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗░████║  ██║░██╔╝██╔════╝╚██╗░██╔╝    ")
print("╚█████╗░░░░██║░░░█████╗░░███████║██╔████╔██║  █████═╝░█████╗░░░╚████╔╝░    ")
print("░╚═══██╗░░░██║░░░██╔══╝░░██╔══██║██║╚██╔╝██║  ██╔═██╗░██╔══╝░░░░╚██╔╝░░    ")
print("██████╔╝░░░██║░░░███████╗██║░░██║██║░╚═╝░██║  ██║░╚██╗███████╗░░░██║░░░    ")
print("╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝  ╚═╝░░╚═╝╚══════╝░░░╚═╝░░░    ")
print("                                                                           ")
print("░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░")
print("██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗")
print("██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝")
print("██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗")
print("╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║")
print("░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝")


print(Style.BRIGHT + Fore.BLUE + Back.BLACK +"Welcome to "+Fore.BLUE	+"Steam Generator by "+Fore.CYAN+"zxrby")
print(Style.BRIGHT + Fore.RED + Back.BLACK + "[1] "+Fore.BLUE+"Steam Keys")



opcion = int(input("Choice: "))

if opcion==1:
	os.system("cls")

	cantidad = input(Style.BRIGHT + Fore.BLUE + Back.BLACK +"\nHow many giftcards want to generate: ")
	while(int(count)<int(cantidad)):
	    Generated = random.choice(string.ascii_uppercase).upper()+''.join(random.choice(string.ascii_uppercase + string.digits).upper() for _ in range(4))+"-"+random.choice(string.ascii_uppercase).upper()+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))+"-"+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))+"-"+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
	    f= open(current_path+"/"+str("GiftCards")+str("")+".txt","a") 
	    f.write(Generated+"\n")
	    print(Style.BRIGHT + Fore.YELLOW + Fore.GREEN +"Steam Giftcard: "+Fore.RED + Generated)
	    count+=1
	input(Fore.GREEN+"\nCodes has been generated & saved !\nPress enter to exit.")
	pass

