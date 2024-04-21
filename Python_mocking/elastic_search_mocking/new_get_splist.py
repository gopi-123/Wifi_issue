
from elasticsearch import Elasticsearch, exceptions

def get_sp_list_with_release_date(
    sp_name, index_service_packs, release_id, machine_type
):
    """
    [{
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

    print(f"release_date_info:{release_date_info}")
    new_sp_list.append(
		{
			sp_name: {
				"released": sp.get("released_flag"),
				"release_date": release_date_info,
			}
		}
	)

    print(f"new_sp_list:{new_sp_list}")

    return new_sp_list

