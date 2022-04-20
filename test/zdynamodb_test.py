from zdynamodb import queries
from decimal import Decimal

connection_params = {
    'region': '',
    's3_key_id': '',
    's3_key_secret': '',
    'dynamo_table': ''
}

table_name = 'carts'
pk = 'id'
pk_value = '02085a13-d62d-40ff-bd67-af42bac87590'
index_name = 'expertidIndex'
index_key = 'expert_id'
index_value = 'f18b6f8f-23bb-4cd1-89fa-510804c12f9e'

t1 = queries.DynamoQueries(table_name=table_name, connection_params=connection_params)
try:
    r1 = t1.get_pk_context(pk=pk, pk_value=pk_value)
    print(r1)
except Exception as e:
    print(e)
    pass

try:
    r2 = t1.get_index_context(index_name=index_name, index_key=index_key, index_value=index_value)
    print(r2)
except Exception as e:
    print(e)
    pass

try:
    r3 = t1.get_pk_context(pk=pk, pk_value=pk_value)
    print(r3)
except Exception as e:
    print(e)
    pass

table_name = 'connection_backend'
random_dict = {
    "a": "",
    "b": {
        "c": ["1", "2"]
    },
    "c": "123",
    "d": "2.5",
    "e": "f",
    "connection_bk":"no_boss_yes_boss"
}

t2 = queries.DynamoQueries(table_name=table_name, connection_params=connection_params)
try:
    r4 = t2.add_context(item=random_dict)
    print(r4)
except Exception as e:
    print(e)
    pass
