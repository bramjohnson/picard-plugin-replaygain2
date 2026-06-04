from functools import partial

from picard.plugin3.api import PluginApi, Album, Metadata
from picard.util import thread

from src.actions.scan_albums import ScanAlbums
from src.common.data import ReplaygainablePair
from src.common.rsgain import build_rsgain_options, calculate_replaygain
from src.common.statusbar import WindowStatusbarReplaygainCalculationMessages
from src.options.config import PluginConfig


def album_metadata_processor_callback(
    api: PluginApi, album: Album, metadata: Metadata, options
):
    if not PluginConfig(api).should_calculate_on_album_load:
        return

    # def runwhenloaded():
    #     album_name = album.metadata["album"]
    #     WindowStatusbarReplaygainCalculationMessages.inprogress(album_name, 1, "album")

    #     config = PluginConfig(api)
    #     thread.run_task(
    #         partial(
    #             calculate_replaygain,
    #             ReplaygainablePair.from_album(album),
    #             build_rsgain_options(config),
    #         ),
    #         partial(albumgain_callback, "", album),
    #     )

    scan_albums = ScanAlbums()
    # Must run_when_loaded, else tracks will not be present on the Album object
    album.run_when_loaded(lambda: scan_albums.callback([album]))
