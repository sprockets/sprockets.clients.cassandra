from test_helpers import bases
from test_helpers.compat import mock
from test_helpers.mixins import patch_mixin


class App(object):
    """Quick example app for testing."""

    def first(self, fail):
        """Example method under test."""
        self.do_db_lookup('random')
        if fail:
            raise AttributeError

    def do_db_lookup(self, name):
        """Method that reaches out to a database."""
        raise NotImplementedError


class _BaseFirstTestCase(patch_mixin.PatchMixin, bases.BaseTest):
    """Example base test showing current test style."""

    patch_prefix = 'tests.unit.test_example'

    @classmethod
    def configure(cls):
        cls.app = App()

        cls.do_db_lookup = cls.create_patch('App.do_db_lookup')

    @classmethod
    def execute(cls):
        try:
            cls.app.first(cls.fail)
        except AttributeError as exc:
            cls.exception = exc

    def should_do_db_lookup(self):
        self.do_db_lookup.assert_called_once_with(mock.ANY)


class WhenFirstAppSuccessful(_BaseFirstTestCase):

    @classmethod
    def configure(cls):
        cls.fail = False
        super(WhenFirstAppSuccessful, cls).configure()


class WhenFirstAppFails(_BaseFirstTestCase):

    @classmethod
    def configure(cls):
        cls.fail = True
        super(WhenFirstAppFails, cls).configure()

    def should_raise_AttributeError(self):
        self.assertIsInstance(self.exception, AttributeError)
