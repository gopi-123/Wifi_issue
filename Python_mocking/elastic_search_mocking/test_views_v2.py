import unittest
from unittest.mock import patch, MagicMock
import os
from views_v2 import get_fpas_json_v2

class TestGetFpasJson(unittest.TestCase):
    @patch('views_v2.Elasticsearch')  # Patch the Elasticsearch class
    @patch('views_v2.get_sp_list_with_release_date')  # Patch the get_sp_list_with_release_date function
    def test_get_fpas_json_v2(self, mock_get_sp_list_with_release_date, mock_elasticsearch):
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
        mock_es_instance = mock_elasticsearch.return_value
        mock_es_instance.search.return_value = mock_search_result

        # Set up mock get_sp_list_with_release_date function
        mock_get_sp_list_with_release_date.return_value = [
            {"SP01": {"released": True, "release_date": "2024-01-01"}},
            {"SP02": {"released": False, "release_date": "2024-01-02"}}
        ]

        # Call the function under test
        release_id = "7.4.0.b"
        machine_type = "World-Wide"
        result = get_fpas_json_v2(release_id, machine_type)

        # Assert the results
        expected_result = {
            "service_packs": [
                {"SP01": {"released": True, "release_date": "2024-01-01"}},
                {"SP02": {"released": False, "release_date": "2024-01-02"}}
            ]
        }
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
