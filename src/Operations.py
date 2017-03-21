import subprocess

class Operations():
    def runProcess(self,command):
        subprocess.call(command, shell=True)

    def stringIndexerMapping(self, indexed_dataframe, column1, column2):
        #retrieve the correspondences between the generated index values and the original strings
        indexed_dataframe.select(column1, column2).distinct().show()
