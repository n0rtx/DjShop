import { Link } from "react-router-dom";
import Credit from "../components/Credit.jsx";
import Icon from "../components/Icon.jsx";
import PageHero from "../components/PageHero.jsx";
import SectionHead from "../components/SectionHead.jsx";

export function Timeline({ items }) {
  return (
    <ol className="timeline">
      {items.map((step) => (
        <li key={step.year} className="timeline__item">
          <span className="timeline__year">{step.year}</span>
          <h3>{step.title}</h3>
          <p>{step.text}</p>
        </li>
      ))}
    </ol>
  );
}

export function Values({ items }) {
  return (
    <div className="values">
      {items.map((value) => (
        <div key={value.title} className="value-card">
          <span className="value-card__icon">
            <Icon src={value.icon} size={28} />
          </span>
          <h3>{value.title}</h3>
          <p>{value.text}</p>
        </div>
      ))}
    </div>
  );
}

export default function About({ data, payload }) {
  return (
    <div className="about">
      <PageHero title={data.title} subtitle={data.subtitle} image={data.image} tone="dark" />
      <Credit credit={data.image_credit} className="credit--right" />
      <section className="about__intro">
        <p className="about__text">{data.description}</p>
        <div className="stats">
          {data.stats.map((stat) => (
            <div key={stat.label} className="stat">
              <strong>{stat.value}</strong>
              <span>{stat.label}</span>
            </div>
          ))}
        </div>
      </section>
      <section className="block">
        <SectionHead title="Our journey" link="/about/history/" linkTitle="Full history" />
        <Timeline items={data.timeline} />
      </section>
      <section className="block">
        <SectionHead title="What we stand for" link="/about/values/" />
        <Values items={data.values} />
      </section>
      <section className="block">
        <SectionHead title="Learn more" />
        <div className="link-cards">
          {payload.subsections.map((item) => (
            <Link key={item.slug} to={item.url} className="link-card">
              <Icon src={item.icon} size={28} />
              <strong>{item.title}</strong>
              <Icon name="arrow-right" size={20} className="link-card__arrow" />
            </Link>
          ))}
        </div>
      </section>
    </div>
  );
}
