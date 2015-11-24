#!/usr/bin/python
import zipfile
import argparse
from threading import Thread
import sys


# Function to extract password-protected ZIP file with a given password
def extractZIP(zFile, password):
    try:
        # Check if the password is correct and return it. The password needs to be converted to 'bytes'
        zFile.extractall(pwd=str.encode(password))

        print("The password is: " + password)
        return password

    except Exception as e:
        # Return to Main with incorrect password
        return


# Define main
def main():
    # Handle arguments
    parser = argparse.ArgumentParser(description="ZIP password cracker with multithreading")
    parser._optionals.title = "arguments"
    parser.add_argument("-f", action='store', help="Specify ZIP file", dest="zipFile")
    parser.add_argument("-d", action='store', help="Specify dictionary file", dest="dictFile")
    args = parser.parse_args()

    # Print Usage syntax if both ZIP file and dictionary file are not provided
    if args.zipFile is None or args.dictFile is None:
        parser.print_usage()
        sys.exit(1)

    else:
        try:
            # Open the ZIP file
            zipFile = zipfile.ZipFile(args.zipFile)

        except IOError as e:
            print('ZIP file \'' + args.zipFile + '\' does not exist!')
            parser.print_usage()
            sys.exit(1)

        try:
            # Open the Dictionary file in read mode
            passFile = open(args.dictFile, 'r')

        except IOError as e:
            print('Dictionary file \'' + args.dictFile + '\' does not exist!')
            parser.print_usage()
            sys.exit(1)

        # Check each line in the dictionary file
        for line in passFile.readlines():

            # Strip newline characters
            password = line.strip('\n')

            # Create new thread and call the extractZIP function
            t = Thread(target=extractZIP, args=(zipFile, password))
            t.start()

# Execute main
if __name__ == '__main__':
    main()
