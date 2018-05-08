from unittest import TestCase
from src.HadoopOperations import HadoopOperations
import os
import glob

class HadoopOperationsTest(TestCase):

    def setUp(self):
        self.hadoopoperations=HadoopOperations()

    def tearDown(self):
        files = glob.glob('../output/*')
        for f in files:
            os.remove(f)

    def test_show_content(self):
        self.hadoopoperations.show_directory_contents("")
        self.hadoopoperations.show_directory_contents("/user/hadoop")

    def test_get_data(self):
        data=self.hadoopoperations.get_data_from_hdfs("/user/hadoop/test/hello.txt")
        if data==-1:
            print "error with path"
        else:
            print data
        data = self.hadoopoperations.get_data_from_hdfs("/user/hadoop/test/yuiop.txt")
        if data == -1:
            print "error with path"

    def test_create_remove_directory(self):
        self.hadoopoperations.create_directory("")
        self.hadoopoperations.create_directory("lol")   #by default creates in /user/hadoop

        self.hadoopoperations.remove_directory("")
        self.hadoopoperations.remove_directory("/user/hadoop/lol")

    def test_hdfs_to_local(self):
        self.hadoopoperations.copy_from_hdfs_to_local("/user/hadoop/test/hello.txt")    #by default copies to output folder
        self.hadoopoperations.copy_from_hdfs_to_local("")

    def test_local_to_hdfs(self):
        self.hadoopoperations.remove_directory("/hello.txt")
        self.hadoopoperations.copy_from_local_to_hdfs("../output/hello.txt","")
        self.hadoopoperations.copy_from_local_to_hdfs("","")
        self.hadoopoperations.copy_from_local_to_hdfs("../output/hey.txt","/")
        self.hadoopoperations.copy_from_local_to_hdfs("../output/hello.txt","/")
        self.hadoopoperations.remove_directory("/hello.txt")

    def test_remove(self):
        self.hadoopoperations.remove_directory("/user/hadoop/test.copy")
        self.hadoopoperations.remove_directory("/user/hello.txt")
