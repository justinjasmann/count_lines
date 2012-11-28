#Count Lines
***
##Overview
Hello Visitors!

I created this simple Python script to count the number of lines of files residing within a directory (or sub directory) that match certain file extensions.

###Description

If you'd like, you can modify the global variable "file_extensions" to include or exclude various file extensions to match on.
	
	file_extensions = [".java", "xml"]
	
###Run

To run it, feed this script to the Python interpreter with whichever root directory you'd like to start the count from.

	python count_lines.py $HOME/workspace/test_dir
	
Results will be shown in the console.
	
	directory "$HOME/workspace/test_dir"
	100 files with extensions matching ['.java', 'xml']
	5000 lines counted
	
###Feedback

Keep in mind, I am very new to Python development, but if you have any suggestions for improvement, I'd love to hear them.

###Contact

Justin Jasmann  
<justin.jasmann@gmail.com>