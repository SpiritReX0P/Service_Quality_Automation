#===================================
#FILE STORING:---(STATIC CONTENT)
#EMAIL_GREETING
#EMAIL_NOTES
#PARAMETER_TABLE_HTML
#SIGNATURE_HTML
#DRIVE_LINK
#===================================

# ==========================================
# EMAIL GREETING
# ==========================================

EMAIL_GREETING = """
Dear All,

Please find below a summary of key insights from the latest Service Quality Improvement data:
"""


# ==========================================
# EMAIL NOTE 
# ==========================================

EMAIL_NOTE = """
<b>Note:</b><br><br>

In data, Day Arrival, GSL, and GNPS is calculated from 1st of Month to *(N-2)* days based on the available snapshot data,<br>
and all other parameters are reported MTD up to the previous day *(N-1)*.
"""

# ==========================================
# PARAMETER TABLE
# ==========================================

PARAMETER_TABLE_HTML = """
<br><br>

<table border="1"
       cellspacing="0"
       cellpadding="4"
       style="border-collapse:collapse;
              font-family:Calibri;
              font-size:11pt;">

<tr>
    <th style="background-color:#d9d9d9;">Parameters</th>
    <th style="background-color:#d9d9d9;">YTD/MTD</th>
    <th style="background-color:#d9d9d9;">Explanation</th>
</tr>

<tr style="background-color:#f4cccc;">
    <td>Partial Deliveries</td>
    <td>YTD</td>
    <td>Total number of partial deliveries out of total deliveries</td>
</tr>

<tr style="background-color:#b6d7a8;">
    <td>GSL</td>
    <td>MTD</td>
    <td>Dockets to be delivered within original ADD</td>
</tr>

<tr style="background-color:#a2c4c9;">
    <td>GNPS</td>
    <td>MTD</td>
    <td>GSL + customer/external NDR</td>
</tr>

<tr style="background-color:#9fc5e8;">
    <td>Undelivered</td>
    <td>YTD</td>
    <td>YTD not delivered and still lying in the delivery cycle</td>
</tr>

<tr style="background-color:#ffd966;">
    <td>TFD</td>
    <td>PD</td>
    <td>TFD against stock (if stock + till 12 am stock of last working day)</td>
</tr>

<tr style="background-color:#f6b26b;">
    <td>TFD Conversion</td>
    <td>MTD</td>
    <td>Total delivered out of all TFD</td>
</tr>

<tr style="background-color:#d5a6bd;">
    <td>PU Conversion</td>
    <td>MTD</td>
    <td>Ontime pickups out of total pickup funnel requests</td>
</tr>

</table>
"""

# ==========================================
# DRIVE LINK
# ==========================================

DRIVE_LINK = "https://allcargologisticsltd-my.sharepoint.com/:f:/r/personal/amr_66424_allcargogati_com/Documents/Data_Analytics_Projects/Random%20Work/MIS%20requests/3.shared/Service_Quality_Improvement_Drive?csf=1&web=1&e=gHi6FR"


# ==========================================
# SIGNATURE
# ==========================================

EMAIL_SIGNATURE = """
<br><br>

Regards,<br><br>

Vaibhav Kumar Sharma<br>
Business Analyst - Data Analytics, CoE<br>

<b>ALLCARGO LOGISTICS LIMITED</b><br><br>

M: +91 8506881810<br>
E: vaibhavkumar.sharma@allcargologistics.com<br><br>

<a href="https://www.allcargologistics.com">
www.allcargologistics.com
</a>

<br><br>

<a href="https://www.linkedin.com/company/allcargogati/">LinkedIn</a> |
<a href="https://www.facebook.com/gatilimited">Facebook</a> |
<a href="https://www.instagram.com/gatiltd/">Instagram</a> |
<a href="https://x.com/GATIKWEIndia">X</a> |
<a href="https://www.youtube.com/channel/UCYo7sIFSRC9AWWw7becHTIw">YouTube</a>
"""  