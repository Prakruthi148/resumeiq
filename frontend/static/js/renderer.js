/**
 * frontend/static/js/renderer.js
 * ================================
 * Responsibility: Take the API result object and render all UI sections.
 * No API calls, no file handling — only DOM manipulation.
 *
 * Exported functions (used by main.js):
 *   renderResults(data)
 *   showError(msg)
 *   showLoader(visible)
 *   setUploadOpacity(dim)
 */

// ── Helpers ────────────────────────────────────────────────────────────────

function animateNumber(elementId, target) {
    const el = document.getElementById(elementId);
    let current = 0;
    const step = target / 60;
    const timer = setInterval(() => {
        current = Math.min(current + step, target);
        el.textContent = Math.round(current);
        if (current >= target) clearInterval(timer);
    }, 16);
}

function tag(text, cls) {
    return `<span class="tag ${cls}">${text}</span>`;
}

function feedbackItem(text, dotCls, icon) {
    return `<li><div class="dot ${dotCls}">${icon}</div><div>${text}</div></li>`;
}

// ── Score ring ─────────────────────────────────────────────────────────────

function renderScoreRing(score, scoreMeta) {
    const circumference = 2 * Math.PI * 65;    // r=65 in the SVG
    const offset = circumference - (score / 100) * circumference;

    setTimeout(() => {
        const ring = document.getElementById('scoreRing');
        ring.style.strokeDashoffset = offset;
        // Color by tier
        const colorMap = { success: 'var(--success)', accent: 'var(--accent)', warning: 'var(--warning)', danger: 'var(--danger)' };
        ring.style.stroke = colorMap[scoreMeta.color] || 'var(--accent)';
    }, 100);

    animateNumber('scoreNum', score);
    document.getElementById('scoreLabel').textContent = scoreMeta.label;
    document.getElementById('scoreDesc').textContent  = scoreMeta.description;
}

// ── Skills & Sections ─────────────────────────────────────────────────────

function renderSkillsAndSections(parsed) {
    // Skills
    const skillsEl = document.getElementById('skillsList');
    skillsEl.innerHTML = parsed.skills.length
        ? parsed.skills.map(s => tag(s, 'tag-skill')).join('')
        : tag('No recognized skills detected', 'tag-no');

    // Section presence
    const sections = [
        ['Contact Info',  parsed.has_contact],
        ['Summary',       parsed.has_summary],
        ['Education',     parsed.has_education],
        ['Experience',    parsed.has_experience],
        ['Projects',      parsed.has_projects],
        ['Achievements',  parsed.has_achievements],
    ];
    document.getElementById('sectionsList').innerHTML = sections
        .map(([name, present]) => tag(`${present ? '✓' : '✗'} ${name}`, present ? 'tag-yes' : 'tag-no'))
        .join('');
}

// ── Feedback ──────────────────────────────────────────────────────────────

function renderFeedback(feedback) {
    document.getElementById('strengthsList').innerHTML =
        feedback.strengths.map(s => feedbackItem(s, 'dot-good', '✓')).join('');

    document.getElementById('weaknessesList').innerHTML =
        feedback.weaknesses.map(s => feedbackItem(s, 'dot-bad', '✗')).join('');

    document.getElementById('suggestionsList').innerHTML =
        feedback.suggestions.map(s => feedbackItem(s, 'dot-tip', '💡')).join('');
}

// ── Job Matches ───────────────────────────────────────────────────────────

function renderJobMatches(jobMatches) {
    const container = document.getElementById('jobMatchesList');

    if (!jobMatches.length) {
        container.innerHTML = '<p style="color:var(--muted)">No matching roles found based on detected skills.</p>';
        return;
    }

    container.innerHTML = jobMatches.map(m => `
        <div class="job-match">
            <div>
                <div class="job-match-name">${m.role}</div>
                <div class="job-match-bar">
                    <div class="job-match-fill" data-pct="${m.match_percent}"></div>
                </div>
                <div style="font-size:0.78rem;color:var(--muted);margin-top:6px;">
                    Matched: ${m.matched_skills.join(', ') || '—'}
                    ${m.missing_skills.length ? ' &nbsp;|&nbsp; Missing: ' + m.missing_skills.join(', ') : ''}
                </div>
            </div>
            <div class="job-pct">${m.match_percent}%</div>
        </div>
    `).join('');

    // Animate bars after DOM paint
    setTimeout(() => {
        document.querySelectorAll('.job-match-fill').forEach(el => {
            el.style.width = el.dataset.pct + '%';
        });
    }, 200);
}

// ── Career Path ───────────────────────────────────────────────────────────

function renderCareerPath(career) {
    document.getElementById('topRole').textContent = career.top_role;

    const { current, next, advanced, learn } = career.path;
    const steps = [
        { num: '1', title: current,  sub: 'Your starting point — build here.' },
        { num: '2', title: next,     sub: 'With 2–4 years of experience.' },
        { num: '3', title: advanced, sub: 'The long-term goal — leadership & impact.' },
    ];

    document.getElementById('careerPath').innerHTML = steps.map(s => `
        <div class="path-step">
            <div class="path-step-dot">${s.num}</div>
            <div class="path-step-content">
                <div class="path-step-title">${s.title}</div>
                <div class="path-step-sub">${s.sub}</div>
            </div>
        </div>
    `).join('');

    document.getElementById('learnTags').innerHTML = learn.map(l =>
        `<span class="tag learn-tag">+ ${l}</span>`
    ).join('');
}

// ── Public API ────────────────────────────────────────────────────────────

function renderResults(data) {
    const resultsEl = document.getElementById('results');
    resultsEl.style.display = 'block';
    resultsEl.scrollIntoView({ behavior: 'smooth', block: 'start' });

    renderScoreRing(data.score, data.score_meta);
    renderSkillsAndSections(data.parsed);
    renderFeedback(data.feedback);
    renderJobMatches(data.job_matches);
    renderCareerPath(data.career);
}

function showError(msg) {
    const el = document.getElementById('errorMsg');
    el.textContent = msg;
    el.style.display = 'block';
}

function showLoader(visible) {
    document.getElementById('loader').style.display = visible ? 'block' : 'none';
}

function setUploadOpacity(dim) {
    document.querySelector('.upload-card').style.opacity = dim ? '0.5' : '1';
}