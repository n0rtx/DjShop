import { useEffect, useMemo, useRef, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { formatPrice } from "../api.js";
import Icon from "./Icon.jsx";

export default function Search({ index }) {
  const [query, setQuery] = useState("");
  const [focused, setFocused] = useState(false);
  const [active, setActive] = useState(0);
  const navigate = useNavigate();
  const box = useRef(null);

  const results = useMemo(() => {
    const words = query.trim().toLowerCase().split(/\s+/).filter(Boolean);
    if (!words.length) return [];
    return index.filter((item) => words.every((word) => `${item.name} ${item.brand}`.toLowerCase().includes(word))).slice(0, 6);
  }, [query, index]);

  useEffect(() => {
    const close = (event) => box.current && !box.current.contains(event.target) && setFocused(false);
    document.addEventListener("mousedown", close);
    return () => document.removeEventListener("mousedown", close);
  }, []);

  useEffect(() => setActive(0), [query]);

  const go = (item) => {
    setQuery("");
    setFocused(false);
    navigate(item.url);
  };

  const onKeyDown = (event) => {
    if (!results.length) return;
    if (event.key === "ArrowDown") {
      event.preventDefault();
      setActive((value) => (value + 1) % results.length);
    } else if (event.key === "ArrowUp") {
      event.preventDefault();
      setActive((value) => (value - 1 + results.length) % results.length);
    } else if (event.key === "Enter") {
      go(results[active]);
    } else if (event.key === "Escape") {
      setFocused(false);
    }
  };

  const showDropdown = focused && query.trim().length > 0;

  return (
    <div className="search" ref={box}>
      <Icon name="magnify" size={22} className="search__icon" />
      <input
        className="search__input"
        type="search"
        placeholder="Search controllers, headphones, brands…"
        value={query}
        onChange={(event) => setQuery(event.target.value)}
        onFocus={() => setFocused(true)}
        onKeyDown={onKeyDown}
        aria-label="Search products"
      />
      {showDropdown && (
        <div className="search__dropdown">
          {results.length ? (
            results.map((item, position) => (
              <Link
                key={item.url}
                to={item.url}
                className={`search__result ${position === active ? "is-active" : ""}`}
                onClick={() => {
                  setQuery("");
                  setFocused(false);
                }}
                onMouseEnter={() => setActive(position)}
              >
                <img src={item.image} alt="" />
                <span className="search__name">
                  <small>{item.brand}</small>
                  {item.name}
                </span>
                <strong>{formatPrice(item.price)}</strong>
              </Link>
            ))
          ) : (
            <p className="search__empty">Nothing found for “{query}”. Try “Pioneer” or “headphones”.</p>
          )}
        </div>
      )}
    </div>
  );
}
