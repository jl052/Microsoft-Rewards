## Enjoy your Microsoft Search Rewards Point
## By Jason L Nov 2021
from re import M, T


class reward():
	def __init__(self):
		self.website="https://www.bing.com/search?q="
		self.random_search="keyword"  ##enter your own keyword
	def edge_pc_search_spam(self,i):
		for x in range(i):
			ran=random.random()*1000
			target=f'{self.website}{self.random_search}{ran}'
			webbrowser.register('edge',
					None,
					webbrowser.BackgroundBrowser("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"))  ## change to where your msedge.exe locate
			webbrowser.get('edge').open(target)
			sleep(1)

	def chrome_mobile_spam(self,i): #"C:\Program Files\Google\Chrome\Application\chrome.exe"
		target="this.document.location = 'http://www.bing.com/search?q="
		keyword="gbp to usd'"
		webbrowser.register('chrome',
					None,
					webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))  ## change to where your msedge.exe locate
		webbrowser.get('chrome').open('http://www.bing.com')
		sleep(10)
		#driver = webdriver.Chrome(executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe')
		pyautogui.press("F12")
		sleep(10)

		for j in range(i):
			target2=target+str(int(random.random()*1000))+keyword
			for x in list(target2):
				pyautogui.press(x)
			pyautogui.press('Enter')
			sleep(0.1)
		sleep(5)

		os.system("taskkill /im chrome.exe /f")
		os.system("taskkill /im msedge.exe /f")
#		driver=webdriver.Edge('C:\Users\\Jason\\Desktop\\App\\Virtual Harddisk\\File Exchange\\edgedriver_win64') #C:\Users\Jason\Desktop\App\chromedriver_win32
#		driver=webdriver.Chrome('C:\\Users\\Jason\\Desktop\\App\\chromedriver_win32')
#		driver.get('https://www.bing.com/')
#		driver.execute_script("this.document.location = 'http://www.bing.com/search?q=1 gbp to usd'")
#
#		webbrowser.register('edge',
#					None,
#					webbrowser.BackgroundBrowser("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"))  ## change to where your msedge.exe locate
#		webbrowser.get('edge').open("https://www.bing.com/search?q=tsla")
#		sleep(1000)

import webbrowser, random, os
from selenium import webdriver
from time import sleep 
import pyautogui
i=reward()
i.edge_pc_search_spam(40)
sleep(5)
i.chrome_mobile_spam(30)




