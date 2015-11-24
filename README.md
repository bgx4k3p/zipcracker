ZIPcracker
==============
ZIPcracker performs dictionary attack on password protected ZIP files. It uses multi-threading for faster performance.

Arguments
--------------

    $ python zipcracker.py -h
    usage: zipcracker.py [-h] [-f ZIPFILE] [-d DICTFILE]

    ZIP password cracker with multithreading

    arguments:
     -h, --help   show this help message and exit
     -f ZIPFILE   Specify ZIP file
     -d DICTFILE  Specify dictionary file


Usage Example
--------------

    $ python zipcracker.py -f evil.zip -d dictionary.txt
    The password is: secret

