from __future__ import unicode_literals

import logging

from mopidy import backend

import pykka

logger = logging.getLogger(__name__)


class MplayerBackend(pykka.ThreadingActor, backend.Backend):
    def __init__(self, config, audio):
        super(MplayerBackend, self).__init__()
        #from .audio import MplayerAudio
        #from .library import MplayerLibraryProvider
        from .playlists import MplayerPlaylistsProvider
        #self.audio = MplayerAudio(config)
        self.uri_schemes = ['mplayer']
        #self.playback = MediaplayerPlaybackProvider(audio=self.audio,
        #                                            backend=self)
        self.library = MplayerLibraryProvider(backend=self)
        self.playlists = MplayerPlaylistsProvider(backend=self, config=config)