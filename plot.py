import plotly.plotly as py
from plotly.graph_objs import *
import anydbm, sys
from bs4 import BeautifulSoup

class plot_bot:
	def __init__(self,filename):
		self.filename = filename
		self.cgpa = []
		self.sgpa = []
		self.roll_no = []

	def get_data(self):
		file = anydbm.open('myscraps','r')
		for roll_no in sorted(file.keys()):
			soup = BeautifulSoup(file[roll_no])
			self.roll_no.append(roll_no[-3:])
			self.sgpa.append(soup.find(id='lblSGPA').get_text())
			self.cgpa.append(soup.find(id='lblcgpa').get_text())
	
	def plot(self):
		sgpa = Bar(
			x = self.roll_no,
			y = self.sgpa
		)

		cgpa = Bar(
			x = self.roll_no,
			y = self.cgpa
		)

		data = Data([sgpa,cgpa])
		py.plot(data,filename=self.filename)
name = raw_input('Provide a filename : ')
if name:
	b = plot_bot(name)
	b.get_data()
	b.plot()
else:
	print 'Please provide a valid filename'
	exit()
