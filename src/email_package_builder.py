from src.email_generator import build_email_body

from src.email_subjects import (
    get_zone_subject,
    get_edc_subject
)

from config.report_config import (
    ZONE_FILES,
    EDC_FILES
)

from config.zone_mapping import (
    EDC_ZONE_MAPPING
)

def build_email_package(row):

    email_package = {}

    if row["TYPE"] == "Zone":

        zone = row["ZONE"]

        email_package["type"] = "Zone"
        email_package["zone"] = zone
        email_package["edc"] = None

        email_package["to"] = row["TO"]
        email_package["cc"] = row["CC"]

        email_package["subject"] = get_zone_subject(zone)

        report_file = ZONE_FILES[zone]

        email_package["attachment"] = report_file

        email_package["body"] = build_email_body(
            report_file
        )

    elif row["TYPE"] == "EDC":

        zone = row["ZONE"]
        edc = row["EDC"]

        email_package["type"] = "EDC"
        email_package["zone"] = zone
        email_package["edc"] = edc

        email_package["to"] = row["TO"]
        email_package["cc"] = row["CC"]

        email_package["subject"] = get_edc_subject(
            zone,
            edc
        )

        report_file = EDC_FILES[edc]

        email_package["attachment"] = report_file

        email_package["body"] = build_email_body(
            report_file
        )
    return email_package