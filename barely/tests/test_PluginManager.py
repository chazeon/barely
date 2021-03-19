import os
import unittest
from mock import patch
from unittest.mock import MagicMock
from barely.plugins import PluginBase
from barely.plugins.PluginManager import PluginManager


class TestPluginBase(unittest.TestCase):

    def test_register(self):
        plugin = PluginBase()
        registration_info = plugin.register()
        self.assertTupleEqual(("Base", -1, []), registration_info)

    def test_action(self):
        plugin = PluginBase()
        golden_item = {
            "test": "dict"
        }

        test_item = plugin.action(item=golden_item)
        test_noitem = plugin.action(True)

        self.assertDictEqual(golden_item, test_item)
        self.assertIsNone(test_noitem)


class TestPluginManager(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        with patch.object(PluginManager, "__init__", lambda x: None):
            self.PM = PluginManager()

        os.chdir("PluginManager")

    @classmethod
    def tearDownClass(self):
        os.chdir("..")

    def test_discover_plugins(self):
        # Content Plugins register with filetypes and a priority
        test_dict = self.PM.discover_plugins(["content"])

        self.assertEqual(3, len(test_dict))
        self.assertIn("md", test_dict)
        self.assertIn("pdf", test_dict)
        self.assertIn("png", test_dict)

        self.assertEqual(1, len(test_dict["md"]))
        self.assertTrue(issubclass(test_dict["md"][0], PluginBase))

        self.assertEqual(2, len(test_dict["png"]))
        self.assertTrue(issubclass(test_dict["png"][0], PluginBase))
        self.assertTrue(issubclass(test_dict["png"][1], PluginBase))

        self.assertTrue(test_dict["png"][0]().register()[0] == "P2")
        self.assertTrue(test_dict["png"][1]().register()[0] == "P1")

        self.assertEqual(1, len(test_dict["pdf"]))
        self.assertTrue(issubclass(test_dict["pdf"][0], PluginBase))

        # Backup/Publication Plugins only register with their class
        test_list = self.PM.discover_plugins(["other"], type_content=False)
        self.assertEqual(2, len(test_list))
        self.assertTrue(issubclass(test_list[0], PluginBase))
        self.assertTrue(issubclass(test_list[1], PluginBase))
        self.assertTrue(test_list[0]().register()[0] == "P4")
        self.assertTrue(test_list[1]().register()[0] == "P3")

    def test_hook_content(self):
        # Sample Item, to be processed by plugins registered for the "test" extension
        item = {
            "extension": "test"
        }

        # The first sample plugin returns 2 items for every input item, merely duplicating it
        sample_plugin1 = PluginBase()
        sample_plugin1.action = MagicMock(return_value=[item, item])

        # The second plugin is the constant 1-function
        sample_plugin2 = PluginBase()
        sample_plugin2.action = MagicMock(return_value=1)

        # Both plugins are "registered" for the test extension
        self.PM.plugins_content = {
            "test": [sample_plugin1, sample_plugin2]
        }

        # The hook should return two "1"s.
        returned_content = self.PM.hook_content(item)
        self.assertEqual([1, 1], returned_content)

    def test_hook_backup(self):
        sample_plugin = PluginBase()
        sample_plugin.action = MagicMock()

        self.PM.plugins_backup = [sample_plugin]

        self.assertFalse(sample_plugin.action.called)
        self.PM.hook_backup()
        self.assertTrue(sample_plugin.action.called)

    def test_hook_publication(self):
        sample_plugin1 = PluginBase()
        sample_plugin1.action = MagicMock()

        sample_plugin2 = PluginBase()
        sample_plugin2.action = MagicMock()

        self.PM.plugins_publication = [sample_plugin1, sample_plugin2]

        self.assertFalse(sample_plugin1.action.called)
        self.assertFalse(sample_plugin2.action.called)
        self.PM.hook_publication()
        self.assertTrue(sample_plugin1.action.called)
        self.assertTrue(sample_plugin2.action.called)
