import unittest
from unittest.mock import patch
from views_v2 import get_sp_list_with_release_date

class TestGetSpListWithReleaseDate(unittest.TestCase):
    @patch('views_v2.Elasticsearch')
    def test_get_sp_list_with_release_date(self, mock_elasticsearch):
        # Mock Elasticsearch client and search result
        mock_search_result = {
            "hits": {
                "hits": [
                    {"_source": {"released_flag": True, "released_converted": "2024-01-01"}, "_id": "1"},
                    {"_source": {"released_flag": False, "released_converted": "2024-01-02"}, "_id": "2"}
                ]
            }
        }
        mock_es_instance = mock_elasticsearch.return_value
        mock_es_instance.search.return_value = mock_search_result

        # Call the function under test
        sp_list = ['SP01', 'SP02']
        index_service_packs = 'fco-on-demand-service-packs'
        release_id = '7.4.0.b'
        machine_type = 'World-Wide'
        result = get_sp_list_with_release_date(sp_list, index_service_packs, release_id, machine_type)

        # Assert the results
        expected_result = [
            {'SP01': {'released': True, 'release_date': '2024-01-01 (True)'}},
            {'SP02': {'released': False, 'release_date': '2024-01-02 (False)'}}
        ]
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
