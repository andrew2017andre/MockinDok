import phonenumbers,sys
from phonenumbers import geocoder,timezone

print('''
             WELCOME TO BANgLADESH
                ==============
                  BANgLADESH
                     V1.O
''')
print("\n  কপি করিসনা আবার(+xx1234567890)")



def info():

         while True:
                b=input("    টুনির মার নম্বার: ")
                inp=input(" ভরতে চাস ? Y/n: ")
                if inp=="n":
                        sys.exit("\n  বিদাই পিতিবি... ")
                if inp=="y":
                        print("\n ভরে দেওয়া নম্বার... \n")
                else:
                        print(f"\n   কানাষুদা '{inp}' দেখে লেখ \n")
                        break
                ex=phonenumbers.parse(b)
#       ex=phonenumbers.PhoneMetadata.load_all(inp)
#               exp=timezone.time_zones_for_number(ex, "GB")
                exp=geocoder.description_for_number(ex,"en")

                print("দেশ =",exp)

                

                def time():
                        p=phonenumbers.parse(b)
                        e=timezone.time_zones_for_number(p)
                        print("সময়যাত্রা=",e)
                time()

#               def infos():
#                       p=phonenumbers.PhoneMetadata.load_all(inp)
#                       print(p)
#               infos()

info()
