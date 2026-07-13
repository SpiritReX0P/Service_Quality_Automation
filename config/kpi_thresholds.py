# ==========================================
# KPI THRESHOLDS
# ==========================================

# -------------------------
# EDC KPI RULES
# -------------------------
EDC_KPI_RULES = {

    # Partial Delivery %
    5: {
        "name": "Partial Delivery %",
        "type": "lower_pct",
        "green": 0.01,
        "yellow": 0.05
    },

    # Day Arrival
    6: {
        "name": "Day Arrival",
        "type": "higher",
        "green": 90,
        "yellow": 85
    },

    # GSL
    7: {
        "name": "GSL",
        "type": "higher",
        "green": 85,
        "yellow": 80
    },

    # GNPS
    8: {
        "name": "GNPS",
        "type": "higher",
        "green": 95,
        "yellow": 90
    },

    # 7+ Undelivered %
    13: {
        "name": "Undelivered %",
        "type": "lower_pct",
        "green": 5,
        "yellow": 10
    },

    # TFD
    14: {
        "name": "TFD",
        "type": "higher",
        "green": 85,
        "yellow": 80
    },

    # TFD Conversion
    15: {
        "name": "TFD Conversion",
        "type": "higher",
        "green": 90,
        "yellow": 85
    },

    # Pickup Conversion
    16: {
        "name": "Pickup Conversion",
        "type": "higher",
        "green": 95,
        "yellow": 90
    }
}


# -------------------------
# ZONE KPI RULES
# (Same KPIs, all shifted one column left)
# -------------------------
ZONE_KPI_RULES = {

    # Partial Delivery %
    4: {
        "name": "Partial Delivery %",
        "type": "lower_pct",
        "green": 0.01,
        "yellow": 0.05
    },

    # Day Arrival
    5: {
        "name": "Day Arrival",
        "type": "higher",
        "green": 90,
        "yellow": 85
    },

    # GSL
    6: {
        "name": "GSL",
        "type": "higher",
        "green": 85,
        "yellow": 80
    },

    # GNPS
    7: {
        "name": "GNPS",
        "type": "higher",
        "green": 95,
        "yellow": 90
    },

    # 7+ Undelivered %
    12: {
        "name": "Undelivered %",
        "type": "lower_pct",
        "green": 5,
        "yellow": 10
    },

    # TFD
    13: {
        "name": "TFD",
        "type": "higher",
        "green": 85,
        "yellow": 80
    },

    # TFD Conversion
    14: {
        "name": "TFD Conversion",
        "type": "higher",
        "green": 90,
        "yellow": 85
    },

    # Pickup Conversion
    15: {
        "name": "Pickup Conversion",
        "type": "higher",
        "green": 95,
        "yellow": 90
    }
}