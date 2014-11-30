from __future__ import unicode_literals

import unittest

from mock import MagicMock

from mopidy import exceptions

from mopidy.audio import scan

from mopidy.models import Track

from mopidy_mplayer import Extension

from mopidy_mplayer.library import MplayerLibraryProvider


class ExtensionTest(unittest.TestCase):
    def test_get_default_config(self):
        ext = Extension()
        config = ext.get_default_config()
        self.assertIn('[mplayer]', config)
        self.assertIn('enabled = true', config)


class MplayerLibraryProviderTest(unittest.TestCase):
    def setUp(self):
        scan.Scanner.scan = MagicMock()

    def test_lookup_identifies_uri_schema(self):
        prov = MplayerLibraryProvider(backend=None)
        track = prov.lookup('mplayer:http://test_uri')[0]
        self.assertEqual(track.uri, 'mplayer:http://test_uri')

    def test_lookup_ignores_other_uris(self):
        prov = MplayerLibraryProvider(backend=None)
        tracks = prov.lookup('stream:http://test_uri')
        self.assertEqual(tracks, None)

    def test_lookup_scans_the_actual_uri(self):
        prov = MplayerLibraryProvider(backend=None)
        prov.lookup('mplayer:http://test_uri')
        scan.Scanner.scan.assert_called_with('http://test_uri')

    def test_creates_track_and_name(self):
        temp = Track(uri='mplayer:http://test_uri', name='blah')
        Track.copy = MagicMock(return_value=temp)
        prov = MplayerLibraryProvider(backend=None)
        track = prov.lookup('mplayer:http://test_uri')[0]
        self.assertEquals(track.name, 'blah')

    def test_simplifies_track_name_when_scan_fails(self):
        scan.Scanner.scan = MagicMock(
            side_effect=exceptions.ScannerError('error'))
        prov = MplayerLibraryProvider(backend=None)
        track = prov.lookup('mplayer:http://test_uri')[0]
        self.assertEquals(track.name, 'test_uri')
