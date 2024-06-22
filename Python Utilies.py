### basic logging
import logging
import sys

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("debug.log"), logging.StreamHandler(sys.stdout)],
)

### to see all the properties of a class
import inspect

for i in inspect.getmembers(x):

    # to remove private and protected
    # functions
    if not i[0].startswith('_'):

        # To remove other methods that
        # doesnot start with a underscore
        if not inspect.ismethod(i[1]):
            print(i)

### pulling path to another file in same directory
import Path

base_path = str(Path(__file__).parent)
specific_path = base_path+"\\"+str(filenamehere)+".txt"