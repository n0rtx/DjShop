import { Link, useLocation } from "react-router-dom";
import Icon from "../components/Icon.jsx";
import SchemaForm from "../components/SchemaForm.jsx";

const PERKS = [
  { icon: "history", text: "Every order saved in your history" },
  { icon: "lightning-bolt-outline", text: "Faster checkout with saved details" },
  { icon: "shield-check-outline", text: "Study project: no real payments" },
];

export default function Auth({ payload, data }) {
  const location = useLocation();
  const isLogin = payload.page === "login";
  return (
    <div className="auth">
      <section className="auth__card">
        <span className="auth__icon">
          <Icon name={isLogin ? "login-variant" : "account-plus-outline"} size={28} />
        </span>
        <h1 className="page-title">{data.title}</h1>
        <p className="page-lead">{data.subtitle}</p>
        <SchemaForm
          form={data.form}
          action={location.pathname + location.search}
          submitLabel={isLogin ? "Sign in" : "Create account"}
          submitIcon={isLogin ? "login" : "account-check-outline"}
          footer={
            <p className="auth__switch">
              {data.switch.text} <Link to={data.switch.url}>{data.switch.label}</Link>
            </p>
          }
        />
      </section>
      <aside className="auth__aside">
        <div className="auth__disc" aria-hidden="true" />
        <h2>Join the NEON PULSE crew</h2>
        <ul>
          {PERKS.map((perk) => (
            <li key={perk.text}>
              <Icon name={perk.icon} size={22} />
              {perk.text}
            </li>
          ))}
        </ul>
      </aside>
    </div>
  );
}
