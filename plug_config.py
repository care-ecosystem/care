from plugs.manager import PlugManager
from plugs.plug import Plug

plugs = [
    
    Plug(
        name="abdm",
        package_name="git+https://github.com/care-ecosystem/care_abdm.git",
        version="@develop",
        configs={},
    ),
    Plug(
        name="care_scribe",
        package_name="git+https://github.com/care-ecosystem/care_scribe.git",
        version="@master",
        configs={},
    ),
]

manager = PlugManager(plugs)
