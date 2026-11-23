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
  const finalPath = response.redirected ? new URL(response.url).pathname : null;
  return { payload, finalPath };
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
