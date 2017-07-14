import logging

l = logging.getLogger('file b')

class B():
    @classmethod
    def helloworld(cls):
        l.debug("Should not print out in file b")
        l.setLevel(logging.DEBUG)
        l.info("Should print out in file b")
        l.debug("Should not print out in file b")
        print(__file__)

