import { useState } from "react";
import { Link } from "react-router-dom";
import { formatDate, formatPrice, postJson } from "../api.js";
import Icon from "../components/Icon.jsx";
import { useSession } from "../session.js";

function initials(name) {
  return name
    .split(/\s+/)
    .map((part) => part[0])
    .join("")
    .slice(0, 2)
    .toUpperCase();
}

function OrderCard({ order, open, onToggle, fresh }) {
  return (
    <article className={`order ${open ? "is-open" : ""} ${fresh ? "is-fresh" : ""}`}>
      <button type="button" className="order__head" onClick={onToggle} aria-expanded={open}>
        <span className="order__number">
          <strong>{order.number}</strong>
          <small>{formatDate(order.created)}</small>
        </span>
        <span className="order__thumbs" aria-hidden="true">
          {order.items.slice(0, 4).map((item) => (
            <img key={item.product_id} src={item.image} alt="" />
          ))}
        </span>
        <span className="order__status">
          <Icon name="check-circle" size={16} />
          {order.status}
        </span>
        <strong className="order__total">{formatPrice(order.total)}</strong>
        <Icon name="chevron-down" size={22} className="order__chevron" />
      </button>
      {open && (
        <div className="order__body">
          <ul className="summary-list">
            {order.items.map((item) => (
              <li key={item.product_id}>
                <img src={item.image} alt="" />
                <div>
                  <Link to={item.url}>{item.name}</Link>
                  <small>
                    {item.brand} · {item.sku} · {item.qty} × {formatPrice(item.price)}
                  </small>
                </div>
                <strong>{formatPrice(item.line_total)}</strong>
              </li>
            ))}
          </ul>
          <dl className="order__meta">
            <div>
              <dt>Recipient</dt>
              <dd>
                {order.full_name}
                <br />
                {order.phone} · {order.email}
              </dd>
            </div>
            <div>
              <dt>Delivery</dt>
              <dd>
                {order.delivery}
                <br />
                {[order.city, order.address].filter(Boolean).join(", ")}
              </dd>
            </div>
            <div>
              <dt>Payment</dt>
              <dd>{order.payment}</dd>
            </div>
            {order.comment && (
              <div>
                <dt>Comment</dt>
                <dd>{order.comment}</dd>
              </div>
            )}
          </dl>
        </div>
      )}
    </article>
  );
}

export default function Account({ data }) {
  const { go, csrf } = useSession();
  const { profile, stats, orders, highlight } = data;
  const [openId, setOpenId] = useState(highlight ?? orders[0]?.id ?? null);
  const [leaving, setLeaving] = useState(false);
  const fresh = orders.find((order) => order.id === highlight);

  const logout = async () => {
    setLeaving(true);
    try {
      await postJson("/account/logout/", {}, csrf);
    } finally {
      go("/");
    }
  };

  return (
    <div className="account">
      <aside className="account__side">
        <div className="card profile">
          <span className="profile__avatar">{initials(profile.name)}</span>
          <h1>{profile.name}</h1>
          <p>@{profile.username}</p>
          <p>{profile.email}</p>
          <small>Member since {formatDate(profile.joined)}</small>
          <button type="button" className="button button--ghost button--block" onClick={logout} disabled={leaving}>
            <Icon name="logout" size={18} />
            Sign out
          </button>
        </div>
        <div className="stats">
          <div>
            <strong>{stats.orders}</strong>
            <span>Orders</span>
          </div>
          <div>
            <strong>{stats.items}</strong>
            <span>Items</span>
          </div>
          <div>
            <strong>{formatPrice(stats.spent)}</strong>
            <span>Spent</span>
          </div>
        </div>
      </aside>
      <section className="account__main">
        {fresh && (
          <div className="success-banner" role="status">
            <Icon name="party-popper" size={28} />
            <div>
              <strong>Order {fresh.number} placed!</strong>
              <p>It is a study project, so the order went straight to your history. Nothing will be charged or shipped.</p>
            </div>
          </div>
        )}
        <div className="section-head">
          <h2 className="section-head__title">Order history</h2>
        </div>
        {orders.length ? (
          <div className="orders">
            {orders.map((order) => (
              <OrderCard
                key={order.id}
                order={order}
                fresh={order.id === highlight}
                open={openId === order.id}
                onToggle={() => setOpenId((current) => (current === order.id ? null : order.id))}
              />
            ))}
          </div>
        ) : (
          <div className="empty">
            <Icon name="package-variant" size={64} />
            <h3>No orders yet</h3>
            <p>Your orders will appear here right after checkout.</p>
            <Link to="/catalog/" className="button button--primary">
              Go to catalog
            </Link>
          </div>
        )}
      </section>
    </div>
  );
}
