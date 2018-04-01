from bs4 import BeautifulSoup
import re
import urllib.parse

class HtmlParser():
	#下载后html的解析器

	def _get_new_urls(self,page_url,soup):
		"""获取当前页面中其他词条的url"""
		new_urls = set()
		#词条页面URL: /item/......
		links = soup.find_all('a',href=re.compile(r'/item/'))
		for link in links:
			new_url = link['href']
			new_full_url = urllib.parse.urljoin(page_url,new_url)
			new_urls.add(new_full_url)
		return new_urls


	def _get_new_data(self,page_url,soup):
		"""对page_url进行解析解析出标题和段落"""
		res_data = {}
		#将解析的url写入字典中
		res_data['url'] = page_url

		#将标题的内容写入字典
		#<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
		title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find("h1")
		res_data['title'] = title_node.get_text()

		#将段落的内容写入字典
		#<div class="lemma-summary" label-module="lemmaSummary">
		summary_node = soup.find('div',class_="lemma-summary")
		res_data['summary'] = summary_node.get_text()

		return res_data


	def parse(self,page_url,html_cont):
		"""对传入的url进行解析，解析出新的urls和数据"""
		if page_url is None or html_cont is None:
			return

		soup = BeautifulSoup(html_cont,'html.parser')#,from_encoding='utf-8')
		new_urls = self._get_new_urls(page_url,soup)
		new_data = self._get_new_data(page_url,soup)
		return new_urls,new_data