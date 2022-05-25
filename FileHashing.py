import os
import stat
import time
import hashlib
import argparse
import csv
import logging
import sys
from tkinter import filedialog
from tkinter import *

log = logging.getLogger('main._checkHash')
log.info("I'm here in _checkHash!")

# tkinter
win = Tk()
win.dirName = filedialog.askdirectory();

# add 0806 =========================
h_rootPath = win.dirName
h_reportPath = "./"
h_hashType = "SHA512"
csvFile = "fileSystemReport.csv"
###############################################################
# Name: WalkPath() Function

def WalkPath():

    processCount = 0
    errorCount = 0

    oCVS = _CSVWriter(h_reportPath+csvFile, h_hashType)

    # Create a loop that process all the files starting
    # at the rootPath, all sub-directories will also be processed

    log.info('Root Path: ' + h_rootPath)

    for root, dirs, files in os.walk(h_rootPath):

        # for each file obtain the filename and call the HashFile Function
        for file in files:

            fname = os.path.join(root, file)

            result = HashFile(fname, file, oCVS)

            print(result)

            # if hashing was successful then increment the ProcessCount
            if result is True:
                processCount += 1
            # if not sucessful, the increment the ErrorCount
            else:
                errorCount += 1


    oCVS.writerClose()

    return(processCount)

#End WalkPath==================================================

###############################################################
# Name: HashFile Function

def HashFile(theFile, simpleName, o_result):

    # Verify that the path is valid
    if os.path.exists(theFile):

        #Verify that the path is not a symbolic link
        if not os.path.islink(theFile):

            #Verify that the file is real
            if os.path.isfile(theFile):

                try:
                    #Attempt to open the file
                    f = open(theFile, 'rb')
                except IOError:
                    #if open fails report the error
                    log.warning('Open Failed: ' + theFile)
                    return
                else:
                    try:
                        # Attempt to read the file
                        rd = f.read()
                    except IOError:
                        # if read fails, then close the file and report error
                        f.close()
                        log.warning('Read Failed: ' + theFile)
                        return
                    else:
                        #success the file is open and we can read from it
                        #lets query the file stats

                        theFileStats =  os.stat(theFile)
                        (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(theFile)

                        #Print the simple file name
                        DisplayMessage("Processing File: " + theFile)
                        logging.info("Processing File: " + theFile)

                        # print the size of the file in Bytes
                        fileSize = str(size)

                        #print MAC Times
                        modifiedTime = time.ctime(mtime)
                        accessTime = time.ctime(atime)
                        createdTime = time.ctime(ctime)

                        ownerID = str(uid)
                        groupID = str(gid)
                        fileMode = bin(mode)

                        #process the file hashes

                        #Calculate and Print the SHA512
                        hash=hashlib.sha512()
                        hash.update(rd)
                        hexSHA512 = hash.hexdigest()
                        hashValue = hexSHA512.upper()

                        #File processing completed
                        #Close the Active File
                        print("================================");
                        f.close()

                        # write one row to the output file

                        o_result.writeCSVRow(simpleName, theFile, fileSize, modifiedTime, accessTime, createdTime, hashValue, ownerID, groupID, mode)

                        return True
            else:
                log.warning('[' + repr(simpleName) + ', Skipped NOT a File' + ']')
                return False
        else:
            log.warning('[' + repr(simpleName) + ', Skipped Link NOT a File' + ']')
            return False
    else:
            log.warning('[' + repr(simpleName) + ', Path does NOT exist' + ']')
    return False

# End HashFile Function ===================================

###############################################################
# Name: DisplayMessage() Function

def  DisplayMessage(msg):

    print(msg)
    logging.info(msg)

    return

#End DisplayMessage=====================================

###############################################################
# Class: _CSVWriter
#
# Methods  constructor:     Initializes the CSV File
#                writeCVSRow:   Writes a single row to the csv file
#                writerClose:      Closes the CSV File

class _CSVWriter:

    def __init__(self, fileName, hashType):
        try:
            # create a writer object and then write the header row
            self.csvFile = open(fileName, 'wb')
            self.writer = csv.writer(self.csvFile, delimiter=',', quoting=csv.QUOTE_ALL)
            self.writer.writerow( ('File', 'Path', 'Size', 'Modified Time', 'Access Time', 'Created Time', hashType, 'Owner', 'Group', 'Mode') )
        except:
            log.error('CSV File Failure')

    def writeCSVRow(self, fileName, filePath, fileSize, mTime, aTime, cTime, hashVal, own, grp, mod):
        self.writer.writerow((fileName, filePath, fileSize, mTime, aTime, cTime, hashVal, own, grp, mod))

    def writerClose(self):
        self.csvFile.close()


if __name__ == '__main__':

    CHECKHASH_VERSION = '1.0'

    # Turn on Logging
    logging.basicConfig(filename='checkHash.log',level=logging.DEBUG,format='%(asctime)s %(message)s')

    # Record the Starting Time
    startTime = time.time()

    # Record the Welcome Message
    logging.info('')
    logging.info('Welcome to checkHash version 1.0 ... New Scan Started')
    logging.info('')
    DisplayMessage('Wecome to checkHash ... version '+ CHECKHASH_VERSION)

    # Record some information regarding the system
    logging.info('')
    logging.info('System: '+ sys.platform)
    logging.info('')
    logging.info('Version: '+ sys.version)
    logging.info('')

    # Traverse the file system directories and hash the files
    filesProcessed = WalkPath()

    # Record the end time and calculate the duration
    endTime = time.time()
    duration = endTime - startTime

    logging.info('Files Processed: ' + str(filesProcessed) )
    logging.info('Elapsed Time: ' + str(duration) + ' seconds')
    logging.info('')
    logging.info('Program Terminated Normally')
    logging.info('')

    DisplayMessage("Program End")