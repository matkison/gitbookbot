def main():
	print("attempting to open the file...")
	with open ("books/frankenstein.txt") as f:
		# this saves the frankenstein.txt as f I guess
		file_contents = f.read()
	return file_contents
def print_file_contents():
	file_contents = main()
	print(file_contents)
print_file_contents()

