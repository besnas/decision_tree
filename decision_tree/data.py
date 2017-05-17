import csv
import random


class Samples:
	def __init__(self, file_name):
		"""reads in the sample data"""
		self.data = []
		self.binaryClass = []
		self.attrs = {}
		self.attr_changed = {0:[0,1,2,3], 1:[0,1,2,3], 2:[0,1,2,3], 3:[0,1,2], 4:[0,1,2], 5:[0,1,2]}
		self.new_data = []

		for row in csv.reader(open(file_name, 'rb')):
			self.data.append(row)
			for i in range(len(row) - 1):
				if self.attrs.get(i):  # if attr exists
					if not row[i] in self.attrs[i]:  # if there's no such attr
						self.attrs[i].append(row[i])
				else:
					self.attrs[i] = [row[i]]
		print self.attrs

	def convert_to_num(self):
		"""converts data attr to numbers"""
		used_data = self.data
		random.shuffle(used_data)

		index = 0
		new_data = []
		last_data = []
		for row in used_data:
			if row[-1] == "unacc":
				self.binaryClass.append("unacc")
			else:
				self.binaryClass.append("good")
			z = 0
			i = 0
			while i < len(row) - 1:
				#print row[i]
				k = 0
				while k < (len(self.attrs[i])):
					# print self.attrs[i][k]
					if row[i] == self.attrs[i][k]:
						index = k
					k += 1
				# print index
				new_data.append(index)
				i += 1
			# print new_data
			last_data.append(new_data)
			new_data = []
			z += 1
		# print last_data
		return last_data

	def attributes(self):
		"""attributes linked to their values"""
		return self.attrs

	def binary_class(self):
		"""binary class"""
		return self.binaryClass

	def data_r(self):
		"""data returns"""
		return self.data

	def random_split(self):
		"""creates random splits of the data"""
		used_data =self.data
		random.shuffle(used_data)
		middle = 3 * len(used_data) / 4
		return (used_data[0:middle], used_data[middle:])
