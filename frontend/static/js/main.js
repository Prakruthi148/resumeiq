/**
 * frontend/static/js/main.js
 * ===========================
 * Responsibility: Orchestrate the full user interaction flow.
 * Imports from: upload.js (file picking), api.js (HTTP), renderer.js (DOM)
 *
 * This is the ONLY file that ties everything together.
 * Keep it small — delegate to the modules above.
 */

/**
 * Called when the user clicks "Analyze My Resume".
 * Wired directly in the HTML: onclick="analyzeResume()"
 */
async function analyzeResume() {
    const file = document.getElementById('resumeInput').files[0];

    if (!file) {
        showError('Please select a file first.');
        return;
    }

    // ── Show loading state ─────────────────────────────────────────────────
    document.getElementById('results').style.display = 'none';
    document.getElementById('analyzeBtn').disabled = true;
    setUploadOpacity(true);
    showLoader(true);

    try {
        // ── Call API ───────────────────────────────────────────────────────
        const data = await uploadResume(file);    // api.js

        showLoader(false);
        setUploadOpacity(false);
        document.getElementById('analyzeBtn').disabled = false;

        if (data.error) {
            showError(data.error);                // renderer.js
            return;
        }

        // ── Render results ─────────────────────────────────────────────────
        renderResults(data);                      // renderer.js

    } catch (err) {
        showLoader(false);
        setUploadOpacity(false);
        document.getElementById('analyzeBtn').disabled = false;
        showError('Something went wrong. Make sure the Django server is running on port 8000.');
        console.error('[main.js] Error:', err);
    }
}