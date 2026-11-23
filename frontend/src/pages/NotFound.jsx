import { Link } from "react-router-dom";
import Icon from "../components/Icon.jsx";
import { ProductGrid } from "../components/ProductCard.jsx";
import SectionHead from "../components/SectionHead.jsx";

export default function NotFound({ data, payload }) {
  return (
    <div className="not-found">
      <section className="not-found__hero">
        <div className="not-found__visual" aria-hidden="true">
          <span>4</span>
          <span className="vinyl">
            <span className="vinyl__label" />
          </span>
          <span>4</span>
        </div>
        <h1>{data.title}</h1>
        <p>{data.subtitle}</p>
        <code className="not-found__path">{payload.path}</code>
        <div className="not-found__links">
          {data.links.map((link) => (
            <Link key={link.url} to={link.url} className="button button--ghost">
              <Icon src={link.icon} size={18} />
              {link.title}
            </Link>
          ))}
        </div>
      </section>
      <section className="block">
        <SectionHead title="Popular right now" link="/catalog/" />
        <ProductGrid products={data.products} />
      </section>
    </div>
  );
}
