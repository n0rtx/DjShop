import Icon from "./Icon.jsx";

export default function PageHero({ title, subtitle, icon, image, children, tone = "violet" }) {
  return (
    <section className={`page-hero page-hero--${tone} ${image ? "page-hero--image" : ""}`}>
      {image && <img className="page-hero__bg" src={image} alt="" />}
      <div className="page-hero__content">
        {icon && (
          <span className="page-hero__icon">
            <Icon src={icon} size={26} />
          </span>
        )}
        <h1 className="page-hero__title">{title}</h1>
        {subtitle && <p className="page-hero__subtitle">{subtitle}</p>}
        {children}
      </div>
    </section>
  );
}
