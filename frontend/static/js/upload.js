/**
 * frontend/static/js/upload.js
 * ==============================
 * Responsibility: Handle file selection, drag-and-drop, and upload button state.
 * No analysis logic — just UI for file input.
 */

const dropZone   = document.getElementById('dropZone');
const fileInput  = document.getElementById('resumeInput');
const fileNameEl = document.getElementById('fileName');
const analyzeBtn = document.getElementById('analyzeBtn');

/** Show selected filename and reveal the Analyze button */
function onFileSelected(file) {
    if (!file) return;
    fileNameEl.textContent = '📎 ' + file.name;
    fileNameEl.style.display = 'block';
    analyzeBtn.style.display = 'inline-block';
    document.getElementById('errorMsg').style.display = 'none';
}

// ── File input change ──────────────────────────────────────────────────────
fileInput.addEventListener('change', () => {
    if (fileInput.files[0]) onFileSelected(fileInput.files[0]);
});

// ── Drag & Drop ────────────────────────────────────────────────────────────
dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropZone.classList.add('drag-over');
});

dropZone.addEventListener('dragleave', () => {
    dropZone.classList.remove('drag-over');
});

dropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropZone.classList.remove('drag-over');
    const file = e.dataTransfer.files[0];
    if (file) {
        // Inject into the native file input so analyzeResume() can read it
        const dt = new DataTransfer();
        dt.items.add(file);
        fileInput.files = dt.files;
        onFileSelected(file);
    }
});