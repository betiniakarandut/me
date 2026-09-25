export function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

const MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

/** "2025-02" -> "Feb 2025"; "2017" and free text pass through unchanged. */
export function formatEventDate(rawDate) {
  if (!rawDate) return "";
  const match = /^(\d{4})-(\d{2})(?:-\d{2})?$/.exec(rawDate);
  if (match) {
    const month = MONTHS[Number(match[2]) - 1];
    return month ? `${month} ${match[1]}` : rawDate;
  }
  return String(rawDate);
}

export function formatDateRange(start, end, isCurrent) {
  const from = formatEventDate(start);
  const to = isCurrent ? "Present" : formatEventDate(end);
  return to ? `${from} – ${to}` : from;
}

export function renderParagraphs(text, className = "muted") {
  return String(text ?? "")
    .split(/\n\s*\n/)
    .map((paragraph) => paragraph.trim())
    .filter(Boolean)
    .map((paragraph) => `<p class="${className}">${escapeHtml(paragraph)}</p>`)
    .join("");
}
