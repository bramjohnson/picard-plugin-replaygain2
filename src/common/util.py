import os
import shutil

from .statusbar import StatusbarMessages


def isinstanceany(obj: object, types):
    return any(isinstance(obj, t) for t in types)


# Make sure the rsgain executable exists
def does_rsgain_path_still_exist(rsgain_command: str) -> bool:
    if os.path.exists(rsgain_command) or shutil.which(rsgain_command) is not None:
        return True
    # INVARIANT: rsgain no longer exists ):

    StatusbarMessages.rsgain_not_found()
    return False
