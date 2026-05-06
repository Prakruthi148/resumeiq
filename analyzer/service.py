"""
analyzer/service.py
====================
Responsibility: Orchestrate all analysis modules into a single pipeline.
This is the ONLY file that imports from all modules.
Views call this — they never import individual modules directly.

Functions:
    run_analysis(file) → dict  (the full result sent to the frontend)
"""

from .modules.parser        import extract_text, parse_resume
from .modules.scorer        import calculate_score, get_score_label
from .modules.feedback      import get_feedback
from .modules.job_matcher   import get_job_matches
from .modules.career_advisor import get_career_path


def run_analysis(file) -> dict:
    """
    Full resume analysis pipeline.

    Step 1: Extract raw text from uploaded file      (parser)
    Step 2: Parse text into structured data          (parser)
    Step 3: Score the resume 0–100                   (scorer)
    Step 4: Generate AI feedback                     (feedback)
    Step 5: Match to job roles                       (job_matcher)
    Step 6: Suggest career path                      (career_advisor)

    Args:
        file: Django InMemoryUploadedFile from request.FILES

    Returns:
        Full result dict — or {'error': str} on failure
    """
    # Step 1 — Extract text
    text = extract_text(file)
    if not text.strip():
        return {'error': 'Could not read the file. Please upload a .txt file with your resume content.'}

    # Step 2 — Parse
    parsed = parse_resume(text)

    # Step 3 — Score
    score       = calculate_score(parsed)
    score_meta  = get_score_label(score)

    # Step 4 — Feedback
    feedback = get_feedback(parsed, score)

    # Step 5 — Job matches
    job_matches = get_job_matches(parsed['skills'])

    # Step 6 — Career path
    career = get_career_path(job_matches)

    return {
        'score':        score,
        'score_meta':   score_meta,
        'parsed':       parsed,
        'feedback':     feedback,
        'job_matches':  job_matches,
        'career':       career,
    }