from plugs.manager import PlugManager
from plugs.plug import Plug  # noqa: F401

care_digit_integration_plug = Plug(
    name="care_digit_integration",
    package_name="git+https://github.com/care-ecosystem/care_digit_integration.git",
    version="@main",
    configs={
        "HOST": "",
        "DIGIT_TOKEN_ENDPOINT": "",
        "PGR_CREATE_ENDPOINT": "",
        "USERNAME": "",
        "PASSWORD": "",
        "USER_TYPE": "",
        "GRANT_TYPE": "",
    },
)

plugs = [
    care_digit_integration_plug,
]

manager = PlugManager(plugs)
