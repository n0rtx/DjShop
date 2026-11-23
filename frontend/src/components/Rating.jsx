import Icon from "./Icon.jsx";

export default function Rating({ value, reviews, compact = false }) {
  const stars = [1, 2, 3, 4, 5].map((index) => {
    const name = value >= index ? "star" : value >= index - 0.5 ? "star-half-full" : "star-outline";
    return <Icon key={index} name={name} size={compact ? 14 : 18} className="rating__star" />;
  });
  return (
    <span className={`rating ${compact ? "rating--compact" : ""}`} title={`${value} out of 5`}>
      <span className="rating__stars">{stars}</span>
      {reviews !== undefined && <span className="rating__count">{reviews.toLocaleString("en-US")}</span>}
    </span>
  );
}
