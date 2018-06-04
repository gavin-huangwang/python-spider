import requests
from operator import itemgetter
import pygal
from pygal.style import LightColorizedStyle as lcs, LightenStyle as ls

url='https://hacker-news.firebaseio.com/v0/topstories.json'
r=requests.get(url)
print('state code: ',r.status_code)

ids=r.json()
n_dicts = []
for nid in ids[:30]:
	url=('https://hacker-news.firebaseio.com/v0/item'+str(nid)+'.json')
	nid_r=requests.get(url)
	print(nid_r.status_code)
	response_dict=nid_r.json()
	
	n_dict={
	'title':response_dict['title'],
	'link':response_dict['http://news.ycombinator.com/item?id='+str(nid)],
	'comments':response_dict.get('descendants',0)
	}
	n_dicts.append(n_dict)
	
n_dicts=sorted(n_dicts,key=itemgetter('comments'),reverse=True)
title_list = []
for i_dict in n_dicts:
	print('\ntitle:',i_dict['title'])
	print('discussion link:',i_dict['link'])
	print('comments:',i_dict['comments'])
	title_list.append(i_dict['title'])
	
my_style=ls('#336699',base_style=lcs)
my_config=pygal.Config()
my_config.x_label_rotation=45
my_config.show_legend=False
my_config.title_font_size=30
my_config.label_font_size=20
my_config.major_label_font_size=30
my_config.truncate_label=15
my_config.show_y_guides=False
my_config.width=1260

chart = pygal.Bar(my_config,style=my_style)
chart.title='n_api'
chart.x_labels=title_list

chart.add('',n_dicts)
chart.render_to_file('n_api.svg')	
