# Code inspired by http://dropbearcode.blogspot.hk/2011/09/multiple-file-latex-diff.html

import sys, os

flattened = ''

def shouldFlatten(line):
	line = line.strip()
	if line.startswith('\include{') and line.endswith('}'):
		return True
	if line.startswith('\input{') and line.endswith('}'):
		return True
	return False


def flattenLatex( rootFilename ):
	dirpath, filename = os.path.split(rootFilename)
	with open(rootFilename,'r') as fh:
		for line in fh:
			match = shouldFlatten(line)
			if match:
				newFile = line[line.find('{')+1:line.find('}')]
				if not newFile.endswith('tex'):
					newFile += '.tex'
				newdir = os.path.join(dirpath,newFile)

				# handle duplicate directory, if any
				folder,fname = os.path.split(dirpath)
				nestedFolder = '' if '/' not in newFile else newFile[:newFile.find('/')]
				if fname == nestedFolder:
					newdir = os.path.join(folder, newFile)

				# recursively flatten tex files
				flattenLatex( newdir)
			else:
				global flattened
				flattened += line + '\n'

if __name__ == "__main__":
	# The first argument is the path to the main tex file
	flattenLatex( sys.argv[1] )
	# The second argument is the path to the output flattened tex file
	with open(sys.argv[2],'w') as difffile:
		difffile.write(flattened)

