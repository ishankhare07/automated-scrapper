from __future__ import print_function
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import pytesseract, Image, time, anydbm, json


class handler:
	def __init__(self):
		file = raw_input('enter output file : ')
		self.file = anydbm.open('/home/ishan/Desktop/automated-scrapper/data/%s' %file,'c')
		self.driver = webdriver.Firefox()

	#select course
	def navigate(self):
		try:
			self.driver.get('http://result.rgpv.ac.in/exam/programselect.aspx')
			self.driver.find_element_by_id('radlstProgram_0').click()
			return True
		except:
			try:
				Alert(self.driver).dismiss()
				self.navigate()
			except:
				return None

	#enter details
	def enter(self,roll):
		crc = 0
		if roll in self.file.keys():
			return None
		self.current_roll = roll
		#enter name
		try:
			roll = self.driver.find_element_by_id('txtrollno')
			roll.send_keys(self.current_roll)
		except:
			pass

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
		while crc <= 3:
			text = self.recover_text('myfile.png').strip()
			if text:
				print(text)
				break
			else:
				crc += 1

		#entering captcha text
		txtbox1 = self.driver.find_element_by_id('TextBox1')
		txtbox1.send_keys(text)

		#submit
		time.sleep(5)				#waiting in order to avoid server-side check (refer comment https://gist.github.com/ishankhare07/2a96ca58981ba99aca91#comment-1314588)
		try:
			Alert(self.driver).dismiss()
			return None
		except:
			pass
		self.driver.find_element_by_name('btnviewresult').click()

		return True

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

	def save(self):
		try:
			Alert(self.driver).dismiss()
			return
		except:
			pass
		result = self.driver.page_source.encode('utf-8')
		if self.current_roll not in self.file.keys():
			try:
				self.driver.find_element_by_id('lblStreamGrading')
				self.file[self.current_roll] = result
				print('saved', self.current_roll)
			except Exception as e:
				print(e)

if __name__ == '__main__':

	static_roll = '0111me121'
	dynamic_roll = [static_roll + '%03d' %x for x in range(1,131)]
	h = handler()
	for roll_no in dynamic_roll:
		if h.navigate() and h.enter(roll_no):
			h.save()
