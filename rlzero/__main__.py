import sys
from rlzero import *

file = sys.argv[1]
print(file)
#file_text = "from rlzero import *\n"
file_text = open(file).read()
#file_text += "\nrun()\n"
exec(file_text)
run()