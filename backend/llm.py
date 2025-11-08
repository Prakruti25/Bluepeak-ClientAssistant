def generate_summary(data, score, label):
    company = data.get("company") or "Unknown company"
    website = data.get("website") or "n/a"
    service = data.get("service") or "marketing help"
    budget = data.get("budget") or "unspecified budget"
    timeline = data.get("timeline") or "unspecified timeline"
    goal = data.get("goal") or "No specific goal given"

    lines = [
        f"Company: {company} ({website})",
        f"Need: {service}",
        f"Budget & timeline: {budget}, starting {timeline}",
        f"Goal: {goal}",
        f"Lead quality: {label} ({score}/16)."
    ]
    return "\n".join(lines)
