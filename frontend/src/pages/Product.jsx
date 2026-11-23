import { useState } from "react";
import { Link } from "react-router-dom";
import { formatPrice } from "../api.js";
import { useCart } from "../cart.jsx";
import Credit from "../components/Credit.jsx";
import Icon from "../components/Icon.jsx";
import Price from "../components/Price.jsx";
import { ProductGrid } from "../components/ProductCard.jsx";
import Rating from "../components/Rating.jsx";
import SectionHead from "../components/SectionHead.jsx";

export default function Product({ data }) {
  const { product, category, related } = data;
  const { add, setOpen } = useCart();
  const [photo, setPhoto] = useState(0);
  const [tab, setTab] = useState("description");
  const current = product.images[photo];
  const lowStock = product.in_stock && product.stock <= 3;

  const buyNow = () => {
    add(product);
    setOpen(true);
  };

  return (
    <div className="product">
      <div className="product__top">
        <section className="gallery">
          <div className="gallery__main">
            <img src={current.url} alt={current.alt} />
            <span className="product-card__chips">
              {product.badge && <span className="chip chip--violet">{product.badge}</span>}
              {product.discount > 0 && <span className="chip chip--red">−{product.discount}%</span>}
            </span>
          </div>
          {product.images.length > 1 && (
            <div className="gallery__thumbs">
              {product.images.map((image, index) => (
                <button key={image.url} type="button" className={index === photo ? "is-active" : ""} onClick={() => setPhoto(index)} aria-label={image.alt}>
                  <img src={image.url} alt="" />
                </button>
              ))}
            </div>
          )}
          <Credit credit={current.credit} />
        </section>

        <section className="product__info">
          <Link to={category.url} className="product__category">
            <Icon src={category.icon} size={18} />
            {category.short_title}
          </Link>
          <h1 className="product__title">{product.name}</h1>
          <div className="product__meta">
            <Rating value={product.rating} />
            <span>{product.rating.toFixed(1)}</span>
            <span className="dot" />
            <span>{product.reviews.toLocaleString("en-US")} reviews</span>
            <span className="dot" />
            <span className="muted">SKU {product.sku}</span>
          </div>
          <p className="product__summary">{product.summary}</p>

          <div className="buy-box">
            <div className="buy-box__price">
              <Price price={product.price} oldPrice={product.old_price} size="lg" />
              {product.old_price && <span className="buy-box__save">You save {formatPrice(product.old_price - product.price)}</span>}
            </div>
            <span className={`stock stock--big ${product.in_stock ? (lowStock ? "stock--low" : "stock--in") : "stock--out"}`}>
              <Icon name={product.in_stock ? "check-circle-outline" : "close-circle-outline"} size={18} />
              {product.in_stock ? (lowStock ? `Only ${product.stock} left` : "In stock, ready to ship") : "Out of stock"}
            </span>
            <div className="buy-box__actions">
              <button type="button" className="button button--primary button--lg" disabled={!product.in_stock} onClick={buyNow}>
                <Icon name="lightning-bolt" size={20} />
                Buy now
              </button>
              <button type="button" className="button button--outline button--lg" disabled={!product.in_stock} onClick={() => add(product)}>
                <Icon name="cart-plus" size={20} />
                Add to cart
              </button>
            </div>
            <ul className="buy-box__perks">
              <li>
                <Icon name="truck-fast-outline" size={20} />
                <span>
                  <strong>Free delivery in Ukraine</strong> · ships today if ordered before 4 PM
                </span>
              </li>
              <li>
                <Icon name="storefront-outline" size={20} />
                <span>
                  <strong>Pickup</strong> in Odesa, Paris, Vienna or Warsaw
                </span>
              </li>
              <li>
                <Icon name="shield-check-outline" size={20} />
                <span>
                  <strong>{product.badge === "RENEWED" || product.badge === "BUNDLE" ? "12-month store warranty" : "2-year official warranty"}</strong> · 14 days to return
                </span>
              </li>
            </ul>
          </div>
        </section>
      </div>

      <section className="product__details">
        <div className="tabs" role="tablist">
          {[
            ["description", "Description"],
            ["specs", "Specifications"],
          ].map(([key, title]) => (
            <button key={key} type="button" role="tab" aria-selected={tab === key} className={tab === key ? "is-active" : ""} onClick={() => setTab(key)}>
              {title}
            </button>
          ))}
        </div>
        {tab === "description" ? (
          <div className="product__description">
            <p>{product.description}</p>
            <ul className="feature-list">
              {product.features.map((feature) => (
                <li key={feature}>
                  <Icon name="check-decagram" size={20} />
                  {feature}
                </li>
              ))}
            </ul>
          </div>
        ) : (
          <dl className="specs">
            <div>
              <dt>Brand</dt>
              <dd>{product.brand}</dd>
            </div>
            {product.specs.map((spec) => (
              <div key={spec.label}>
                <dt>{spec.label}</dt>
                <dd>{spec.value}</dd>
              </div>
            ))}
          </dl>
        )}
      </section>

      {related.length > 0 && (
        <section className="block">
          <SectionHead title="You may also like" link={category.url} linkTitle={`All ${category.short_title.toLowerCase()}`} />
          <ProductGrid products={related} />
        </section>
      )}
    </div>
  );
}
