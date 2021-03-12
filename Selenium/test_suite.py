import unittest
from dmx import DMXTest
from assertion_test_script import HomePageTest

# Get all test from DMXTest and HomePageTest
dmx = unittest.TestLoader().loadTestsFromTestCase(DMXTest)
home_page = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# Create Testsuite from test case
test_suite = unittest.TestSuite([home_page, dmx])

# Run the suite above
unittest.TextTestRunner(verbosity=2).run(test_suite)
