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
        version="@main",
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
            "EAUSHADHI_DEPLOYMENT": "karnataka",
            "EAUSHADHI_API_SECRET_KEY": os.getenv(
                "EAUSHADHI_API_SECRET_KEY"
            ),
            "EAUSHADHI_API_RETRY_COUNT": os.getenv(
                "EAUSHADHI_API_RETRY_COUNT"
            ),
            "EAUSHADHI_VALIDATION_ENABLED": os.getenv(
                "EAUSHADHI_VALIDATION_ENABLED"
            )
        }
    ),
    Plug(
            name="encounter_access_authorization",
            package_name="git+https://github.com/care-ecosystem/care_state_hmis.git",
            version="@next",
                    configs={}

        ),
        Plug(
        name="encounter_identifiers",
        package_name="git+https://github.com/care-ecosystem/care_state_hmis.git",
        version="@next",
               configs={}

    ),
    Plug(
        name="patient_demographics",
        package_name="git+https://github.com/care-ecosystem/care_state_hmis.git",
        version="@next",
        configs={"HMIS_EXTENSIONS_ENABLE_LOCATION_KIND":"True","HMIS_EXTENSIONS_ENABLE_ATTENDER":"True","HMIS_EXTENSIONS_LOCATION_REQUIRED":"True","HMIS_EXTENSIONS_PATIENT_RELIGION_REQUIRED":"True"}
    ),
    Plug(
        name="appointment_invoice_payment",
        package_name="git+https://github.com/care-ecosystem/care_state_hmis.git",
        version="@next",
        configs={}
    ),
    Plug(
        name="invoice_auto_balance",
        package_name="git+https://github.com/care-ecosystem/care_state_hmis.git",
        version="@next",
                configs={}

    ),
    Plug(
        name="care_pinelabs",
        package_name="git+https://github.com/care-ecosystem/care_pinelabs.git",
        version="@main",
        configs={
            "PINELABS_API_BASE_URL": os.getenv(
                "PINELABS_API_BASE_URL"
            ),
            "PINELABS_SECRET_KEY": os.getenv(
                "PINELABS_SECRET_KEY"
            )
        }
    ),
    Plug(
        name="care_dvdms",
        package_name="git+https://github.com/care-ecosystem/care_dvdms.git",
        version="@main",
        configs={
            "DVDMS_API_ENDPOINT": os.getenv(
                "DVDMS_API_ENDPOINT"
            ),
            "DVDMS_AUTH_TOKEN": os.getenv(
                "DVDMS_AUTH_TOKEN"
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
