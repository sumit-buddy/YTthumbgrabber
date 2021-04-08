import os, sys, json
import requests
import wget
from cfonts import render
from urllib.error import HTTPError
from termcolor import colored

class fontcolor():
	def green(string):
		return colored(string, "green", attrs=['bold'])
	def white(string):
		return colored(string, "white", attrs=['bold'])
	def cyan(string):
		return colored(string, "cyan", attrs=['bold'])
	def red(string):
		return colored(string, "red", attrs=['bold'])

class smb:
	WARN = fontcolor.red(" [-] ")
	DONE = fontcolor.green(" [+] ")
	INPUT = fontcolor.cyan(" [»] ")
	ONE = fontcolor.cyan(" [1] ")
	TWO = fontcolor.cyan(" [2] ")
	THREE = fontcolor.cyan(" [3] ")
	FOUR = fontcolor.cyan(" [4] ")
	FIVE = fontcolor.cyan(" [5] ")

#banner art
banner = render("youtube thumbnail downloader", font='chrome',colors=["green","green","green"],align='center')
print(banner)

#instructions menu
print(smb.DONE + fontcolor.green("USAGE INSTRUCTIONS :"))
print(smb.ONE + fontcolor.white("Paste YouTube Video Link"))
print(smb.TWO + fontcolor.white("Select Desired Resolution"))

#getting youtube link
yt_link = None
while not yt_link:
	yt_link = input("\n" + smb.INPUT + fontcolor.white("Paste YouTube Video Link : "))

#validating link using oembed API
pre_link = "https://www.youtube.com/oembed?format=json&url="
url = pre_link + yt_link
id = yt_link.split('/')[-1]

def check_url():
	request = requests.get(url)
	return request.status_code == 200

while check_url() == False:
	print("\n" + smb.WARN + fontcolor.red("Invalid Link ! It Should Be Like – https://youtu.be/video_id !"))
	quit()

# getting video title and channel menu
get_info = requests.get(url).json()
title = get_info['title']
channel = get_info['author_name']
print("\n" + smb.DONE + fontcolor.green("VIDEO INFORMATION :"))
print(smb.INPUT + fontcolor.cyan("Title : ") + fontcolor.white(title))
print(smb.INPUT + fontcolor.cyan("Channel : ") + fontcolor.white(channel))

# selecting resolution menu
print("\n" + smb.DONE + fontcolor.green("RESOLUTIONS :"))
print(smb.ONE + fontcolor.white("HD-Default 1080p(1280*720px) - Maximum Resolution"))
print(smb.TWO + fontcolor.white("SD-Default 720p(640*480px)"))
print(smb.THREE + fontcolor.white("HQ-Default 480p(480*360px)"))
print(smb.FOUR + fontcolor.white("MQ-Default 360p(320*180px)"))
print(smb.FIVE + fontcolor.white("Default 144p(120*90) - Lowest Resolution"))

#input resolution
usr = None
while not usr:
	usr = input("\n" + smb.INPUT + fontcolor.white("Select Resolution [1,2,3,4,5] > "))

#get images from "i3.ytimg.com" or "img.youtube.com"
yt_url1='https://img.youtube.com/vi/'+id+'/maxresdefault.jpg'
yt_url2='https://img.youtube.com/vi/'+id+'/sddefault.jpg'
yt_url3='https://img.youtube.com/vi/'+id+'/hqdefault.jpg'
yt_url4='https://img.youtube.com/vi/'+id+'/mqdefault.jpg'
yt_url5='https://img.youtube.com/vi/'+id+'/default.jpg'

#Download message
def msg():
	print("\n" + smb.DONE + fontcolor.green("Downloaded Successfully...Saved As ==>"),local_image_filename)

#Downloding thumbnail over users input [1,2,3,4,5]
if usr == '1':
	try:
		local_image_filename=wget.download(yt_url1)
		msg()
	except HTTPError:
		print("\n" + smb.WARN + fontcolor.red("Resolution Unavailable...Download A Lower Resolution."))

elif usr == '2':
	try:
		local_image_filename=wget.download(yt_url2)
		msg()
	except HTTPError:
		print("\n" + smb.WARN + fontcolor.red("Resolution Unavailable...Download A Lower Resolution."))

elif usr == '3':
	try:
		local_image_filename=wget.download(yt_url3)
		msg()
	except HTTPError:
		print("\n" + smb.WARN + fontcolor.red("Resolution Unavailable...Download A Lower Resolution."))

elif usr == '4':
	try:
		local_image_filename=wget.download(yt_url4)
		msg()
	except HTTPError:
		print("\n" + smb.WARN + fontcolor.red("Resolution Unavailable...Download A Lower Resolution."))

elif usr == '5':
	try:
		local_image_filename=wget.download(yt_url5)
		msg()
	except HTTPError:
		print("\n" + smb.WARN + fontcolor.red("Resolution Unavailable...Download A Lower Resolution."))

else:
	print("\n" + smb.WARN + fontcolor.red("Please Select A Valid Input ! "))

#function for clearing screen
def clr_scr():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

#Restarting program
def restart_program():
        python = sys.executable
        os.execl(python, python, * sys.argv)

if __name__ == "__main__":
    answer = input("\n" + smb.INPUT + fontcolor.cyan("Do You Want To Continue? (Y/N) : "))
    if answer.lower().strip() in "y".split():
        clr_scr()
        restart_program()