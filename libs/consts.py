"""
"""

# Error codes
error_codes = {
    "Unauthorized": 401,
    "URI Too Long": 414,
    "Bad Request": 400
}

# Valid Test Values
valid_body = "Dummy Request Body"
valid_search_query = "DYNACULT"
valid_queries = ["DYNACULT", "", "jhgfdghjnbvcfghjmnb vghjm", "Cytometer"]
valid_objectIds = ["-9223372036854775808", "9223372036854775808", "", "6823", "&&6ds76fa7sd6f7a67^&^876d76sa8df"]
valid_missionDirectorates = ["DYNACULT", "mars", "", "6823"]


# Invalid Test Values
invalid_queries = [{"value":"x"*2084, "error code": error_codes["URI Too Long"]}]
invalid_objectIds = [
    # ISSUE: API is not validating int64 maximum and minimum values. 
    {"value":"hjsdkjfhsdkjfh", "error code": error_codes["URI Too Long"]},
    {"value":"4567876asdf6asfd7asdf", "error code": error_codes["URI Too Long"]},
    {"value":"123%$%^@212377^^", "error code": error_codes["URI Too Long"]},
    {"value":"9223372036854775809", "error code": error_codes["URI Too Long"]}, 
    {"value":"-9223372036854775809", "error code": error_codes["URI Too Long"]}
]
invalid_missionDirectorates = [
    {"value":"x"*2084, "error code": error_codes["URI Too Long"]},
    # ISSUE: API is not stating the nature of the Bad request. Documentation includes type string.
    #        No mention that Mission directives should not have spaces
    {"value":"sadfasd87f8asd7f87as6df asdf", "error code": error_codes["Bad Request"]}
]
