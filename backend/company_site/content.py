from catalog.content import BRANDS, CATEGORIES, bestsellers, catalog_menu, deals, products_by_ids, cards, search_index
from catalog.credits import credit

from .assets import flag, icon, image

SITE = {
    "name": "NEON PULSE",
    "tagline": "Gear for DJs who play after midnight",
    "currency": "USD",
    "theme": {
        "style": "modern-neon",
        "colors": {
            "background": "#f4f5fa",
            "surface": "#ffffff",
            "dark": "#11111b",
            "primary": "#6c3cff",
            "secondary": "#ff2e88",
            "accent": "#00b894",
            "warning": "#ffb020",
            "text": "#1b1b2f",
            "muted": "#6b6f80",
        },
        "fonts": {
            "heading": "Unbounded",
            "body": "Manrope",
        },
    },
    "logo": icon("disc-player", "ff2e88"),
    "promo": "Free shipping in Ukraine on every order · 2-year warranty · Booth-tested gear",
    "phone": {"value": "+380 48 700 12 34", "href": "tel:+380487001234"},
    "navigation": [
        {"key": "home", "title": "Home", "url": "/", "icon": icon("home-outline")},
        {"key": "catalog", "title": "Catalog", "url": "/catalog/", "icon": icon("view-grid-outline")},
        {"key": "news", "title": "News", "url": "/news/", "icon": icon("newspaper-variant-outline")},
        {"key": "management", "title": "Team", "url": "/management/", "icon": icon("account-group-outline")},
        {"key": "about", "title": "About", "url": "/about/", "icon": icon("information-outline")},
        {"key": "contacts", "title": "Contacts", "url": "/contacts/", "icon": icon("map-marker-outline")},
    ],
    "catalog_menu": catalog_menu(),
    "search_index": search_index(),
    "socials": [
        {"name": "Instagram", "url": "https://instagram.com/neonpulse.dj", "icon": icon("instagram")},
        {"name": "YouTube", "url": "https://youtube.com/@neonpulsedj", "icon": icon("youtube")},
        {"name": "SoundCloud", "url": "https://soundcloud.com/neonpulsedj", "icon": icon("soundcloud")},
        {"name": "Telegram", "url": "https://t.me/neonpulsedj", "icon": icon("send")},
    ],
    "footer_links": [
        {
            "title": "Shop",
            "links": [{"title": item["short_title"], "url": f"/catalog/{item['slug']}/"} for item in CATEGORIES],
        },
        {
            "title": "Company",
            "links": [
                {"title": "About us", "url": "/about/"},
                {"title": "Our history", "url": "/about/history/"},
                {"title": "Brands", "url": "/about/brands/"},
                {"title": "Team", "url": "/management/"},
                {"title": "News", "url": "/news/"},
            ],
        },
        {
            "title": "Help",
            "links": [
                {"title": "Delivery & payment", "url": "/about/delivery/"},
                {"title": "Contacts", "url": "/contacts/"},
                {"title": "Showroom in Odesa", "url": "/contacts/ukraine/"},
                {"title": "Buying guides", "url": "/news/guides/"},
            ],
        },
    ],
    "payments": ["Visa", "Mastercard", "Apple Pay", "Google Pay", "PayPal"],
    "footer": "© 2026 NEON PULSE DJ Supply. Educational project. All prices in USD.",
    "photo_note": "Product photos: Wikimedia Commons contributors, used under Creative Commons licenses. See each product page for credits.",
}

ADVANTAGES = [
    {"title": "Fast shipping", "text": "Same-day dispatch for orders placed before 4 PM.", "icon": icon("truck-fast-outline")},
    {"title": "Official warranty", "text": "2-year manufacturer warranty, 12 months on renewed gear.", "icon": icon("shield-check-outline")},
    {"title": "DJ support", "text": "Working DJs answer your questions, not call-center bots.", "icon": icon("headset")},
    {"title": "Booth tested", "text": "Each unit is checked in our demo booth before it ships.", "icon": icon("lightning-bolt-outline")},
]


def article(pid, slug, date, tag, title, excerpt, image_slug, folder, body, read_time):
    return {
        "id": pid,
        "slug": slug,
        "date": date,
        "tag": tag,
        "tag_slug": tag.lower(),
        "title": title,
        "excerpt": excerpt,
        "image": image(folder, image_slug),
        "image_credit": credit(image_slug),
        "body": body,
        "read_time": read_time,
        "url": f"/news/{tag.lower()}/{slug}/",
    }


NEWS_ITEMS = [
    article(
        1, "traktor-s4-mk3-in-stock", "2026-11-20", "Arrivals",
        "Traktor Kontrol S4 MK3 is back in stock",
        "The haptic-drive flagship has landed in our warehouse. Limited batch at $899 instead of $999.",
        "traktor-kontrol-s4-mk3", "products",
        [
            "After two months of waiting the new batch of Native Instruments Traktor Kontrol S4 MK3 has arrived at our Odesa warehouse.",
            "We tested every unit in the demo booth: jog wheels, displays and the audio interface. Until the end of November the controller costs $899 instead of $999.",
            "Orders placed before 4 PM ship the same day. Pickup is available in the Odesa showroom and at our Paris, Vienna and Warsaw points.",
        ],
        3,
    ),
    article(
        2, "neon-week-headphones", "2026-11-17", "Sale",
        "Neon Week: up to 15% off DJ headphones",
        "Sennheiser, Beyerdynamic and Audio-Technica headphones at cyber prices until November 30.",
        "sennheiser-hd-25", "products",
        [
            "Neon Week is our biggest sale of the year. This time we focus on headphones, the tool every DJ uses every night.",
            "The Sennheiser HD 25 drops to $149.95, the Beyerdynamic DT 770 PRO to $159. Stock is limited and prices return to normal on December 1.",
            "Not sure which model fits you? Read our headphone guide or ask the crew in Telegram.",
        ],
        2,
    ),
    article(
        3, "cdj-firmware-explained", "2026-11-09", "Firmware",
        "CDJ firmware updates explained",
        "Our tech crew explains how to update older CDJs safely and what changes after the update.",
        "pioneer-cdj-2000", "products",
        [
            "Many DJs still play on CDJ-2000 and CDJ-2000NXS players. Pioneer DJ keeps publishing firmware updates for them, and installing them is easy.",
            "Download the firmware file from the official website, copy it to the root of a USB drive, hold the menu button while switching the player on and follow the instructions on the screen.",
            "Never switch the player off during the update. If something goes wrong, bring the player to our showroom: we will restore it for free.",
        ],
        4,
    ),
    article(
        4, "odesa-showroom-night", "2026-10-28", "Events",
        "Showroom Night in Odesa",
        "Free entry, live b2b sets and hands-on time with flagship mixers and controllers.",
        "club-booth", "banners",
        [
            "On December 6 the Odesa showroom turns into a club. Our crew and guest DJs will play b2b sets on the full Pioneer DJ club setup.",
            "Between sets you can try any controller, mixer or turntable from the catalog and ask our team anything about your setup.",
            "Entry is free. The party starts at 19:00 at 12 Derybasivska St.",
        ],
        2,
    ),
    article(
        5, "mic-guide-for-mcs", "2026-10-15", "Guides",
        "Choosing a vocal mic for your DJ set",
        "SM58 or Beta 58A? A practical guide for DJs who also hold the mic.",
        "shure-beta-58a", "products",
        [
            "If you talk to the crowd or MC during your sets, a good dynamic microphone is a must. The two most popular choices are the Shure SM58 and Beta 58A.",
            "The SM58 is warm, forgiving and cheap. The Beta 58A is brighter, louder and its supercardioid pattern rejects more noise from the speakers.",
            "Our advice: start with the SM58. If you play loud clubs and need your voice to cut through, choose the Beta 58A.",
        ],
        5,
    ),
    article(
        6, "vinyl-is-back", "2026-10-02", "Arrivals",
        "Renewed Technics turntables have arrived",
        "SL-1200MK5 and SL-1210MK2 decks, fully serviced by our vinyl techs, are now in the catalog.",
        "technics-sl-1210-mk2", "products",
        [
            "Vinyl DJing is more popular than ever, and the Technics SL-1200 series is still the reference.",
            "Each renewed deck gets a full service: calibration, tonearm cleaning, new feet and a fresh dust cover. They come with a 12-month store warranty.",
            "Stock is very limited: only a few units of each model.",
        ],
        3,
    ),
    article(
        7, "first-controller-guide", "2026-09-18", "Guides",
        "Your first DJ controller: what to buy in 2026",
        "FLX4, REV1 or Mixtrack Pro FX? We compare the best controllers for beginners.",
        "pioneer-ddj-flx4", "products",
        [
            "Choosing your first controller is the hardest decision. Here is our short answer: buy the Pioneer DJ DDJ-FLX4 if you want to play in clubs one day.",
            "If scratching is your thing, the DDJ-REV1 copies the battle layout of turntables and a mixer. On a budget? The Numark Mixtrack Pro FX gives you big jog wheels for $249.",
            "All three are in stock and can be tried in our showroom.",
        ],
        6,
    ),
    article(
        8, "studio-week", "2026-09-05", "Events",
        "Studio Week: free production workshops",
        "Learn to make your own edits with MPC and KRK monitors. Five evenings, free entry.",
        "akai-mpc-live", "products",
        [
            "Many DJs want to produce their own edits. During Studio Week our product team shows how to do it with an Akai MPC Live and a pair of KRK monitors.",
            "Each evening covers one topic: sampling, drums, bass, arrangement and mixdown.",
            "Workshops are free, but places are limited. Follow our Telegram channel to get the schedule.",
        ],
        2,
    ),
]

NEWS_TAGS = [
    {"slug": "arrivals", "title": "New Arrivals", "description": "Fresh gear that just landed in our warehouse.", "icon": icon("package-variant-closed")},
    {"slug": "sale", "title": "Sales & Deals", "description": "Discounts and limited offers on DJ equipment.", "icon": icon("sale")},
    {"slug": "firmware", "title": "Firmware", "description": "Software and firmware news for your decks.", "icon": icon("update")},
    {"slug": "events", "title": "Events", "description": "Showroom nights, workshops and live sets.", "icon": icon("calendar-star")},
    {"slug": "guides", "title": "Guides", "description": "Practical buying and setup guides for DJs.", "icon": icon("book-open-variant")},
]

HOME = {
    "slides": [
        {
            "title": "Plug in. Drop the bass. Own the night.",
            "subtitle": "Controllers, CDJs, mixers and headphones for DJs only. Tested in our booth before they reach yours.",
            "cta": {"title": "Shop the catalog", "url": "/catalog/"},
            "image": image("banners", "club-booth"),
            "image_credit": credit("club-booth"),
            "tone": "violet",
        },
        {
            "title": "Neon Week: up to 15% off headphones",
            "subtitle": "Sennheiser HD 25, Beyerdynamic DT 770 PRO and more. Until November 30.",
            "cta": {"title": "See the deals", "url": "/catalog/headphones/"},
            "image": image("banners", "tresor-turntable"),
            "image_credit": credit("tresor-turntable"),
            "tone": "pink",
        },
        {
            "title": "Your first controller starts at $249",
            "subtitle": "Pioneer DJ, Native Instruments and Numark controllers with free setup consultation.",
            "cta": {"title": "Choose a controller", "url": "/catalog/controllers/"},
            "image": image("banners", "ddj-sx-outdoor"),
            "image_credit": credit("ddj-sx-outdoor"),
            "tone": "teal",
        },
    ],
    "categories": catalog_menu(),
    "deals": deals(),
    "bestsellers": bestsellers(),
    "advantages": ADVANTAGES,
    "brands": BRANDS,
    "news": NEWS_ITEMS[:3],
    "showroom": {
        "title": "Try before you buy",
        "text": "Visit our Odesa showroom: a full club booth where you can test every controller, mixer and turntable from the catalog.",
        "image": image("banners", "cdj-nxs2-setup"),
        "image_credit": credit("cdj-nxs2-setup"),
        "cta": {"title": "Plan a visit", "url": "/contacts/ukraine/"},
    },
}

NEWS = {
    "title": "News & Stories",
    "subtitle": "Gear releases, firmware updates, events and guides from the NEON PULSE crew.",
    "icon": icon("newspaper-variant-outline"),
    "tags": NEWS_TAGS,
    "items": NEWS_ITEMS,
}

MEMBERS = [
    {"id": 1, "slug": "ceo", "name": "Maksym Koval", "initials": "MK", "alias": "DJ VOLTAGE", "position": "Founder & CEO", "bio": "Club resident for 12 years before building the store he always wanted to shop in.", "gradient": ["#6c3cff", "#ff2e88"], "icon": icon("account-music")},
    {"id": 2, "slug": "coo", "name": "Olena Shevchuk", "initials": "OS", "alias": "NEONA", "position": "Chief Operating Officer", "bio": "Runs logistics and makes sure every CDJ reaches its booth on time.", "gradient": ["#00b894", "#6c3cff"], "icon": icon("account-tie")},
    {"id": 3, "slug": "product", "name": "Artem Bondar", "initials": "AB", "alias": "SUBFRAME", "position": "Head of Product", "bio": "Tests every controller, mixer and headphone before it hits the catalog.", "gradient": ["#ffb020", "#ff2e88"], "icon": icon("cog-outline")},
    {"id": 4, "slug": "support", "name": "Iryna Melnyk", "initials": "IM", "alias": "GLITCHA", "position": "Head of Customer Support", "bio": "Leads a team of working DJs who answer customer questions day and night.", "gradient": ["#2d9cff", "#00b894"], "icon": icon("headset")},
]

MANAGEMENT = {
    "title": "Meet the Crew",
    "subtitle": "Working DJs who run NEON PULSE and pick every product in the catalog.",
    "icon": icon("account-group-outline"),
    "members": MEMBERS,
}

TIMELINE = [
    {"year": 2018, "title": "First drop", "text": "Started as a small Telegram shop selling used CDJs."},
    {"year": 2020, "title": "Online store", "text": "Launched the online catalog and nationwide delivery."},
    {"year": 2022, "title": "Demo booth", "text": "Opened a demo booth where every product can be tested."},
    {"year": 2024, "title": "Official dealer", "text": "Became an official dealer for leading DJ brands."},
    {"year": 2025, "title": "Europe", "text": "Opened pickup points in Paris, Vienna and Warsaw."},
    {"year": 2026, "title": "Showroom", "text": "Opened the flagship showroom in Odesa."},
]

VALUES = [
    {"title": "DJs only", "text": "No guitars, no pianos. Only gear for DJs and producers.", "icon": icon("disc-player")},
    {"title": "Honest advice", "text": "We recommend what fits your set, not what costs more.", "icon": icon("handshake-outline")},
    {"title": "Tested gear", "text": "Each unit is checked in the booth before shipping.", "icon": icon("shield-check-outline")},
    {"title": "Second life", "text": "We renew legendary gear so more DJs can afford it.", "icon": icon("recycle")},
]

ABOUT = {
    "title": "About NEON PULSE",
    "subtitle": "A DJ-only store born in the booth.",
    "icon": icon("information-outline"),
    "image": image("banners", "cdj-nxs2-setup"),
    "image_credit": credit("cdj-nxs2-setup"),
    "description": "NEON PULSE sells equipment for DJs and nothing else: controllers, media players, turntables, mixers, headphones, microphones and studio gear. Every product is chosen and tested by working DJs.",
    "stats": [
        {"label": "Years on the decks", "value": "8"},
        {"label": "DJs equipped", "value": "25,000+"},
        {"label": "Products tested", "value": "1,200+"},
        {"label": "Brands", "value": "40+"},
    ],
    "timeline": TIMELINE,
    "values": VALUES,
}

HOURS = [
    {"days": "Mon – Fri", "time": "11:00 – 21:00"},
    {"days": "Sat", "time": "12:00 – 22:00"},
    {"days": "Sun", "time": "12:00 – 18:00"},
]


def osm(lat, lng):
    return {
        "lat": lat,
        "lng": lng,
        "zoom": 16,
        "url": f"https://www.openstreetmap.org/?mlat={lat}&mlon={lng}#map=16/{lat}/{lng}",
        "embed": f"https://www.openstreetmap.org/export/embed.html?bbox={lng - 0.006}%2C{lat - 0.003}%2C{lng + 0.006}%2C{lat + 0.003}&layer=mapnik&marker={lat}%2C{lng}",
    }


def channels(address, phone, phone_href, email):
    return [
        {"type": "address", "label": "Address", "value": address, "icon": icon("map-marker-outline")},
        {"type": "phone", "label": "Phone", "value": phone, "href": f"tel:{phone_href}", "icon": icon("phone-outline")},
        {"type": "email", "label": "Email", "value": email, "href": f"mailto:{email}", "icon": icon("email-outline")},
    ]


def office(slug, country, code, office_name, city, address, phone, phone_href, hours, shipping, lat, lng, note):
    return {
        "slug": slug,
        "title": country,
        "icon": flag(code),
        "data": {
            "country": country,
            "office": office_name,
            "city": city,
            "flag": flag(code),
            "note": note,
            "channels": channels(address, phone, phone_href, f"{slug}@neonpulse.dj"),
            "hours": hours,
            "shipping": shipping,
            "map": osm(lat, lng),
        },
    }


OFFICES = [
    office(
        "ukraine", "Ukraine", "ua", "Flagship Showroom", "Odesa", "12 Derybasivska St, Odesa 65026, Ukraine",
        "+380 48 700 12 34", "+380487001234", HOURS, {"days": "1–2", "cost": 0.00, "free_from": 0.00}, 46.4843, 30.7387,
        "Full club booth, test any product, free parking for customers.",
    ),
    office(
        "france", "France", "fr", "Paris Pickup Point", "Paris", "48 Rue Oberkampf, 75011 Paris, France",
        "+33 1 84 60 12 34", "+33184601234",
        [{"days": "Tue – Sat", "time": "12:00 – 20:00"}, {"days": "Sun – Mon", "time": "Closed"}],
        {"days": "3–5", "cost": 19.00, "free_from": 499.00}, 48.8650, 2.3770,
        "Pickup and returns. Demo of headphones and controllers.",
    ),
    office(
        "austria", "Austria", "at", "Vienna Pickup Point", "Vienna", "Mariahilfer Str. 88, 1070 Vienna, Austria",
        "+43 1 253 12 34", "+4312531234",
        [{"days": "Mon – Fri", "time": "11:00 – 19:00"}, {"days": "Sat", "time": "10:00 – 17:00"}, {"days": "Sun", "time": "Closed"}],
        {"days": "3–4", "cost": 15.00, "free_from": 399.00}, 48.1980, 16.3460,
        "Pickup, returns and warranty service.",
    ),
    office(
        "poland", "Poland", "pl", "Warsaw Pickup Point", "Warsaw", "ul. Mokotowska 51, 00-542 Warsaw, Poland",
        "+48 22 307 12 34", "+48223071234",
        [{"days": "Mon – Fri", "time": "10:00 – 19:00"}, {"days": "Sat", "time": "11:00 – 16:00"}, {"days": "Sun", "time": "Closed"}],
        {"days": "2–3", "cost": 12.00, "free_from": 299.00}, 52.2240, 21.0180,
        "Pickup and returns. Turntable service corner.",
    ),
]

CONTACTS = {
    "title": "Contacts",
    "subtitle": "Visit the showroom, pick up your order in Europe or reach the crew online.",
    "icon": icon("map-marker-outline"),
    "channels": [
        {"type": "address", "label": "Showroom", "value": "12 Derybasivska St, Odesa, Ukraine", "icon": icon("map-marker-outline")},
        {"type": "phone", "label": "Phone", "value": "+380 48 700 12 34", "href": "tel:+380487001234", "icon": icon("phone-outline")},
        {"type": "email", "label": "Email", "value": "hello@neonpulse.dj", "href": "mailto:hello@neonpulse.dj", "icon": icon("email-outline")},
        {"type": "telegram", "label": "Telegram", "value": "@neonpulsedj", "href": "https://t.me/neonpulsedj", "icon": icon("send")},
    ],
    "hours": HOURS,
    "hours_icon": icon("clock-outline"),
    "map": osm(46.4843, 30.7387),
    "offices": [{"slug": item["slug"], "url": f"/contacts/{item['slug']}/", **item["data"]} for item in OFFICES],
}


def news_category(tag):
    return {
        "slug": tag["slug"],
        "title": tag["title"],
        "icon": tag["icon"],
        "data": {**tag, "items": [item for item in NEWS_ITEMS if item["tag_slug"] == tag["slug"]]},
    }


def member_profile(slug, responsibilities, favorite_gear, quote, skills):
    member = next(item for item in MEMBERS if item["slug"] == slug)
    return {
        "slug": slug,
        "title": member["position"],
        "icon": member["icon"],
        "data": {
            **member,
            "quote": quote,
            "skills": skills,
            "responsibilities": responsibilities,
            "favorite_gear": cards(products_by_ids(favorite_gear)),
        },
    }


SUBSECTIONS = {
    "news": [news_category(tag) for tag in NEWS_TAGS],
    "management": [
        member_profile("ceo", ["Company strategy", "Brand partnerships", "Artist relations"], [15, 9, 16], "Every DJ deserves gear that never lets the floor go quiet.", ["Techno", "Vinyl", "12 years in clubs"]),
        member_profile("coo", ["Logistics and warehouse", "International pickup points", "Delivery partners"], [2, 17, 23], "If it ships tonight, it plays tomorrow.", ["Operations", "House", "Supply chain"]),
        member_profile("product", ["Catalog curation", "Booth testing", "Renewed gear program"], [1, 14, 21], "Nothing enters the catalog until it survives a six-hour set.", ["Drum & bass", "Production", "Hardware repair"]),
        member_profile("support", ["Customer support", "Warranty and returns", "Setup consultations"], [3, 18, 24], "Ask us anything about your setup. We have been there.", ["Open format", "Scratch", "Teaching"]),
    ],
    "about": [
        {
            "slug": "history",
            "title": "History",
            "icon": icon("history"),
            "data": {"kind": "history", "title": "Our History", "description": "From a Telegram shop with used CDJs to a flagship DJ showroom.", "timeline": TIMELINE, "image": image("banners", "tresor-turntable"), "image_credit": credit("tresor-turntable")},
        },
        {
            "slug": "values",
            "title": "Values",
            "icon": icon("heart-pulse"),
            "data": {"kind": "values", "title": "Our Values", "description": "Principles every member of the crew follows.", "values": VALUES},
        },
        {
            "slug": "brands",
            "title": "Brands",
            "icon": icon("factory"),
            "data": {
                "kind": "brands",
                "title": "Our Brands",
                "description": "We are an official dealer for leading DJ equipment manufacturers.",
                "brands": [
                    {"name": "Pioneer DJ", "country": "Japan", "since": 1938, "categories": ["Controllers", "Players", "Mixers"]},
                    {"name": "Technics", "country": "Japan", "since": 1965, "categories": ["Turntables"]},
                    {"name": "Native Instruments", "country": "Germany", "since": 1996, "categories": ["Controllers"]},
                    {"name": "Numark", "country": "USA", "since": 1971, "categories": ["Controllers"]},
                    {"name": "Reloop", "country": "Germany", "since": 1995, "categories": ["Turntables", "Headphones", "Accessories"]},
                    {"name": "Sennheiser", "country": "Germany", "since": 1945, "categories": ["Headphones"]},
                    {"name": "Audio-Technica", "country": "Japan", "since": 1962, "categories": ["Headphones"]},
                    {"name": "Beyerdynamic", "country": "Germany", "since": 1924, "categories": ["Headphones"]},
                    {"name": "Shure", "country": "USA", "since": 1925, "categories": ["Microphones"]},
                    {"name": "KRK", "country": "USA", "since": 1986, "categories": ["Monitors"]},
                    {"name": "Akai Professional", "country": "USA", "since": 1984, "categories": ["Samplers"]},
                ],
            },
        },
        {
            "slug": "delivery",
            "title": "Delivery & Payment",
            "icon": icon("truck-delivery-outline"),
            "data": {
                "kind": "delivery",
                "title": "Delivery & Payment",
                "description": "How we ship your gear and how you can pay for it.",
                "delivery": [
                    {"title": "Ukraine", "text": "Free delivery in 1–2 days with Nova Poshta, or pickup in the Odesa showroom.", "icon": icon("truck-fast-outline")},
                    {"title": "European Union", "text": "Delivery in 2–5 days. Free from $299 to $499 depending on the country.", "icon": icon("earth")},
                    {"title": "Pickup points", "text": "Paris, Vienna and Warsaw. We will text you when the order is ready.", "icon": icon("storefront-outline")},
                ],
                "payment": [
                    {"title": "Card online", "text": "Visa, Mastercard, Apple Pay and Google Pay.", "icon": icon("credit-card-outline")},
                    {"title": "Cash on delivery", "text": "Pay when you receive the parcel (Ukraine only).", "icon": icon("cash")},
                    {"title": "Installments", "text": "Split the price into up to 10 payments with partner banks.", "icon": icon("calendar-month-outline")},
                ],
                "warranty": [
                    "2-year manufacturer warranty on new gear.",
                    "12-month store warranty on renewed gear.",
                    "14 days to return a product that did not fit your setup.",
                ],
            },
        },
    ],
    "contacts": OFFICES,
}


def subsection_slugs(section):
    return [item["slug"] for item in SUBSECTIONS.get(section, [])]


def find_subsection(section, slug):
    return next((item for item in SUBSECTIONS.get(section, []) if item["slug"] == slug), None)


def find_article(tag, slug):
    return next((item for item in NEWS_ITEMS if item["tag_slug"] == tag and item["slug"] == slug), None)


NOT_FOUND = {
    "title": "This track is not in our crate",
    "subtitle": "The page you are looking for does not exist or was moved. Try one of these instead:",
    "links": [
        {"title": "Home", "url": "/", "icon": icon("home-outline")},
        {"title": "Catalog", "url": "/catalog/", "icon": icon("view-grid-outline")},
        {"title": "News", "url": "/news/", "icon": icon("newspaper-variant-outline")},
        {"title": "Contacts", "url": "/contacts/", "icon": icon("map-marker-outline")},
    ],
    "products": bestsellers(4),
}

PAGES = {
    "home": {"title": "Home", "data": HOME},
    "news": {"title": "News", "data": NEWS},
    "management": {"title": "Team", "data": MANAGEMENT},
    "about": {"title": "About", "data": ABOUT},
    "contacts": {"title": "Contacts", "data": CONTACTS},
    "not_found": {"title": "Page not found", "data": NOT_FOUND},
}
