from unittest import TestLoader, TextTestRunner
from multi_registry import tests

suite = TestLoader().loadTestsFromModule(tests)
TextTestRunner(verbosity = 2).run(suite)
