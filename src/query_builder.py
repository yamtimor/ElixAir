import re

class QueryBuilder:
    def __init__(self, sql_query):
        self.sql_query = sql_query

    def to_elasticsearch_query(self):
        # Capture SELECT fields
        pattern = r"SELECT\s+(.*?)\s+FROM\s+\w+"
        match = re.match(pattern, self.sql_query, re.IGNORECASE)
        
        if match:
            select_part = match.group(1).strip()  # Fields to select
            selected_fields = [field.strip() for field in select_part.split(",")]

            # Construct the Elasticsearch query
            elasticsearch_query = {
                "_source": selected_fields,  # Specify which fields to return
                "query": {
                    "match_all": {}  # Placeholder; modify for actual filtering logic if needed
                }
            }

            return {
                "index": index_name,
                "query": elasticsearch_query
            }

        raise ValueError("Unsupported query format.")
