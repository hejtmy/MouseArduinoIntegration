class Experiment:
    name = "Nice experiment"
    ##set up experiment parametres, initialize variables

    def __init__(self, initLag = None, imgLag = None, finishLag = None, repeat = None):
        self.initLag
        self.imgLag
        self.finishLag
        self.repeat

###PROPERTIES
    @property
    def initLag(self):
        return self.__initLag

    def imgLag(self):
        return self.__imgLag

    def finishLag(self):
        return self.__finishLag

    def repeat(self):
        return self.__repeat

    @initLag.setter
    def initLag(self, initLag):
        #if --- raise exception
        self.__initLag = 5

    @imgLag.setter
    def imgLag(self, imgLag):
        #if --- raise exception
        self.__imgLag = imgLag

    @finishLag.setter
    def finishLag(self, finishLag):
        #if --- raise exception
        self.__finishLag = finishLag

    @repeat.setter
    def repeat(self, repeat):
        #if --- raise exception
        self.__repeat = repeat


    def setup(self):
        try:
            self.initLag = input("Duration of PHASE 1 (seconds): ")
            self.imgLag = input("Duration of PHASE 2 (seconds): ")
            self.finishLag = input("Duration of PHASE 3 (seconds): ")
            self.repeat = input("Enter number of repetitions: ")
        except Exception as ex:
            print(ex)