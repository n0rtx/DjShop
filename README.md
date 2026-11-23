# NEON PULSE — DJ equipment store

Educational project: Django backend + React frontend for an online store that sells gear for DJs only.

```
DjShop/
├── backend/                Django (no models, no forms, no database)
│   ├── manage.py
│   ├── requirements.txt
│   ├── company_site/       main project: home, news, team, about, contacts, routing, 404
│   ├── catalog/            second app: categories and products
│   ├── templates/          HTML fallback templates + React mount point
│   └── static/
│       ├── img/            real product photos (Wikimedia Commons, CC licenses)
│       └── app/            built React bundle (app.js, app.css)
└── frontend/               React 18 + Vite + React Router
    └── src/
```

## Run (only Django is needed, the React bundle is already built)

```bash
python3 -m venv .venv
.venv/bin/pip install -r backend/requirements.txt
cd backend
../.venv/bin/python manage.py runserver
```

Open http://127.0.0.1:8000/

## Frontend development

```bash
cd frontend
npm install
npm run dev      # http://localhost:5173, data is proxied from Django on :8000
npm run build    # writes backend/static/app/app.js and app.css
```

## Sections

| Section  | URL            | Subsections |
|----------|----------------|-------------|
| Home     | `/`            | — |
| Catalog  | `/catalog/`    | controllers, players, mixers, headphones, studio, mics-accessories + product pages |
| News     | `/news/`       | arrivals, sale, firmware, events, guides + article pages |
| Team     | `/management/` | ceo, coo, product, support |
| About    | `/about/`      | history, values, brands, delivery |
| Contacts | `/contacts/`   | ukraine, france, austria, poland |

## Redirects and 404

- Unknown subsection inside a section → redirect to the section (`/news/yellowsubmarine` → `/news/`, `/catalog/guitars` → `/catalog/`).
- Unknown product in an existing category → 404 page.
- Unknown top-level section (`/nope`) → custom 404 page with status 404.
- Old aliases: `/contact/...` → `/contacts/...`, `/team/` → `/management/`, `/shop/` → `/catalog/` (301).
- URL without trailing slash → redirect to the slash version.

Product photos are taken from Wikimedia Commons and used under Creative Commons licenses; the author and license are shown on each product page.
