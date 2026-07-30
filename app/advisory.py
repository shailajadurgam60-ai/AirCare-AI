def get_health_advisory(aqi):

    if aqi == 1:
        return {
            "General Public": "✅ Enjoy outdoor activities without restrictions.",
            "Children": "🟢 Safe to play outdoors.",
            "Elderly": "🟢 Outdoor walks are generally safe.",
            "Respiratory Patients": "🟢 Air quality is favorable."
        }

    elif aqi == 2:
        return {
            "General Public": "🙂 Air quality is acceptable.",
            "Children": "🟡 Sensitive children should avoid prolonged outdoor activity.",
            "Elderly": "🟡 Take short breaks during long outdoor walks.",
            "Respiratory Patients": "🟡 Carry medication if needed."
        }

    elif aqi == 3:
        return {
            "General Public": "⚠️ Reduce prolonged outdoor exercise.",
            "Children": "🟠 Limit outdoor play during peak hours.",
            "Elderly": "🟠 Avoid long outdoor exposure.",
            "Respiratory Patients": "🟠 Wear a mask and avoid strenuous activity."
        }

    elif aqi == 4:
        return {
            "General Public": "🔴 Avoid prolonged outdoor exposure.",
            "Children": "🔴 Stay indoors when possible.",
            "Elderly": "🔴 Avoid outdoor activities.",
            "Respiratory Patients": "🔴 Stay indoors and follow medical advice."
        }

    else:
        return {
            "General Public": "⚫ Stay indoors as much as possible.",
            "Children": "⚫ Outdoor activities are not recommended.",
            "Elderly": "⚫ Remain indoors.",
            "Respiratory Patients": "⚫ Avoid outdoor exposure completely."
        }