import win32com.client

from config.settings import DRAFT_MODE


def get_outlook():

    outlook = win32com.client.Dispatch(
        "Outlook.Application"
    )

    return outlook


def create_email_draft(package):

    outlook = get_outlook()

    mail = outlook.CreateItem(0)

    mail.To = package["to"]

    mail.CC = package["cc"]

    mail.Subject = package["subject"]
        
    mail.HTMLBody = package["body"]

    mail.Attachments.Add(
        str(package["attachment"])
    )

    if DRAFT_MODE:
        mail.Save()
    else:
        mail.Send()

    print(
        f"Draft Created : {package['subject']}"
    )