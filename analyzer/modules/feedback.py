"""
analyzer/modules/feedback.py
=============================
Responsibility: Generate human-readable AI feedback from parsed resume data.
No file reading, no scoring, no job data — only feedback generation.

Functions:
    get_feedback(parsed, score) → dict with strengths, weaknesses, suggestions
"""


def get_feedback(parsed: dict, score: int) -> dict:
    """
    Analyze parsed resume data and return structured feedback.

    Args:
        parsed: Output from parser.parse_resume()
        score:  Output from scorer.calculate_score()

    Returns:
        {
            strengths:   list[str],
            weaknesses:  list[str],
            suggestions: list[str],
        }
    """
    strengths   = []
    weaknesses  = []
    suggestions = []

    # ── Contact ──────────────────────────────────────────────────────────────
    if parsed.get('has_contact'):
        strengths.append("Contact information is clearly present.")
    else:
        weaknesses.append("Missing contact details (email, phone, LinkedIn).")
        suggestions.append("Add your email, phone number, and LinkedIn/GitHub profile links at the top.")

    # ── Summary ───────────────────────────────────────────────────────────────
    if parsed.get('has_summary'):
        strengths.append("Professional summary gives recruiters a quick overview.")
    else:
        weaknesses.append("No professional summary or objective found.")
        suggestions.append("Write a 3–4 sentence summary highlighting your expertise and career goal.")

    # ── Experience ────────────────────────────────────────────────────────────
    if parsed.get('has_experience'):
        strengths.append("Work experience section detected — great for demonstrating background.")
    else:
        weaknesses.append("No work experience section found.")
        suggestions.append("Add internships, freelance work, or part-time jobs even if limited.")

    # ── Education ─────────────────────────────────────────────────────────────
    if parsed.get('has_education'):
        strengths.append("Education section is present.")
    else:
        weaknesses.append("Education section is missing.")
        suggestions.append("Include your degree, institution name, and graduation year.")

    # ── Projects ──────────────────────────────────────────────────────────────
    if parsed.get('has_projects'):
        strengths.append("Projects section shows hands-on ability — employers love this.")
    else:
        weaknesses.append("No projects section found.")
        suggestions.append("Add 2–3 personal or academic projects with descriptions and GitHub links.")

    # ── Achievements ──────────────────────────────────────────────────────────
    if parsed.get('has_achievements'):
        strengths.append("Awards and certifications boost your credibility.")
    else:
        suggestions.append("Add certifications, awards, or notable achievements to stand out.")

    # ── Skills ────────────────────────────────────────────────────────────────
    skill_count = len(parsed.get('skills', []))
    if skill_count >= 8:
        strengths.append(f"Strong skills profile with {skill_count} recognized technologies.")
    elif skill_count >= 4:
        strengths.append(f"{skill_count} skills detected — a decent foundation.")
    else:
        weaknesses.append("Very few technical skills detected.")
        suggestions.append("List relevant technical and soft skills in a dedicated Skills section.")

    # ── Word Count ────────────────────────────────────────────────────────────
    wc = parsed.get('word_count', 0)
    if wc < 200:
        weaknesses.append(f"Resume is too short ({wc} words). Recruiters may see this as underdeveloped.")
        suggestions.append("Expand your resume to at least 300–500 words with more detail in each section.")
    elif wc > 900:
        weaknesses.append(f"Resume is quite long ({wc} words). Consider trimming for readability.")
        suggestions.append("Keep your resume concise — ideally 1 page for under 5 years of experience.")
    else:
        strengths.append(f"Good resume length ({wc} words) — easy to read.")

    # ── Universal Tips ────────────────────────────────────────────────────────
    suggestions.extend([
        "Use strong action verbs like 'Developed', 'Led', 'Optimized', 'Designed'.",
        "Quantify achievements where possible (e.g., 'Improved load time by 40%').",
        "Tailor your resume keywords to match each job description (ATS optimization).",
    ])

    return {
        'strengths':   strengths,
        'weaknesses':  weaknesses,
        'suggestions': suggestions,
    }