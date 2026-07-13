#==============================================================

from src.report_generator import load_master_workbook
from src.excel_template import create_zone_template
from src.excel_template import create_edc_template
from config.report_config import (
    ZONE_FILES,
    EDC_FILES
)
from src.report_generator import (
    load_master_workbook,
    get_zone_data,
    get_edc_data,
    populate_zone_report,
    populate_edc_report,
    populate_all_zone_reports,
    populate_all_edc_reports
)
from config.settings import MASTER_REPORT_FILE

# ==========================================
# CREATE ALL ZONE TEMPLATES
# ==========================================
for zone, file_path in ZONE_FILES.items():

    create_zone_template(file_path)

    print(f"{zone} created")

# ==========================================
# CREATE ALL EDC TEMPLATES
# ==========================================
for edc, file_path in EDC_FILES.items():

    create_edc_template(file_path)

    print(f"{edc} created")

#=============================================

# MASTER_FILE = r"data\Master_Report.xlsx"

edc_df, gdw_df = load_master_workbook(
    MASTER_REPORT_FILE
)

#edc_df, gdw_df = load_master_workbook(MASTER_FILE)

populate_all_zone_reports(edc_df)

populate_all_edc_reports(gdw_df)

print("\n===== PERCENTAGE CHECK =====")

print(edc_df["%age"].iloc[0])
print(type(edc_df["%age"].iloc[0]))

print(edc_df["Day Arrival"].iloc[0])
print(type(edc_df["Day Arrival"].iloc[0]))

print("\n===== EDC SHEET =====")
print(edc_df.head())

print("\n===== GDW SHEET =====")
print(gdw_df.head())

print("\n===== EDC COLUMNS =====")
print(edc_df.columns.tolist())

print("\n===== GDW COLUMNS =====")
print(gdw_df.columns.tolist())



#============================================================================================


from src.email_config_loader import load_email_config
from src.email_subjects import (
    get_zone_subject,
    get_edc_subject
)

from src.email_generator import (
    excel_to_html_table
)

from src.email_generator import build_email_body

from config.report_config import (
    ZONE_FILES,
    EDC_FILES
)

from config.zone_mapping import (
    EDC_ZONE_MAPPING
)

from pathlib import Path

from src.email_generator import build_email_body

from src.email_package_builder import (
    build_email_package
)


from src.outlook_sender import create_email_draft

print("\n===== EMAIL CONFIG =====")
print(load_email_config().head())

print("\n===== SUBJECT TEST =====")
print(get_zone_subject("BLRZS"))
print(get_edc_subject("BLRZS", "EBLRN"))

print("\n===== HTML TEST =====")
html = excel_to_html_table(
    ZONE_FILES["BLRZS"]
)
print(html[:1000])


print("\n======EMAIL BODY TEST=======")
body = build_email_body(
    ZONE_FILES["BLRZS"]
)

with open(
    "test_email.html",
    "w",
    encoding="utf-8"
) as f:
    f.write(body)

print("HTML file created")


print("\n========== ALL EMAILS ==========\n")

df = load_email_config()

for _, row in df.iterrows():

    if row["TYPE"] == "Zone":

        zone = row["ZONE"]

        print("=" * 80)

        print("TYPE       :", "Zone")
        print("ZONE       :", zone)
        print("SUBJECT    :", get_zone_subject(zone))
        print("ATTACHMENT :", ZONE_FILES[zone])

    elif row["TYPE"] == "EDC":

        edc = row["EDC"]

        zone = EDC_ZONE_MAPPING[edc]

        print("=" * 80)

        print("TYPE       :", "EDC")
        print("ZONE       :", zone)
        print("EDC        :", edc)
        print("SUBJECT    :", get_edc_subject(zone, edc))
        print("ATTACHMENT :", EDC_FILES[edc])


print("\n========== FINAL VALIDATION ==========\n")

missing_files = []

for _, row in df.iterrows():

    if row["TYPE"] == "Zone":

        file_path = ZONE_FILES[row["ZONE"]]

    else:

        file_path = EDC_FILES[row["EDC"]]

    if not Path(file_path).exists():

        missing_files.append(file_path)

if len(missing_files) == 0:

    print("SUCCESS")
    print("All attachments found")

else:

    print("MISSING FILES")

    for f in missing_files:

        print(f)        


print("\n========== GENERATING ALL PREVIEWS ==========\n")

preview_count = 0

for _, row in df.iterrows():

    if row["TYPE"] == "Zone":

        zone = row["ZONE"]

        report_file = ZONE_FILES[zone]

        body = build_email_body(report_file)

        filename = (
            f"output/email_preview/"
            f"Zone_{zone}.html"
        )

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(body)

        print(f"Created -> {filename}")

        preview_count += 1

    elif row["TYPE"] == "EDC":

        zone = row["ZONE"]
        edc = row["EDC"]

        report_file = EDC_FILES[edc]

        body = build_email_body(report_file)

        filename = (
            f"output/email_preview/"
            f"EDC_{zone}_{edc}.html"
        )

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(body)

        print(f"Created -> {filename}")

        preview_count += 1

print("\nTOTAL PREVIEWS :", preview_count)


print("\n========== PACKAGE TEST ==========\n")

zone_row = df[
    df["TYPE"] == "Zone"
].iloc[0]

zone_package = build_email_package(
    zone_row
)

print(zone_package)


print("\n========== EDC PACKAGE TEST ==========\n")

edc_row = df[
    df["TYPE"] == "EDC"
].iloc[0]

edc_package = build_email_package(
    edc_row
)

print(edc_package)


print("\n========== ALL EMAIL PACKAGES ==========\n")

all_packages = []

for _, row in df.iterrows():

    package = build_email_package(row)

    all_packages.append(package)

print(f"TOTAL PACKAGES : {len(all_packages)}")


print("\n========== SAMPLE PACKAGES ==========\n")

for package in all_packages[:]:

    print("=" * 80)

    print("TYPE       :", package["type"])
    print("ZONE       :", package["zone"])
    print("EDC        :", package["edc"])
    print("SUBJECT    :", package["subject"])
    print("ATTACHMENT :", package["attachment"])


print("\n========== CREATING OUTLOOK DRAFTS ==========\n")

draft_count = 0

for _, row in df.iterrows():

    package = build_email_package(row)

    create_email_draft(package)

    draft_count += 1

print(f"\nTOTAL DRAFTS CREATED : {draft_count}")