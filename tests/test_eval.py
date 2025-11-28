import json
import pytest
from agents.network_scanner import NetworkScanner
from tools.mock_network import MockNetwork

def test_network_scanner_golden_set():
    """
    Simulates 'adk eval' by running the NetworkScanner against a golden dataset.
    """
    # Load Golden Set
    with open("tests/golden_dataset.json", "r") as f:
        dataset = json.load(f)

    # Initialize Agent
    agent = NetworkScanner(use_mock=True)
    
    print(f"\nRunning Evaluation for {dataset['eval_set_id']}...")
    
    for case in dataset["eval_cases"]:
        print(f"  Running Case: {case['eval_id']}")
        
        # Run Agent
        # Note: NetworkScanner.scan takes 'target_network' as arg.
        # We need to parse the input or just pass the target directly for this unit test.
        # For simplicity, we extract the target from the input string manually here.
        target = case["input"].split(" ")[-1]
        
        result = agent.scan(target_network=target)
        
        # Verify Output
        result_str = str(result)
        for expected in case["expected_output_contains"]:
            assert expected in result_str, f"Expected '{expected}' in output for {case['eval_id']}"
            
        print(f"  ✅ Case {case['eval_id']} Passed")

if __name__ == "__main__":
    test_network_scanner_golden_set()
