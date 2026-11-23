import Avatar from "../components/Avatar.jsx";
import Icon from "../components/Icon.jsx";
import { ProductGrid } from "../components/ProductCard.jsx";
import SectionHead from "../components/SectionHead.jsx";

export default function Member({ data }) {
  const [from, to] = data.gradient;
  return (
    <div className="member">
      <section className="member__hero" style={{ background: `linear-gradient(120deg, ${from}, ${to})` }}>
        <Avatar member={data} size={140} />
        <div>
          <span className="member__alias">{data.alias}</span>
          <h1>{data.name}</h1>
          <p className="member__position">{data.position}</p>
          <div className="member__skills">
            {data.skills.map((skill) => (
              <span key={skill}>{skill}</span>
            ))}
          </div>
        </div>
      </section>
      <div className="member__grid">
        <section className="card">
          <h2 className="card__title">About</h2>
          <p>{data.bio}</p>
          <blockquote className="quote">
            <Icon name="format-quote-open" size={32} />
            {data.quote}
          </blockquote>
        </section>
        <section className="card">
          <h2 className="card__title">Responsibilities</h2>
          <ul className="feature-list">
            {data.responsibilities.map((item) => (
              <li key={item}>
                <Icon name="check-decagram" size={20} />
                {item}
              </li>
            ))}
          </ul>
        </section>
      </div>
      <section className="block">
        <SectionHead title={`${data.alias.split(" ").pop()}'s favorite gear`} subtitle="Personally tested and recommended" link="/catalog/" />
        <ProductGrid products={data.favorite_gear} />
      </section>
    </div>
  );
}
