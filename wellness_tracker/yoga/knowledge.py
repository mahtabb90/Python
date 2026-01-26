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

def describe_yoga(yoga_type: str) -> str:
    data = YOGA_STYLES.get(yoga_type)

    if not data:
        return f"{yoga_type}: Ingen beskrivning tillgänglig."

    return (
        f"\n🧘‍♀️ {yoga_type}\n"
        f"Beskrivning: {data['description']}\n"
        f"Fokus: {data['focus']}\n"
        f"Hur: {data['how']}\n"
    )

    
def list_yoga_styles() -> list[str]:
    """Returnerar alla tillgängliga yogastilar."""
    return sorted(YOGA_STYLES.keys())
