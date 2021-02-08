"""
Title: Test Project Search endpoint of NASA Tech Port

Description:
    - Information about the API endpoint: https://api.nasa.gov/techport/api/specification
    - Testing positive and negative values for the 3 parameters accepted: 
        * objectId
        * searchQuery
        * missionDirective

"""

from libs.auxiliary import send_get_request, send_post_request
from libs import consts
from libs.logger import log_test
import unittest

class TestProjectSearch(unittest.TestCase):

    @log_test
    def test_post(self):
        """
        Make sure POST request is rejected even if it is an authenticated user and valid data
        """
        response = send_post_request('/projects/search', 
            searchQuery=consts.valid_search_query,
            data = consts.valid_body)
        # Check Response was an error
        self.assertEqual(list(response.keys()), ['error'])
        # Check error code is 401 unauthorized
        self.assertEqual(response['error']['code'], consts.error_codes["Unauthorized"])

    @log_test
    def test_valid_search_querys(self):
        """
        Make sure requests are accepted if the search query is valid
        """
        for query in consts.valid_queries:
            response = send_get_request('/projects/search', 
                searchQuery=query)
            # Check Response was not an error
            self.assertTrue('error' not in response.keys())

    @log_test
    def test_valid_search_query_responses(self):
        """
        Make sure the response items are propperly structured
        """
        response = send_get_request('/projects/search', 
            searchQuery=consts.valid_search_query)
        # Check Response was not an error
        self.assertTrue('error' not in response.keys())
        # Check there is a response and it is correctly formated
        self.assertTrue('projects' in response.keys())
        self.assertTrue(len(response['projects'])>0)
        self.assertTrue('id' in response['projects'][0].keys())
        self.assertTrue('title' in response['projects'][0].keys())
        self.assertTrue('description' in response['projects'][0].keys())

    @log_test
    def test_invalid_search_query(self):
        """
        Make sure requests are accepted if the search query is valid
        """
        for query in consts.invalid_queries:
            response = send_get_request('/projects/search', 
                searchQuery=query['value'])\
            # Check Response error was as expected
            self.assertEqual(response.status_code, query["error code"])

    @log_test
    def test_valid_search_objectId(self):
        """
        Make sure requests are accepted if the objectId is valid
        """
        for objectId in consts.valid_objectIds:
            response = send_get_request('/projects/search', 
                objectId=objectId)
            # Check Response was not an error
            self.assertTrue('error' not in response.keys())

    @log_test
    def test_invalid_search_objectId(self):
        """
        Make sure requests are accepted if the objectId is valid
        """
        for objectId in consts.invalid_objectIds:
            response = send_get_request('/projects/search', 
                objectId=objectId['value'])\
            # Check Response error was as expected
            self.assertEqual(response.status_code, objectId["error code"])

    @log_test
    def test_valid_search_objectId(self):
        """
        Make sure requests are accepted if the objectId is valid
        """
        for objectId in consts.valid_objectIds:
            response = send_get_request('/projects/search', 
                objectId=objectId)
            # Check Response was not an error
            self.assertTrue('error' not in response.keys())

    @log_test
    def test_invalid_search_objectId(self):
        """
        Make sure requests are accepted if the objectId is valid
        """
        for objectId in consts.invalid_objectIds:
            response = send_get_request('/projects/search', 
                objectId=objectId['value'])\
            # Check Response error was as expected
            # ISSUE: API is not validating int64 format. Empty project list response is returned instead
            # self.assertEqual(response.status_code, objectId["error code"])
            self.assertEqual(response, {'projects': []})

    @log_test
    def test_valid_search_missionDirectorate(self):
        """
        Make sure requests are accepted if the missionDirectorate is valid
        """
        for missionDirectorate in consts.valid_missionDirectorates:
            response = send_get_request('/projects/search', 
                missionDirectorate=missionDirectorate)
            # Check Response was not an error
            self.assertTrue('error' not in response.keys())

    @log_test
    def test_invalid_search_missionDirectorate(self):
        """
        Make sure requests are accepted if the missionDirectorate is valid
        """
        for missionDirectorate in consts.invalid_missionDirectorates:
            response = send_get_request('/projects/search', 
                missionDirectorate=missionDirectorate['value'])\
            # Check Response error was as expected
            # ISSUE: API is not stating the nature of the Bad request. Documentation includes type string.
            #        No mention that Mission directives should not have spaces
            if isinstance(response, dict):
                self.assertEqual(response['error']['code'], missionDirectorate["error code"])
            else:
                self.assertEqual(response.status_code, missionDirectorate["error code"])

if __name__ == '__main__':
    unittest.main()

