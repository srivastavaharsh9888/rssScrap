from django.shortcuts import render,redirect
import requests
from bs4 import BeautifulSoup

def home(request):
	return render(request,'home.html',{})

def showHome(request):
	return redirect('/home/')

def scrapeData(request):

	if request.method=="POST":
		url = request.POST.get("query")
		resp = requests.get(url)

		soup = BeautifulSoup(resp.content, features="xml")

		items = soup.findAll('item')

		news_items = []

		for item in items:
			news_item = {}
			try:
				news_item['title'] = item.title.text
			except:
				pass

			try:	
				news_item['description'] = item.description.text
			except:
				pass

			try:	
				news_item['link'] = item.link.text
			except:
				pass	

			try:
				news_item['img_show']=True
				news_item['content'] = item.content['url']
			except:
				news_item['img_show']=False
				news_item['content'] = ""

			try:
				news_item['pub_date'] = item.pubDate.text				
			except:
				pass
			print(news_item)
			news_items.append(news_item)
		return render(request,'index.html',{'news_items':news_items})
	else:
		return render(request,'home.html',{})