import requests
import sys, time
import json, re
from random import randint
from itertools import cycle

class KrowdKrawler:
	message_cycle = cycle(range(100))
	urls = []

	def __init__(self, initial_page):
   		self.message_cycle = cycle(range(initial_page, initial_page+100))

	def search_backers(self):

		url = "https://app.krowdster.co/backer/directory/json"

		querystring = {"category":"Art","g-recaptcha-response":"03AHJ_VuukueMJJMDNYSBnfRgGvY_74DUmkmuus9NMtFv0IxGRqnQuUrKskWhViuLnsREcJSWsbBgeuac3wxZR9v6IUZfCEU1uG3ZIfDR1GPEL8uohe05XXix0AgMfShIpoaFMrM3x--0q63bzON1pfUUMIhmbN-frmkCgnv47Ad1xgmP1PNP0_pvbwsQxoW5owwaOV0JstKexWwg6Z00saWiT-dfF7iNanBjSJ-3s-6KydhDPGNczplmt8xxNkAVfd52X_aWW-LAlwuqLAVCKp0sLuCmI3k0baUtJMTvR3KUvN9WkHEnw6YhzbLUKSGbCQIWS4hpeZQNtGBhNW2Y4AD_RV0aSZGy5CUzKW6fGkqkJ73VkicU5HQMOjrNUKYHaZ6vIPIX4ONUjK0J1hCqS76_ZuGpfo8lcWuPOmiVKRddJcXLKEaZnyqM0gIogkRyzwi4ANhw0cBEDWY6D3jqbwkKtMYm8hAheZlVLckLteznJCcioj7xPwhdtCguO6iRPcumyrqIGYY30JiyBqiUYK9WTV1ASH5d2S7Z1XLpVQd85JQX-jIJ136Rkc43GyHcQssa4KcrX2p7b5qxrrkpM7CNfK9AeoYj7Cei5iKHc4EC9v--BK74NFHoDj5mhsY1HYZ9Kd0rfPJlyrvg1_Zg34uBFp1kE5XmTlu1KBvhw-z9bfQrreKQpXF8zAZTViSnk8w-nM0VKN4xu-3knyfRr-LQZIYl1EzOG_6J6q-lj0hHal9kz-MmpLVUGeczxA32HyF6wtoZ8gKpF_a3Ekc0vqFLOf0vSo98NrF_pIrr3NC1JRz_7dv6dx1XGuHuOm5FbwpHHXHqqnLQSLmFzD4a0r6KfN1GNEdXonmaI1Z2mKtLYUUO1EFojcjzYiwu5T4MjUmUc2IPMpuOmcbFZjc8DbLBGoqk0IWGfTN90Bu8-4I2qV_hZg5mOcVsJ1l2tyRBixiT_V7jRAESLfnOWwYX7GCr9xDf1dHqfURQ6BYMLZ59tw-8CYTJqlik","num_contributions":"20","page":self.message_cycle.next(),"platform":"Kickstarter"}

		headers = {
		    'accept': "application/json, text/plain, */*",
		    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
		    'dnt': "1",
		    'referer': "https://app.krowdster.co/backer/directory",
		    'accept-encoding': "gzip, deflate, sdch, br",
		    'accept-language': "en-US,en;q=0.8",
		    'cookie': "_gat=1; hsfirstvisit=https%3A%2F%2Fapp.krowdster.co%2F|https%3A%2F%2Fapp.krowdster.co%2Fprofile%2Ffree|1467146769034; laravel_session=eyJpdiI6Ik5uR05LNStjZjNUUGtFc202WHBwbHc9PSIsInZhbHVlIjoidmVpMkltZXhaTUNHeUtxZ21pbWRua0NscmhVZTRHS2hMTHdiOTBzWFRIRW5nc043alVEb1wvcUlHdVo0OFYyYmRmb25DMUlMcUVJTytpdTVEbms3aWl3PT0iLCJtYWMiOiJiZGE4OTc4NjMwN2I3ZmU5NDRhMDI3YmJkZDIzNzJiYjk4MjdhNzU3MDkzMzE2MjdiMTBmMGQ0MGM2YzYyNjEyIn0%3D; _ga=GA1.2.2073108638.1467146051; __hstc=256735060.6f0029247dda55aed3c11287c9bdf732.1467146769046.1467146769046.1467155654816.2; __hssrc=1; __hssc=256735060.6.1467155654816; hubspotutk=6f0029247dda55aed3c11287c9bdf732; intercom-session-b3ojslmo=RWFpZ2hSaFZpL0RSRzM1WWxwWVo5OTFPRVdNa0ptZWVBK0thYVd0eEJqVXJSeDIrWklCY1IrZVJiU21ZSUFlMC0tUjNZVXB0UFJpdTBxZk1lYzdQK3JVUT09--5a54921e86a43f4d6b7a971deb5d6cad0568ec2a; hsfirstvisit=https%3A%2F%2Fapp.krowdster.co%2F|https%3A%2F%2Fapp.krowdster.co%2Fprofile%2Ffree|1467146769034; _gat=1; remember_82e5d2c56bdd0811318f0cf078b78bfc=eyJpdiI6ImlrZFNKZHBUMGxCWkVFdVMweWdlVEE9PSIsInZhbHVlIjoiTDZQM1cybzY5eE9iZk8rVWNEdmZBNm9tVmNJVGZlXC81ZzZ0elU1c1ZpVkpLMFVsOWFwZWNscTlHTHFtWmlvVmlJTHc5UWxINjI5WmNibDBMcTJhc1p6YmYrWHRUSVRoUkpvb3pcL2ZSQW5mMD0iLCJtYWMiOiJmZTA3ZTQwNGZkYjk2NzlmNDEyOWNhNDEwYTZiYmIzN2Q2OTBiNjQ2MzMxNDVlMTU4Zjc1N2ZlMzQ2YjI5YWVjIn0%3D; _ga=GA1.2.2073108638.1467146051; __hstc=256735060.6f0029247dda55aed3c11287c9bdf732.1467146769046.1467146769046.1467155654816.2; __hssrc=1; __hssc=256735060.7.1467155654816; __hssc=256735060.7.1467155654816; hubspotutk=6f0029247dda55aed3c11287c9bdf732; intercom-session-b3ojslmo=bVhXY1M2S1RGZjkxdzFsS0V0Ky90WnNwYzF4bzNVcVhxTjFRMDZLc3JsS2lRZndVTzlKdWFjWjhFNHhKbFhWeS0tdmRoemJlaDVta1JMS0VFWjFYcVFDQT09--2b17c4f623405ac2244735073cb71dcc3064d8f3; laravel_session=eyJpdiI6IlVyb2xIcmI1Tnd6UlFzUmVpN0dsMkE9PSIsInZhbHVlIjoiXC9pWXB6QTZNU01HVjZCdnI4NFhMZnZcL0dZZGVRSHZrSEdlRkxBbVwvRGE2aGpSN01DVm8weXdQMmlkMktjcVFJMGQrbXFSRGJ0UnB2M0tkUExxNmt0bmc9PSIsIm1hYyI6ImE0MWUyMjUzOTQ4YzE4Mzc5NDMzOTUxZDcyZDQ2NWMzNmQyNDcyYzdlYmNkYjE4NmJlZmNiNzcyZDRhOWIwNWEifQ%3D%3D",
		    'cache-control': "no-cache",
		    'postman-token': "ec513bef-b7d5-d9ee-6702-9ff5bbb5402f"
		    }

		response = requests.request("GET", url, headers=headers, params=querystring)

		print(response.text)
		json1_data = json.loads(response.text)
		try:
			for entry in json1_data["data"]:
				twit_url = "@" + re.findall(r"http[s]*.+?.com/(.+?)$", entry["twitter_url"])[0]
				print twit_url
				self.urls.append(twit_url)
		except Exception as e:
			print("Exception: " + str(e))
			print entry
			print response.text

	def search_journalists(self,query):

		url = "https://app.krowdster.co/buzzsumo/influencer"

		querystring = {"blogger":"true","company":"true","ignore_broadcasters":"false","influencer":"true","journalist":"true","page":"1","q":query,"regular_people":"true","result_type":"relevancy"}

		headers = {
		    'accept': "application/json, text/plain, */*",
		    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
		    'dnt': "1",
		    'referer': "https://app.krowdster.co/influencer/marketing",
		    'accept-encoding': "gzip, deflate, sdch, br",
		    'accept-language': "en-US,en;q=0.8",
		    'cookie': "hsfirstvisit=https%3A%2F%2Fapp.krowdster.co%2F|https%3A%2F%2Fapp.krowdster.co%2Fprofile%2Ffree|1467146769034; remember_82e5d2c56bdd0811318f0cf078b78bfc=eyJpdiI6ImlrZFNKZHBUMGxCWkVFdVMweWdlVEE9PSIsInZhbHVlIjoiTDZQM1cybzY5eE9iZk8rVWNEdmZBNm9tVmNJVGZlXC81ZzZ0elU1c1ZpVkpLMFVsOWFwZWNscTlHTHFtWmlvVmlJTHc5UWxINjI5WmNibDBMcTJhc1p6YmYrWHRUSVRoUkpvb3pcL2ZSQW5mMD0iLCJtYWMiOiJmZTA3ZTQwNGZkYjk2NzlmNDEyOWNhNDEwYTZiYmIzN2Q2OTBiNjQ2MzMxNDVlMTU4Zjc1N2ZlMzQ2YjI5YWVjIn0%3D; _ga=GA1.2.2073108638.1467146051; __hstc=256735060.6f0029247dda55aed3c11287c9bdf732.1467146769046.1467155654816.1467252116961.3; __hssrc=1; __hssc=256735060.2.1467252116961; hubspotutk=6f0029247dda55aed3c11287c9bdf732; intercom-session-b3ojslmo=aEwzSllJQ0lNU3hqMkhjRCs2ZGEza2FvQ00vWEVrWTVlU1ZSZWpSZy9NTVRGZnQzUjV1T0dGaGFEKzE2QUd2My0tY0FOeGpiVldjK3lsVlZBSXlpamQxdz09--b3d882b249eb215abee64cf2532c3746066f6ba4; laravel_session=eyJpdiI6Ik9YUmh1Uks1dmZCSHNUOCtDdUdzN1E9PSIsInZhbHVlIjoibEc0Unl5K3FPWmgxZldiNjJDdzNjV2ZRdGZMcXpFaFZsdXp6NVkySVErZlI4SEx3TWNkdHRjeDc3QVVpMllJMkoxdHc4aXhYd29DbzZXQTlSQ1htRGc9PSIsIm1hYyI6ImY0ZWFjZTA5MTkxMTA3MDI4NTJmNGIxY2JlZGJlNGQ3YzVjMTUyNzk5ODUwNjYwYzY1NGNmYjRmNDExZGU3YjkifQ%3D%3D; hsfirstvisit=https%3A%2F%2Fapp.krowdster.co%2F|https%3A%2F%2Fapp.krowdster.co%2Fprofile%2Ffree|1467146769034; _gat=1; remember_82e5d2c56bdd0811318f0cf078b78bfc=eyJpdiI6InFFZE1QdmoxcFRYRmdnQ01JKzgzVWc9PSIsInZhbHVlIjoiVGF5Q3pxdzNGK1pXcW9wUitMeWJYcFNHSlF5bVhGak8zR0pxdGZhXC9aWWpYNDZYMUVtMnBYckUweGVLNkpsblY2ZlVMU1lOWkRxVXgrcVwvMHFTdERNSlBvWERRaE10UU55WDNVUVNCNUZpdz0iLCJtYWMiOiI4OWUwZDdjMTgzMTQzYzI5ODA3NGU4YTc3ZGY5M2M0MzAyOWI4MTY1Yjk5OTk4ZGFiMTg5Mjk1MmZlNWFiMTU0In0%3D; _ga=GA1.2.2073108638.1467146051; __hstc=256735060.6f0029247dda55aed3c11287c9bdf732.1467146769046.1467252116961.1467657054912.4; __hssrc=1; __hssc=256735060.2.1467657054912; hubspotutk=6f0029247dda55aed3c11287c9bdf732; intercom-session-b3ojslmo=RE9hU2dweWZLYUZ5dFVUWmVUMkUvTUFKT2Z2UlltNVB1ZUxBekU0SldINUgyTmtZckxLNS9rRURqaEJoWFM2VC0tSEN6cXlsRTN4a1RwbkZNRE1MM2E2QT09--e8df05074e685de33385eb603a70dfcf1b11d650; laravel_session=eyJpdiI6ImxyaFJXNGpySkdUOWtEbG85dWFXNWc9PSIsInZhbHVlIjoiT05aUVh1V3NFcUNvTGoxWVBNSFErXC9CMnRYbzIxV0tmQlJaemw2WUl1KzVxRDFncTJGcmFNN29OWExqMzRFZENGXC9ieFwvaWpiemJHUm1mUTdjeFErK3c9PSIsIm1hYyI6IjBjZjYxNDFmZDExNmMzNjdhNWFjYmYyMTFhMzY3NDVlZDM2MDQ3ZmY0MTc5Nzg0MGQ4Y2ZmZWY1MDk2NzM2YmQifQ%3D%3D",
		    'cache-control': "no-cache",
		    'postman-token': "ae2e6fbb-304e-7797-3aed-f071b30d8f2c"
		    }

		response = requests.request("GET", url, headers=headers, params=querystring)

		print(response.text)
		json1_data = json.loads(response.text)
		try:
			for entry in json1_data["results"]:
				twit_url = "@" + entry["username"]
				print twit_url
				self.urls.append(twit_url)
		except Exception as e:
			print("Exception: " + str(e))
			print entry
			print response.text
			

def crawl_krowd(start):
	kk = KrowdKrawler(start)
	for x in range(1):
		kk.search_journalists("animal photography")
		nap = randint(1, 60*2)
		#time.sleep(nap)
	return kk.urls

crawl_krowd(1)
