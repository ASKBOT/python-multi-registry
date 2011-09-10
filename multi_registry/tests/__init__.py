import unittest
from multi_registry import MultiRegistry
from multi_registry.tests import settings1
from multi_registry.tests import settings2

class MultiRegistryTests(unittest.TestCase):

    def init_from_modules(self):
        return MultiRegistry(settings1, settings2)

    def test_init_from_modules(self):
        r = self.init_from_modules()
        self.assertEqual(len(r.registry_stores), 2)
        return r

    def test_init_by_appending(self):
        r = MultiRegistry()
        r.append(settings1)
        r.append('multi_registry.tests.settings2')
        self.assertEqual(r.registry_stores[0], settings1)
        self.assertEqual(r.registry_stores[1], settings2)

    def test_init_by_inserting(self):
        r = MultiRegistry()
        r.append(settings1)
        r.insert(0, 'multi_registry.tests.settings2')
        self.assertEqual(r.registry_stores[1], settings1)
        self.assertEqual(r.registry_stores[0], settings2)
        self.assertEqual(r.ONE, '21')

    def test_init_from_paths(self):
        r = MultiRegistry(
            'multi_registry.tests.settings1',
            'multi_registry.tests.settings2'
        )
        self.assertEqual(len(r.registry_stores), 2)

    def test_append_order(self):
        r = self.init_from_modules()
        self.assertEqual(r.registry_stores[1], settings2)

    def test_values_order(self):
        r = self.init_from_modules()
        self.assertEqual(r.ONE, '11')
        self.assertEqual(r.THREE, '23')
