from datetime import datetime
import sqlalchemy as sa
from sqlalchemy_utils import TSVectorType
from tests import ModelFormTestCase


class TestFieldExclusion(ModelFormTestCase):
    def test_does_not_include_datetime_columns_with_default(self):
        self.init(sa.DateTime, default=datetime.now())
        assert not self.has_field('test_column')

    def test_excludes_surrogate_primary_keys_by_default(self):
        self.init()
        assert not self.has_field('id')


class TestTSVectorType(ModelFormTestCase):
    dns = 'postgres://postgres@localhost/wtforms_alchemy_test'

    def test_does_not_include_tsvector_typed_columns_with_default(self):
        self.init(TSVectorType)
        assert not self.has_field('test_column')
