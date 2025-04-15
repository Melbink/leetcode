 import unittest

# Assuming the optimized Logger class is defined as:
class Logger(object):
    def __init__(self):
        self.arr_mes = {}

    def shouldPrintMessage(self, timestamp, message):
        # Return a default value of -infinity if message isn't present.
        last_timestamp = self.arr_mes.get(message, -float('inf'))
        if timestamp - last_timestamp < 10:
            return False
        self.arr_mes[message] = timestamp
        return True

class TestLogger(unittest.TestCase):
    def test_first_occurrence(self):
        logger = Logger()
        # The first time "foo" appears, it should return True.
        self.assertTrue(logger.shouldPrintMessage(1, "foo"))
    
    def test_duplicate_too_soon(self):
        logger = Logger()
        logger.shouldPrintMessage(1, "foo")
        # A subsequent call within 10 seconds should return False.
        self.assertFalse(logger.shouldPrintMessage(2, "foo"))
    
    def test_duplicate_after_ten_seconds(self):
        logger = Logger()
        logger.shouldPrintMessage(1, "foo")
        # A call after 10 seconds have passed should return True.
        self.assertTrue(logger.shouldPrintMessage(11, "foo"))
    
    def test_multiple_messages(self):
        logger = Logger()
        # Different messages should not block each other.
        self.assertTrue(logger.shouldPrintMessage(1, "foo"))
        self.assertTrue(logger.shouldPrintMessage(2, "bar"))
        # The same message within 10 seconds should be blocked.
        self.assertFalse(logger.shouldPrintMessage(3, "foo"))
        self.assertFalse(logger.shouldPrintMessage(4, "bar"))
        # After 10 seconds, each message is allowed again.
        self.assertTrue(logger.shouldPrintMessage(11, "foo"))
        self.assertTrue(logger.shouldPrintMessage(12, "bar"))
    
    def test_no_overlap(self):
        logger = Logger()
        # Test a sequence of timestamps where messages don't overlap
        self.assertTrue(logger.shouldPrintMessage(1, "foo"))
        self.assertTrue(logger.shouldPrintMessage(12, "foo"))
        self.assertTrue(logger.shouldPrintMessage(23, "foo"))

if __name__ == '__main__':
    unittest.main()