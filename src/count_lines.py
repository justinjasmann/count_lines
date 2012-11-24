import os
import sys

def count_lines(fname):
	f = open(fname, 'r')
	return len(f.readlines())

def find_java_or_xml(rootdir):
	java_or_xml = []
	for dirpath, dirnames, filenames in os.walk(rootdir):
		for file in filenames:
			if file.endswith(".xml") or file.endswith(".java"):
				java_or_xml.append(dirpath + "/" + file)
	return java_or_xml

def total_line_count():
	total = 0
	for fname in find_java_or_xml(sys.argv[1]):
		total += count_lines(fname)
	return total

print "\n"
print "**********************************************"
print "total lines writen (.java & .xml): " + str(total_line_count())
print "**********************************************"
print "\n"