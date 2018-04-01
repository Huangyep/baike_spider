
class UrlManager():
	#url管理器
	def __init__(self):
		#创建两个列表，用于存储新旧url,这样不会重复抓取数据
		self.new_urls = set()
		self.old_urls = set()

	def add_new_url(self,url):
		"""将新的url添加进new_urls列表"""
		if url is None:
			return
		if url not in self.new_urls and url not in self.old_urls:
			self.new_urls.add(url)

	def add_new_urls(self,urls):
		"""向管理器添加批量的url"""
		if urls is None or len(urls)==0:
			return
		for url in urls:
			self.add_new_url(url)

	def has_new_url(self):
		"""判断是否有新的url"""
		return len(self.new_urls) != 0

	def get_new_url(self):
		"""从new_urls列表中获取url,用于爬取数据"""
		new_url = self.new_urls.pop()
		self.old_urls.add(new_url)
		return new_url
	