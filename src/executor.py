import requests

class Executor:
    def __init__(self, sql_query):
        self.sql_query = sql_query
        self.duckdb_conn = duckdb.connect(Config.DUCKDB_DATABASE_PATH)
        self.es = Elasticsearch(Config.ELASTICSEARCH_HOST)