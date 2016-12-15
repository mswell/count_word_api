import inspect
import os

import vcr


class BaseTest(object):
    def _test_name_for_vcr_file(self):
        return self.__str__().split(' ')[0]

    def _vcr_file_name(self, method_name):
        file_name = "{0}.{1}.yml".format(self._test_name_for_vcr_file(),
                                         method_name)
        file_name = file_name.replace('<', '')
        return os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                'recorded',
                self.__class__.__name__,
                file_name
            )
        )

    def vcr(self):
        method_name = inspect.stack()[1][3]
        return vcr.use_cassette(
            self._vcr_file_name(method_name),
            record_mode='new_episodes',
            filter_headers=['x-api-key', 'User-Agent', 'Connection'],
            filter_query_parameters=['x-api-key'],
            match_on=['method', 'scheme', 'host', 'port', 'path', 'query',
                      'headers', 'body'],
        )
