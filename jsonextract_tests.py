import unittest
from jsonextract import summarize_repo_info

class TestSummaryFunction(unittest.TestCase):
    # Mock data simulating a real GitHub API response
    def test_summary_output_contains_expected_fields(self):
        mock_data = {
            "full_name": "nodejs/node",
            "description": "Node.js runtime",
            "stargazers_count": 99999,
            "forks_count": 25000,
            "open_issues_count": 1000,
            "watchers_count": 5000,
            "license": {"name": "MIT"},
            "default_branch": "main",
            "updated_at": "2024-06-30T00:00:00Z"
        }

        # Call the function to test
        result = summarize_repo_info(mock_data)

        # Assert some expected content is present
        self.assertIn("nodejs/node", result)
        self.assertIn("Stars: 99999", result)
        self.assertIn("License: MIT", result)

# Allows the test to run when executed directly
if __name__ == "__main__":
    unittest.main()
