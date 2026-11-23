import { useState } from "react";
import { postJson } from "../api.js";
import { useSession } from "../session.js";
import Icon from "./Icon.jsx";

const WIDE = new Set(["radio", "textarea"]);

function initialValues(form) {
  return Object.fromEntries(form.fields.map((field) => [field.name, field.value]));
}

function PasswordInput({ field, value, onChange, invalid }) {
  const [visible, setVisible] = useState(false);
  return (
    <div className="field__password">
      <input
        id={`id_${field.name}`}
        name={field.name}
        type={visible ? "text" : "password"}
        value={value}
        onChange={onChange}
        required={field.required}
        autoComplete={field.autocomplete || undefined}
        aria-invalid={invalid}
      />
      <button type="button" onClick={() => setVisible((current) => !current)} aria-label={visible ? "Hide password" : "Show password"}>
        <Icon name={visible ? "eye-off-outline" : "eye-outline"} size={20} />
      </button>
    </div>
  );
}

function Control({ field, value, onChange, icons }) {
  const invalid = field.errors.length > 0;
  const common = {
    id: `id_${field.name}`,
    name: field.name,
    value,
    onChange: (event) => onChange(field.name, event.target.value),
    required: field.required,
    placeholder: field.placeholder || undefined,
    autoComplete: field.autocomplete || undefined,
    "aria-invalid": invalid,
  };
  if (field.type === "password") return <PasswordInput field={field} value={value} onChange={common.onChange} invalid={invalid} />;
  if (field.type === "textarea") return <textarea rows={3} {...common} />;
  if (field.type === "select") {
    return (
      <select {...common}>
        {field.choices.map((choice) => (
          <option key={choice.value} value={choice.value}>
            {choice.label}
          </option>
        ))}
      </select>
    );
  }
  if (field.type === "radio") {
    return (
      <div className="choice-grid" role="radiogroup" aria-labelledby={`label_${field.name}`}>
        {field.choices.map((choice) => (
          <label key={choice.value} className={`choice ${value === choice.value ? "is-checked" : ""}`}>
            <input type="radio" name={field.name} value={choice.value} checked={value === choice.value} onChange={() => onChange(field.name, choice.value)} />
            {icons?.[choice.value] && <Icon name={icons[choice.value]} size={22} />}
            <span>{choice.label}</span>
          </label>
        ))}
      </div>
    );
  }
  return <input type={field.type} {...common} />;
}

export default function SchemaForm({ form, action, submitLabel, submitIcon, extra, onSuccess, isHidden, icons, disabled, footer }) {
  const { go, csrf } = useSession();
  const [schema, setSchema] = useState(form);
  const [values, setValues] = useState(() => initialValues(form));
  const [busy, setBusy] = useState(false);
  const [failure, setFailure] = useState(null);

  const change = (name, value) => {
    setValues((current) => ({ ...current, [name]: value }));
    setSchema((current) => ({
      ...current,
      fields: current.fields.map((field) => (field.name === name && field.errors.length ? { ...field, errors: [] } : field)),
    }));
  };

  const submit = async (event) => {
    event.preventDefault();
    if (busy || disabled) return;
    setBusy(true);
    setFailure(null);
    try {
      const { ok, data } = await postJson(action, { ...values, ...(extra ? extra() : {}) }, csrf);
      if (ok && data?.ok) {
        onSuccess?.(data);
        go(data.redirect);
        return;
      }
      if (data?.form) setSchema(data.form);
      else setFailure("Your session has expired. Refresh the page and try again.");
    } catch {
      setFailure("Could not reach the server. Is Django running?");
    }
    setBusy(false);
  };

  const errors = failure ? [...schema.errors, failure] : schema.errors;

  return (
    <form className="form" onSubmit={submit} noValidate>
      {errors.length > 0 && (
        <div className="form__alert" role="alert">
          <Icon name="alert-circle-outline" size={20} />
          <div>
            {errors.map((error) => (
              <p key={error}>{error}</p>
            ))}
          </div>
        </div>
      )}
      <div className="form__grid">
        {schema.fields
          .filter((field) => !isHidden?.(field.name, values))
          .map((field) => (
            <div key={field.name} className={`field field--${field.name} ${WIDE.has(field.type) ? "field--wide" : ""} ${field.errors.length ? "has-error" : ""}`}>
              <label id={`label_${field.name}`} htmlFor={field.type === "radio" ? undefined : `id_${field.name}`} className="field__label">
                {field.label}
                {!field.required && <span className="field__optional">optional</span>}
              </label>
              <Control field={field} value={values[field.name] ?? ""} onChange={change} icons={icons} />
              {field.errors.map((error) => (
                <p key={error} className="field__error">
                  {error}
                </p>
              ))}
              {!field.errors.length && field.help && <p className="field__help">{field.help}</p>}
            </div>
          ))}
      </div>
      <button type="submit" className="button button--primary button--lg button--block" disabled={busy || disabled}>
        {busy ? <span className="spinner" aria-hidden="true" /> : submitIcon && <Icon name={submitIcon} size={20} />}
        {busy ? "Please wait…" : submitLabel}
      </button>
      {footer}
    </form>
  );
}
