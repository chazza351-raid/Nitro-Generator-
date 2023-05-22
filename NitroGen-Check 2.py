import random, string
import webbrowser
import time
import requests
time.sleep(0.3)
print("Creator  -  spzzlol#4806 ")
time.sleep(0.3)
print("Twitter: https://twitter.com/eeee_5ytfgh  \n")
time.sleep(0.2)

nitroamount=input('How many codes do you want to generate? ')

f=open("Nitro Codes.txt","w", encoding='utf-8')

print("Generating Codes... (2% chance of working.)")  

for n in range(int(float(nitroamount))):
   y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
   f.write('https://discord.gift/')
   f.write(y)
   f.write("\n")

f.close()

#=============Checker=========================


with open("Nitro Codes.txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(" Valid Code| {} ".format(line.strip("\n")))
            break
        else:
        	print(" Invalid Code| {} ".format(line.strip("\n")))