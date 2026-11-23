const BASE = "https://api.iconify.design/mdi";

export function iconUrl(name) {
  return `${BASE}/${name}.svg`;
}

export default function Icon({ name, src, size = 20, className = "" }) {
  const url = src ? src.split("?")[0] : iconUrl(name);
  const style = { width: size, height: size, WebkitMaskImage: `url("${url}")`, maskImage: `url("${url}")` };
  return <span className={`icon ${className}`} style={style} aria-hidden="true" />;
}
