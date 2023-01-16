# a script to start a new test
import os
import sys


def addMoreImports(argc, argv):
    # find the -i flag and add the given import(s) to the imports list
    global IMPORTS
    pos_i = -1
    try:
        pos_i = argv.index("-i", 1)
    except:
        pass

    if pos_i == -1:
        return
    assert pos_i + 1 < argc, "Usage: python new-test.py <test-name> -i <import1> <import2> ..."
    for i in range(pos_i + 1, argc):
        IMPORTS.append(argv[i])


def makeTestClass(testName):
    return ""\
        f"class {TEST_NAME}(unittest.TestCase):\n"\
        "    def setUp(self):\n"\
        "        pass\n"\
        "\n"\
        "    def tearDown(self):\n"\
        "        pass\n"\
        "\n"\
        "    def test(self):\n"\
        "        pass\n"\
        "\n"\
        "\n"


def makeMainFunction():
    return ""\
        "def main():\n"\
        "    # run the tests\n"\
        "    unittest.main()\n"\
        "    return\n"\
        "\n"\
        "\n"\
        "if __name__ == '__main__':\n"\
        "    main()\n"\
        "\n"


def makeData():
    # make the data string
    global DATA

    # add the imports
    for i in IMPORTS:
        DATA += f"import {i}\n"
    DATA += "\n"

    # add the test class
    DATA += makeTestClass(TEST_NAME)

    # add the main function
    DATA += makeMainFunction()


def main(argc, argv):
    assert argc >= 2, "Usage: python new-test.py <test-name>"
    # make a new .test.py file with given name in this dir with following imports
    # # import the necessary packages
    # import unittest
    # import os, sys
    # import time

    global TEST_NAME
    global IMPORTS
    global DATA

    DATA = ""
    IMPORTS = [
        "unittest",
        "os", "sys",
        "time"
    ]

    TEST_NAME = argv[1]
    # if -i flag is given, add the given import(s) to the imports list
    addMoreImports(argc, argv)

    makeData()

    # create the new test file
    try:
        with open(TEST_NAME + ".test.py", "x") as f:
            f.write(DATA)
    except Exception as e:
        # overwrite the file if it already exists
        # ask for confirmation
        isOk = input(
            f"File {TEST_NAME}.test.py already exists. Overwrite? (y/n): ")
        isOk.strip()

        if isOk[0] != "y":
            exit(1, "Aborted")
        else:
            # overwrite the file
            with open(TEST_NAME + ".test.py", "w") as f:
                f.write(DATA)
    return


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
