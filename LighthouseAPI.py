import requests
import datetime
import time
import xml.etree.ElementTree as ET
import csv
import os
import sys

uri = 'https://api.litmos.com/v1.svc/'
apikey = '406b2203-656a-4657-abe7-0e89b99d8bd1'
paths = ['users', 'courses', 'results/details']
content_type = 'xml'
source = 'lighthouse'
limit = '1000'
if len(sys.argv) > 1:
	data_days = int(sys.argv[1])
else:
	data_days = 1
timestamp = datetime.datetime.now().strftime('%Y''%m''%d''%H''%M''%S')
since = datetime.datetime.strftime(datetime.datetime.now() - datetime.timedelta(data_days), '%Y-%m-%d')
print(f'''
{uri} ; uri 
{apikey} ; apikey
{paths} ; paths
{content_type} ; content_type
{source} ; source
{limit} ; limit
{data_days} ; data_days
{since}  ;  since
initialized.''')
time.sleep(2)


def create_xml_files():
	filedict = {}
	print(f'Dictionary {filedict} initialized')
	for path in paths:
		URL = str(uri + path + '?apikey=' + apikey + '&source=' + source + '&format=' + content_type + '&limit=' + limit + '&since=' + since )
		r = requests.get(URL)
		print(URL)
		time.sleep(0.5)
		print(r.text)
		time.sleep(2)
		filepath = str(source + "_" + path + "_" + timestamp + '.xml').replace("/", "")
		filedict[path] = filepath
		print(f'{filepath} added to filedict')
		with open(filepath, 'w', encoding='utf-8') as file:
			file.write(r.text)
			print(f'{file} has been written.')
			time.sleep(0.5)
	return filedict


def parse_user_data(file):

	tree = ET.parse(file)
	print(f'{file} parsed to tree.')
	time.sleep(0.5)
	root = tree.getroot()
	print(f'{tree.getroot} rooted.')
	time.sleep(0.5)

	with open('user_data_' + timestamp + '.csv', 'w', encoding='utf-8', newline='') as file:
		
		print(f'File {file} opened as user_data.csv.')
		csvwriter = csv.writer(file)
		user_head = []
		print(f'List {user_head} initialized')

		count = 0
		for member in root.findall('User'):
			user = []
			print(f'List {user} initialized')
			if count == 0:
				userId = member.find('Id').tag
				user_head.append(userId)
				print(f'{userId} added to user header.')
				
				userName = member.find('UserName').tag
				user_head.append(userName)
				print(f'{userName} added to user header.')
				
				firstName = member.find('FirstName').tag
				user_head.append(firstName)
				print(f'{firstName} added to user header.')
				
				lastName = member.find('LastName').tag
				user_head.append(lastName)
				print(f'{lastName} added to user header.')
				
				active = member.find('Active').tag
				user_head.append(active)
				print(f'{active} added to user header.')
				
				email = member.find('Email').tag
				user_head.append(email)
				print(f'{email} added to user header.')
				
				accessLevel = member.find('AccessLevel').tag
				user_head.append(accessLevel)
				print(f'{accessLevel} added to user header.')
				
				csvwriter.writerow(user_head)
				print(f'Header construction complete for {user_head}')
				count += 1
			
			userId = member.find('Id').text
			user.append(userId)
			
			userName = member.find('UserName').text
			user.append(userName)
			
			firstName = member.find('FirstName').text
			user.append(firstName)
			
			lastName = member.find('LastName').text
			user.append(lastName)
			
			active = member.find('Active').text
			user.append(active)
			
			email = member.find('Email').text
			user.append(email)
			
			accessLevel = member.find('AccessLevel').text
			user.append(accessLevel)
			
			csvwriter.writerow(user)
			print('Row written to csv file.')
			

def parse_course_data(file):

	tree = ET.parse(file)
	print(f'{file} parsed to tree.')
	time.sleep(0.5)
	root = tree.getroot()
	print(f'{tree.getroot} rooted.')
	time.sleep(0.5)

	with open('course_data_' + timestamp + '.csv', 'w', encoding='utf-8', newline='') as file:

		csvwriter = csv.writer(file)
		course_head = []
		print(f'List {course_head} initialized')

		count = 0
		for member in root.findall('Course'):
			course = []
			print(f'List {course} initialized')
			if count == 0:
				courseId = member.find('Id').tag
				course_head.append(courseId)
				print(f'{courseId} added to course header.')
				
				code = member.find('Code').tag
				course_head.append(code)
				print(f'{code} added to course header.')
				
				name = member.find('Name').tag
				course_head.append(name)
				print(f'{name} added to course header.')
				
				active = member.find('Active').tag
				course_head.append(active)
				print(f'{active} added to course header.')
				
				forSale = member.find('ForSale').tag
				course_head.append(forSale)
				print(f'{forSale} added to course header.')
				
				originalId = member.find('OriginalId').tag
				course_head.append(originalId)
				print(f'{originalId} added to course header.')
				
				description = member.find('Description').tag
				course_head.append(description)
				print(f'{description} added to course header.')
				
				csvwriter.writerow(course_head)
				count += 1
				time.sleep(0.1)

			courseId = member.find('Id').text
			course.append(courseId)
			
			code = member.find('Code').text
			course.append(code)
			
			name = member.find('Name').text
			course.append(name)
			
			active = member.find('Active').text
			course.append(active)
			
			forSale = member.find('ForSale').text
			course.append(forSale)
			
			originalId = member.find('OriginalId').text
			course.append(originalId)
			
			description = member.find('Description').text
			course.append(description)
			
			csvwriter.writerow(course)
			print('Row written to csv file.')
			

def parse_result_data(file):

	tree = ET.parse(file)
	print(f'{file} parsed to tree.')
	time.sleep(0.5)
	root = tree.getroot()
	print(f'{tree.getroot} rooted.')
	time.sleep(0.5)

	with open('result_data_' + timestamp + '.csv', 'w', encoding='utf-8', newline='') as file:

		csvwriter = csv.writer(file)
		result_head = []
		print(f'List {result_head} initialized')

		count = 0
		for member in root.findall('User'):
			result = []
			print(f'List {result} initialized')
			if count == 0:
				UserId = member.find('Id').tag
				result_head.append(UserId)
				print(f'{UserId} added to result header.')
				
				UserOriginalId = member.find('UserOriginalId').tag
				result_head.append(UserOriginalId)
				print(f'{UserOriginalId} added to result header.')
				
				CourseId = member.find('CourseId').tag
				result_head.append(CourseId)
				print(f'{CourseId} added to result header.')
				
				CourseOriginalId = member.find('CourseOriginalId').tag
				result_head.append(CourseOriginalId)
				print(f'{CourseOriginalId} added to result header.')
				
				CourseName = member.find('CourseName').tag
				result_head.append(CourseName)
				print(f'{CourseName} added to result header.')
				
				Completed = member.find('Completed').tag
				result_head.append(Completed)
				print(f'{Completed} added to result header.')
				
				PercentageComplete = member.find('PercentageComplete').tag
				result_head.append(PercentageComplete)
				print(f'{PercentageComplete} added to result header.')
				
				CompletedDate = member.find('CompletedDate').tag
				result_head.append(CompletedDate)
				print(f'{CompletedDate} added to result header.')
				
				UpToDate = member.find('UpToDate').tag
				result_head.append(UpToDate)
				print(f'{UpToDate} added to result header.')
				
				Overdue = member.find('Overdue').tag
				result_head.append(Overdue)
				print(f'{Overdue} added to result header.')
				
				csvwriter.writerow(result_head)
				count += 1
				time.sleep(0.1)

			UserId = member.find('Id').text
			result.append(UserId)
			
			UserOriginalId = member.find('UserOriginalId').text
			result.append(UserOriginalId)
			
			CourseId = member.find('CourseId').text
			result.append(CourseId)
			
			CourseOriginalId = member.find('CourseOriginalId').text
			result.append(CourseOriginalId)
			
			CourseName = member.find('CourseName').text
			result.append(CourseName)
			
			Completed = member.find('Completed').text
			result.append(Completed)
			
			PercentageComplete = member.find('PercentageComplete').text
			result.append(PercentageComplete)
			
			CompletedDate = member.find('CompletedDate').text
			result.append(CompletedDate)
			
			UpToDate = member.find('UpToDate').text
			result.append(UpToDate)
			
			Overdue = member.find('Overdue').text
			result.append(Overdue)
			
			csvwriter.writerow(result)
			print('Row written to csv file.')
			time.sleep(0.1)


def parse_files_to_csv(xml_file_dict):
	users_filename = xml_file_dict['users']
	print(f'Users file {users_filename} parsed to csv.')
	course_filename = xml_file_dict['courses']
	print(f'Courses file {course_filename} parsed to csv.')
	result_filename = xml_file_dict['results/details']
	print(f'Result file {result_filename} parsed to csv.')
	
	parse_user_data(users_filename)
	parse_course_data(course_filename)
	parse_result_data(result_filename)
	
	
	print(f'Removing {users_filename} from file system.')
	os.remove(users_filename)
	print(f'Removing {course_filename} from file system.')
	os.remove(course_filename)
	print(f'Removing {result_filename} from file system.')
	os.remove(result_filename)	
	

def main():

	xml_file_dict = create_xml_files()
	parse_files_to_csv(xml_file_dict)
	exit(0)

	
main()
	
	

