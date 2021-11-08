import sys

 
sys.argv.remove(sys.argv[0])
sys.argv = sys.argv[::-1]
 
for str1 in sys.argv:
	if str1 != sys.argv[-1]:
		print(str1[::-1].swapcase(), end=" ")
	else:
		print(str1[::-1].swapcase())

