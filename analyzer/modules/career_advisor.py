"""
analyzer/modules/career_advisor.py
====================================
Responsibility: Suggest a career progression path based on the top job match.
No file reading, no scoring, no feedback — only career path logic.

Functions:
    get_career_path(job_matches) → dict
"""


# ─── Career path map ──────────────────────────────────────────────────────────
# Maps a job role to a 3-step progression + recommended skills to learn.
# Edit or add new paths here without touching anything else.
CAREER_PATHS = {
    'Frontend Developer': {
        'current':  'Junior Frontend Developer',
        'next':     'Senior Frontend Developer',
        'advanced': 'Frontend Architect / Engineering Manager',
        'learn':    ['TypeScript', 'Testing (Jest)', 'Performance Optimization', 'Accessibility (WCAG)'],
    },
    'Backend Developer': {
        'current':  'Junior Backend Developer',
        'next':     'Senior Backend Developer',
        'advanced': 'Backend Architect / CTO',
        'learn':    ['System Design', 'Microservices', 'Redis/Caching', 'CI/CD Pipelines'],
    },
    'Full Stack Developer': {
        'current':  'Junior Full Stack Developer',
        'next':     'Senior Full Stack Developer',
        'advanced': 'Tech Lead / Solutions Architect',
        'learn':    ['Cloud (AWS/GCP)', 'System Design', 'Docker & Kubernetes', 'GraphQL'],
    },
    'Data Scientist': {
        'current':  'Junior Data Analyst',
        'next':     'Data Scientist',
        'advanced': 'Lead Data Scientist / ML Engineer',
        'learn':    ['Deep Learning', 'MLOps', 'Big Data (Spark)', 'Statistical Modeling'],
    },
    'DevOps Engineer': {
        'current':  'Junior DevOps Engineer',
        'next':     'DevOps Engineer',
        'advanced': 'Platform Engineer / SRE Lead',
        'learn':    ['Kubernetes', 'Terraform', 'Prometheus/Grafana', 'Security Hardening'],
    },
    'Mobile Developer': {
        'current':  'Junior Mobile Developer',
        'next':     'Mobile Developer',
        'advanced': 'Senior Mobile Engineer / App Architect',
        'learn':    ['CI/CD for Mobile', 'State Management', 'App Store Optimization', 'Native APIs'],
    },
    'UI/UX Designer': {
        'current':  'Junior UI/UX Designer',
        'next':     'UX Designer',
        'advanced': 'Lead Designer / Head of Product Design',
        'learn':    ['User Research', 'Prototyping', 'Design Systems', 'Motion Design'],
    },
    'Cloud Engineer': {
        'current':  'Junior Cloud Engineer',
        'next':     'Cloud Engineer',
        'advanced': 'Cloud Architect / Platform Lead',
        'learn':    ['Multi-cloud Strategy', 'FinOps', 'Zero Trust Security', 'IaC (Terraform)'],
    },
    'Software Engineer': {
        'current':  'Junior Software Engineer',
        'next':     'Software Engineer',
        'advanced': 'Senior Engineer / Technical Lead',
        'learn':    ['System Design', 'Distributed Systems', 'Code Review Culture', 'Mentoring'],
    },
}

DEFAULT_PATH = {
    'current':  'Junior Developer',
    'next':     'Mid-level Developer',
    'advanced': 'Senior Developer / Tech Lead',
    'learn':    ['System Design', 'Cloud Computing', 'CI/CD', 'Leadership Skills'],
}


def get_career_path(job_matches: list) -> dict:
    """
    Return a career progression path based on the highest-matched job role.

    Args:
        job_matches: Output from job_matcher.get_job_matches()

    Returns:
        {
            top_role: str,
            path: {
                current:  str,
                next:     str,
                advanced: str,
                learn:    list[str],
            }
        }
    """
    top_role = job_matches[0]['role'] if job_matches else 'Software Engineer'
    path = CAREER_PATHS.get(top_role, DEFAULT_PATH)

    return {
        'top_role': top_role,
        'path': path,
    }