import { Link } from "react-router-dom";
import { formatPrice } from "../api.js";
import Icon from "../components/Icon.jsx";
import PageHero from "../components/PageHero.jsx";

export function Channels({ channels }) {
  return (
    <div className="channels">
      {channels.map((channel) => {
        const content = (
          <>
            <span className="channel__icon">
              <Icon src={channel.icon} size={22} />
            </span>
            <span>
              <small>{channel.label}</small>
              <strong>{channel.value}</strong>
            </span>
          </>
        );
        return channel.href ? (
          <a key={channel.type} href={channel.href} className="channel" target={channel.href.startsWith("http") ? "_blank" : undefined} rel="noopener noreferrer">
            {content}
          </a>
        ) : (
          <div key={channel.type} className="channel">
            {content}
          </div>
        );
      })}
    </div>
  );
}

export function Hours({ hours }) {
  return (
    <section className="card">
      <h2 className="card__title">
        <Icon name="clock-outline" size={22} /> Opening hours
      </h2>
      <dl className="hours">
        {hours.map((row) => (
          <div key={row.days}>
            <dt>{row.days}</dt>
            <dd className={row.time === "Closed" ? "is-closed" : ""}>{row.time}</dd>
          </div>
        ))}
      </dl>
    </section>
  );
}

export function MapCard({ map, title }) {
  return (
    <section className="map-card">
      <iframe title={title} src={map.embed} loading="lazy" />
      <a href={map.url} target="_blank" rel="noopener noreferrer" className="button button--light map-card__button">
        <Icon name="map-outline" size={18} /> Open in OpenStreetMap
      </a>
    </section>
  );
}

export default function Contacts({ data }) {
  return (
    <div className="contacts">
      <PageHero title={data.title} subtitle={data.subtitle} icon={data.icon} tone="violet" />
      <Channels channels={data.channels} />
      <div className="contacts__grid">
        <MapCard map={data.map} title="NEON PULSE showroom map" />
        <Hours hours={data.hours} />
      </div>
      <section className="block">
        <h2 className="block__title">Our locations</h2>
        <div className="office-grid">
          {data.offices.map((office) => (
            <Link key={office.slug} to={office.url} className="office-card">
              <img src={office.flag} alt="" className="office-card__flag" />
              <div>
                <h3>{office.city}</h3>
                <p className="office-card__name">{office.office}</p>
                <p>{office.note}</p>
                <span className="office-card__ship">
                  <Icon name="truck-outline" size={16} />
                  {office.shipping.days} days · {office.shipping.cost ? `from ${formatPrice(office.shipping.cost)}` : "free"}
                </span>
              </div>
              <Icon name="chevron-right" size={22} className="office-card__arrow" />
            </Link>
          ))}
        </div>
      </section>
    </div>
  );
}
