# -*- coding: utf-8 -*-

from picard.plugin3.api import PluginApi

from .src.callbacks.album_load import album_metadata_processor_callback
from .src.actions.scan_albums import ScanAlbums
from .src.actions.scan_cluster import ScanCluster
from .src.actions.scan_tracks import ScanTracks
from .src.options.options_page import ReplayGain2OptionsPage


def enable(api: PluginApi):
    """Called when plugin is enabled."""

    ScanTracks.register_with(api)
    ScanAlbums.register_with(api)
    ScanCluster.register_with(api)
    ReplayGain2OptionsPage.register_with(api)
    api.register_album_metadata_processor(album_metadata_processor_callback)
