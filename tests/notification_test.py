import unittest
from .mocks import MockNotification
from srvcheck.notification import Notification

class TestNotification(unittest.TestCase):
    def test_send(self):
        n = Notification('Test')
        mn = MockNotification({})
        n.addProvider(mn)
        n.send('Hello WorldS!')
        self.assertEqual(mn.events[0], 'Test Hello WorldS!')

    def test_sendPhoto(self):
        n = Notification('Test')
        mn = MockNotification({})
        n.addProvider(mn)
        n.sendPhoto('/tmp/test.jpg')
        self.assertEqual(mn.events[0], 'Sending photo: /tmp/test.jpg')

    def test_append(self):
        n = Notification('Test')
        mn = MockNotification({})
        n.addProvider(mn)
        n.append('Hello WorldA!')
        n.append('Hello WorldB!')
        n.flush()
        self.assertEqual(mn.events[0], 'Test Hello WorldA!\nTest Hello WorldB!')


    