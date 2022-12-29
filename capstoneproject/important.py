[10:49 am, 03/12/2022] suresh Hcl: import os
import re
import win32api
import UploadFiles
import concurrent.futures

# Class FindFileLocation is used to search for a file in our local drives by using multi-threading
# This class then calls UploadFilesToDB to store file search results in sql db
class FindFileLocation:

    # Method find_file is used to search for a file in our local drive
    # Input: This method accepts drive and filename as parameter
    def find_file(self, root_folder, rex):
        for root, dirs, files in os.walk(root_folder):
            for f in files:
                result = rex.search(f)
                if result:
                    print("File name: {} - File location: {}".format(f, root))
                    #print("File location: {}".format(root))
                    # call to method insert_file_search_results to upload file search results to db
                    self.insert_file_search_results(root, f, 0)
                    break  # if you want to find only one

    # Method find_file_in_all_drives is used to get all the available drives in our local system/VM
    def find_file_in_all_drives(self, file_name):
        # create a regular expression for the file
        rex = re.compile(file_name)

        drives = [drivestr for drivestr in  win32api.GetLogicalDriveStrings().split('\000')[:-1]]
        print(drives)
        # concurrency call to acheive multi-threading
        with concurrent.futures.ThreadPoolExecutor() as executor:
            [executor.submit(self.find_file, drive, rex) for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]]

    # Method insert_file_search_results is used to  call method upload_file_results_todb which is in class UploadFilesToDB
    def insert_file_search_results(self, fileLocation, fileName, searchCount = 0):
        uploadObject.upload_file_results_todb(fileName, fileLocation, searchCount)

    # Method search_forfile_indb is used to search file results in db.
    # input: accepts filename as input
    # this method internally call method search_in_db_for_file which is in class UploadFilesToDB
    def search_forfile_indb(self, fileName):
        # call method search_in_db_for_file to search for a file result in db
        uploadObject.search_in_db_for_file(fileName)
        print("File search results from local drive")
        self.find_file_in_all_drives(fileName)

# required objects of class
locationObject = FindFileLocation()
locationObject.find_file_in_all_drives("newFile.txt")
uploadObject = UploadFiles.UploadFilesToDB()
fileToSearch = input()
locationObject.search_forfile_indb(fileToSearch)
