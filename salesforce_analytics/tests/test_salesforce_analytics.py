""" Test template to test against the SalesForceAnalytics library
Nothing Fancy
"""

import unittest
import json
import os
from salesforce_analytics import SalesForceAnalytics

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path+"/mock/sample-tickets.json", 'r') as f:
    tickets = f.read()

class TestSalesForceAnalytics(unittest.TestCase):
    def setUp(self):
        self.analytics = SalesForceAnalytics(
            tickets=tickets
            )

    def test_prepare_analytics(self):
        self.assertNotEqual(0, len(self.analytics.count))
        self.assertEqual(
            self.analytics.count,
            {
                u'status': {},
                u'priority': {'1': 0, '3': 0, '2': 0},
                u'handoff': {},
                u'createdDate': {},
                u'owner': {},
                u'lastModifiedDate': {},
                u'typev2': {},
                u'accountNumber': {},
                u'subject': {}
                }
            )

    def test_iterate_tickets(self):
        results = self.analytics.run()
        cresults = results['count']
        mresults = results['mtc']
        self.assertEqual(
            cresults['priority'],
            {'1': 1065, '3': 1042, '2': 1075}
        )
        self.assertEqual(
            cresults['status'],
            {u'In-Progress': 829, u'New': 782, u'Waiting-Customer': 822, u'Closed': 749}
        )
        self.assertEqual(
            cresults['handoff'],
            3182
        )
        self.assertEqual(
            cresults['typev2'],
            {u'Networking': 525, u'Compliance': 532, u'Change Request': 527, u'System': 531, u'Other': 543, u'System / Environment Build': 524}
        )
        self.assertEqual(
            cresults['accountNumber'],
            {'150': 59, '135': 50, '112': 64, '115': 76, '132': 56, '117': 73, '130': 66, '137': 53, '110': 62, '113': 65, '134': 62, '139': 71, '138': 65, '119': 63, '118': 64, '116': 59, '128': 54, '146': 63, '147': 60, '144': 51, '145': 59, '142': 52, '143': 61, '140': 74, '141': 64, '148': 55, '149': 61, '120': 64, '121': 69, '122': 77, '109': 72, '124': 69, '125': 68, '129': 72, '127': 57, '102': 56, '103': 50, '100': 75, '101': 71, '106': 57, '107': 70, '104': 56, '105': 60, '133': 77, '114': 49, '108': 59, '131': 71, '123': 53, '111': 64, '126': 46, '136': 58}
        )
        self.assertEqual(
            cresults['compliance'],
            {'old_compliance': 659}
        )
        self.assertEqual(
            mresults['total'],
            '372 days, 16:12:53.305740'
        )


if __name__ == '__main__':
    unittest.main()
