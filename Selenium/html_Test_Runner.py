import unittest
import HtmlTestRunner
import os
from dmx import DMXTest
from assertion_test_script import HomePageTest

# Get directory to export report file
dir = os.getcwd()

# Get all test case from other test case module
dmx = unittest.TestLoader().loadTestsFromTestCase(DMXTest)
home_page = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# Create test_suite
test_suite = unittest.TestSuite([home_page, dmx])

# Open report file
outfile = open(dir + 'html_Test_Runner_Example.html', "w")

# Configure HtmlTestRunner options
runner = HtmlTestRunner.HTMLTestRunner(
    stream=outfile, report_title='Test report', descriptions='Acceptance Test')

# Run suite using html test runner
runner.run(test_suite)
