import { formatPrice } from "../api.js";
import Icon from "../components/Icon.jsx";
import { Channels, Hours, MapCard } from "./Contacts.jsx";

export default function Office({ data }) {
  const { shipping } = data;
  return (
    <div className="office">
      <section className="office__hero">
        <img src={data.flag} alt={data.country} className="office__flag" />
        <div>
          <span className="eyebrow">{data.country}</span>
          <h1>{data.office}</h1>
          <p>
            {data.city} · {data.note}
          </p>
        </div>
      </section>
      <Channels channels={data.channels} />
      <div className="contacts__grid">
        <MapCard map={data.map} title={`${data.office} map`} />
        <div className="stack">
          <Hours hours={data.hours} />
          <section className="card">
            <h2 className="card__title">
              <Icon name="truck-fast-outline" size={22} /> Shipping to {data.country}
            </h2>
            <dl className="hours">
              <div>
                <dt>Delivery time</dt>
                <dd>{shipping.days} days</dd>
              </div>
              <div>
                <dt>Cost</dt>
                <dd>{shipping.cost ? formatPrice(shipping.cost) : "Free"}</dd>
              </div>
              {shipping.free_from > 0 && (
                <div>
                  <dt>Free shipping</dt>
                  <dd>from {formatPrice(shipping.free_from)}</dd>
                </div>
              )}
            </dl>
          </section>
        </div>
      </div>
    </div>
  );
}
