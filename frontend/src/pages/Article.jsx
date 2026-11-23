import { Link } from "react-router-dom";
import { formatDate } from "../api.js";
import Credit from "../components/Credit.jsx";
import Icon from "../components/Icon.jsx";

export default function Article({ data }) {
  return (
    <article className="article">
      <header className="article__head">
        <Link to={`/news/${data.tag_slug}/`} className="chip chip--violet">
          {data.tag}
        </Link>
        <h1 className="article__title">{data.title}</h1>
        <div className="article__meta">
          <Icon name="calendar-blank-outline" size={18} />
          <time dateTime={data.date}>{formatDate(data.date)}</time>
          <span className="dot" />
          <Icon name="clock-outline" size={18} />
          <span>{data.read_time} min read</span>
        </div>
      </header>
      <figure className="article__figure">
        <img src={data.image} alt="" />
        <figcaption>
          <Credit credit={data.image_credit} />
        </figcaption>
      </figure>
      <div className="article__body">
        <p className="article__lead">{data.excerpt}</p>
        {data.body.map((paragraph) => (
          <p key={paragraph}>{paragraph}</p>
        ))}
      </div>
      <footer className="article__foot">
        <Link to="/news/" className="button button--ghost">
          <Icon name="arrow-left" size={18} />
          All news
        </Link>
        <Link to="/catalog/" className="button button--primary">
          Shop the catalog
          <Icon name="arrow-right" size={18} />
        </Link>
      </footer>
    </article>
  );
}
