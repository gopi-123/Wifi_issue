
from elasticsearch import Elasticsearch, exceptions
import os

def get_sp_list_with_release_date(
    sp_list, index_service_packs, release_id, machine_type
):
    """Function that creates a service pack list having dictionary of service packs having values as 'released' flags and 'released dates'
    It uses elastic search to query the relevant data based on given sp_list, index_service_packs, release_id, machine_type

    Arguments:
        sp_list -- list of service pack number obtained for elastic search  in format ['SP01', 'SP02']
        index_service_packs -- string having index_service_packs with value Ex: "fco-on-demand-service-packs"
        release_id -- string  having release version id like "7.4.0.b", "6.3.0.b"
        machine_type -- string having machine types values like "World-Wide", "NXE:3600"

    Returns:
        Returns a list having dictionary of service packs with released flags and relased dates
        Example:
        [{
            "SP34": {
                "released": false,
                "release_date": "wkyyww.d (yyyy-mm-dd)"
            }
        },
        {
            "SP33": {
                "released": true,
                "release_date": "wk2412.4 (2024-03-21)"
            }
        }]
    """
    body = {}
    res = {}
    new_sp_list = []
    es = Elasticsearch()
    
    for sp_name in sp_list:
        body = {
            "query": {
                "bool": {
                    "must": [
                        {"match": {"product": "AT"}},
                        {"match": {"release": release_id}},
                        {"match": {"name": sp_name}},
                        {"match": {"machine_type": machine_type}},
                    ]
                }
            }
        }

        res = es.search(index=index_service_packs, body=body)
        sp = res.get("hits").get("hits")[0].get("_source")
        release_date_info = f"{sp.get('released_converted')} ({sp.get('released')})"
        new_sp_list.append(
            {
                sp_name: {
                    "released": sp.get("released_flag"),
                    "release_date": release_date_info,
                }
            }
        )

    return new_sp_list


def get_fpas_json_v2(release_id, machine_type):
    body = {}
    index_service_packs = "fco-on-demand-service-packs"
    res = {}
    ret = {}

    #es = Elasticsearch([os.environ["ES_HOST"]])    
    es = Elasticsearch()

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