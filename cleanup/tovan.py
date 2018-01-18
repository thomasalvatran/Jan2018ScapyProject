import sys
import csv
import string
import re
linecount = 0



def add_str_to_lines(f_name, str_to_add):
	with open(f_name, "r") as f:
		lines = f.readlines()
		for index, line in enumerate(lines):
			lines[index] = line.strip() + str_to_add + "\n"

	with open(f_name, "w") as f:
		for line in lines:
			f.write(line)

def cat(filename):
	f = open(filename, 'r')
	for line in f:
		# line.append("<BR>")

		print line
	f.close()

def main():
	print sys.argv
	# cat(sys.argv[1])
	# add_str_to_lines(sys.argv[1], "<BR>")
	with open('out.html', 'w') as out_file:
		with open(sys.argv[1], 'r') as in_file:
			for line in in_file:
				# out_file.write(line.rstrip('\n') + s + '\n')
				# out_file.write((line.strip('{ }') + "<BR>").translate(None, '\t(\){\}"'))
				# re.sub('[\(\)\{\}<>]', '', out_file.write((line.strip('{ }') + "<BR>")))
				# line = '<meta charset="utf-8">' + line
				line = ((line.strip('{}') + "<BR>").translate(None, '[]\(){}"').replace('ttt', ""))
				out_file.write(line.replace("</a>,", "</a>").replace("Date:","").replace("Posted:",""))
				# out_file.write((line.strip('{ }') + "<BR>").translate(string.maketrans("'\t\t\t'\t\r(){}""","           ")))
				# print(line[26:30])

	with open('out.html','r+') as f:
		content = f.read()
		f.seek(0,0)
		f.write('<meta charset="utf-8">' + '\n' + content)  #append utf-8 for browser as Dreamweaver shows

	f = open('out.html', 'r') #testing
	for line in f:
		print line
if __name__=='__main__':
	main()