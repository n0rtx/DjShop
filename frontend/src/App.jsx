import { useEffect, useRef, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { loadPage, readEmbeddedPayload } from "./api.js";
import Layout from "./components/Layout.jsx";
import Home from "./pages/Home.jsx";
import Catalog from "./pages/Catalog.jsx";
import Product from "./pages/Product.jsx";
import News from "./pages/News.jsx";
import Article from "./pages/Article.jsx";
import Team from "./pages/Team.jsx";
import Member from "./pages/Member.jsx";
import About from "./pages/About.jsx";
import AboutDetail from "./pages/AboutDetail.jsx";
import Contacts from "./pages/Contacts.jsx";
import Office from "./pages/Office.jsx";
import NotFound from "./pages/NotFound.jsx";

function pickPage(payload) {
  const { page, subsection, data } = payload;
  if (page === "home") return Home;
  if (page === "catalog") return data.product ? Product : Catalog;
  if (page === "news") return data.body ? Article : News;
  if (page === "management") return subsection ? Member : Team;
  if (page === "about") return subsection ? AboutDetail : About;
  if (page === "contacts") return subsection ? Office : Contacts;
  return NotFound;
}

export default function App() {
  const location = useLocation();
  const navigate = useNavigate();
  const [payload, setPayload] = useState(readEmbeddedPayload);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const loadedPath = useRef(payload ? location.pathname : null);

  useEffect(() => {
    const path = location.pathname;
    if (path.startsWith("/static/")) {
      navigate("/", { replace: true });
      return undefined;
    }
    if (loadedPath.current === path) return undefined;
    let cancelled = false;
    setLoading(true);
    setError(null);
    loadPage(path + location.search)
      .then(({ payload: next, finalPath }) => {
        if (cancelled) return;
        if (finalPath && finalPath !== path) {
          loadedPath.current = finalPath;
          navigate(finalPath, { replace: true });
        } else {
          loadedPath.current = path;
        }
        setPayload(next);
        window.scrollTo({ top: 0, behavior: "instant" });
      })
      .catch(() => !cancelled && setError("Could not reach the server. Is Django running?"))
      .finally(() => !cancelled && setLoading(false));
    return () => {
      cancelled = true;
    };
  }, [location.pathname, location.search, navigate]);

  useEffect(() => {
    if (payload) document.title = `${payload.title} | ${payload.site.name}`;
  }, [payload]);

  if (!payload) {
    return (
      <div className="boot">
        <div className="boot__disc" />
        <p>{error || "Loading NEON PULSE…"}</p>
      </div>
    );
  }

  const Page = pickPage(payload);

  return (
    <Layout payload={payload} loading={loading}>
      <Page key={payload.path} payload={payload} data={payload.data} site={payload.site} />
    </Layout>
  );
}
