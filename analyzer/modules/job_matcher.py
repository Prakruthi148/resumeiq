"""
analyzer/modules/job_matcher.py
================================
Responsibility: Match detected skills against known job role requirements
and return a ranked list of job matches.
No file reading, no scoring, no feedback — only job matching logic.

Functions:
    get_job_matches(skills) → list[dict]
"""


# ─── Job role definitions ──────────────────────────────────────────────────────
# Each role maps to the list of skills that are relevant for it.
# Add or edit roles here without touching anything else.
JOB_ROLES = {
    'Frontend Developer':     ['html', 'css', 'javascript', 'react', 'typescript', 'figma'],
    'Backend Developer':      ['python', 'django', 'node', 'java', 'sql', 'postgresql', 'mongodb'],
    'Full Stack Developer':   ['html', 'css', 'javascript', 'react', 'python', 'django', 'node', 'sql'],
    'Data Scientist':         ['python', 'machine learning', 'data analysis', 'sql'],
    'DevOps Engineer':        ['docker', 'aws', 'linux', 'git'],
    'Mobile Developer':       ['flutter', 'kotlin', 'javascript', 'react'],
    'UI/UX Designer':         ['figma', 'photoshop', 'css', 'html'],
    'Database Administrator': ['sql', 'postgresql', 'mongodb'],
    'Cloud Engineer':         ['aws', 'docker', 'linux', 'kubernetes', 'terraform'],
    'Software Engineer':      ['python', 'java', 'c++', 'c#', 'git', 'agile'],
}

TOP_N_MATCHES = 5   # How many matches to return


def get_job_matches(skills: list) -> list:
    """
    Compare a list of detected skills against all known job roles.
    Returns the top matches sorted by match percentage (highest first).

    Args:
        skills: list of skill strings (from parser.parse_resume)

    Returns:
        list of dicts, each containing:
            role:            str   — job title
            match_percent:   int   — 0–100
            matched_skills:  list  — skills you already have
            missing_skills:  list  — skills the role needs but you lack
    """
    matches = []

    for role, required_skills in JOB_ROLES.items():
        matched  = [s for s in required_skills if s in skills]
        missing  = [s for s in required_skills if s not in skills]

        if not matched:
            continue    # Skip roles with zero overlap

        percent = int((len(matched) / len(required_skills)) * 100)

        matches.append({
            'role':           role,
            'match_percent':  percent,
            'matched_skills': matched,
            'missing_skills': missing,
        })

    # Sort by match % descending, return top N
    matches.sort(key=lambda m: m['match_percent'], reverse=True)
    return matches[:TOP_N_MATCHES]