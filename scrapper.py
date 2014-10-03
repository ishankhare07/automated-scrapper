from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import urllib2, pytesseract,Image


class handler:
	def __init__(self):
		self.starting = '0842ar121011'
		self.driver = webdriver.Firefox()

	#select course
	def navigate(self):
		self.driver.get('http://result.rgpv.ac.in/exam/programselect.aspx')
		self.driver.find_element_by_id('radlstProgram_3').click()

	#enter details
	def enter(self):
		#enter name
		roll = self.driver.find_element_by_id('txtrollno')
		roll.send_keys(self.starting)

		#select semester
		sem = Select(self.driver.find_element_by_name('drpSemester'))
		sem.select_by_value('4')

		#taking screenshot
		self.take_screenshot()

		#crop image
		image_element = self.driver.find_element_by_xpath("//img[@alt='Captcha']")
		location = image_element.location
		size = image_element.size
		self.crop_image(location,size)

		#capture image text
		text = self.recover_text('myfile.png').strip()
		print text

		#entering captcha text
		txtbox1 = self.driver.find_element_by_id('TextBox1')
		txtbox1.send_keys(text)

		#submit
		self.driver.find_element_by_name('btnviewresult').click()

	#taking screenshot
	def take_screenshot(self):
		self.driver.save_screenshot('myfile.png')

	#cropping image
	def crop_image(self,location,size):
		image = Image.open('myfile.png')
		x,y = location['x'], location['y']
		w,h = size['width'], size['height']
		image.crop((x, y, x+w, y+h)).save('myfile.png')

	#retrieving text
	def recover_text(self,filename):
		image = Image.open('myfile.png')
		r,g,b,a = image.split()			#removing the alpha channel
		image = Image.merge('RGB',(r,g,b))
		return pytesseract.image_to_string(image)


if __name__ == '__main__':
	h = handler()
	h.navigate()
	h.enter()