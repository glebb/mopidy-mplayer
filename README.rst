****************************
Mopidy-Mplayer
****************************

.. image:: https://img.shields.io/pypi/v/Mopidy-Mplayer.svg?style=flat
    :target: https://pypi.python.org/pypi/Mopidy-Mplayer/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/dm/Mopidy-Mplayer.svg?style=flat
    :target: https://pypi.python.org/pypi/Mopidy-Mplayer/
    :alt: Number of PyPI downloads

.. image:: https://img.shields.io/travis/glebb/mopidy-mplayer/master.png?style=flat
    :target: https://travis-ci.org/glebb/mopidy-mplayer
    :alt: Travis CI build status

.. image:: https://img.shields.io/coveralls/glebb/mopidy-mplayer/master.svg?style=flat
   :target: https://coveralls.io/r/glebb/mopidy-mplayer?branch=master
   :alt: Test coverage

Mopidy extension for using mplayer to play audio (streams) instead of GStreamer with Mopidy.


Installation
============

Install by running::

    pip install Mopidy-Mplayer

Or, if available, install the Debian/Ubuntu package from `apt.mopidy.com
<http://apt.mopidy.com/>`_.


Configuration
=============

Before starting Mopidy, you must add configuration for
Mopidy-Mplayer to your Mopidy configuration file::

    [mplayer]
	enabled = true
	playlist = mplayer:Radio
		mplayer:http://83.102.39.40/Radiorock.mp3
		mplayer:http://rstream2.nelonenmedia.fi/RadioSuomiPop.mp3
		mplayer:http://icelive0.43660-icelive0.cdn.qbrick.com/4916/43660_radio_city.mp3
		mplayer:http://icelive0.43660-icelive0.cdn.qbrick.com/9883/43660_RadioJyvaskyla.mp3
		mplayer:http://icelive0.41168-icelive0.cdn.qbrick.com/5050/41168_radionova1.mp3

Project resources
=================

- `Source code <https://github.com/glebb/mopidy-mplayer>`_
- `Issue tracker <https://github.com/glebb/mopidy-mplayer/issues>`_
- `Development branch tarball <https://github.com/glebb/mopidy-mplayer/archive/master.tar.gz#egg=Mopidy-Mplayer-dev>`_


Changelog
=========

v0.1.0 (UNRELEASED)
----------------------------------------

- Initial release.
