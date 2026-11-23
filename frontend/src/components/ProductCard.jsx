import { Link } from "react-router-dom";
import { useCart } from "../cart.jsx";
import Icon from "./Icon.jsx";
import Price from "./Price.jsx";
import Rating from "./Rating.jsx";

const BADGE_TONES = { HIT: "pink", BESTSELLER: "violet", SALE: "red", NEW: "teal", RENEWED: "dark", LIMITED: "amber", BUNDLE: "violet" };

export default function ProductCard({ product }) {
  const { add } = useCart();
  return (
    <article className={`product-card ${product.in_stock ? "" : "product-card--out"}`}>
      <Link to={product.url} className="product-card__media">
        <img src={product.image} alt={product.name} loading="lazy" />
        <span className="product-card__chips">
          {product.badge && <span className={`chip chip--${BADGE_TONES[product.badge] || "violet"}`}>{product.badge}</span>}
          {product.discount > 0 && <span className="chip chip--red">−{product.discount}%</span>}
        </span>
      </Link>
      <div className="product-card__body">
        <span className="product-card__brand">{product.brand}</span>
        <Link to={product.url} className="product-card__title">
          {product.name}
        </Link>
        <Rating value={product.rating} reviews={product.reviews} compact />
        <div className="product-card__bottom">
          <Price price={product.price} oldPrice={product.old_price} />
          <button
            type="button"
            className="icon-button icon-button--cart"
            onClick={() => add(product)}
            disabled={!product.in_stock}
            aria-label={`Add ${product.name} to cart`}
            title={product.in_stock ? "Add to cart" : "Out of stock"}
          >
            <Icon name={product.in_stock ? "cart-plus" : "cart-off"} size={22} />
          </button>
        </div>
        <span className={`stock ${product.in_stock ? "stock--in" : "stock--out"}`}>{product.in_stock ? "In stock" : "Out of stock"}</span>
      </div>
    </article>
  );
}

export function ProductGrid({ products, columns = "auto" }) {
  return (
    <div className={`product-grid product-grid--${columns}`}>
      {products.map((product) => (
        <ProductCard key={product.id} product={product} />
      ))}
    </div>
  );
}
