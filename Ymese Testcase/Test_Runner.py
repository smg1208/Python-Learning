import unittest
import HtmlTestRunner
import os
from main import Fullpage_Protected_Test

# Get directory to export report file
dir = os.getcwd()

# Get all test case from class Fullpage_Protected_Test
main = unittest.TestLoader().loadTestsFromTestCase(Fullpage_Protected_Test)


# Create test_suite
test_suite = unittest.TestSuite([main])

# Open report file
output_file = open(dir + "\Protected Test.html", "w")

# Configure HtmlTestRunner options
runner = HtmlTestRunner.HTMLTestRunner(
    stream=output_file, report_title='Test report', descriptions='Acceptance Test')

# Run test_suite using html test runner
runner.run(test_suite)
