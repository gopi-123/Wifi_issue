import unittest
from unittest.mock import patch, MagicMock
from views_v2 import get_fpas_json_v2, Elasticsearch, exceptions

class TestGetFpasJsonV2(unittest.TestCase):
    @patch('views_v2.Elasticsearch')
    def test_get_fpas_json_v2(self, mock_elasticsearch):
        # Set up mock Elasticsearch client
        mock_search_result = {
            "aggregations": {
                "distinct": {
                    "buckets": [
                        {"key": "SP01"},
                        {"key": "SP02"}
                    ]
                }
            }
        }

        print("mock_elasticsearch.return_value",mock_elasticsearch.return_value)
        mock_es_instance = mock_elasticsearch.return_value
        mock_es_instance.search.return_value = mock_search_result

        # Call the function under test
        release_id = "7.4.0.b"
        machine_type = "World-Wide"
        result = get_fpas_json_v2(release_id, machine_type)

        # Assert the results
        expected_result = {
            "service_packs": ["SP02", "SP01"]
        }
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()