import os
from plugs.manager import PlugManager
from plugs.plug import Plug


plugs = [
    Plug(
        name="abdm",
        package_name="git+https://github.com/10bedicu/care_abdm.git",
        version="@develop",
        configs={},
    ),
    Plug(
        name="nhcx",
        package_name="git+https://github.com/ohcnetwork/care_nhcx.git",
        version="@develop",
        configs={},
    ),
    Plug(
        name="care_radiology",
        package_name="git+https://github.com/care-ecosystem/care_radiology.git",
        version="@updates",
        configs={
        "CARE_RADIOLOGY_DCM4CHEE_DICOMWEB_BASEURL": os.getenv(
            "CARE_RADIOLOGY_DCM4CHEE_DICOMWEB_BASEURL"
        ),
        "CARE_RADIOLOGY_WEBHOOK_SECRET": os.getenv(
            "CARE_RADIOLOGY_WEBHOOK_SECRET"
        )
        }
    ),
    Plug(
        name="care_scribe",
        package_name="git+https://github.com/10bedicu/care_scribe.git",
        version="@master",
        configs={},
    )
]

manager = PlugManager(plugs)
