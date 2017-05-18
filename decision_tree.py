#!/usr/bin/evn python

import sys
import decision_tree.analyze as analyze

		
def main():
	"""Starts program"""
	prune = False
	if len(sys.argv) == 5:
		prune = (not not sys.argv[2])
		analyzer = analyze.Analyzer(sys.argv[1], prune, sys.argv[3], sys.argv[4])
	else:
		analyzer = analyze.Analyzer(sys.argv[1], False, sys.argv[2], sys.argv[3])

	analyzer.analyze()

if __name__ == '__main__':
	main()