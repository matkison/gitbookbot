def main():
	print("attempting to open the file...")
	with open ("books/frankenstein.txt") as f:
		# this saves the frankenstein.txt as f I guess
		file_contents = f.read()
	return file_contents
def print_file_contents():
	file_contents = main()
	print(file_contents)
def count_words():
	print("Counting words...")
	file_contents = main()
	split_file_contents = file_contents.split()
	word_count = len(split_file_contents)
	print(word_count)
	return word_count
def each_char_count():
	file_contents = main()
	lower_file_contents = file_contents.lower()
	each_char_count = {}
	for char in lower_file_contents:
		#if char in each_char_count != " ":
			#print("this isn't a space")
		if char not in each_char_count:
			#print("first time encountering this char")
			each_char_count[char] = 1
		else:
			#print("adding 1 to this char count")
			each_char_count[char] += 1
	return each_char_count
	print(each_char_count)
def make_report():
	each_char_count = each_char_count()
	word_count = count_words()
	print("--- Begin report of books/frankenstein.txt ---")
	print(f"{word_count} words found in the document")
	for item in each_char_count:
		print(f"The {item} character was found {each_char_count[item]} times")
	print("End Report")
make_report()



