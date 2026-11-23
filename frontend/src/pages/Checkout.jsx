import { Link } from "react-router-dom";
import { formatPrice } from "../api.js";
import { useCart } from "../cart.jsx";
import Icon from "../components/Icon.jsx";
import SchemaForm from "../components/SchemaForm.jsx";

const ICONS = {
  courier: "truck-fast-outline",
  post: "package-variant-closed",
  pickup: "storefront-outline",
  card: "credit-card-outline",
  cash: "cash",
  invoice: "file-document-outline",
};

export default function Checkout({ data }) {
  const { items, count, total, clear } = useCart();

  if (!items.length) {
    return (
      <div className="empty">
        <Icon name="cart-off" size={64} />
        <h3>Your cart is empty</h3>
        <p>Add something to the cart first, then come back to place the order.</p>
        <Link to="/catalog/" className="button button--primary">
          Go to catalog
        </Link>
      </div>
    );
  }

  return (
    <div className="checkout">
      <section className="checkout__main card">
        <h1 className="page-title">{data.title}</h1>
        <p className="page-lead">{data.subtitle}</p>
        <SchemaForm
          form={data.form}
          action="/checkout/"
          submitLabel={`Place order · ${formatPrice(total)}`}
          submitIcon="check-decagram-outline"
          icons={ICONS}
          isHidden={(name, values) => name === "address" && values.delivery === "pickup"}
          extra={() => ({ items: items.map((item) => ({ id: item.id, qty: item.qty })) })}
          onSuccess={clear}
        />
      </section>
      <aside className="checkout__summary card">
        <h2 className="card__title">
          <Icon name="cart-outline" size={22} />
          Your order <span className="checkout__count">{count}</span>
        </h2>
        <ul className="summary-list">
          {items.map((item) => (
            <li key={item.id}>
              <img src={item.image} alt="" />
              <div>
                <Link to={item.url}>{item.name}</Link>
                <small>
                  {item.qty} × {formatPrice(item.price)}
                </small>
              </div>
              <strong>{formatPrice(item.price * item.qty)}</strong>
            </li>
          ))}
        </ul>
        <dl className="summary-total">
          <div>
            <dt>Delivery</dt>
            <dd>Free</dd>
          </div>
          <div className="summary-total__grand">
            <dt>Total</dt>
            <dd>{formatPrice(total)}</dd>
          </div>
        </dl>
        <p className="checkout__note">
          <Icon name="information-outline" size={18} />
          Nothing is charged. The order simply moves to your order history.
        </p>
      </aside>
    </div>
  );
}
