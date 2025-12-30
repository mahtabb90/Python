YOGA_STYLES = {
    "Yin": {
        "description": "Långsamma positioner som hålls länge.",
        "focus": "Bindväv, lugn, återhämtning.",
        "how": "Andas lugnt, slappna av i musklerna."
    },
    "Hatha": {
        "description": "Klassisk yoga i lugnt tempo.",
        "focus": "Balans mellan styrka och rörlighet.",
        "how": "Utför positioner kontrollerat."
    },
    "Flow": {
        "description": "Dynamisk yoga med flyt mellan positioner.",
        "focus": "Styrka, puls och fokus.",
        "how": "Synkronisera rörelse med andetag."
    },
    "Vinyasa": {
        "description": "Kreativ och flödande yoga.",
        "focus": "Kondition, koordination.",
        "how": "Rör dig mjukt mellan positioner."
    },
}

def describe_yoga(style: str) -> str:
    info = YOGA_STYLES.get(style)
    if not info:
        return "Okänd yogatyp."
    return (
        f"{style}\n"
        f"Beskrivning: {info['description']}\n"
        f"Fokus: {info['focus']}\n"
        f"Hur: {info['how']}"
    )
