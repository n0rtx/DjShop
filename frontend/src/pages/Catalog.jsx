import { useMemo, useState } from "react";
import { Link } from "react-router-dom";
import Icon from "../components/Icon.jsx";
import { ProductGrid } from "../components/ProductCard.jsx";

const SORTS = [
  { key: "popular", title: "Most popular", fn: (a, b) => b.reviews - a.reviews },
  { key: "cheap", title: "Price: low to high", fn: (a, b) => a.price - b.price },
  { key: "expensive", title: "Price: high to low", fn: (a, b) => b.price - a.price },
  { key: "rating", title: "Top rated", fn: (a, b) => b.rating - a.rating },
  { key: "discount", title: "Biggest discount", fn: (a, b) => b.discount - a.discount },
];

const PRICES = [
  { key: "all", title: "Any price", test: () => true },
  { key: "low", title: "Under $200", test: (price) => price < 200 },
  { key: "mid", title: "$200 – $700", test: (price) => price >= 200 && price <= 700 },
  { key: "high", title: "Over $700", test: (price) => price > 700 },
];

export default function Catalog({ data }) {
  const category = data.category;
  const [brands, setBrands] = useState([]);
  const [price, setPrice] = useState("all");
  const [inStock, setInStock] = useState(false);
  const [onSale, setOnSale] = useState(false);
  const [sort, setSort] = useState("popular");
  const [filtersOpen, setFiltersOpen] = useState(false);

  const products = useMemo(() => {
    const priceTest = PRICES.find((item) => item.key === price).test;
    const sorter = SORTS.find((item) => item.key === sort).fn;
    return data.products
      .filter((item) => !brands.length || brands.includes(item.brand))
      .filter((item) => priceTest(item.price))
      .filter((item) => !inStock || item.in_stock)
      .filter((item) => !onSale || item.old_price)
      .sort(sorter);
  }, [data.products, brands, price, inStock, onSale, sort]);

  const toggleBrand = (brand) => setBrands((current) => (current.includes(brand) ? current.filter((item) => item !== brand) : [...current, brand]));
  const reset = () => {
    setBrands([]);
    setPrice("all");
    setInStock(false);
    setOnSale(false);
  };
  const activeFilters = brands.length + (price !== "all") + inStock + onSale;

  return (
    <div className="catalog">
      <header className="catalog__head">
        <h1 className="page-title">{category ? category.title : data.title}</h1>
        <p className="page-lead">{category ? category.description : data.subtitle}</p>
      </header>

      {!category && (
        <div className="category-pills">
          {data.categories.map((item) => (
            <Link key={item.slug} to={item.url} className="category-pill">
              <img src={item.image} alt="" />
              <span>
                <strong>{item.short_title}</strong>
                <small>{item.count} products</small>
              </span>
            </Link>
          ))}
        </div>
      )}

      <div className="catalog__layout">
        <aside className={`filters ${filtersOpen ? "is-open" : ""}`}>
          <div className="filters__head">
            <h2>Filters</h2>
            {activeFilters > 0 && (
              <button type="button" className="link-button" onClick={reset}>
                Reset
              </button>
            )}
          </div>
          <fieldset className="filters__group">
            <legend>Availability</legend>
            <label className="check">
              <input type="checkbox" checked={inStock} onChange={(event) => setInStock(event.target.checked)} />
              <span>In stock only</span>
            </label>
            <label className="check">
              <input type="checkbox" checked={onSale} onChange={(event) => setOnSale(event.target.checked)} />
              <span>On sale</span>
            </label>
          </fieldset>
          <fieldset className="filters__group">
            <legend>Price</legend>
            {PRICES.map((item) => (
              <label key={item.key} className="check check--radio">
                <input type="radio" name="price" checked={price === item.key} onChange={() => setPrice(item.key)} />
                <span>{item.title}</span>
              </label>
            ))}
          </fieldset>
          <fieldset className="filters__group">
            <legend>Brand</legend>
            {data.brands.map((brand) => (
              <label key={brand} className="check">
                <input type="checkbox" checked={brands.includes(brand)} onChange={() => toggleBrand(brand)} />
                <span>{brand}</span>
                <small>{data.products.filter((item) => item.brand === brand).length}</small>
              </label>
            ))}
          </fieldset>
          <button type="button" className="button button--primary button--block filters__apply" onClick={() => setFiltersOpen(false)}>
            Show {products.length} products
          </button>
        </aside>

        <section className="catalog__results">
          <div className="toolbar">
            <button type="button" className="button button--ghost toolbar__filters" onClick={() => setFiltersOpen(true)}>
              <Icon name="tune-variant" size={18} />
              Filters {activeFilters > 0 && <span className="count-dot">{activeFilters}</span>}
            </button>
            <span className="toolbar__count">
              {products.length} of {data.products.length} products
            </span>
            <label className="select">
              <span>Sort:</span>
              <select value={sort} onChange={(event) => setSort(event.target.value)}>
                {SORTS.map((item) => (
                  <option key={item.key} value={item.key}>
                    {item.title}
                  </option>
                ))}
              </select>
            </label>
          </div>
          {products.length ? (
            <ProductGrid products={products} />
          ) : (
            <div className="empty">
              <Icon name="filter-remove-outline" size={48} />
              <h3>No products match these filters</h3>
              <button type="button" className="button button--primary" onClick={reset}>
                Reset filters
              </button>
            </div>
          )}
        </section>
      </div>
    </div>
  );
}
