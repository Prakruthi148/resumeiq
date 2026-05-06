/**
 * frontend/static/js/api.js
 * ==========================
 * Responsibility: Send the resume file to the Django API and return the result.
 * No UI rendering — just the HTTP layer.
 */

const API_URL = '/api/analyze/';

/**
 * Upload a file and get back the analysis result.
 * @param {File} file
 * @returns {Promise<Object>} parsed JSON response
 * @throws {Error} if the network request fails
 */
async function uploadResume(file) {
    const formData = new FormData();
    formData.append('resume', file);

    const response = await fetch(API_URL, {
        method: 'POST',
        body: formData,
    });

    const data = await response.json();
    return data;
}