#most star python project on github 
import requests
import pygal
from pygal.style import LightColorizedStyle as lcs, LightenStyle as ls

url='https://api.github.com/search/repositories?q=language:Perl&sort=stars'
r=requests.get(url)

print('Status code :',r.status_code)

response_dict=r.json() 
print('total_respons_sum :',response_dict['total_count'])

repo_dicts=response_dict['items']
print('itesms sum :',len(repo_dicts))

#repo_dict=repo_dicts[0]
#print('\nKeys_sum :',len(repo_dict))
#print('name: ',repo_dict['name'])
#print('selected information about each repository')
#for repo_dict in repo_dicts:
#	print('\nname :',repo_dict['name'])
#	print('owner :',repo_dict['owner']['login'])
#	print('repository :',repo_dict['html_url'])
#	print('description :',repo_dict['description'])
	
names,plot_dicts = [],[]
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	plot_dict={
		'value':repo_dict['stargazers_count'],
		'label':repo_dict['description'],
		'xlink':repo_dict['html_url'],
	}
	plot_dicts.append(plot_dict)
	
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
chart.title='Most-Star Perl Projects on Github'
chart.x_labels=names

chart.add('',plot_dicts)
chart.render_to_file('python_github_Perl.svg')
