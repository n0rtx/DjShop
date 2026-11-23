import Credit from "../components/Credit.jsx";
import Icon from "../components/Icon.jsx";
import PageHero from "../components/PageHero.jsx";
import { Timeline, Values } from "./About.jsx";

function Brands({ items }) {
  return (
    <div className="brand-grid">
      {items.map((brand) => (
        <div key={brand.name} className="brand-card">
          <span className="brand-card__logo">{brand.name.slice(0, 2).toUpperCase()}</span>
          <div>
            <h3>{brand.name}</h3>
            <p>
              {brand.country} · since {brand.since}
            </p>
            <div className="tags">
              {brand.categories.map((category) => (
                <span key={category}>{category}</span>
              ))}
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}

function InfoCards({ title, items }) {
  return (
    <section className="block">
      <h2 className="block__title">{title}</h2>
      <div className="info-cards">
        {items.map((item) => (
          <div key={item.title} className="info-card">
            <span className="value-card__icon">
              <Icon src={item.icon} size={26} />
            </span>
            <h3>{item.title}</h3>
            <p>{item.text}</p>
          </div>
        ))}
      </div>
    </section>
  );
}

function Delivery({ data }) {
  return (
    <>
      <InfoCards title="Delivery" items={data.delivery} />
      <InfoCards title="Payment" items={data.payment} />
      <section className="block card">
        <h2 className="card__title">Warranty & returns</h2>
        <ul className="feature-list">
          {data.warranty.map((item) => (
            <li key={item}>
              <Icon name="shield-check-outline" size={20} />
              {item}
            </li>
          ))}
        </ul>
      </section>
    </>
  );
}

export default function AboutDetail({ data }) {
  return (
    <div className="about-detail">
      <PageHero title={data.title} subtitle={data.description} image={data.image} tone={data.image ? "dark" : "violet"} />
      {data.image_credit && <Credit credit={data.image_credit} className="credit--right" />}
      {data.kind === "history" && (
        <section className="block">
          <Timeline items={data.timeline} />
        </section>
      )}
      {data.kind === "values" && (
        <section className="block">
          <Values items={data.values} />
        </section>
      )}
      {data.kind === "brands" && (
        <section className="block">
          <Brands items={data.brands} />
        </section>
      )}
      {data.kind === "delivery" && <Delivery data={data} />}
    </div>
  );
}
