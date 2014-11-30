from __future__ import unicode_literals

import logging

from mopidy import backend, exceptions

from mopidy.audio import scan

from mopidy.models import Track

logger = logging.getLogger(__name__)


class MplayerLibraryProvider(backend.LibraryProvider):

    def __init__(self, *args, **kwargs):
        self._scanner = scan.Scanner(min_duration=None, timeout=5000)
        super(MplayerLibraryProvider, self).__init__(*args, **kwargs)

    def lookup(self, uri):
        if 'mplayer:' in uri:
            stripped_uri = uri.replace('mplayer:', '')
            try:
                data = self._scanner.scan(stripped_uri)
                track = scan.audio_data_to_track(data).copy(uri=uri)
            except exceptions.ScannerError as e:
                logger.warning('Problem looking up %s: %s', uri, e)
                track = Track(uri=uri, name=stripped_uri.split('/')[-1])
            return [track]
