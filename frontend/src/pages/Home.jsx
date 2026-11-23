import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import Credit from "../components/Credit.jsx";
import Icon from "../components/Icon.jsx";
import { ProductGrid } from "../components/ProductCard.jsx";
import SectionHead from "../components/SectionHead.jsx";
import { NewsCard } from "./News.jsx";

function Slider({ slides }) {
  const [index, setIndex] = useState(0);
  const [paused, setPaused] = useState(false);

  useEffect(() => {
    if (paused) return undefined;
    const timer = setInterval(() => setIndex((value) => (value + 1) % slides.length), 6000);
    return () => clearInterval(timer);
  }, [paused, slides.length]);

  const move = (step) => setIndex((value) => (value + step + slides.length) % slides.length);

  return (
    <div className="slider" onMouseEnter={() => setPaused(true)} onMouseLeave={() => setPaused(false)}>
      {slides.map((slide, position) => (
        <article key={slide.title} className={`slide slide--${slide.tone} ${position === index ? "is-active" : ""}`} aria-hidden={position !== index}>
          <img src={slide.image} alt="" className="slide__image" />
          <div className="slide__content">
            <h1 className="slide__title">{slide.title}</h1>
            <p className="slide__subtitle">{slide.subtitle}</p>
            <Link to={slide.cta.url} className="button button--light" tabIndex={position === index ? 0 : -1}>
              {slide.cta.title}
              <Icon name="arrow-right" size={18} />
            </Link>
          </div>
          <Credit credit={slide.image_credit} className="slide__credit" />
        </article>
      ))}
      <button type="button" className="slider__arrow slider__arrow--prev" onClick={() => move(-1)} aria-label="Previous slide">
        <Icon name="chevron-left" size={28} />
      </button>
      <button type="button" className="slider__arrow slider__arrow--next" onClick={() => move(1)} aria-label="Next slide">
        <Icon name="chevron-right" size={28} />
      </button>
      <div className="slider__dots">
        {slides.map((slide, position) => (
          <button
            key={slide.title}
            type="button"
            className={position === index ? "is-active" : ""}
            onClick={() => setIndex(position)}
            aria-label={`Slide ${position + 1}`}
          />
        ))}
      </div>
    </div>
  );
}

export default function Home({ data }) {
  return (
    <div className="home">
      <section className="home-hero">
        <aside className="side-categories">
          {data.categories.map((category) => (
            <Link key={category.slug} to={category.url} className="side-categories__item">
              <Icon src={category.icon} size={20} />
              <span>{category.short_title}</span>
              <Icon name="chevron-right" size={18} className="side-categories__arrow" />
            </Link>
          ))}
          <Link to="/about/delivery/" className="side-categories__promo">
            <Icon name="truck-fast-outline" size={22} />
            <span>
              <strong>Free delivery</strong>
              <small>on every order in Ukraine</small>
            </span>
          </Link>
        </aside>
        <Slider slides={data.slides} />
      </section>

      <section className="advantages">
        {data.advantages.map((item) => (
          <div key={item.title} className="advantage">
            <span className="advantage__icon">
              <Icon src={item.icon} size={26} />
            </span>
            <div>
              <h3>{item.title}</h3>
              <p>{item.text}</p>
            </div>
          </div>
        ))}
      </section>

      <section className="block">
        <SectionHead title="Hot deals" subtitle="Limited prices on booth-tested gear" link="/catalog/" />
        <ProductGrid products={data.deals.slice(0, 5)} columns="five" />
      </section>

      <section className="block">
        <SectionHead title="Shop by category" link="/catalog/" linkTitle="Full catalog" />
        <div className="category-tiles">
          {data.categories.map((category) => (
            <Link key={category.slug} to={category.url} className="category-tile">
              <img src={category.image} alt="" loading="lazy" />
              <span className="category-tile__label">
                <strong>{category.short_title}</strong>
                <small>{category.count} products</small>
              </span>
            </Link>
          ))}
        </div>
      </section>

      <section className="showroom">
        <img src={data.showroom.image} alt="" loading="lazy" />
        <div className="showroom__content">
          <span className="eyebrow">Odesa showroom</span>
          <h2>{data.showroom.title}</h2>
          <p>{data.showroom.text}</p>
          <Link to={data.showroom.cta.url} className="button button--primary">
            {data.showroom.cta.title}
            <Icon name="arrow-right" size={18} />
          </Link>
        </div>
        <Credit credit={data.showroom.image_credit} className="showroom__credit" />
      </section>

      <section className="block">
        <SectionHead title="Bestsellers" subtitle="What DJs buy the most this month" link="/catalog/" />
        <ProductGrid products={data.bestsellers.slice(0, 5)} columns="five" />
      </section>

      <section className="block">
        <SectionHead title="Official dealer" subtitle="Brands we work with directly" link="/about/brands/" linkTitle="All brands" />
        <div className="brand-strip">
          {data.brands.map((brand) => (
            <span key={brand} className="brand-strip__item">
              {brand}
            </span>
          ))}
        </div>
      </section>

      <section className="block">
        <SectionHead title="News & stories" link="/news/" linkTitle="All news" />
        <div className="news-grid">
          {data.news.map((item) => (
            <NewsCard key={item.id} item={item} />
          ))}
        </div>
      </section>
    </div>
  );
}
