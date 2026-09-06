# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "environment": {
# META       "environmentId": "19b664a3-d261-9187-4d1f-6ed55db07bba",
# META       "workspaceId": "00000000-0000-0000-0000-000000000000"
# META     }
# META   }
# META }

# CELL ********************

""

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from common.module import APICreation, GetData

gdp_data_api_obj = APICreation()

gdp_data_get_obj = GetData(
    gdp_data_api_obj.url, gdp_data_api_obj.params, gdp_data_api_obj.headers
)

res = gdp_data_get_obj.get_response()
payload = gdp_data_get_obj.get_json_response(res)
keys = gdp_data_get_obj.get_payload_keys(payload)

print(payload["records"])


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
