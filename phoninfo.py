import phonenumbers,sys
from phonenumbers import geocoder,timezone

print('''
             WELCOME TO BANgLADESH
                ==============
                  BANgLADESH
                     V1.O
''')
print("\n Example(+xx1234567890)")



def info():

        while True:
                b=input("   Enter number: ")
                inp=input("Continue ? Y/n: ")
                if inp=="n":
                        sys.exit("\n Shutting down... ")
                if inp=="y":
                        print("\n Target Number... \n")
                else:
                        print(f"\n  Invalid '{inp}'  Try again ! \n")
                        break
                ex=phonenumbers.parse(b)
#       ex=phonenumbers.PhoneMetadata.load_all(inp)
#               exp=timezone.time_zones_for_number(ex, "GB")
                exp=geocoder.description_for_number(ex,"en")

                print("Country=",exp)

                #if inp=="y" or "Y":
                #       sys.exit("\n Shutting down... ")

                def time():
                        p=phonenumbers.parse(b)
                        e=timezone.time_zones_for_number(p)
                        print("Timezone=",e,"\n")
                time()

#               def infos():
#                       p=phonenumbers.PhoneMetadata.load_all(inp)
#                       print(p)
#               infos()

info()
