import unittest
from mas.a2a import Bus, Message

class TestA2A(unittest.TestCase):
    def test_message_creation(self):
        msg = Message(topic="test", payload={"data": 123})
        self.assertEqual(msg.topic, "test")
        self.assertEqual(msg.payload["data"], 123)
        self.assertTrue(len(msg.id) > 0)

    def test_pub_sub(self):
        bus = Bus()
        received = []
        
        def callback(msg):
            received.append(msg)

        bus.subscribe("alerts", callback)
        
        msg1 = Message(topic="alerts", payload={"severity": "high"})
        msg2 = Message(topic="logs", payload={"info": "ignore me"})
        
        bus.publish(msg1)
        bus.publish(msg2)
        
        self.assertEqual(len(received), 1)
        self.assertEqual(received[0].payload["severity"], "high")

    def test_wildcard_sub(self):
        bus = Bus()
        received = []
        
        bus.subscribe("*", lambda m: received.append(m))
        
        bus.publish(Message(topic="A"))
        bus.publish(Message(topic="B"))
        
        self.assertEqual(len(received), 2)

if __name__ == '__main__':
    unittest.main()
