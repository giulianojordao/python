import os
def rename_files():
	#1: Get filenames from a folder
	file_list = os.listdir(r"/Users/swkrause/home/python/prank")
	for file in file_list:
		print (file)
	
	#2: for each filename, rename filename and remove numbers
	path = os.getcwd()
	os.chdir(r"/Users/swkrause/home/python/prank")
	for file_name in file_list:
		# print file_name
		
		os.rename(file_name, file_name.translate(None, "0123456789"))
	
rename_files()
