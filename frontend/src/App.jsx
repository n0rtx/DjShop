import { useCallback, useEffect, useMemo, useRef, useState } from "react";
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
import Auth from "./pages/Auth.jsx";
import Account from "./pages/Account.jsx";
import Checkout from "./pages/Checkout.jsx";
import { SessionContext } from "./session.js";

function pickPage(payload) {
  const { page, subsection, data } = payload;
  if (page === "home") return Home;
  if (page === "catalog") return data.product ? Product : Catalog;
  if (page === "news") return data.body ? Article : News;
  if (page === "management") return subsection ? Member : Team;
  if (page === "about") return subsection ? AboutDetail : About;
  if (page === "contacts") return subsection ? Office : Contacts;
  if (page === "login" || page === "register") return Auth;
  if (page === "account") return Account;
  if (page === "checkout") return Checkout;
  return NotFound;
}

export default function App() {
  const location = useLocation();
  const navigate = useNavigate();
  const [payload, setPayload] = useState(readEmbeddedPayload);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [version, setVersion] = useState(0);
  const loadedPath = useRef(payload ? location.pathname + location.search : null);

  const go = useCallback(
    (to) => {
      loadedPath.current = null;
      setVersion((value) => value + 1);
      navigate(to);
    },
    [navigate],
  );

  useEffect(() => {
    const path = location.pathname + location.search;
    if (location.pathname.startsWith("/static/")) {
      navigate("/", { replace: true });
      return undefined;
    }
    if (loadedPath.current === path) return undefined;
    let cancelled = false;
    setLoading(true);
    setError(null);
    loadPage(path)
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
  }, [location.pathname, location.search, navigate, version]);

  useEffect(() => {
    if (payload) document.title = `${payload.title} | ${payload.site.name}`;
  }, [payload]);

  const session = useMemo(() => ({ user: payload?.user || null, csrf: payload?.csrf || "", go }), [payload, go]);

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
    <SessionContext.Provider value={session}>
      <Layout payload={payload} loading={loading}>
        <Page key={payload.path + version} payload={payload} data={payload.data} site={payload.site} />
      </Layout>
    </SessionContext.Provider>
  );
}
