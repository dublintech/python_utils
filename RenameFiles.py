'''
Created on 5 Jan 2013

This module contains some utilities for renameing file.
The motivation for this was to help me sort out video files before backing them up.

The functions here were for my files.  I put in some extra conditions to make sure I was only 
renaming files I wanted to. You should tweek for your own needs.

In all the renaming functions, I have commented out the line of code which does the renaming.
Double check your renaming is as expected before commenting this line back in.

@author: Alex
'''
import os
import time
from datetime import date
from datetime import datetime


rootDirectory = 'C:\\Users\\Alex\\Videos\\Camcorder23Oct\\SD_VIDEO\\PRG001';

def main():
    rename_files_in_directory_using_last_updatetime(rootDirectory);

    
'''
Purpose of this function is to rename files in a specified directory so that they take 
the name of parent directory and then an increment counter at end.

Result should be:
--myfolder
    -- myfolder1.MOD
    -- myfolder2.MOD
    
Idea is for video files. 1st release works just with .MOD files.

'''
def rename_files_based_on_parent_dir(rootDir=rootDirectory):
    for root, dirs, files in os.walk(rootDir, topdown='true'):
        for filename in files:
            ext = os.path.splitext(file)[-1].lower();
            if (ext == '.mod'):
                folder = os.path.relpath(root, rootDir);
                # just to be careful - only check specific folders.
                if (filename.startswith('Camcorder') and folder.startswith('2')):
                    # In this specific case, I pull out some of the olf file name
                    # I could have used a counter and done... counter+=1;
                    newfilename = folder + '_' + filename[-5:];
                    print('Renaming file %s to %s' % (filename, newfilename))
                    # ******************************************************
                    # ******************************************************
                    #Commenting out rename so you have to comment it back in!
                    # os.rename(root + '\\' +  file, root + '\\' + newfilename);


'''
Renames files in a directory that have .mod extension to be of the form 
YEAR_MONTH_DAY_TIME_COUNTER_VALUE, where the datetime is last modified datetime
of the file. The idea is here that it is much easier to sort your media files if they are
named by timestamp of when they were taken rather than some arbitrary name. It also makes it easier 
to sort them and back them up
'''
def rename_files_in_directory_using_last_updatetime(rootDir=rootDirectory):
    for root, dirs, files in os.walk(rootDir, topdown='true'):
        counter = 1;
        for filename in files:
            ext = os.path.splitext(filename)[-1].lower();
            if (ext == '.mod'):
                statbuf = os.path.getmtime(root + '\\' + filename)
                t = datetime.fromtimestamp(statbuf);
                counter += 1;
                # Some good tips on time formats here: http://www.tutorialspoint.com/python/time_strptime.htm
                newfilename = t.strftime("%Y-%m-%d-%H-%M-%S_" + str(counter))
                print('Renaming file %s to %s' % (filename, newfilename))
                #os.rename(root + '\\' +  filename, root + '\\' + newfilename);
                
                
if __name__ == '__main__':
    main();