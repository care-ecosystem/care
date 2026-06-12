import os
from plugs.manager import PlugManager
from plugs.plug import Plug

plugs = [
    # Plug(
    #     name="abdm",
    #     package_name="git+https://github.com/care-ecosystem/care_abdm.git",
    #     version="@develop",
    #     configs={},
    # ),
    
    # Plug(
    #     name="nhcx",
    #     package_name="git+https://github.com/ohcnetwork/care_nhcx.git",
    #     version="@develop",
    #     configs={},
    # ),
    
    Plug(
        name="super_batch_request",
        package_name="git+https://github.com/care-ecosystem/care_super_batch_be.git",
        version="@main",
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
        name="care_digit_integration",
        package_name="git+https://github.com/care-ecosystem/care_digit_integration.git",
        version="@main",
        configs={
            "HOST": "https://sandbox.digit.org",
            "DIGIT_TOKEN_ENDPOINT": "/user/oauth/token",
            "DIGIT_HEADER_AUTH_TOKEN": "ZWdvdi11c2VyLWNsaWVudDo=",
            "PGR_CREATE_ENDPOINT": "/pgr-services/v2/request/_create",
            "PGR_FETCH_ENDPOINT": "/pgr-services/v2/request/_search",
            "FILESTORE_UPLOAD_ENDPOINT": "/filestore/v1/files",
            "GRANT_TYPE": "password",
            "USERNAME": "9965664222",
            "PASSWORD": "123456",
            "USER_TYPE": "citizen"
        }
    ),
    Plug(
        name="care_scribe",
        package_name="git+https://github.com/10bedicu/care_scribe.git",
        version="@master",
        configs={},
    ),
    Plug(
        name="care_eaushadhi",
        package_name="git+https://github.com/care-ecosystem/care_eaushadhi.git",
        version="@main",
        configs={
            "EAUSHADHI_API_ENDPOINT": os.getenv(
                "EAUSHADHI_API_ENDPOINT"
            ),
            "EAUSHADHI_API_SECRET_KEY": os.getenv(
                "EAUSHADHI_API_SECRET_KEY"
            ),
            "EAUSHADHI_API_RETRY_COUNT": os.getenv(
                "EAUSHADHI_API_RETRY_COUNT"
            )
        }
    ),
    Plug(
        name="care_communication",
        package_name="git+https://github.com/care-ecosystem/care_communication_plugin.git",
        version="@updates",
        configs={},
    )
]

manager = PlugManager(plugs)
