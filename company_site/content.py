ICON_BASE = "https://api.iconify.design/mdi"


def icon(name, color="00f0ff"):
    return f"{ICON_BASE}/{name}.svg?color=%23{color}"


SITE = {
    "name": "NEON PULSE",
    "tagline": "Gear for DJs who play after midnight",
    "currency": "USD",
    "theme": {
        "style": "cyberpunk",
        "colors": {
            "background": "#0a0a12",
            "surface": "#141425",
            "primary": "#00f0ff",
            "secondary": "#ff2bd6",
            "accent": "#f5ff00",
            "text": "#e6e6ff",
            "muted": "#7a7aa8",
        },
        "fonts": {
            "heading": "Orbitron",
            "body": "Rajdhani",
        },
    },
    "logo": icon("disc-player", "ff2bd6"),
    "navigation": [
        {"key": "home", "title": "Home", "url": "/", "icon": icon("home")},
        {"key": "news", "title": "News", "url": "/news/", "icon": icon("newspaper-variant-outline")},
        {"key": "management", "title": "Management", "url": "/management/", "icon": icon("account-tie")},
        {"key": "about", "title": "About", "url": "/about/", "icon": icon("information-outline")},
        {"key": "contacts", "title": "Contacts", "url": "/contacts/", "icon": icon("map-marker")},
    ],
    "socials": [
        {"name": "Instagram", "url": "https://instagram.com/neonpulse.dj", "icon": icon("instagram", "ff2bd6")},
        {"name": "YouTube", "url": "https://youtube.com/@neonpulsedj", "icon": icon("youtube", "ff2bd6")},
        {"name": "SoundCloud", "url": "https://soundcloud.com/neonpulsedj", "icon": icon("soundcloud", "ff2bd6")},
        {"name": "Telegram", "url": "https://t.me/neonpulsedj", "icon": icon("telegram", "ff2bd6")},
    ],
    "footer": "© 2026 NEON PULSE DJ Supply. All prices in USD.",
}

CATEGORIES = [
    {"slug": "controllers", "title": "DJ Controllers", "description": "All-in-one decks for clubs, bedrooms and festival stages.", "icon": icon("tune-vertical")},
    {"slug": "players", "title": "Media Players & Turntables", "description": "CDJs, vinyl turntables and standalone media players.", "icon": icon("record-player")},
    {"slug": "mixers", "title": "DJ Mixers", "description": "Club-standard mixers with pro FX and filters.", "icon": icon("knob")},
    {"slug": "headphones", "title": "DJ Headphones", "description": "Closed-back cans built for loud booths.", "icon": icon("headphones")},
    {"slug": "microphones", "title": "Microphones", "description": "Vocal mics for MCs and hype announcements.", "icon": icon("microphone")},
    {"slug": "monitors", "title": "Booth Monitors", "description": "Studio and booth monitors to hear every kick.", "icon": icon("speaker")},
    {"slug": "accessories", "title": "Accessories", "description": "Cables, cases, needles and slipmats.", "icon": icon("cable-data")},
]

FEATURED_PRODUCTS = [
    {"id": 1, "sku": "NP-CTL-001", "name": "Pioneer DJ DDJ-FLX10", "category": "controllers", "price": 1599.00, "old_price": 1799.00, "rating": 4.9, "in_stock": True, "badge": "HOT", "icon": icon("tune-vertical", "ff2bd6")},
    {"id": 2, "sku": "NP-CTL-002", "name": "Rane Four", "category": "controllers", "price": 2199.00, "old_price": None, "rating": 4.8, "in_stock": True, "badge": "NEW", "icon": icon("tune-vertical", "ff2bd6")},
    {"id": 3, "sku": "NP-PLR-001", "name": "Pioneer DJ CDJ-3000", "category": "players", "price": 2599.00, "old_price": None, "rating": 5.0, "in_stock": True, "badge": "CLUB STANDARD", "icon": icon("disc-player", "ff2bd6")},
    {"id": 4, "sku": "NP-PLR-002", "name": "Technics SL-1200MK7", "category": "players", "price": 1099.00, "old_price": 1199.00, "rating": 4.9, "in_stock": True, "badge": None, "icon": icon("record-player", "ff2bd6")},
    {"id": 5, "sku": "NP-MIX-001", "name": "Allen & Heath Xone:96", "category": "mixers", "price": 1999.00, "old_price": None, "rating": 4.8, "in_stock": False, "badge": None, "icon": icon("knob", "ff2bd6")},
    {"id": 6, "sku": "NP-HPH-001", "name": "Sennheiser HD 25", "category": "headphones", "price": 149.95, "old_price": 169.95, "rating": 4.9, "in_stock": True, "badge": "BESTSELLER", "icon": icon("headphones", "ff2bd6")},
    {"id": 7, "sku": "NP-HPH-002", "name": "Pioneer DJ HDJ-X10", "category": "headphones", "price": 349.00, "old_price": None, "rating": 4.7, "in_stock": True, "badge": None, "icon": icon("headphones", "ff2bd6")},
    {"id": 8, "sku": "NP-MIC-001", "name": "Shure SM58", "category": "microphones", "price": 99.00, "old_price": None, "rating": 4.9, "in_stock": True, "badge": None, "icon": icon("microphone", "ff2bd6")},
    {"id": 9, "sku": "NP-MON-001", "name": "KRK Rokit 5 G4 (pair)", "category": "monitors", "price": 398.00, "old_price": 438.00, "rating": 4.6, "in_stock": True, "badge": "SALE", "icon": icon("speaker", "ff2bd6")},
    {"id": 10, "sku": "NP-ACC-001", "name": "Ortofon Concorde MKII Club (twin)", "category": "accessories", "price": 229.00, "old_price": None, "rating": 4.7, "in_stock": True, "badge": None, "icon": icon("album", "ff2bd6")},
]

ADVANTAGES = [
    {"title": "Fast Shipping", "text": "Same-day dispatch for orders placed before 4 PM.", "icon": icon("truck-fast", "f5ff00")},
    {"title": "Official Warranty", "text": "Every unit is covered by a 2-year manufacturer warranty.", "icon": icon("shield-check", "f5ff00")},
    {"title": "DJ Support", "text": "Working DJs answer your questions, not call-center bots.", "icon": icon("headset", "f5ff00")},
    {"title": "Booth Tested", "text": "Each item is tested in our own demo booth before it ships.", "icon": icon("lightning-bolt", "f5ff00")},
]

HOME = {
    "hero": {
        "title": "PLUG IN. DROP THE BASS. OWN THE NIGHT.",
        "subtitle": "Controllers, CDJs, mixers, headphones and microphones for DJs only.",
        "cta": {"title": "Latest drops", "url": "/news/"},
        "icon": icon("sine-wave", "ff2bd6"),
    },
    "categories": CATEGORIES,
    "featured_products": FEATURED_PRODUCTS,
    "advantages": ADVANTAGES,
}

NEWS = {
    "title": "Transmission Log",
    "subtitle": "Gear releases, firmware updates and events from the NEON PULSE crew.",
    "icon": icon("newspaper-variant-outline"),
    "items": [
        {"id": 1, "slug": "rane-four-in-stock", "date": "2026-11-20", "tag": "Arrivals", "title": "Rane Four is back in stock", "excerpt": "The four-channel Stems-ready controller has landed in our warehouse. Limited batch at $2,199.", "icon": icon("tune-vertical", "ff2bd6")},
        {"id": 2, "slug": "black-friday-neon-week", "date": "2026-11-17", "tag": "Sale", "title": "Neon Week: up to 25% off headphones", "excerpt": "Sennheiser, Pioneer DJ, AIAIAI and V-Moda headphones at cyber prices until November 30.", "icon": icon("headphones", "ff2bd6")},
        {"id": 3, "slug": "cdj-3000-firmware", "date": "2026-11-09", "tag": "Firmware", "title": "New CDJ-3000 firmware explained", "excerpt": "Our tech crew breaks down every change in the latest CDJ-3000 update and how to install it.", "icon": icon("disc-player", "ff2bd6")},
        {"id": 4, "slug": "odesa-showroom-night", "date": "2026-10-28", "tag": "Events", "title": "Showroom Night in Odesa", "excerpt": "Free entry, live b2b sets and hands-on time with flagship mixers and controllers.", "icon": icon("equalizer", "ff2bd6")},
        {"id": 5, "slug": "mic-guide-for-mcs", "date": "2026-10-15", "tag": "Guides", "title": "Choosing a vocal mic for your DJ set", "excerpt": "SM58, Beta 58A or wireless? A practical guide for DJs who also hold the mic.", "icon": icon("microphone", "ff2bd6")},
    ],
}

MANAGEMENT = {
    "title": "Core Crew",
    "subtitle": "The people who keep the beat running at NEON PULSE.",
    "icon": icon("account-tie"),
    "members": [
        {"id": 1, "name": "Maksym Koval", "alias": "DJ VOLTAGE", "position": "Founder & CEO", "bio": "Club resident for 12 years before building the store he always wanted to shop in.", "icon": icon("account-music", "ff2bd6")},
        {"id": 2, "name": "Olena Shevchuk", "alias": "NEONA", "position": "Chief Operating Officer", "bio": "Runs logistics and makes sure every CDJ reaches its booth on time.", "icon": icon("account-tie", "ff2bd6")},
        {"id": 3, "name": "Artem Bondar", "alias": "SUBFRAME", "position": "Head of Product", "bio": "Tests every controller, mixer and headphone before it hits the catalog.", "icon": icon("cog-outline", "ff2bd6")},
        {"id": 4, "name": "Iryna Melnyk", "alias": "GLITCHA", "position": "Head of Customer Support", "bio": "Leads a team of working DJs who answer customer questions day and night.", "icon": icon("headset", "ff2bd6")},
    ],
}

ABOUT = {
    "title": "About NEON PULSE",
    "subtitle": "A DJ-only store born in the booth.",
    "icon": icon("information-outline"),
    "description": "NEON PULSE sells equipment for DJs and nothing else: controllers, media players, turntables, mixers, headphones, microphones, booth monitors and accessories. Every product is chosen and tested by working DJs.",
    "stats": [
        {"label": "Years on the decks", "value": "8"},
        {"label": "DJs equipped", "value": "25,000+"},
        {"label": "Products in catalog", "value": "1,200+"},
        {"label": "Brands", "value": "40+"},
    ],
    "timeline": [
        {"year": 2018, "title": "First drop", "text": "Started as a small Telegram shop selling used CDJs."},
        {"year": 2020, "title": "Online store", "text": "Launched the online catalog and nationwide delivery."},
        {"year": 2022, "title": "Demo booth", "text": "Opened a demo booth where every product can be tested."},
        {"year": 2024, "title": "Official dealer", "text": "Became an official dealer for leading DJ brands."},
        {"year": 2026, "title": "Showroom", "text": "Opened the flagship showroom in Odesa."},
    ],
    "values": [
        {"title": "DJs only", "text": "No guitars, no pianos. Only gear for DJs.", "icon": icon("disc-player", "f5ff00")},
        {"title": "Honest advice", "text": "We recommend what fits your set, not what costs more.", "icon": icon("headset", "f5ff00")},
        {"title": "Tested gear", "text": "Each unit is checked in the booth before shipping.", "icon": icon("shield-check", "f5ff00")},
    ],
}

CONTACTS = {
    "title": "Connect to the Grid",
    "subtitle": "Visit the showroom or reach the crew online.",
    "icon": icon("map-marker"),
    "channels": [
        {"type": "address", "label": "Showroom", "value": "12 Derybasivska St, Odesa, Ukraine", "icon": icon("map-marker", "ff2bd6")},
        {"type": "phone", "label": "Phone", "value": "+380 48 700 12 34", "href": "tel:+380487001234", "icon": icon("phone", "ff2bd6")},
        {"type": "email", "label": "Email", "value": "hello@neonpulse.dj", "href": "mailto:hello@neonpulse.dj", "icon": icon("email-outline", "ff2bd6")},
        {"type": "telegram", "label": "Telegram", "value": "@neonpulsedj", "href": "https://t.me/neonpulsedj", "icon": icon("telegram", "ff2bd6")},
    ],
    "hours": [
        {"days": "Mon - Fri", "time": "11:00 - 21:00"},
        {"days": "Sat", "time": "12:00 - 22:00"},
        {"days": "Sun", "time": "12:00 - 18:00"},
    ],
    "hours_icon": icon("clock-outline", "f5ff00"),
    "map": {
        "lat": 46.4843,
        "lng": 30.7387,
        "zoom": 16,
        "url": "https://www.openstreetmap.org/?mlat=46.4843&mlon=30.7387#map=16/46.4843/30.7387",
    },
}

PAGES = {
    "home": {"title": "Home", "data": HOME},
    "news": {"title": "News", "data": NEWS},
    "management": {"title": "Management", "data": MANAGEMENT},
    "about": {"title": "About", "data": ABOUT},
    "contacts": {"title": "Contacts", "data": CONTACTS},
}
