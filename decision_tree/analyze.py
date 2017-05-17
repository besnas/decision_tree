import data
import tree
import csv

class Analyzer:
	def __init__(self, file_name, prune, firstA, secondA):
		self.samples = data.Samples(file_name)
		self.builder = tree.Builder()
		self.file_name = file_name.split('/')[-1]
		self.prune = prune
		self.firstAttr = int(firstA)
		self.secondAttr = int(secondA)
		print self.secondAttr
		if prune:
			print "With pruning!"
	
	def analyze(self):
		"""calculates averages for correctly classified and node count"""
		
		"""generate sample sets"""
		samples, length = [], 0
		#for i in range(10):
		(tr, te) = self.samples.random_split()
		samples.append((tr, te))
		data_set = self.samples.data_r()
		binary_class = self.samples.binary_class()
		#print binary_class[2]
		length = len(tr)
		length2 = len(te)
		print length2
		self.samples.binary_class()



		step = self.step(length)
		
		"""calculate averages"""
		counts, node_counts, averages, average_nodes, per, total = {}, {}, {}, {}, {}, 0
		for i in step:
			print i
			for sample in samples:
				if not counts.get(i):
					counts[i] = 0
				if not node_counts.get(i):
					node_counts[i] = 0
				(tr, te) = sample
				tree = self.builder.build(tr[0:i], self.samples.attributes(), self.prune)
				counts[i] += self.test(tree, te)
				node_counts[i] += tree.number_of_nodes()
				total = len(te)
				#print counts
			averages[i] = counts[i] / float(len(samples) * total)
			average_nodes[i] = node_counts[i] / float(len(samples))
			per[i] = self.test(tree, te) / float(length2)
			print  per[i]
			self.write(averages, average_nodes, per)

		#plot graphics
		attr_changed = []
		class_changed = []
		attr_changed = self.samples.convert_to_num()
		class_changed = self.samples.binary_class()
		chart = []
		i =0
		while i < len(self.samples.attributes()[self.secondAttr]):
			chart.append([0]*len(self.samples.attributes()[self.firstAttr]))
			i+=1
		k =0

		#print class_changed
		k=0
		#for row in attr_changed:
		for k in range(100):
			if class_changed[k] == "unacc":
				chart[attr_changed[k][self.secondAttr]][attr_changed[k][self.firstAttr]] = "X"
			else:
				chart[attr_changed[k][self.secondAttr]][attr_changed[k][self.firstAttr]] = "O"
			#k+=1
		for row in chart:
			print row



	
	def write(self, ave, node_ave, per):
		"""outputs averages"""
		file_name = "output/correct_averages_%s" % (self.file_name)
		if self.prune:
			file_name = "output/pruned_correct_averages_%s" % (self.file_name)
		w = csv.writer(open(file_name, 'wb'), dialect='excel')
		for k in sorted(ave.keys()):
			w.writerow([k, ave[k]])
		
		file_name = "output/node_averages_%s" % (self.file_name)
		if self.prune:
			file_name = "output/pruned_node_averages_%s" % (self.file_name)
		w = csv.writer(open(file_name, 'wb'), dialect='excel')
		for k in sorted(node_ave.keys()):
			w.writerow([k, node_ave[k]])

		file_name = "output/percents_%s" % (self.file_name)
		w = csv.writer(open(file_name, 'wb'), dialect='excel')
		for k in sorted(per.keys()):
			w.writerow([ per[k]])
					
	def test(self, tree, tests):
		"""compares expected with actual values"""
		count = 0
		for test in tests:
			if test[-1] == tree.choose(test):
				count += 1
		return count
	
	def step(self, length):
		"""generates the steps to iterate over"""
		"""does every 5 starting at 5, 1, and n if its not a multiple of 5"""
		step = [i for i in range(50, length, 50)]
		step.insert(0, 1)
		if length % 50 != 0:
			step.append(length)
		print step
		return step
			