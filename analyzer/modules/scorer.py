"""
analyzer/modules/scorer.py
===========================
Responsibility: Calculate a numeric score (0–100) from parsed resume data.
No file I/O, no feedback text, no job data — only scoring logic.

Functions:
    calculate_score(parsed) → int
    get_score_label(score)  → dict
"""


# ─── Points awarded per section ───────────────────────────────────────────────
SECTION_POINTS = {
    'has_contact':      10,
    'has_summary':      10,
    'has_education':    15,
    'has_experience':   20,
    'has_projects':     15,
    'has_achievements': 10,
}

MAX_SKILL_POINTS = 20       # Cap: 2 pts per skill, max 20
POINTS_PER_SKILL = 2

IDEAL_WORD_MIN = 300
IDEAL_WORD_MAX = 800
BONUS_WORD_POINTS = 10      # Awarded for ideal length
PARTIAL_WORD_POINTS = 5     # Awarded for near-ideal length


def calculate_score(parsed: dict) -> int:
    """
    Score the resume out of 100 based on:
      - Present sections (contact, summary, education, etc.)
      - Number of detected skills (capped)
      - Word count (ideal range gets bonus)

    Args:
        parsed: Output from parser.parse_resume()

    Returns:
        Integer score from 0 to 100
    """
    score = 0

    # Section scores
    for section_key, points in SECTION_POINTS.items():
        if parsed.get(section_key):
            score += points

    # Skill score (2 pts each, max 20)
    skill_count = len(parsed.get('skills', []))
    score += min(skill_count * POINTS_PER_SKILL, MAX_SKILL_POINTS)

    # Word count bonus
    wc = parsed.get('word_count', 0)
    if IDEAL_WORD_MIN <= wc <= IDEAL_WORD_MAX:
        score += BONUS_WORD_POINTS
    elif (200 <= wc < IDEAL_WORD_MIN) or (IDEAL_WORD_MAX < wc <= 1000):
        score += PARTIAL_WORD_POINTS

    return min(score, 100)


def get_score_label(score: int) -> dict:
    """
    Convert a numeric score into a human-readable label and description.

    Returns:
        { label: str, description: str, color: str }
    """
    if score >= 80:
        return {'label': 'Excellent',   'description': '🏆 You have a strong, competitive resume!',     'color': 'success'}
    elif score >= 60:
        return {'label': 'Good',        'description': '👍 Solid resume with room to improve.',          'color': 'accent'}
    elif score >= 40:
        return {'label': 'Average',     'description': '📊 Some areas need attention.',                  'color': 'warning'}
    elif score >= 20:
        return {'label': 'Weak',        'description': '⚠️ Several key sections are missing.',           'color': 'warning'}
    else:
        return {'label': 'Needs Work',  'description': '🔴 Your resume needs significant improvements.', 'color': 'danger'}