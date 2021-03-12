import unittest
import HtmlTestRunner
import os
from main import Fullpage_Protected_Test

# Get directory to export report file
dir = os.getcwd()

# Get all test case from other test case module
main = unittest.TestLoader().loadTestsFromTestCase(Fullpage_Protected_Test)


# Create test_suite
test_suite = unittest.TestSuite([main])

# Open report file
output_file = open(dir + '/Protected Test.html', "w")

# Configure HtmlTestRunner options
runner = HtmlTestRunner.HTMLTestRunner(
    stream=output_file, report_title='Test report', descriptions='Acceptance Test')

# Run suite using html test runner
runner.run(test_suite)
