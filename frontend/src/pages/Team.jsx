import { Link } from "react-router-dom";
import Avatar from "../components/Avatar.jsx";
import Icon from "../components/Icon.jsx";
import PageHero from "../components/PageHero.jsx";

export default function Team({ data }) {
  return (
    <div className="team">
      <PageHero title={data.title} subtitle={data.subtitle} icon={data.icon} tone="teal" />
      <div className="team-grid">
        {data.members.map((member) => (
          <Link key={member.slug} to={`/management/${member.slug}/`} className="member-card">
            <div className="member-card__cover" style={{ background: `linear-gradient(135deg, ${member.gradient[0]}22, ${member.gradient[1]}33)` }}>
              <Avatar member={member} size={104} />
            </div>
            <div className="member-card__body">
              <span className="member-card__alias">{member.alias}</span>
              <h2>{member.name}</h2>
              <p className="member-card__position">{member.position}</p>
              <p>{member.bio}</p>
              <span className="member-card__more">
                Profile <Icon name="arrow-right" size={16} />
              </span>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}
