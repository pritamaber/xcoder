# This python script removes the duplicates files from the current folder . this script is meant to 
# Delete only the duplicate python files in a given folder (to remove other type of files in place of python you have to change the variable)
# Value of the variable name extension on line 14


import os ,hashlib # Required modules os( to remove the files and walk in the directory) , hashlib( to get the md5sum of any files)

def files(directory,list_dir,delim,extension):   # This functon return all the available python files in the current folder
	file_list = dict()		# Dictionary to hold the file name and the corresponding md5values
	file_count = 0			# Optional counter to count number of 
	for file_name in list_dir:
		if extension in file_name.split(delim):
			file_list[file_name] = hashlib.md5(open(file_name,'rb').read()).hexdigest()
			file_count+=1
	if file_count == 0:
		print('no',extension,'files found')
	else:
		print('total',extension,'files ',file_count)
	return file_list


def remove_duplicates(directory,extension): # This funtion removes all the duplicate files in the current folder
	unique = []
	duplicates_file_count = 0
	for filename in os.listdir(directory):
		if os.path.isdir(filename):
			continue
		if os.path.isfile(filename):
			filehash = hashlib.md5(open(filename,'rb').read()).hexdigest()
			if filehash not in unique:
				unique.append(filehash)
			else:	
				duplicates_file_count+=1
				os.remove(filename)
	print('Total duplicate file was',duplicates_file_count)
	print('Duplicate',extension,' files was removed')

def main():
	print('This Program removes duplicate files in a given\nfolder , all you have to do is specify the extension\nex enter mp3 for audio files\npdf for removing duplciate pdf files\n.py for removeing duplicate python files')
	extension = input('Enter extension ') # change this to your desired extension depending on which file duplicates you want to remove (ex: jpg , py,mp3,png)

	directory = os.getcwd()  # Current directory

	list_dir = os.listdir(directory) # Files in current Directory

	delim = '.' # Delimiter to separate extension from filename

	filesVar = files(directory,list_dir,delim,extension)

	remove_duplicates(directory,extension)

main()
