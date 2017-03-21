import pydoop.hdfs as hdfs
import os.path

class HadoopOperations():
    def __init__(self,host="default",port=0):
        self.handle=hdfs.hdfs(host,port)

    def create_directory(self,dir_name):
        if(dir_name==""):
            print "Blank directory!"
            return False
        hdfs.mkdir(dir_name)
        return True

    def file_exist(self,file_location_hdfs):
        if(file_location_hdfs)=="":
            print "File does not exist"
            return False
        if self.handle.exists(file_location_hdfs)==False:
            print "File does not exist"
            return False
        return True

    def get_data_from_hdfs(self,file_location_hdfs):
        if (self.file_exist(file_location_hdfs))==False:
            return -1
        data=hdfs.load(file_location_hdfs)
        return data

    def show_directory_contents(self,directory_location):
        if (self.file_exist(directory_location))==False:
            return False
        print hdfs.ls(directory_location)
        return True

    def copy_from_hdfs_to_local(self,src_hdfs_location,dest_local_location="../output/"):
        if src_hdfs_location=="":
            print "No source specified"
            return False
        elif self.handle.exists(src_hdfs_location)==False:
            print "File does not exist"
            return False
        hdfs.get(src_hdfs_location,dest_local_location)
        return True

    def remove_directory(self,hdfs_path):
        if (hdfs_path == ""):
            print "No directory specified to delete!"
            return False
        elif(self.file_exist(hdfs_path)==False):
            return False
        hdfs.rmr(hdfs_path)
        return True

    def copy_from_local_to_hdfs(self,src_local_location,dest_local_location):
        if(dest_local_location==""):
            print "Not a valid hdfs path"
            return False
        elif os.path.exists(src_local_location)==True:
            hdfs.put(src_local_location, dest_local_location)
            return True
        else:
            print "Local destination does not exist"
            return False