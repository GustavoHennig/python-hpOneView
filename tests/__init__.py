import unittest
import pprint

# Implement assertIsNotNone for Python runtimes < 2.7 or < 3.1
if not hasattr(unittest.TestCase, 'assertIsNotNone'):
    def assertIsNotNone(self, value, *args):
        self.assertNotEqual(value, None, *args)

    unittest.TestCase.assertIsNotNone = assertIsNotNone

# Implement assertIsNone for Python runtimes < 2.6 or < 3.1
if not hasattr(unittest.TestCase, 'asertIsNone'):
    def assertIsNone(self, value, *args):
        self.assertEqual(value, None, *args)

    unittest.TestCase.assertIsNone = assertIsNone

# Implement assertIsInstance for Python runtimes < 2.6 or 3.1
if not hasattr(unittest.TestCase, 'assertIsInstance'):
    def assertIsInstance(self, obj, cls, msg=None):
        if not isinstance(obj, cls):
            if not msg or msg.isspace():
                msg = '%s is not an instance of %r' % (pprint.saferepr(obj), cls)
            self.fail(msg)

    unittest.TestCase.assertIsInstance = assertIsInstance
