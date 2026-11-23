export default function Credit({ credit, className = "" }) {
  if (!credit) return null;
  return (
    <p className={`credit ${className}`}>
      Photo: {credit.author} ·{" "}
      <a href={credit.source} target="_blank" rel="noopener noreferrer">
        {credit.license}, {credit.provider}
      </a>
    </p>
  );
}
