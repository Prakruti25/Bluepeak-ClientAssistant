def score_lead(budget, timeline, company_size, goal_text):
    score = 0

    # Budget
    score += {"<2k": 0, "2-5k": 2, "5-10k": 4, "10k+": 6}.get(budget, 0)

    # Timeline
    score += {"now": 4, "2-4w": 3, "1-3m": 1}.get(timeline, 0)

    # Company size
    score += {"1-10": 0, "11-50": 1, "51-200": 2, "200+": 3}.get(company_size, 0)

    # Goal fit (very simple heuristic)
    goal = (goal_text or "").lower()
    if any(k in goal for k in ["lead", "pipeline", "demo", "conversion"]):
        score += 3
    else:
        score += 1

    label = "Hot" if score >= 12 else "Warm" if score >= 8 else "Cold"
    return score, label
