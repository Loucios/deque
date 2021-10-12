import unittest

from deque.deque import Deque


class Test(unittest.TestCase):
    def test_deque(self):
        test_map = (
            {
                'input_values': [4, 4, 'push_front 861', 'push_front -819',
                                 'pop_back', 'pop_back'],

                'result_values': ['861', '-819']
            },

            {
                'input_values': [7, 10, 'push_front -855', 'push_front 720',
                                 'pop_back', 'pop_back', 'push_back 844',
                                 'pop_back', 'push_back 823'],

                'result_values': ['-855', '720', '844']
            },

            {
                'input_values': [6, 6, 'push_front -201', 'push_back 959',
                                 'push_back 102', 'push_front 20', 'pop_front',
                                 'pop_back'],

                'result_values': ['20', '102']
            }
        )
        for case in test_map:
            input_values, result_values = case.values()
            with self.subTest('test_deque'):
                deque = Deque(input_values[1])
                report = deque.execute_commands_and_generate_report(
                    input_values[2:]
                )
                self.assertEqual(result_values, report)
