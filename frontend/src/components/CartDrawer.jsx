import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { formatPrice } from "../api.js";
import { useCart } from "../cart.jsx";
import Icon from "./Icon.jsx";

export default function CartDrawer() {
  const { items, total, count, update, clear, open, setOpen } = useCart();
  const [notice, setNotice] = useState(false);

  useEffect(() => {
    const onKey = (event) => event.key === "Escape" && setOpen(false);
    document.addEventListener("keydown", onKey);
    return () => document.removeEventListener("keydown", onKey);
  }, [setOpen]);

  useEffect(() => {
    document.body.classList.toggle("no-scroll", open);
    if (!open) setNotice(false);
  }, [open]);

  return (
    <div className={`drawer ${open ? "is-open" : ""}`} aria-hidden={!open}>
      <div className="drawer__overlay" onClick={() => setOpen(false)} />
      <aside className="drawer__panel" role="dialog" aria-label="Cart">
        <div className="drawer__head">
          <h2>
            Cart <span>{count}</span>
          </h2>
          <button type="button" className="icon-button" onClick={() => setOpen(false)} aria-label="Close cart">
            <Icon name="close" size={22} />
          </button>
        </div>
        {items.length ? (
          <>
            <ul className="drawer__list">
              {items.map((item) => (
                <li key={item.id} className="cart-item">
                  <Link to={item.url} onClick={() => setOpen(false)}>
                    <img src={item.image} alt="" />
                  </Link>
                  <div className="cart-item__info">
                    <Link to={item.url} onClick={() => setOpen(false)} className="cart-item__name">
                      {item.name}
                    </Link>
                    <div className="cart-item__row">
                      <div className="qty">
                        <button type="button" onClick={() => update(item.id, item.qty - 1)} aria-label="Decrease">
                          <Icon name="minus" size={16} />
                        </button>
                        <span>{item.qty}</span>
                        <button type="button" onClick={() => update(item.id, item.qty + 1)} aria-label="Increase">
                          <Icon name="plus" size={16} />
                        </button>
                      </div>
                      <strong>{formatPrice(item.price * item.qty)}</strong>
                    </div>
                  </div>
                  <button type="button" className="icon-button icon-button--ghost" onClick={() => update(item.id, 0)} aria-label="Remove">
                    <Icon name="trash-can-outline" size={20} />
                  </button>
                </li>
              ))}
            </ul>
            <div className="drawer__foot">
              <div className="drawer__total">
                <span>Total</span>
                <strong>{formatPrice(total)}</strong>
              </div>
              {notice && <p className="drawer__notice">This is an educational project, so checkout is disabled. Thanks for testing NEON PULSE!</p>}
              <button type="button" className="button button--primary button--block" onClick={() => setNotice(true)}>
                Checkout
              </button>
              <button type="button" className="button button--ghost button--block" onClick={clear}>
                Clear cart
              </button>
            </div>
          </>
        ) : (
          <div className="drawer__empty">
            <Icon name="cart-outline" size={64} />
            <h3>Your cart is empty</h3>
            <p>Add a controller, a pair of headphones or a fresh slipmat.</p>
            <Link to="/catalog/" className="button button--primary" onClick={() => setOpen(false)}>
              Go to catalog
            </Link>
          </div>
        )}
      </aside>
    </div>
  );
}
