import os
import sys

file_extensions = [".java", "xml"]

def count_lines(fname):
	f = open(fname, 'r')
	return len(f.readlines())

def find_java_or_xml(rootdir):
	java_or_xml = []
	for dirpath, dirnames, filenames in os.walk(rootdir):
		for file in filenames:
			for file_ext in file_extensions:
				if file.endswith(file_ext):
					java_or_xml.append(dirpath + "/" + file)
					break;
	return java_or_xml

def total_line_count(dirname):
	total = 0
	java_or_xml_files = find_java_or_xml(dirname)
	if len(java_or_xml_files) == 0:
		print num_files_found_message(0)
	else:
		print num_files_found_message(len(java_or_xml_files))
		for fname in java_or_xml_files:
			total += count_lines(fname)
	return total

def num_files_found_message(num_files):
	msg = str(num_files) + " files matched extensions: " + str(file_extensions)
	return indent_msg(msg)

def indent_msg(msg):
	return "\t" + msg

def main(dirname):
	print indent_msg("directory \"" + str(dirname) + "\"")
	print indent_msg(str(total_line_count(dirname)) + " total lines counted")
	
if __name__ == "__main__":
	print 
	if len(sys.argv) == 2:
		directory = sys.argv[1]
		if os.path.isdir(directory) == True:
			main(directory)
		else:
			print indent_msg("\"" + directory + "\" is not a directory")
	else:
		print indent_msg("Usage: python count_lines.py <directory_with_files>")
	print 