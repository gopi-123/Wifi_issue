


from elasticsearch import Elasticsearch, exceptions

def get_fpas_json_v2(release_id, machine_type):
    body = {}
    index_service_packs = "fco-on-demand-service-packs"
    res = {}
    ret = {}

    es = Elasticsearch([os.environ["ES_HOST"]])    
    
    body = {
        "size": 0,
        "aggs": {"distinct": {"terms": {"field": "name", "size": 10000}}},
        "query": {
            "bool": {
                "must": [
                    {"match": {"product": "AT"}},
                    {"match": {"release": release_id}},
                    {"match": {"machine_type.keyword": machine_type}},
                ]
            }
        },
    }

    res = es.search(index=index_service_packs, body=body)
    ret["service_packs"] = []
    
    for bucket in (
        res.get("aggregations", {}).get("distinct", {}).get("buckets", [])
    ):
        ret["service_packs"].append(bucket.get("key"))

    ret["service_packs"].sort(reverse=True)

    # Call a Function and create a service pack list having dictionary of service packs number having values as 'released' flags and 'released dates'
    ret["service_packs"] = get_sp_list_with_release_date(
        ret["service_packs"], index_service_packs, release_id, machine_type
    )
        
    return ret
	

#######

Solution 1:

import unittest
from unittest.mock import patch, MagicMock
import os
from your_module import get_fpas_json_v2

class TestGetFpasJson(unittest.TestCase):
    @patch('your_module.Elasticsearch')  # Patch the Elasticsearch class
    @patch('your_module.get_sp_list_with_release_date')  # Patch the get_sp_list_with_release_date function
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



###########


#### Solution 2 ###########

import unittest
from unittest.mock import patch, MagicMock
from your_module import get_fpas_json_v2, Elasticsearch, exceptions

class TestGetFpasJsonV2(unittest.TestCase):
    @patch('your_module.Elasticsearch')
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



###################

