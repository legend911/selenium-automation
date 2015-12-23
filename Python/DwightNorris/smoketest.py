import os
import unittest
import HTMLTestRunner

from navigation2 import Navigation2
from navigation import Navigation
from about import About
from about2 import About2

# get the directory path to the output file
dir = os.getcwd()

# get all the tests from both classes
navigation = unittest.TestLoader().loadTestsFromTestCase(Navigation)
navigation2 = unittest.TestLoader().loadTestsFromTestCase(Navigation2)
about = unittest.TestLoader().loadTestsFromTestCase(About)
about2 = unittest.TestLoader().loadTestsFromTestCase(About2)

# create a test suite
smoke_test = unittest.TestSuite([navigation, navigation2, about, about2])

# open the report file
outfile = open(dir + "\\reports\SmokeTestReport.html", "w")

# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(
    stream = outfile,
    title = 'Test Report',
    description = 'Smoke Test'
)

# run the tests
runner.run(smoke_test)