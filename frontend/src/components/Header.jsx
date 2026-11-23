import { Link, NavLink } from "react-router-dom";
import { useCart } from "../cart.jsx";
import { useSession } from "../session.js";
import CatalogMenu from "./CatalogMenu.jsx";
import Icon from "./Icon.jsx";
import Search from "./Search.jsx";

export default function Header({ site, page }) {
  const { count, setOpen } = useCart();
  const { user } = useSession();
  return (
    <>
      <div className="promo-bar">
        <div className="container">{site.promo}</div>
      </div>
      <header className="header">
        <div className="container header__row">
          <Link to="/" className="logo" aria-label={`${site.name} home`}>
            <span className="logo__mark">
              <Icon name="album" size={26} />
            </span>
            <span className="logo__text">
              NEON<span>PULSE</span>
            </span>
          </Link>
          <CatalogMenu categories={site.catalog_menu} />
          <Search index={site.search_index} />
          <div className="header__actions">
            <a href={site.phone.href} className="header__phone">
              <Icon name="phone-outline" size={20} />
              <span>
                <strong>{site.phone.value}</strong>
                <small>11:00 – 21:00, every day</small>
              </span>
            </a>
            <Link to={user ? "/account/" : "/account/login/"} className={`header__account ${page === "account" ? "is-active" : ""}`}>
              <Icon name={user ? "account-circle" : "account-circle-outline"} size={26} />
              <span>
                <small>{user ? "My account" : "Welcome"}</small>
                <strong>{user ? user.name : "Sign in"}</strong>
              </span>
            </Link>
            <button type="button" className="header__cart" onClick={() => setOpen(true)} aria-label="Open cart">
              <Icon name="cart-outline" size={26} />
              {count > 0 && <span className="header__badge">{count}</span>}
            </button>
          </div>
        </div>
      </header>
      <nav className="main-nav" aria-label="Main">
        <div className="container main-nav__row">
          {site.navigation.map((item) => (
            <NavLink
              key={item.key}
              to={item.url}
              end={item.url === "/"}
              className={() => `main-nav__link ${item.key === page ? "is-active" : ""}`}
            >
              <Icon src={item.icon} size={18} />
              {item.title}
            </NavLink>
          ))}
        </div>
      </nav>
    </>
  );
}
