export function readEmbeddedPayload() {
  const node = document.getElementById("page-data");
  if (!node) return null;
  try {
    return JSON.parse(node.textContent);
  } catch {
    return null;
  }
}

export async function loadPage(path) {
  const separator = path.includes("?") ? "&" : "?";
  const response = await fetch(`${path}${separator}format=json`, {
    headers: { Accept: "application/json" },
  });
  const payload = await response.json();
  return { payload, finalPath: response.redirected ? cleanPath(response.url) : null };
}

function cleanPath(url) {
  const parsed = new URL(url);
  parsed.searchParams.delete("format");
  return parsed.pathname + parsed.search;
}

export function csrfToken() {
  const match = document.cookie.match(/(?:^|;\s*)csrftoken=([^;]+)/);
  return match ? decodeURIComponent(match[1]) : "";
}

export async function postJson(path, body, fallbackToken = "") {
  const separator = path.includes("?") ? "&" : "?";
  const response = await fetch(`${path}${separator}format=json`, {
    method: "POST",
    credentials: "same-origin",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
      "X-CSRFToken": csrfToken() || fallbackToken,
    },
    body: JSON.stringify(body),
  });
  let data = null;
  try {
    data = await response.json();
  } catch {
    data = null;
  }
  return { ok: response.ok, status: response.status, data };
}

export function formatPrice(value) {
  return new Intl.NumberFormat("en-US", { style: "currency", currency: "USD", minimumFractionDigits: value % 1 ? 2 : 0 }).format(value);
}

export function formatDate(value) {
  return new Date(value).toLocaleDateString("en-GB", { day: "numeric", month: "long", year: "numeric" });
}

export function isInternal(url) {
  return typeof url === "string" && url.startsWith("/") && !url.startsWith("//") && !url.startsWith("/static/");
}
