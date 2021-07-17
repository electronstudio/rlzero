import sys
from rlzero import *

def main():
    file = sys.argv[1]
    print(file)
    #file_text = "from rlzero import *\n"
    file_text = open(file).read()
    #file_text += "\nrun()\n"
    print("\nMAIN1")
    exec(file_text, globals())
    run(sys.modules[__name__])

