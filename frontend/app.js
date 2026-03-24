const API_BASE = 'http://localhost:8000';

const queryText = document.getElementById('queryText');
const imageInput = document.getElementById('imageInput');
const previewWrapper = document.getElementById('previewWrapper');
const previewImage = document.getElementById('previewImage');
const fileName = document.getElementById('fileName');
const removeImageBtn = document.getElementById('removeImageBtn');
const runBtn = document.getElementById('runBtn');
const resetBtn = document.getElementById('resetBtn');
const newBtn = document.getElementById('newBtn');
const resultsGrid = document.getElementById('resultsGrid');
const resultCount = document.getElementById('resultCount');
const historyList = document.getElementById('historyList');
const summaryBox = document.getElementById('summaryBox');
const statusBox = document.getElementById('status');

imageInput.addEventListener('change', () => {
  const file = imageInput.files?.[0];
  if (!file) return;
  fileName.textContent = file.name;
  const reader = new FileReader();
  reader.onload = (e) => {
    previewImage.src = e.target.result;
    previewWrapper.classList.remove('hidden');
  };
  reader.readAsDataURL(file);
});

removeImageBtn.addEventListener('click', () => clearImage());
resetBtn.addEventListener('click', () => resetAll());
newBtn.addEventListener('click', () => resetAll());
runBtn.addEventListener('click', () => submitQuery());

document.addEventListener('DOMContentLoaded', () => {
  loadHistory();
});

function clearImage() {
  imageInput.value = '';
  previewImage.src = '';
  fileName.textContent = '';
  previewWrapper.classList.add('hidden');
}

function resetAll() {
  queryText.value = '';
  clearImage();
  resultsGrid.innerHTML = '';
  summaryBox.classList.add('hidden');
  summaryBox.innerHTML = '';
  resultCount.textContent = '0 item(s)';
  statusBox.textContent = 'Ready';
}

async function loadHistory() {
  try {
    const res = await fetch(`${API_BASE}/api/history`);
    const data = await res.json();
    historyList.innerHTML = '';
    data.forEach((entry) => {
      const item = document.createElement('div');
      item.className = 'history-item';
      item.innerHTML = `<strong>${escapeHtml(entry.title)}</strong><span class="muted">${escapeHtml(entry.subtitle)}</span>`;
      historyList.appendChild(item);
    });
  } catch (error) {
    historyList.innerHTML = '<div class="history-item"><strong>Backend unavailable</strong><span class="muted">Start the API on port 8000.</span></div>';
  }
}

async function submitQuery() {
  statusBox.textContent = 'Running retrieval...';
  runBtn.disabled = true;

  const form = new FormData();
  form.append('text', queryText.value || '');
  const file = imageInput.files?.[0];
  if (file) form.append('image', file);

  try {
    const res = await fetch(`${API_BASE}/api/query`, {
      method: 'POST',
      body: form,
    });

    if (!res.ok) throw new Error('Query failed');

    const data = await res.json();
    renderSummary(data);
    renderResults(data.results || []);
    await loadHistory();
    statusBox.textContent = 'Completed';
  } catch (error) {
    statusBox.textContent = 'Error';
    summaryBox.classList.remove('hidden');
    summaryBox.innerHTML = `<strong>Request failed.</strong><div class="muted">Make sure the FastAPI backend is running on port 8000.</div>`;
  } finally {
    runBtn.disabled = false;
  }
}

function renderSummary(data) {
  summaryBox.classList.remove('hidden');
  summaryBox.innerHTML = `
    <h3>Generated summary</h3>
    <p><strong>Normalized query:</strong> ${escapeHtml(data.normalized_query)}</p>
    <p><strong>Report:</strong> ${escapeHtml(data.report)}</p>
  `;
}

function renderResults(results) {
  resultsGrid.innerHTML = '';
  resultCount.textContent = `${results.length} item(s)`;

  results.forEach((result) => {
    const card = document.createElement('article');
    card.className = 'result-card';

    const tags = (result.tags || []).map(tag => `<span class="chip">${escapeHtml(tag)}</span>`).join('');
    const sources = (result.sources || []).map(src => `
      <span class="chip source-chip">
        <span>${escapeHtml(src.label)}</span>
        <span class="source-kind">${escapeHtml(src.kind)}</span>
      </span>
    `).join('');

    card.innerHTML = `
      <h3>${escapeHtml(result.title)}</h3>
      <div class="score">Relevance score: ${escapeHtml(String(result.relevance_score))}%</div>
      <p><strong>Findings:</strong> ${escapeHtml(result.findings)}</p>
      <p><strong>Impression:</strong> ${escapeHtml(result.impression)}</p>
      <div class="chips">${tags}</div>
      <div class="chips">${sources}</div>
    `;

    resultsGrid.appendChild(card);
  });
}

function escapeHtml(value) {
  return String(value)
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#039;');
}
