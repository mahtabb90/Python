CHAKRAS = {
    "root": "Trygghet, stabilitet. Ex: lugn andning, jordning.",
    "sacral": "Känslor, kreativitet. Ex: kroppsscanning, mjuk närvaro.",
    "solar plexus": "Vilja, självkänsla. Ex: fokusmeditation, affirmation.",
    "heart": "Medkänsla, kärlek. Ex: loving-kindness (metta).",
    "throat": "Kommunikation, sanning. Ex: mantra, medveten röst.",
    "third eye": "Intuition, klarhet. Ex: visualization, stillhet.",
    "crown": "Andlighet, helhet. Ex: tyst meditation, kontemplation.",
}

def describe(chakra: str) -> str:
    return CHAKRAS.get(chakra, "Okänd chakra.")
