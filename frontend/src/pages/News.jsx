import { Link } from "react-router-dom";
import { formatDate } from "../api.js";
import Icon from "../components/Icon.jsx";
import PageHero from "../components/PageHero.jsx";

export function NewsCard({ item, featured = false }) {
  return (
    <article className={`news-card ${featured ? "news-card--featured" : ""}`}>
      <Link to={item.url} className="news-card__media">
        <img src={item.image} alt="" loading="lazy" />
        <span className="chip chip--light">{item.tag}</span>
      </Link>
      <div className="news-card__body">
        <div className="news-card__meta">
          <time dateTime={item.date}>{formatDate(item.date)}</time>
          <span className="dot" />
          <span>{item.read_time} min read</span>
        </div>
        <Link to={item.url} className="news-card__title">
          {item.title}
        </Link>
        <p>{item.excerpt}</p>
        <Link to={item.url} className="news-card__more">
          Read more <Icon name="arrow-right" size={16} />
        </Link>
      </div>
    </article>
  );
}

export default function News({ data, payload }) {
  const isTag = Boolean(payload.subsection);
  const [first, ...rest] = data.items;
  return (
    <div className="news">
      <PageHero title={data.title} subtitle={isTag ? data.description : data.subtitle} icon={data.icon} tone="pink" />
      {data.items.length === 0 ? (
        <div className="empty">
          <Icon name="newspaper-variant-outline" size={48} />
          <h3>No stories here yet</h3>
          <Link to="/news/" className="button button--primary">
            All news
          </Link>
        </div>
      ) : (
        <div className="news-grid news-grid--page">
          <NewsCard item={first} featured={!isTag && data.items.length > 2} />
          {rest.map((item) => (
            <NewsCard key={item.id} item={item} />
          ))}
        </div>
      )}
    </div>
  );
}
