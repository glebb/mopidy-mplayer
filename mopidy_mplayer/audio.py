from __future__ import unicode_literals

import logging

from mplayer import Player

logger = logging.getLogger(__name__)


class Wrap:
    def __init__(self, val):
        self.val = val

    def get(self):
        return self.val


class MplayerAudio():
    def __init__(self, config):
        self.config = config
        self.state = u'stopped'
        self.uri = None
        self.player = Player()

    def emit_data(buffer_):
        return Wrap(False)

    def emit_end_of_stream(self):
        pass

    def get_mute(self):
        return Wrap(self.player.mute)

    def get_position(self):
        return Wrap(1)
    '''
    def get_volume(self):
        return Wrap(int(self.player.volume))
        return Wrap(0)
    '''

    def pause_playback(self):
        if not self.player.paused:
            self.player.pause()
            self.state = u'paused'
        return Wrap(True)

    '''
    def prepare_change(self):
        pass
    '''

    def set_appsrc(self, caps, need_data=None,
                   enough_data=None, seek_data=None):
        pass

    def set_metadata(self, track):
        return Wrap(False)

    def set_mute(self, mute):
        self.player.mute = mute
        return Wrap(True)

    def set_position(self, position):
        return Wrap(False)

    def set_uri(self, uri):
        self.uri = uri
        return Wrap(True)

    def set_volume(self, volume):
        #  self.player.volume = volume
        return Wrap(True)

    def start_playback(self):
        if self.player.paused:
            self.player.pause()
        if not self.player.filename:
            self.player.loadfile(self.uri.replace('mplayer:', ''))
        self.state = u'playing'
        return Wrap(True)

    def stop_playback(self):
        self.player.stop()
        self.state = u'stopped'
        return Wrap(True)

    def prepare_change(self):
        self.player.stop()
        return Wrap(True)

    def set_about_to_finish_callback(self, callback):
        pass
