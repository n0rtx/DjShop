import { Link } from "react-router-dom";
import Icon from "./Icon.jsx";

export default function SectionHead({ title, subtitle, link, linkTitle = "See all" }) {
  return (
    <div className="section-head">
      <div>
        <h2 className="section-head__title">{title}</h2>
        {subtitle && <p className="section-head__subtitle">{subtitle}</p>}
      </div>
      {link && (
        <Link to={link} className="section-head__link">
          {linkTitle}
          <Icon name="arrow-right" size={18} />
        </Link>
      )}
    </div>
  );
}
