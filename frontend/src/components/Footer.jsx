import { Link } from "react-router-dom";
import Icon from "./Icon.jsx";

export default function Footer({ site }) {
  return (
    <footer className="footer">
      <div className="container footer__grid">
        <div className="footer__brand">
          <Link to="/" className="logo logo--light">
            <span className="logo__mark">
              <Icon name="album" size={26} />
            </span>
            <span className="logo__text">
              NEON<span>PULSE</span>
            </span>
          </Link>
          <p>{site.tagline}. Controllers, players, mixers and headphones tested by working DJs.</p>
          <div className="footer__socials">
            {site.socials.map((social) => (
              <a key={social.name} href={social.url} target="_blank" rel="noopener noreferrer" aria-label={social.name} title={social.name}>
                <Icon src={social.icon} size={20} />
              </a>
            ))}
          </div>
        </div>
        {site.footer_links.map((column) => (
          <div key={column.title} className="footer__column">
            <h3>{column.title}</h3>
            <ul>
              {column.links.map((link) => (
                <li key={link.url}>
                  <Link to={link.url}>{link.title}</Link>
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>
      <div className="container footer__bottom">
        <p>{site.footer}</p>
        <div className="footer__payments">
          {site.payments.map((name) => (
            <span key={name}>{name}</span>
          ))}
        </div>
      </div>
      <div className="container footer__note">{site.photo_note}</div>
    </footer>
  );
}
