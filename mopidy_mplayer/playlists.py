from __future__ import unicode_literals

import logging

from mopidy import backend, exceptions

from mopidy.audio import scan

from mopidy.models import Playlist, Track

logger = logging.getLogger(__name__)


class MplayerPlaylistsProvider(backend.PlaylistsProvider):
    def __init__(self, backend, config):
        self._backend = backend
        self._config = config
        self._scanner = scan.Scanner(min_duration=None, timeout=5000)
        self._playlists = None

    def create(self, name):
        pass  # TODO

    def delete(self, uri):
        pass  # TODO

    def lookup(self, uri):
        for pl in self._playlists:
            if pl.uri == uri:
                return pl

    @property
    def playlists(self):
        if not self._playlists:
            result = []
            tracks = []
            uris = list(self._config['mplayer']['playlist'])
            playlist_name = uris.pop(0)
            playlist = None
            for uri in uris:
                if 'mplayer:' in uri:
                    stripped_uri = uri.replace('mplayer:', '')
                '''
                try:
                    data = self._scanner.scan(stripped_uri)
                    track = scan.audio_data_to_track(data).copy(uri=stripped_uri, length=1)
                except exceptions.ScannerError as e:
                    logger.warning('Problem looking up %s: %s', uri, e)
                    track = Track(uri=stripped_uri, name=stripped_uri.split('/')[-1], length=1)
                '''
                track = Track(uri=stripped_uri, name=stripped_uri.split('/')[-1], length=1)

                if track:
                    tracks.append(track)
            if tracks:
                playlist = Playlist(name=playlist_name.replace('mplayer:', ''), #
                                    tracks=tuple(tracks), uri=playlist_name)
            if playlist:
                result.append(playlist)

            self._playlists = result
        return self._playlists

    def refresh(self):
        pass  # Not needed as long as we don't cache anything.

    def save(self, playlist):
        pass  # TODO
