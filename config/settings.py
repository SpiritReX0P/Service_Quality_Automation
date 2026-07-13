from pathlib import Path

# ==========================================
# PROJECT ROOT
# ==========================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ==========================================
# DATA FILES
# ==========================================

MASTER_REPORT_FILE = (
    PROJECT_ROOT / "data" / "Master_Report.xlsx"
)

EMAIL_RECIPIENT_FILE = (
    PROJECT_ROOT / "data" / "email_recipients.xlsx"
)

# ==========================================
# OUTPUT
# ==========================================

OUTPUT_FOLDER = PROJECT_ROOT / "output"

ZONE_OUTPUT_FOLDER = (
    OUTPUT_FOLDER / "Zones"
)

EMAIL_PREVIEW_FOLDER = (
    OUTPUT_FOLDER / "email_preview"
)

# ==========================================
# EMAIL
# ==========================================

DRAFT_MODE = False