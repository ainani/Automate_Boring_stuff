#!/usr/bin/python

import zipfile
import sys

def zip_file_obj(archive_name):
    try:
        testZip = zipfile.ZipFile(archive_name)
        return testZip
    except IOError as e:
        print "IOError: ", e
        sys.exit()

def list_archive(testZip):
    print testZip.namelist()

def file_info(file_name):
    try:
        info = testZip.getinfo(file_name)
        print info.file_size
    except KeyError as e:
        print "EXCEPTION: ", e

if __name__ == "__main__":
    testZip = zip_file_obj('test.zip')
    list_archive(testZip)
    file_info('test1.txt')
    file_info('test5.txt')       # test5.txt is not present in list of archive, so an exception will be raised
    file_info('test3/')
    file_info('test3/test4/test5.txt')
