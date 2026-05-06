"""
analyzer/api/views.py
======================
Responsibility: Handle HTTP request/response for the analyze endpoint.
No business logic here — all analysis is delegated to service.run_analysis().

Endpoints:
    POST /api/analyze/   →  analyze_view()
"""

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from analyzer.service import run_analysis

MAX_FILE_SIZE = 5 * 1024 * 1024    # 5 MB
ALLOWED_TYPES = ['text/plain', 'application/octet-stream']


@csrf_exempt
@require_POST
def analyze_view(request):
    """
    POST /api/analyze/
    Accepts a multipart form upload with key 'resume'.
    Returns JSON with the full analysis result.
    """
    resume_file = request.FILES.get('resume')

    # ── Validation ────────────────────────────────────────────────────────────
    if not resume_file:
        return JsonResponse(
            {'error': 'No file uploaded. Send a .txt file with key "resume".'},
            status=400
        )

    if resume_file.size > MAX_FILE_SIZE:
        return JsonResponse(
            {'error': f'File too large. Maximum size is 5MB.'},
            status=400
        )

    # ── Run analysis pipeline ─────────────────────────────────────────────────
    result = run_analysis(resume_file)

    if 'error' in result:
        return JsonResponse(result, status=422)

    return JsonResponse(result)