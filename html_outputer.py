
class HtmlOutputer():
	def __init__(self):
		self.datas = []

	def collect_data(self,data):
		"""收集数据"""
		if data is None:
			return
		self.datas.append(data)

	def output_html(self):
		"""将数据写成html文件"""
		fout = open('output.html','w',encoding='utf-8')

		fout.write("<html>")
		fout.write("<body>")
		fout.write("<meta charset='utf-8'>")

		for data in self.datas:
			fout.write('<a href="%s" target="_blank">%s</a>' 
				%(data['url'],data['title']))
			fout.write("<p>%s</p>" %data['summary'])
	
		fout.write("</body>")
		fout.write("</html>")

		fout.close()