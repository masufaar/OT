import unittest
import unittest
from google_local.adk.agents import Agent, Model, Tool
from google_local.adk.tools import google_search

class MockModel(Model):
    def generate_content(self, prompt: str) -> str:
        return "Mock Response"

class TestAgent(Agent):
    def run(self, input_text: str, context: dict = None) -> str:
        return f"Processed: {input_text}"

class TestADK(unittest.TestCase):
    def test_agent_initialization(self):
        agent = TestAgent(name="TestBot", instruction="Do testing")
        self.assertEqual(agent.name, "TestBot")
        self.assertEqual(agent.instruction, "Do testing")
        self.assertEqual(agent.tools, [])

    def test_tool_addition(self):
        agent = TestAgent(name="TestBot", instruction="Do testing")
        t = Tool(name="my_tool", func=lambda x: x, description="test tool")
        agent.add_tool(t)
        self.assertEqual(len(agent.tools), 1)
        self.assertEqual(agent.tools[0].name, "my_tool")

    def test_model_integration(self):
        model = MockModel()
        agent = TestAgent(name="TestBot", instruction="Do testing", model=model)
        response = agent.model.generate_content("Hello")
        self.assertEqual(response, "Mock Response")

if __name__ == '__main__':
    unittest.main()
