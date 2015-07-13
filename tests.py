"""
Tests for the sprockets.clients.cassandra package

"""
import os
import socket
import time

from cassandra.cluster import Cluster
from cassandra.protocol import SyntaxException
from tornado.testing import AsyncTestCase, gen_test

from sprockets.clients.cassandra import CassandraConnection


class TestCassandraConnectionClass(AsyncTestCase):

    def setUp(self):
        super(TestCassandraConnectionClass, self).setUp()
        self.cluster = Cluster(self.find_cassandra())
        self.session = self.cluster.connect()
        self.keyspace = 'sprocketstest{0}'.format(int(time.time()*10000))
        self.create_fixtures()
        self.connection = CassandraConnection()

    def tearDown(self):
        super(TestCassandraConnectionClass, self).tearDown()
        self.session.execute("DROP KEYSPACE {0}".format(self.keyspace))
        self.connection.shutdown()

    def find_cassandra(self):
        uri = os.environ.get('CASSANDRA_URI', 'cassandra://localhost')
        hostname = uri[12:]
        return [hostname.split(':')[0]]
        _, _, ips = socket.gethostbyname_ex(hostname)
        return ips

    def create_fixtures(self):
        self.session.execute(
            "CREATE KEYSPACE IF NOT EXISTS {0} WITH REPLICATION = "
            "{{'class': 'SimpleStrategy', "
            "'replication_factor': 1}}".format(self.keyspace))
        self.session.execute("USE {0}".format(self.keyspace))
        self.session.execute(
            "CREATE TABLE IF NOT EXISTS names (name text PRIMARY KEY)")
        self.session.execute(
            "INSERT INTO names (name) VALUES ('Peabody')")

    @gen_test
    def test_several_queries(self):
        futures = []
        count = 100
        for i in range(count):
            futures.append(self.connection.execute(
                "SELECT name FROM {0}.names".format(self.keyspace)))
        results = 0
        for future in futures:
            yield future
            results += 1
        self.assertEqual(count, results)

    @gen_test
    def test_bad_query(self):
        with self.assertRaises(SyntaxException):
            yield self.connection.execute('goobletygook')

    @gen_test
    def test_set_keyspace(self):
        self.connection.set_keyspace(self.keyspace)

    @gen_test
    def test_prepared_statement(self):
        yield self.connection.execute('use %s' % self.keyspace)
        stmt = self.connection.prepare('SELECT * FROM names;', 'get_names')
        copy = self.connection.prepare('SELECT * FROM names;', 'get_names')
        self.assertIs(stmt, copy, 'Should return the cached statement')
        results = yield self.connection.execute(stmt)
        self.assertEqual(results[0].name, 'Peabody')
