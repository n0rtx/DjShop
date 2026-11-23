import { formatPrice } from "../api.js";

export default function Price({ price, oldPrice, size = "md" }) {
  return (
    <div className={`price price--${size} ${oldPrice ? "price--sale" : ""}`}>
      {oldPrice ? <del className="price__old">{formatPrice(oldPrice)}</del> : null}
      <strong className="price__current">{formatPrice(price)}</strong>
    </div>
  );
}
