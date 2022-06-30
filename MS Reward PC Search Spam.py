## Enjoy your Microsoft Search Rewards Point
## By Jason L Nov 2021
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
		os.system("taskkill /im msedge.exe /f")

import webbrowser, random, os
from time import sleep 
i=reward()
i.edge_pc_search_spam(40)



