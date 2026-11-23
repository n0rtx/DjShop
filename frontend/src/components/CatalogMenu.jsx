import { useEffect, useRef, useState } from "react";
import { Link, useLocation } from "react-router-dom";
import Icon from "./Icon.jsx";

export default function CatalogMenu({ categories }) {
  const [open, setOpen] = useState(false);
  const location = useLocation();
  const box = useRef(null);

  useEffect(() => setOpen(false), [location.pathname]);

  useEffect(() => {
    const close = (event) => box.current && !box.current.contains(event.target) && setOpen(false);
    document.addEventListener("mousedown", close);
    return () => document.removeEventListener("mousedown", close);
  }, []);

  return (
    <div className="catalog-menu" ref={box}>
      <button type="button" className={`catalog-menu__button ${open ? "is-open" : ""}`} onClick={() => setOpen((value) => !value)} aria-expanded={open}>
        <Icon name={open ? "close" : "view-grid-outline"} size={22} />
        <span>Catalog</span>
      </button>
      {open && (
        <div className="catalog-menu__panel">
          <div className="catalog-menu__grid">
            {categories.map((category) => (
              <Link key={category.slug} to={category.url} className="catalog-menu__item">
                <img src={category.image} alt="" />
                <span>
                  <strong>{category.title}</strong>
                  <small>{category.count} products</small>
                </span>
              </Link>
            ))}
          </div>
          <Link to="/catalog/" className="catalog-menu__all">
            Open full catalog <Icon name="arrow-right" size={18} />
          </Link>
        </div>
      )}
    </div>
  );
}
