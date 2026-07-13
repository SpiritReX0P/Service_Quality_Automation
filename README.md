# Service Quality Automation

## Overview

This project automates the complete Service Quality reporting and email distribution process.

The automation performs the following tasks:

1. Reads the Master Report.
2. Generates Zone-wise reports.
3. Generates EDC-wise reports.
4. Creates HTML email content.
5. Builds email packages (To, CC, Subject, Body, Attachment).
6. Creates Outlook email drafts and sends emails automatically.
7. Distributes reports to the configured recipients.

---

# Project Structure

```
Service_Quality_Automation
│
├── config
│   ├── settings.py
│   ├── report_config.py
│   ├── zone_mapping.py
│   └── email_template.py
│
├── data
│   ├── Master_Report.xlsx
│   └── email_recipients.xlsx
│
├── output
│   ├── Zones
│   ├── North
│   ├── South
│   ├── East
│   ├── West
│   └── email_preview
│
├── src
│   ├── report_generator.py
│   ├── excel_template.py
│   ├── email_generator.py
│   ├── email_subjects.py
│   ├── email_config_loader.py
│   ├── email_package_builder.py
│   └── outlook_sender.py
│
|
├── main_test.py
├── requirements.txt (libraries)
└── README.md
```

---

# Process Flow

```
Master_Report.xlsx
        │
        ▼
Load Master Workbook
        │
        ▼
Generate Zone Reports
        │
        ▼
Generate EDC Reports
        │
        ▼
Build Email Content
        │
        ▼
Build Email Packages
        │
        ▼
Create Outlook Drafts
        │
        ▼
Send Emails
```

---

# Installation

## Step 1 - Install Python

Install Python 3.13 (recommended).

Verify installation:

```bash
python --version
```

---

## Step 2 - Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## Step 3 - Install Outlook Desktop

Microsoft Outlook Desktop must be installed and configured.

The mailbox must be able to:

* Open Outlook
* Create Drafts
* Send Emails

---

# Configuration

## Master Report

Replace:

```
data/Master_Report.xlsx
```

with the latest report before execution.

---

## Email Recipient Configuration

Update:

```
data/email_recipients.xlsx
```

Columns:

| TYPE | ZONE | EDC | TO | CC | ACTIVE |
| ---- | ---- | --- | -- | -- | ------ |

ACTIVE must be:

```
Y
```

for emails to be processed.

---

## Settings

Open:

```
config/settings.py
```

### Draft Mode

For testing:

```python
DRAFT_MODE = True
```

Creates Outlook Drafts only.

For production:

```python
DRAFT_MODE = False
```

Sends emails automatically.

---

# Execution

## Test Mode

```bash
python main_test.py
```

Validates:

* Email configuration
* Attachments
* HTML generation
* Email package creation
* Outlook draft creation

---

## Production Mode

```bash
python main.py
```

Performs:

* Report generation
* Email package generation
* Outlook draft creation / sending

---

# Output Folders

Zone Reports:

```
output/Zones
```

EDC Reports:

```
output/North
output/South
output/East
output/West
```

Email Preview Files:

```
output/email_preview
```

---

# Deployment to New System

1. Copy complete project folder.
2. Install Python.
3. Install Outlook Desktop.
4. Install requirements:

```bash
pip install -r requirements.txt
```

5. Replace:

```
data/Master_Report.xlsx
```

6. Verify:

```
data/email_recipients.xlsx
```

7. Set:

```python
DRAFT_MODE = True
```

8. Run:

```bash
python main_test.py
```

9. Verify Outlook Drafts.

10. Set:

```python
DRAFT_MODE = False
```

11. Run:

```bash
python main.py
```

---

# Author

Service Quality Automation Project

Version: 1.0
