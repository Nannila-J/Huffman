#!/usr/local/bin/python3
import sys
import argparse
 
class Tree:
	def __init__(self,left_val,right_val,root_val):
		self.left = left_val
		self.right = right_val
		self.root_val = root_val
	
	def get_root(self):
		return self.root_val
 
	def set_root(self,curr):
		self.root = curr
 
	def get_left(self):
		return self.left
	
	def get_right(self):
		return self.right
 
	def set_left(self,left):
		self.left = left
 
	def set_right(self,right):
		self.right = right
 
class Huffman(Tree):
	def __init__(self):
		self.tree = None
		self.list_of_char = None
		self.data = None
		self.info = ''
 
	def set_tree(self,tree):
		self.tree = tree
	
	def get_tree(self):
		return self.tree
	
	def set_list_of_char(self,char_list):
		self.list_of_char = char_list
 
	def get_list_of_char(self):
		return self.list_of_char
 
	def set_data(self,data):
		self.data = data
	
	def get_data(self):
		return self.data
 
	def set_info(self,info):
		self.info = info
	
	def get_info(self):
		return self.info
 
def build_tree(input_text):
    
	characters = '\'"AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz 1234567890!@#$%^&*()-_+={}[]\|<>,.?/~`\n'
	
	char_count = []
	node = []
	#Store charecters and their frequency in a list
	for i in characters:
		if i in input_text:
			char_count.append([i,input_text.count(i)])
	
	char_count.sort(key = lambda x: x[1])
 
	for i in char_count:
		node.append(Tree(None,None,i))
 
	tree = node
	
	while(len(tree))>1:
		if(isinstance(tree[0].get_root(),list) and isinstance(tree[1].get_root(),list)):
			newroot = tree[0].get_root()[1] + tree[1].get_root()[1]
			if(tree[0].get_root()[1] <= tree[1].get_root()[1]):
				newLeft,newRight = tree[0],tree[1]
			else:
				newLeft,newRight = tree[1],tree[0]
			
			newTree = Tree(newLeft,newRight,newroot)
			tree.append(newTree)
			tree.remove(newTree.get_left())
			tree.remove(newTree.get_right())
		
		elif(isinstance(tree[0].get_root(),int) and isinstance(tree[1].get_root(),int)):
			newroot = tree[0].get_root() + tree[1].get_root()
			if(tree[0].get_root() <= tree[1].get_root()):
				newLeft,newRight = tree[0],tree[1]
			else:
				newLeft,newRight = tree[1],tree[0]
		
			newTree = Tree(newLeft,newRight,newroot)
			tree.append(newTree)
			tree.remove(newTree.get_left())
			tree.remove(newTree.get_right())
		
		elif(isinstance(tree[0].get_root(),int) and isinstance(tree[1].get_root(),list)):
			newroot = tree[0].get_root() + tree[1].get_root()[1]
			if(tree[0].get_root() <= tree[1].get_root()[1]):
				newLeft,newRight = tree[0],tree[1]
			else:
				newLeft,newRight = tree[1],tree[0]
			
			newTree = Tree(newLeft,newRight,newroot)
			tree.append(newTree)
			tree.remove(newTree.get_left())
			tree.remove(newTree.get_right())
		
		elif(isinstance(tree[0].get_root(),list) and isinstance(tree[1].get_root(),int)):
			newroot = tree[0].get_root()[1] + tree[1].get_root()
			if(tree[0].get_root()[1] <= tree[1].get_root()):
				newLeft,newRight = tree[0],tree[1]
			else:
				newLeft,newRight = tree[1],tree[0]
			
			newTree = Tree(newLeft,newRight,newroot)
			tree.append(newTree)
			tree.remove(newTree.get_left())
			tree.remove(newTree.get_right())
		
		tree.sort(key=lambda x : x.get_root() if(isinstance(x.get_root(), int)) else x.get_root()[1])
	
	obj = Huffman()
	obj.set_tree(tree[0])
	obj.set_list_of_char(char_count)
	obj.set_data([tree[0],char_count])
	return (tree[0],char_count)
 
def traverse_tree(data,left,right,val,tot_letter_list):
	if(len(tot_letter_list) == len(data[1])):
		return tot_letter_list
	if left:
		val=val+'0'
	if right:
		val=val+'1'
 
	if(isinstance(data[0].get_root(),int)):
		if(isinstance(data[0].get_left().get_root(),list)):
			for i in data[1]:
				if(i[0] == data[0].get_left().get_root()[0]):
					if[i[0],str(val)+'0'] not in tot_letter_list:
						tot_letter_list.append([i[0],str(val) + '0'])
		if(isinstance(data[0].get_right().get_root(),list)):
			for i in data[1]:
				if(i[0] == data[0].get_right().get_root()[0]):
					if[i[0],str(val)+'1'] not in tot_letter_list:
						tot_letter_list.append([i[0],str(val) + '1'])
		return traverse_tree([data[0].get_left(),data[1]],True,False,val,tot_letter_list) or traverse_tree([data[0].get_right(),data[1]],False,True,val,tot_letter_list)  
 
def get_encoded_text(text,charecters_list):
	encoded_txt = ''
	for char in text:
		for i in charecters_list:
			if char == i[0]:
				encoded_txt += i[1]
		
	return encoded_txt
 
def encode(input_file, output_file):
	print("encoding ", input_file, output_file)
	# write code here
	with open(input_file,'r+') as inp_file,open(output_file,'wb') as out_file:
		text = inp_file.read()
		text = text
		#Build huffman tree
		tree = build_tree(text)
		#Traverse the tree and get the code for each letter
		code_list = traverse_tree(tree,None,None,'',[])
		
		obj1 = Huffman()
		obj1.set_tree(tree)
		obj1.set_list_of_char(code_list)
		
		#for i in code_list:
		#	if(i[0] == '\n'):
		#		i[0] = '\N'
		#Store codewords and Huffman code in a file
		dictonary = {}
		for i in code_list:
			dictonary.update({i[0]:i[1]})
		sorted_dict = sorted(dictonary.items(), key=lambda x: len(x[1]),reverse =True)
		for i in sorted_dict:
			if(i[0] == '\n'):
				out_file.write("\N" + ":" +i[1]+" ")	
				continue
			out_file.write(i[0] + ":" +i[1]+" ")
		encoded = get_encoded_text(text,code_list)
		out_file.write('\n')
		out_file.write(encoded)
 		
	# simply copying the file to bypass the actual test.
	# remove the below lines.
	#if input_file != "" and output_file != "":
	#	shutil.copyfile(input_file, output_file)
  
def decode(input_file, output_file):
	print("decoding ", input_file, output_file)
	# write code here
	with open(input_file,'r') as inp_file,open(output_file,'w') as out_file:
		dic = {}
		file_info = inp_file.readlines()
		codes = file_info[0].split(' ')
		binary = file_info[1]
		out_str = ''
		for i in codes:
			if len(i) <= 1:
				codes.remove(i)
		
		for i in codes:	
			kv = i.split(':')
			if(len(kv[0]) == 0):
				kv[0] = ' '
			dic.update({kv[1]:kv[0]})
		sorted_dict = sorted(dic.items(), key=lambda x: len(x[0]),reverse =True)
		
		while(len(binary) != 0):
			for i in sorted_dict:
				l = len(i[0])
				if(i[0] == (binary[0:l])):
					if(i[1] == '\\N'):
						out_file.write('\n')
						binary = binary[l:]	
						continue
					out_file.write(i[1])
					binary = binary[l:]		
		
		out_file.write(out_str)
 
	# simply copying the file to bypass the actual test.
	# remove the below lines.
	#if input_file != "" and output_file != "":
	#	shutil.copyfile(input_file, output_file)
 
def get_options(args=sys.argv[1:]):
	parser = argparse.ArgumentParser(description="Huffman compression.")
	groups = parser.add_mutually_exclusive_group(required=True)
	groups.add_argument("-e", type=str, help="Encode files")
	groups.add_argument("-d", type=str, help="Decode files")
	parser.add_argument("-o", type=str, help="Write encoded/decoded file", required=True)
	options = parser.parse_args()
	return options
 
if __name__ == "__main__":
	options = get_options()
	if options.e is not None:
		encode(options.e, options.o)
	if options.d is not None:
		decode(options.d, options.o)

