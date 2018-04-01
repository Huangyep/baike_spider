from urllib import request

class HtmlDownloader():
	#url下载器
	def download(self,url):
		"""将url下载，用于解析"""
		if url is None:
			return None

		response = request.urlopen(url)

		if response.getcode() != 200:
			return None

		return response.read()