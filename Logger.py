
class Logger:
    def __init__(self, filepath):
        self.File = open(filepath,'w')
    def log(self,s):
        print(s)
        self.File.write(str(s) + str('\n'))
    def stop(self):
        self.File.close()