from company_site.assets import icon, image

from .credits import credit


def photo(slug, alt):
    return {"url": image("products", slug), "alt": alt, "credit": credit(slug)}


CATEGORIES = [
    {
        "slug": "controllers",
        "title": "DJ Controllers",
        "short_title": "Controllers",
        "description": "All-in-one decks for bedrooms, mobile gigs and club stages. Plug in a laptop and play.",
        "icon": icon("tune-vertical"),
        "image": image("products", "traktor-kontrol-s4-mk3"),
    },
    {
        "slug": "players",
        "title": "Media Players & Turntables",
        "short_title": "Players & Turntables",
        "description": "CDJs, standalone systems and direct-drive turntables for vinyl purists.",
        "icon": icon("record-player"),
        "image": image("products", "reloop-rp-1000-mk3"),
    },
    {
        "slug": "mixers",
        "title": "DJ Mixers",
        "short_title": "Mixers",
        "description": "Club-standard mixers with sound-colour FX, filters and solid faders.",
        "icon": icon("knob"),
        "image": image("products", "pioneer-djm-350"),
    },
    {
        "slug": "headphones",
        "title": "DJ Headphones",
        "short_title": "Headphones",
        "description": "Closed-back headphones that isolate the booth and survive every night out.",
        "icon": icon("headphones"),
        "image": image("products", "audio-technica-ath-m50"),
    },
    {
        "slug": "studio",
        "title": "Studio & Production",
        "short_title": "Studio",
        "description": "Monitors and samplers to produce your own edits and hear every kick.",
        "icon": icon("speaker"),
        "image": image("products", "krk-rokit-5"),
    },
    {
        "slug": "mics-accessories",
        "title": "Microphones & Accessories",
        "short_title": "Mics & Accessories",
        "description": "Vocal mics for MCs, slipmats and the small things every DJ needs.",
        "icon": icon("microphone"),
        "image": image("products", "shure-beta-58a"),
    },
]


def product(pid, slug, name, brand, category, price, old_price, rating, reviews, stock, badge, photos, summary, description, features, specs):
    return {
        "id": pid,
        "slug": slug,
        "sku": f"NP-{category[:3].upper()}-{pid:03d}",
        "name": name,
        "brand": brand,
        "category": category,
        "price": price,
        "old_price": old_price,
        "discount": round((1 - price / old_price) * 100) if old_price else 0,
        "rating": rating,
        "reviews": reviews,
        "stock": stock,
        "in_stock": stock > 0,
        "badge": badge,
        "image": photos[0]["url"],
        "images": photos,
        "summary": summary,
        "description": description,
        "features": features,
        "specs": [{"label": label, "value": value} for label, value in specs],
        "url": f"/catalog/{category}/{slug}/",
    }


PRODUCTS = [
    product(
        1, "traktor-kontrol-s4-mk3", "Native Instruments Traktor Kontrol S4 MK3", "Native Instruments", "controllers",
        899.00, 999.00, 4.8, 214, 7, "HIT",
        [photo("traktor-kontrol-s4-mk3", "Traktor Kontrol S4 MK3 top view")],
        "Four-deck controller with motorized Haptic Drive jog wheels.",
        "The S4 MK3 brings force-feedback jog wheels, full-colour displays in each deck and a built-in 24-bit audio interface. It is the flagship of the Traktor ecosystem and a favourite of open-format DJs.",
        ["Haptic Drive jog wheels with force feedback", "Two high-resolution colour displays", "Built-in 24-bit / 48 kHz audio interface", "Traktor Pro 3 included"],
        [("Decks", "4"), ("Software", "Traktor Pro"), ("Audio interface", "24-bit / 48 kHz"), ("Outputs", "XLR master, RCA booth"), ("Weight", "5.1 kg")],
    ),
    product(
        2, "pioneer-ddj-flx4", "Pioneer DJ DDJ-FLX4", "Pioneer DJ", "controllers",
        299.00, None, 4.9, 1873, 34, "BESTSELLER",
        [photo("pioneer-ddj-flx4", "Pioneer DJ DDJ-FLX4 controller")],
        "The best first controller: rekordbox and Serato ready.",
        "Compact two-channel controller with Smart Fader and Smart CFX that help beginners create smooth transitions. Works with rekordbox, Serato DJ Lite and djay, including on smartphones.",
        ["Smart Fader and Smart CFX", "Works with rekordbox and Serato DJ Lite", "USB bus powered", "Mic input for MCs"],
        [("Decks", "2"), ("Software", "rekordbox, Serato DJ Lite"), ("Power", "USB bus power"), ("Outputs", "RCA master, headphones"), ("Weight", "2.1 kg")],
    ),
    product(
        3, "pioneer-ddj-rev1", "Pioneer DJ DDJ-REV1", "Pioneer DJ", "controllers",
        329.00, 369.00, 4.7, 642, 12, "SALE",
        [photo("pioneer-ddj-rev1", "Pioneer DJ DDJ-REV1 controller")],
        "Battle-style layout for scratch DJs on Serato.",
        "The REV1 copies the layout of a turntable-and-mixer setup: horizontal decks and a battle mixer in the middle. Large jog wheels and a magnetic crossfader make it a perfect tool to learn scratching.",
        ["Battle-style layout", "Magvel-style crossfader", "Serato DJ Lite included", "Tracking LEDs on jog wheels"],
        [("Decks", "2"), ("Software", "Serato DJ Lite / Pro"), ("Crossfader", "Magnetic"), ("Outputs", "RCA master, headphones"), ("Weight", "2.8 kg")],
    ),
    product(
        4, "numark-mixtrack-pro-fx", "Numark Mixtrack Pro FX", "Numark", "controllers",
        249.00, 279.00, 4.5, 931, 21, None,
        [photo("numark-mixtrack-pro", "Numark Mixtrack Pro jog wheel close-up")],
        "Serato controller with paddle FX and 6-inch jog wheels.",
        "Mixtrack Pro FX gives you dual FX paddles, large touch-sensitive jog wheels and a built-in audio interface at an entry-level price.",
        ["Dual FX paddles", "6\" capacitive jog wheels", "Built-in audio interface", "16 performance pads"],
        [("Decks", "2"), ("Software", "Serato DJ Lite"), ("Pads", "16"), ("Outputs", "RCA master, headphones"), ("Weight", "2.3 kg")],
    ),
    product(
        5, "pioneer-ddj-rx-renewed", "Pioneer DJ DDJ-RX (renewed)", "Pioneer DJ", "controllers",
        549.00, 749.00, 4.6, 88, 3, "RENEWED",
        [photo("pioneer-ddj-rx", "Pioneer DJ DDJ-RX controller in use")],
        "Club-layout rekordbox controller, checked by our techs.",
        "Professionally refurbished DDJ-RX with full-size jog wheels and a layout copied from the CDJ and DJM club setup. Tested in our demo booth and covered by a 12-month store warranty.",
        ["Club-style layout", "Full-size jog wheels", "Tested and cleaned by technicians", "12-month store warranty"],
        [("Decks", "4"), ("Software", "rekordbox dj"), ("Condition", "Renewed"), ("Outputs", "XLR, RCA, booth"), ("Weight", "5.8 kg")],
    ),
    product(
        6, "traktor-kontrol-s4-mk2-renewed", "Native Instruments Traktor Kontrol S4 MK2 (renewed)", "Native Instruments", "controllers",
        449.00, None, 4.5, 57, 2, "RENEWED",
        [photo("traktor-kontrol-s4-mk2", "Traktor Kontrol S4 MK2 controller")],
        "Legendary four-deck Traktor controller at a great price.",
        "A renewed S4 MK2 with Remix Deck support and a built-in audio interface. A proven workhorse for DJs moving to four-deck mixing.",
        ["Four-channel mixer section", "Remix Deck support", "Tested by technicians", "12-month store warranty"],
        [("Decks", "4"), ("Software", "Traktor Pro"), ("Condition", "Renewed"), ("Outputs", "XLR, RCA"), ("Weight", "4.6 kg")],
    ),
    product(
        7, "pioneer-cdj-2000-renewed", "Pioneer DJ CDJ-2000 (renewed)", "Pioneer DJ", "players",
        899.00, 1199.00, 4.7, 143, 4, "RENEWED",
        [photo("pioneer-cdj-2000", "Pioneer DJ CDJ-2000 media player")],
        "The player that defined club booths for a decade.",
        "Professionally refurbished CDJ-2000 that plays CD, USB and SD media and connects to rekordbox. Perfect for practising on the same gear you will meet in the club.",
        ["Plays CD, USB and SD", "rekordbox compatible", "New jog wheel sensor", "12-month store warranty"],
        [("Media", "CD, USB, SD"), ("Formats", "MP3, AAC, WAV, AIFF"), ("Condition", "Renewed"), ("Outputs", "RCA, digital coaxial"), ("Weight", "4.6 kg")],
    ),
    product(
        8, "pioneer-xdj-aero", "Pioneer DJ XDJ-AERO", "Pioneer DJ", "players",
        699.00, None, 4.4, 76, 5, None,
        [photo("pioneer-xdj-aero", "Pioneer DJ XDJ-AERO standalone system")],
        "Standalone wireless DJ system with built-in mixer.",
        "XDJ-AERO plays music from USB drives or wirelessly from a smartphone or laptop. Two decks and a two-channel mixer in one body make it ideal for mobile DJs.",
        ["Wireless streaming from phone or laptop", "Two decks and mixer in one unit", "USB playback", "Built-in Beat FX"],
        [("Decks", "2"), ("Media", "USB, Wi-Fi"), ("FX", "Beat FX"), ("Outputs", "RCA, booth"), ("Weight", "5.2 kg")],
    ),
    product(
        9, "technics-sl-1200-mk5-renewed", "Technics SL-1200MK5 (renewed)", "Technics", "players",
        899.00, None, 4.9, 312, 3, "RENEWED",
        [photo("technics-sl-1200-mk5", "Technics SL-1200MK5 turntable")],
        "Iconic direct-drive turntable, restored by our vinyl techs.",
        "The SL-1200 is the most famous DJ turntable ever made. Our renewed units get a full service: new belts where needed, calibrated pitch, cleaned tonearm and a new dust cover.",
        ["Direct-drive motor", "±8% pitch control", "Fully serviced", "12-month store warranty"],
        [("Drive", "Direct drive"), ("Speeds", "33⅓ / 45 rpm"), ("Pitch", "±8%"), ("Condition", "Renewed"), ("Weight", "12.5 kg")],
    ),
    product(
        10, "technics-sl-1210-mk2-renewed", "Technics SL-1210MK2 (renewed)", "Technics", "players",
        749.00, 849.00, 4.9, 207, 2, "RENEWED",
        [photo("technics-sl-1210-mk2", "Technics SL-1210MK2 turntable with Technics slipmat")],
        "Black club classic, serviced and ready to scratch.",
        "The black version of the legendary Technics deck that lived in every club booth for 30 years. Serviced, calibrated and tested with Ortofon cartridges.",
        ["Direct-drive motor", "Quartz-locked pitch", "Fully serviced", "12-month store warranty"],
        [("Drive", "Direct drive"), ("Speeds", "33⅓ / 45 rpm"), ("Pitch", "±8%"), ("Condition", "Renewed"), ("Weight", "12.5 kg")],
    ),
    product(
        11, "reloop-rp-1000-mk3", "Reloop RP-1000 MK3", "Reloop", "players",
        229.00, 259.00, 4.3, 164, 18, "SALE",
        [photo("reloop-rp-1000-mk3", "Reloop RP-1000 MK3 turntable")],
        "Affordable belt-drive turntable to start your vinyl journey.",
        "RP-1000 MK3 is a reliable starter turntable with an S-shaped tonearm, pitch control and a pre-mounted cartridge. Unbox, connect to a mixer and play.",
        ["S-shaped tonearm", "Pre-mounted cartridge", "Pitch control ±10%", "Dust cover included"],
        [("Drive", "Belt drive"), ("Speeds", "33⅓ / 45 rpm"), ("Pitch", "±10%"), ("Outputs", "RCA phono"), ("Weight", "5.4 kg")],
    ),
    product(
        12, "pioneer-djm-350", "Pioneer DJ DJM-350 White", "Pioneer DJ", "mixers",
        449.00, None, 4.6, 98, 6, "LIMITED",
        [photo("pioneer-djm-350", "Pioneer DJ DJM-350 white mixer")],
        "Two-channel club mixer with USB recording, in limited white.",
        "DJM-350 brings the sound and feel of the DJM club series to a compact two-channel format. Record your sets straight to a USB drive.",
        ["Sound Colour FX: Filter, Crush, Jet, Gate", "USB recording", "3-band EQ per channel", "Limited white finish"],
        [("Channels", "2"), ("FX", "Sound Colour FX"), ("Recording", "USB"), ("Outputs", "RCA master, booth"), ("Weight", "3.1 kg")],
    ),
    product(
        13, "pioneer-djm-600-renewed", "Pioneer DJ DJM-600 (renewed)", "Pioneer DJ", "mixers",
        399.00, None, 4.5, 71, 2, "RENEWED",
        [photo("pioneer-djm-600", "Pioneer DJ DJM-600 mixer in a booth")],
        "Four-channel legend that shaped club sound in the 2000s.",
        "A renewed DJM-600 with a classic Beat FX section and bulletproof build quality. New faders installed, every channel tested.",
        ["Four channels", "Beat FX with BPM counter", "New faders installed", "12-month store warranty"],
        [("Channels", "4"), ("FX", "Beat FX"), ("Condition", "Renewed"), ("Outputs", "XLR, RCA, booth"), ("Weight", "5.5 kg")],
    ),
    product(
        14, "pioneer-djm-900nxs-renewed", "Pioneer DJ DJM-900NXS (renewed)", "Pioneer DJ", "mixers",
        1099.00, 1399.00, 4.8, 118, 3, "RENEWED",
        [photo("pioneer-djm-900-booth", "Pioneer DJ DJM-900NXS mixer in a festival booth")],
        "Festival-grade four-channel mixer with Beat FX and USB audio.",
        "The DJM-900NXS was the club-standard mixer for years. Our renewed units are fully tested and come with new faders and knobs.",
        ["Beat FX and Sound Colour FX", "Built-in USB sound card", "New faders and knobs", "12-month store warranty"],
        [("Channels", "4"), ("FX", "Beat FX, Sound Colour FX"), ("Condition", "Renewed"), ("Outputs", "XLR, RCA, booth, digital"), ("Weight", "6.6 kg")],
    ),
    product(
        15, "pioneer-club-set", "Pioneer DJ Club Set: 2× CDJ-2000NXS + DJM-900NXS", "Pioneer DJ", "mixers",
        3999.00, 4699.00, 5.0, 23, 1, "BUNDLE",
        [photo("pioneer-dj-club-bundle", "Two Pioneer CDJ-2000NXS players with DJM-900NXS mixer")],
        "A complete club booth in one box. Renewed and tested.",
        "Two CDJ-2000NXS players and a DJM-900NXS mixer: exactly what you find in most clubs. The set is renewed, matched and tested together in our demo booth.",
        ["2× CDJ-2000NXS players", "DJM-900NXS mixer", "All cables included", "Tested together in our booth"],
        [("Players", "2× CDJ-2000NXS"), ("Mixer", "DJM-900NXS"), ("Condition", "Renewed"), ("Warranty", "12 months"), ("Weight", "15.8 kg")],
    ),
    product(
        16, "sennheiser-hd-25", "Sennheiser HD 25", "Sennheiser", "headphones",
        149.95, 169.95, 4.9, 2541, 48, "BESTSELLER",
        [photo("sennheiser-hd-25", "Sennheiser HD 25 headphones")],
        "The DJ headphone standard since 1988.",
        "Lightweight, extremely loud and almost indestructible. The split headband and rotating ear cup make one-ear monitoring easy, and every part can be replaced.",
        ["Split headband", "Rotating ear cup", "High isolation", "Every part replaceable"],
        [("Type", "Closed, on-ear"), ("Impedance", "70 Ω"), ("Frequency response", "16 Hz – 22 kHz"), ("Cable", "1.5 m straight"), ("Weight", "140 g")],
    ),
    product(
        17, "audio-technica-ath-m50", "Audio-Technica ATH-M50", "Audio-Technica", "headphones",
        149.00, None, 4.8, 1688, 26, None,
        [photo("audio-technica-ath-m50", "Audio-Technica ATH-M50 headphones")],
        "Studio monitor headphones loved by producers and DJs.",
        "ATH-M50 delivers accurate, punchy sound with deep bass. 90° swivelling ear cups make it comfortable for one-ear monitoring in the booth.",
        ["45 mm drivers", "90° swivelling ear cups", "Coiled cable", "Foldable design"],
        [("Type", "Closed, over-ear"), ("Impedance", "38 Ω"), ("Frequency response", "15 Hz – 28 kHz"), ("Cable", "Coiled, 3 m"), ("Weight", "285 g")],
    ),
    product(
        18, "beyerdynamic-dt-770-pro", "Beyerdynamic DT 770 PRO 80 Ω", "Beyerdynamic", "headphones",
        159.00, 179.00, 4.7, 1204, 15, "SALE",
        [photo("beyerdynamic-dt-770-pro", "Beyerdynamic DT 770 PRO headphones")],
        "Comfortable closed studio headphones made in Germany.",
        "Velour ear pads, a spring-steel headband and powerful bass make the DT 770 PRO ideal for long studio sessions and practice at home.",
        ["Made in Germany", "Velour ear pads", "Spring-steel headband", "Excellent isolation"],
        [("Type", "Closed, over-ear"), ("Impedance", "80 Ω"), ("Frequency response", "5 Hz – 35 kHz"), ("Cable", "3 m straight"), ("Weight", "270 g")],
    ),
    product(
        19, "reloop-rhp-20", "Reloop RHP-20", "Reloop", "headphones",
        99.00, None, 4.4, 211, 0, None,
        [photo("reloop-rhp-20", "Reloop RHP-20 headphones")],
        "Robust DJ headphones with a detachable cable.",
        "Loud, compact and robust. RHP-20 has rotating ear cups, a detachable cable and a carrying bag for gigs.",
        ["Rotating ear cups", "Detachable cable", "Carrying bag included", "Foldable"],
        [("Type", "Closed, on-ear"), ("Impedance", "32 Ω"), ("Frequency response", "10 Hz – 25 kHz"), ("Cable", "Detachable, coiled"), ("Weight", "230 g")],
    ),
    product(
        20, "krk-rokit-5", "KRK Rokit 5", "KRK", "studio",
        199.00, 229.00, 4.6, 987, 22, "SALE",
        [photo("krk-rokit-5", "KRK Rokit 5 studio monitor")],
        "Iconic yellow-cone studio monitor for producers and DJs.",
        "Rokit 5 is a bi-amped active monitor with a 5\" woofer and the famous yellow Kevlar cone. Great for home studios and DJ practice. Price per unit.",
        ["5\" Kevlar woofer", "Bi-amped class D", "Front-firing bass port", "Room EQ controls"],
        [("Woofer", "5\""), ("Power", "55 W"), ("Frequency response", "43 Hz – 40 kHz"), ("Inputs", "XLR, TRS"), ("Weight", "5.5 kg")],
    ),
    product(
        21, "akai-mpc-live", "Akai MPC Live", "Akai Professional", "studio",
        1199.00, None, 4.7, 134, 4, "NEW",
        [photo("akai-mpc-live", "Akai MPC Live standalone sampler")],
        "Standalone battery-powered sampler for beat makers.",
        "MPC Live works without a computer: 16 pads, a 7\" touchscreen and a built-in battery let you make beats anywhere and perform live.",
        ["7\" multi-touch display", "Built-in battery", "16 velocity-sensitive pads", "Standalone, no computer needed"],
        [("Pads", "16"), ("Display", "7\" touch"), ("Storage", "16 GB"), ("Power", "Battery / AC"), ("Weight", "2.7 kg")],
    ),
    product(
        22, "akai-mpc-studio", "Akai MPC Studio", "Akai Professional", "studio",
        279.00, None, 4.4, 301, 9, None,
        [photo("akai-mpc-studio", "Akai MPC Studio controller")],
        "Slim MPC controller for your laptop studio.",
        "MPC Studio brings the legendary MPC workflow to your computer in a slim aluminium body. Includes MPC software.",
        ["16 velocity-sensitive pads", "Slim aluminium body", "MPC software included", "USB powered"],
        [("Pads", "16"), ("Software", "MPC 2"), ("Power", "USB"), ("Connection", "USB"), ("Weight", "1.3 kg")],
    ),
    product(
        23, "shure-sm58", "Shure SM58", "Shure", "mics-accessories",
        99.00, None, 4.9, 3122, 57, "BESTSELLER",
        [photo("shure-sm58", "Shure SM58 microphone"), photo("shure-sm58-closeup", "Shure SM58 microphone grille close-up")],
        "The most popular vocal microphone in the world.",
        "SM58 is the industry standard dynamic microphone for vocals. Built to survive drops, spilled drinks and years of shows.",
        ["Cardioid pickup pattern", "Built-in pop filter", "Shock-mounted capsule", "Legendary durability"],
        [("Type", "Dynamic"), ("Pattern", "Cardioid"), ("Frequency response", "50 Hz – 15 kHz"), ("Connector", "XLR"), ("Weight", "298 g")],
    ),
    product(
        24, "shure-beta-58a", "Shure Beta 58A", "Shure", "mics-accessories",
        169.00, 189.00, 4.8, 845, 14, "SALE",
        [photo("shure-beta-58a", "Shure Beta 58A microphone")],
        "Brighter, louder upgrade of the SM58 for MCs.",
        "Supercardioid pattern and higher output help your voice cut through a loud club. Hardened steel grille and the same bulletproof Shure build.",
        ["Supercardioid pattern", "Higher output than SM58", "Hardened steel grille", "Minimal handling noise"],
        [("Type", "Dynamic"), ("Pattern", "Supercardioid"), ("Frequency response", "50 Hz – 16 kHz"), ("Connector", "XLR"), ("Weight", "278 g")],
    ),
    product(
        25, "reloop-slipmat-spin-me-round", "Reloop Slipmats \"Spin me round!\" (pair)", "Reloop", "mics-accessories",
        19.90, None, 4.6, 402, 120, None,
        [photo("reloop-slipmat", "Reloop Spin me round slipmat")],
        "Felt slipmats for smooth scratching and back-cueing.",
        "A pair of thick felt slipmats with a fun print. They reduce friction so your records glide when you scratch or cue.",
        ["Pair of slipmats", "Thick felt", "Anti-static", "Fits all 12\" turntables"],
        [("Quantity", "2"), ("Material", "Felt"), ("Diameter", "12\""), ("Thickness", "3 mm"), ("Weight", "120 g")],
    ),
]

BRANDS = sorted({item["brand"] for item in PRODUCTS})


def find_category(slug):
    return next((item for item in CATEGORIES if item["slug"] == slug), None)


def find_product(category, slug):
    return next((item for item in PRODUCTS if item["category"] == category and item["slug"] == slug), None)


def products_in(category):
    return [item for item in PRODUCTS if item["category"] == category]


def products_by_ids(ids):
    return [item for pid in ids for item in PRODUCTS if item["id"] == pid]


def card(item):
    keys = ("id", "slug", "name", "brand", "category", "price", "old_price", "discount", "rating", "reviews", "in_stock", "badge", "image", "summary", "url")
    return {key: item[key] for key in keys}


def cards(items):
    return [card(item) for item in items]


def category_with_count(category):
    return {**category, "count": len(products_in(category["slug"])), "url": f"/catalog/{category['slug']}/"}


def catalog_menu():
    return [category_with_count(item) for item in CATEGORIES]


def search_index():
    return [{"name": item["name"], "brand": item["brand"], "url": item["url"], "image": item["image"], "price": item["price"]} for item in PRODUCTS]


def related(item, limit=4):
    same = [other for other in products_in(item["category"]) if other["id"] != item["id"]]
    return cards(same[:limit])


def deals(limit=8):
    return cards(sorted((item for item in PRODUCTS if item["old_price"]), key=lambda item: -item["discount"])[:limit])


def bestsellers(limit=8):
    return cards(sorted(PRODUCTS, key=lambda item: -item["reviews"])[:limit])
