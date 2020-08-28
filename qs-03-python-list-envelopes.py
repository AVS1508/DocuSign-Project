# Python3 Quick start example: list envelopes in the user's account
# Copyright (c) 2018 by DocuSign, Inc.
# License: The MIT License -- https://opensource.org/licenses/MIT

import base64, os
from docusign_esign import ApiClient, EnvelopesApi
import pendulum # pip install pendulum
import pprint
import ssl

# Settings
# Fill in these constants
#
# Obtain an OAuth access token from https://developers.docusign.com/oauth-token-generator
access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjY4MTg1ZmYxLTRlNTEtNGNlOS1hZjFjLTY4OTgxMjIwMzMxNyJ9.eyJUb2tlblR5cGUiOjUsIklzc3VlSW5zdGFudCI6MTU5ODUzNTE4MywiZXhwIjoxNTk4NTYzOTgzLCJVc2VySWQiOiI3NmExNDM0Yy03YjFjLTQzYTAtODljZi1iODE3MDczNTQwOTciLCJzaXRlaWQiOjEsInNjcCI6WyJzaWduYXR1cmUiLCJjbGljay5tYW5hZ2UiLCJvcmdhbml6YXRpb25fcmVhZCIsInJvb21fZm9ybXMiLCJncm91cF9yZWFkIiwicGVybWlzc2lvbl9yZWFkIiwidXNlcl9yZWFkIiwidXNlcl93cml0ZSIsImFjY291bnRfcmVhZCIsImRvbWFpbl9yZWFkIiwiaWRlbnRpdHlfcHJvdmlkZXJfcmVhZCIsImR0ci5yb29tcy5yZWFkIiwiZHRyLnJvb21zLndyaXRlIiwiZHRyLmRvY3VtZW50cy5yZWFkIiwiZHRyLmRvY3VtZW50cy53cml0ZSIsImR0ci5wcm9maWxlLnJlYWQiLCJkdHIucHJvZmlsZS53cml0ZSIsImR0ci5jb21wYW55LnJlYWQiLCJkdHIuY29tcGFueS53cml0ZSJdLCJhdWQiOiJmMGYyN2YwZS04NTdkLTRhNzEtYTRkYS0zMmNlY2FlM2E5NzgiLCJhenAiOiJmMGYyN2YwZS04NTdkLTRhNzEtYTRkYS0zMmNlY2FlM2E5NzgiLCJpc3MiOiJodHRwczovL2FjY291bnQtZC5kb2N1c2lnbi5jb20vIiwic3ViIjoiNzZhMTQzNGMtN2IxYy00M2EwLTg5Y2YtYjgxNzA3MzU0MDk3IiwiYW1yIjpbImludGVyYWN0aXZlIl0sImF1dGhfdGltZSI6MTU5ODUzNTE4MCwicHdpZCI6IjU0YTkwZWFiLWEzNTItNDZiYy1hMDRlLTM0Nzc2MjMzMTIzOSJ9.lP8TwdYi7iCaoKv3otg9XOXlnMefE6z7zqp8AwJ6A6olXjSQoWsO-7UGXiDWjIbiHB8is6zmm29oxYHd_xBwarfRDeNATryewVMOAvjPSIR4Kf2TLyty2JPIsEfYlPI8tW5R4qWu7D7wouOkpU4BunulKvLMIPrD-37Q1QYqudYW9uk2nj2SOBDnIilL4XNKXwQ07keHpyP56cZz1soScUwO7cRuwvOLHgxABw-C4WoXFyIBIjFWGzeowA7neuus4QkRg3qn4kYL4ANx85Akf2faXCqopeIAPiW3Mw5K8jkqmgymnf21zyyOh5OfCgnZBu6oBDsWh-wI0wq3_w9Bhg'
# Obtain your accountId from demo.docusign.com -- the account id is shown in the drop down on the
# upper right corner of the screen by your picture or the default picture. 
account_id = '11321217'; 
base_path = 'https://demo.docusign.net/restapi'

def list_envelopes():
    """
    Lists the user's envelopes created in the last 10 days
    """
    
    #
    # Step 1. Prepare the options object
    #
    from_date = pendulum.now().subtract(days=10).to_iso8601_string()
    #
    # Step 2. Get and display the results
    # 
    api_client = ApiClient()
    api_client.host = base_path
    api_client.set_default_header("Authorization", "Bearer " + access_token)

    envelope_api = EnvelopesApi(api_client)
    results = envelope_api.list_status_changes(account_id, from_date = from_date)
    return results

# Mainline
results = list_envelopes()
print("\nEnvelopes:\n")
pprint.pprint(results, indent=4, width=80)

