import logging 
from logging-b import B

l = logging.getLogger('file a')
logging.basicConfig()
l.setLevel(logging.INFO)

l.info("Here I am in a")


B.helloworld()

l.info("At the end of a")
l.debug("At the end of a")
