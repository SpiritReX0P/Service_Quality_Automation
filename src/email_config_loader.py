import pandas as pd
from config.settings import EMAIL_RECIPIENT_FILE

def load_email_config():

    df = pd.read_excel(
        EMAIL_RECIPIENT_FILE
    )
    # df = pd.read_excel(
    #     "data/email_recipients.xlsx"
    # )

    df = df[
        df["ACTIVE"].astype(str).str.upper() == "Y"
    ]

    return df