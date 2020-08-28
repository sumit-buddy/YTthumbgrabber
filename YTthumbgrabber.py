import requests
import wget
import pyfiglet

class fontcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#banner art
banner = pyfiglet.figlet_format("YOUTUBE \nTHUMB \nGRABBER")
print(banner)

print(f"{fontcolors.WARNING} #####> AUTHOR : Sumit <##### {fontcolors.ENDC}")

#instructions
print(f"\n{fontcolors.OKGREEN}*** USAGE INSTRUCTIONS ***{fontcolors.ENDC}")

print(f"{fontcolors.FAIL}[*]{fontcolors.ENDC}",f"{fontcolors.BOLD}Paste video link & hit enter{fontcolors.ENDC}")

print(f"{fontcolors.FAIL}[*]{fontcolors.ENDC}",f"{fontcolors.BOLD}Select desired resolution & hit enter.{fontcolors.ENDC}")


url=input("\n##> Paste YouTube video link here : ")

print(f"\n{fontcolors.OKGREEN}*** SELECT RESOLUTION ***{fontcolors.ENDC}")

print(f"{fontcolors.FAIL}[1]{fontcolors.ENDC}",f"{fontcolors.BOLD}HD-default 1080p(1280*720px)-maximum resolution{fontcolors.ENDC}")

print(f"{fontcolors.FAIL}[2]{fontcolors.ENDC}",f"{fontcolors.BOLD}SD-default 720p(640*480px){fontcolors.ENDC}")

print(f"{fontcolors.FAIL}[3]{fontcolors.ENDC}",f"{fontcolors.BOLD}HQ-default 480p(480*360px){fontcolors.ENDC}")

print(f"{fontcolors.FAIL}[4]{fontcolors.ENDC}",f"{fontcolors.BOLD}MQ-default 360p(320*180px){fontcolors.ENDC}")

print(f"\n{fontcolors.WARNING}NOTE:{fontcolors.ENDC}",f"{fontcolors.BOLD}You may get error if the channel owner has uploaded a thumbnail lower than the resolution you selected.In such case please try downloading resolution lower than that.{fontcolors.WARNING}")

#valid_input=[1,2,3,4]

usr=input("\n##>")
					
id=url.split('/')[-1]

yt_url1='https://img.youtube.com/vi/'+id+'/maxresdefault.jpg'

yt_url2='https://img.youtube.com/vi/'+id+'/sddefault.jpg'

yt_url3='https://img.youtube.com/vi/'+id+'/hqdefault.jpg'

yt_url4='https://img.youtube.com/vi/'+id+'/mqdefault.jpg'


def msg():
	print(f"\n{fontcolors.OKGREEN} Downloaded Successfully...{fontcolors.ENDC}","saved as",local_image_filename)

if usr == '1':
	local_image_filename=wget.download(yt_url1)
	msg()


elif usr == '2':
	local_image_filename=wget.download(yt_url2)
	msg()


elif usr == '3':
	local_image_filename=wget.download(yt_url3)
	msg()

elif usr == '4':
	local_image_filename=wget.download(yt_url4)
	msg()
	
else:
	print("Please select a valid input ! ")
	
	