



from termcolor import colored
import phonenumbers,sys
from phonenumbers import geocoder,timezone,carrier

print(colored('''
	     WELCOME TO BANgLADESH
                ==============
	          BANgLADESH
                     V1.O
''', 'green'))
print("\n Example(+xx1234567890)")



def info():

	while True:
		b=input(colored("   Enter number: ",'blue'))
		inp=input(colored("Continue ? Y/n: ",'red'))
		if inp=="n":
			sys.exit("\n Shutting down... ")
		if inp=="y":
			print(colored("\n Target Number... \n",'blue'))
		else:
			print(colored(f"\n  Invalid '{inp}'  Try again ! \n", 'red'))
			break
		ex=phonenumbers.parse(b)
#	ex=phonenumbers.PhoneMetadata.load_all(inp)
#		exp=timezone.time_zones_for_number(ex, "GB")
		exp=geocoder.description_for_number(ex,"en")

		print(colored("Country: ",'green'),exp)

		#if inp=="y" or "Y":
		#	sys.exit("\n Shutting down... ")

		def isp():
			i=phonenumbers.parse(b)
			s=carrier.name_for_number(i, "en")
			print(colored("ISP: ",'green'),s)
		isp()
		def time():
			p=phonenumbers.parse(b)
			e=timezone.time_zones_for_number(p)
			print(colored("Timezone: ",'green'),e,"\n")
		time()

#		def infos():
#			p=phonenumbers.PhoneMetadata.load_all(inp)
#			print(p)
#		infos()

info()
