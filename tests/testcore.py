from speaker import Speaker, SpeakerError

import unittest

class SpeakerAPITestCase(unittest.TestCase):
    def setUp(self):

        client_args = {
            'headers': {
                'User-Agent': '__speaker__ Test'
            },
        }

        self.api = Speaker(client_args=client_args)


    def test_issue_gender_recognition_task(self):
        """
            Test Speaker issue_gender_recognition_task works.
        """
        try:
            response = self.api.issue_gender_recognition_task()
            assert 'task_id' in response
        except Exception, e:
            e is SpeakerError

    def test_get_gender_recognition_result(self):
        """
            Test Speaker get_gender_recognition_result works.
        """
        response = self.api.get_gender_recognition_result(task_id='bf4f25f6682d4d2990cec25a91a15e75')
        assert 'gender' in response


if __name__ == '__main__':
    unittest.main()
