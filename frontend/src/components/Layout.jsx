import { Link, NavLink } from "react-router-dom";
import { useCart } from "../cart.jsx";
import CartDrawer from "./CartDrawer.jsx";
import Footer from "./Footer.jsx";
import Header from "./Header.jsx";
import Icon from "./Icon.jsx";

function Breadcrumbs({ items }) {
  if (items.length < 2) return null;
  return (
    <nav className="breadcrumbs" aria-label="Breadcrumbs">
      {items.map((item, index) =>
        index === items.length - 1 ? (
          <span key={item.url} aria-current="page">
            {item.title}
          </span>
        ) : (
          <span key={item.url} className="breadcrumbs__item">
            <Link to={item.url}>{item.title}</Link>
            <Icon name="chevron-right" size={16} />
          </span>
        ),
      )}
    </nav>
  );
}

function SubNav({ payload }) {
  const { page, subsections, subsection, section_title: sectionTitle } = payload;
  if (!subsections.length) return null;
  return (
    <nav className="subnav" aria-label={sectionTitle}>
      <NavLink to={`/${page}/`} end className={() => `subnav__link ${!subsection ? "is-active" : ""}`}>
        All
      </NavLink>
      {subsections.map((item) => (
        <NavLink key={item.slug} to={item.url} className={() => `subnav__link ${item.slug === subsection ? "is-active" : ""}`}>
          <Icon src={item.icon} size={18} />
          {item.title}
        </NavLink>
      ))}
    </nav>
  );
}

function Toast() {
  const { toast, setOpen } = useCart();
  if (!toast) return null;
  return (
    <div className="toast" key={toast.id} role="status">
      <Icon name="check-circle" size={22} />
      <span>{toast.text}</span>
      <button type="button" onClick={() => setOpen(true)}>
        View cart
      </button>
    </div>
  );
}

export default function Layout({ payload, loading, children }) {
  const { site, page } = payload;
  const showChrome = page !== "home" && page !== "not_found";
  return (
    <div className="app">
      <div className={`progress ${loading ? "is-loading" : ""}`} />
      <Header site={site} page={page} />
      <main className={`main ${loading ? "is-loading" : ""}`}>
        <div className="container">
          {showChrome && <Breadcrumbs items={payload.breadcrumbs} />}
          {showChrome && <SubNav payload={payload} />}
          {children}
        </div>
      </main>
      <Footer site={site} />
      <CartDrawer />
      <Toast />
    </div>
  );
}
