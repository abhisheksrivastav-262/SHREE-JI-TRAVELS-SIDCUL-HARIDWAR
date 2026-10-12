#!/usr/bin/env python3
"""Build all static pages for Shree Ji Travels."""
import os
BASE = "/Users/abhisheksrivastav/Documents/Shree Ji Travels"
PHONE = "+91 8077274970"
WA = "918077274970"
TEL = "tel:+918077274970"

U = lambda pid, w=1600: f"https://images.unsplash.com/{pid}?q=80&w={w}&auto=format&fit=crop"
IMG = {
 "hero_home": U("photo-1506905925346-21bda4d32df4"),
 "himalaya": U("photo-1544735716-392fe2489ffa"),
 "mountain_road": U("photo-1464822759023-fed622ff2c3b"),
 "road_trip": U("photo-1469854523086-cc02fe5d8800"),
 "drive": U("photo-1449965408869-eaa3f722e40d"),
 "sedan": U("photo-1549317661-bd32c8ce0db2"),
 "sedan2": U("photo-1502877338535-766e1452684a"),
 "van": U("photo-1570125909232-eb263c188f7e"),
 "ghat": U("photo-1567157577867-05ccb1388e66"),
 "river": U("photo-1437482078695-73f5ca6c96e2"),
 "delhi": U("photo-1587474260584-136574528ed5"),
 "taj": U("photo-1548013146-72479768bada"),
 "kedar": U("photo-1626716493137-b67fe9501e76"),
 "badrinath": U("photo-1601823984263-b87b59798b70"),
 "ganga_aarti": U("photo-1561361513-2d000a50f0dc"),
}

def header(active=""):
    def a(href, label):
        cls = "active" if active == href else ""
        return f'<a href="{href}" class="{cls}">{label}</a>'
    return f"""<header class="site-header"><div class="container header-inner">
<a class="brand" href="index.html" aria-label="Shree Ji Travels — home"><img src="assets/img/logo.svg" alt="Shree Ji Travels logo" width="52" height="52"><span class="brand-text"><strong>SHREE JI TRAVELS</strong><span>SIDCUL • HARIDWAR</span></span></a>
<nav class="nav-desktop" aria-label="Primary">
{a("index.html","Home")}{a("about.html","About")}
<span class="has-dropdown"><button class="drop-btn" aria-haspopup="true" aria-expanded="false">Services ▾</button>
<span class="dropdown">
<a href="one-way-cab.html">🚕 One Way Cabs<small>Haridwar drop trips — fare on request</small></a>
<a href="round-trip-cab.html">🔁 Round Trip Cabs<small>Return journeys, planned together</small></a>
<a href="local-cab.html">🛕 Local Cabs<small>Haridwar sightseeing &amp; transfers</small></a>
<a href="outstation-cab.html">⛰️ Outstation Cabs<small>Long-distance holiday &amp; family trips</small></a>
</span></span>
{a("char-dham-yatra.html","Char Dham Yatra")}{a("gallery.html","Gallery")}{a("contact.html","Contact")}
</nav>
<div class="header-cta">
<a class="btn btn-outline btn-sm" href="{TEL}">📞 Call</a>
<button class="hamburger" data-open-menu aria-label="Open navigation menu"><span></span><span></span><span></span></button>
</div></div></header>
<div class="mobile-panel" id="mobilePanel">
<div class="mp-head"><strong style="color:var(--navy)">SHREE JI TRAVELS</strong><button class="mp-close" data-close-menu aria-label="Close menu">✕ Close</button></div>
<a class="mp-link" href="index.html">🏠 Home</a>
<a class="mp-link" href="about.html">ℹ️ About Us</a>
<div class="mp-services">Services</div>
<a class="mp-link" href="one-way-cab.html">🚕 One Way Cabs</a>
<a class="mp-link" href="round-trip-cab.html">🔁 Round Trip Cabs</a>
<a class="mp-link" href="local-cab.html">🛕 Local Cabs</a>
<a class="mp-link" href="outstation-cab.html">⛰️ Outstation Cabs</a>
<a class="mp-link" href="char-dham-yatra.html">🛕 Char Dham Yatra</a>
<a class="mp-link" href="gallery.html">🖼️ Gallery</a>
<a class="mp-link" href="faq.html">❓ FAQ</a>
<a class="mp-link" href="contact.html">📞 Contact &amp; Booking</a>
<div style="display:flex;gap:10px;margin-top:14px">
<a class="btn btn-wa btn-sm btn-block" href="https://wa.me/{WA}?text=Namaste%20Shree%20Ji%20Travels!%20I%20would%20like%20to%20enquire%20about%20a%20cab%20booking." target="_blank" rel="noopener">💬 Book on WhatsApp</a>
<a class="btn btn-primary btn-sm btn-block" href="{TEL}">📞 Call Now</a>
</div></div>"""

FOOTER = f"""<footer><div class="container footer-grid">
<div class="footer-brand"><img src="assets/img/logo.svg" alt="Shree Ji Travels logo" width="58" height="58">
<h3>SHREE JI TRAVELS</h3>
<p>SIDCUL, Haridwar–based cab and pilgrimage travel service. One-way, round-trip, local, outstation and Char Dham Yatra enquiries with clear communication and comfortable journeys.</p>
<p><a href="{TEL}">📞 {PHONE}</a><br><a href="https://wa.me/{WA}" target="_blank" rel="noopener">💬 WhatsApp: {PHONE}</a><br>📍 SIDCUL, Haridwar, Uttarakhand, India</p></div>
<div><h4>Services</h4><ul class="f-links">
<li><a href="one-way-cab.html">One Way Cabs</a></li><li><a href="round-trip-cab.html">Round Trip Cabs</a></li>
<li><a href="local-cab.html">Local Cabs</a></li><li><a href="outstation-cab.html">Outstation Cabs</a></li>
<li><a href="char-dham-yatra.html">Char Dham Yatra</a></li></ul></div>
<div><h4>Company</h4><ul class="f-links">
<li><a href="about.html">About Us</a></li><li><a href="gallery.html">Gallery</a></li>
<li><a href="faq.html">FAQ</a></li><li><a href="contact.html">Contact &amp; Booking</a></li>
<li><a href="privacy-policy.html">Privacy Policy</a></li><li><a href="terms.html">Terms of Service</a></li></ul></div>
<div><h4>Book Your Cab</h4>
<p>Share your pickup, destination and date — we confirm fare and availability directly.</p>
<p><a class="btn btn-wa btn-sm" href="https://wa.me/{WA}?text=Namaste%20Shree%20Ji%20Travels!%20I%20would%20like%20to%20enquire%20about%20a%20cab%20booking." target="_blank" rel="noopener">💬 WhatsApp Booking</a></p>
<p><a class="btn btn-light btn-sm" href="{TEL}">📞 Tap to Call</a></p></div>
</div><div class="container copy"><span>© <span id="year">2026</span> Shree Ji Travels, SIDCUL Haridwar. All rights reserved.</span><span><a href="privacy-policy.html">Privacy</a> • <a href="terms.html">Terms</a> • <a href="sitemap.xml">Sitemap</a></span></div></footer>
<a class="float-call" href="{TEL}" aria-label="Call Shree Ji Travels now">📞</a>
<a class="float-wa" href="https://wa.me/{WA}?text=Namaste%20Shree%20Ji%20Travels!%20I%20would%20like%20to%20enquire%20about%20a%20cab%20booking." target="_blank" rel="noopener" aria-label="Chat on WhatsApp">💬</a>
<div class="lightbox" id="lightbox" role="dialog" aria-label="Image viewer"><button class="lb-close" data-lb-close aria-label="Close">✕</button><button class="lb-prev" data-lb-prev aria-label="Previous">‹</button><img id="lbImg" src="" alt="Gallery photo"><button class="lb-next" data-lb-next aria-label="Next">›</button></div>
<div class="mobile-book-bar" role="navigation" aria-label="Quick booking"><a class="btn btn-primary btn-sm" href="tel:+918077274970">📞 Call Now</a><a class="btn btn-wa btn-sm" href="https://wa.me/918077274970?text=Namaste%20Shree%20Ji%20Travels!%20I%20would%20like%20to%20enquire%20about%20a%20cab%20booking." target="_blank" rel="noopener">💬 WhatsApp</a></div>
<button class="to-top" aria-label="Back to top">↑</button>
<script src="assets/js/main.js?v=3" defer></script>
<script src="assets/js/dynamic.js?v=3" defer></script>"""

def page(fname, title, desc, active, body, extra_head=""):
    og = f"""<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website"><meta property="og:image" content="assets/img/poster.jpg">"""
    ld = """<script type="application/ld+json">{"@context":"https://schema.org","@type":"LocalBusiness","name":"Shree Ji Travels","telephone":"+91 8077274970","address":{"@type":"PostalAddress","addressLocality":"SIDCUL, Haridwar","addressRegion":"Uttarakhand","addressCountry":"IN"}}</script>"""
    html = f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css?v=4"><link rel="stylesheet" href="assets/css/dynamic.css?v=4">
<meta name="theme-color" content="#071B33">{og}{ld}{extra_head}</head>
<body><a class="skip-link" href="#main">Skip to content</a>{header(active)}<main id="main">{body}</main>{FOOTER}</body></html>"""
    open(os.path.join(BASE, fname), "w").write(html)
    print("wrote", fname)

def booking_form(form="general", journey_fixed="", chardham=False):
    jt_opts = ["One Way","Round Trip","Local","Outstation","Char Dham Yatra"]
    if journey_fixed:
        opts = f'<option value="{journey_fixed}" selected>{journey_fixed}</option>'
    else:
        opts = '<option value="">Select journey type</option>' + "".join(f'<option>{o}</option>' for o in jt_opts)
    extra = ""
    if chardham:
        extra = """<div class="field"><label for="f-pilg">Number of Pilgrims *</label><input id="f-pilg" name="pilgrims" type="number" min="1" max="50" placeholder="e.g. 4" required></div>
<div class="field"><label for="f-dur">Trip Duration (if known)</label><input id="f-dur" name="duration" type="text" placeholder="e.g. 10 days"></div>
<div class="field full"><label for="f-req">Special Requirements</label><textarea id="f-req" name="requirements" placeholder="Elderly travellers, temple priorities, halts..."></textarea></div>"""
    return f"""<form data-whatsapp-form data-form="{form}" novalidate>
<div class="error-msg" role="alert"></div>
<div class="form-grid">
<div class="field"><label>Pickup Location *</label><input name="pickup" type="text" placeholder="e.g. SIDCUL, Haridwar" required></div>
<div class="field"><label>Destination *</label><input name="destination" type="text" placeholder="e.g. Delhi / Kedarnath" required></div>
<div class="field"><label>Journey Type *</label><select name="journeyType" required>{opts}</select></div>
<div class="field"><label>Travel Date *</label><input name="travelDate" type="date" required></div>
<div class="field" data-return-field style="display:none"><label>Return Date *</label><input name="returnDate" type="date"></div>
<div class="field"><label>Number of Passengers *</label><input name="passengers" type="number" min="1" max="50" placeholder="e.g. 4" required></div>
<div class="field"><label>Vehicle Preference</label><select name="vehicle"><option value="">No preference — advise me</option><option>Sedan Cab</option><option>Passenger Van</option></select></div>
<div class="field"><label>Customer Name *</label><input name="customerName" type="text" placeholder="Your full name" required></div>
<div class="field"><label>Mobile Number *</label><input name="mobile" type="tel" placeholder="10-digit mobile" required></div>
{extra}</div>
<div class="form-foot"><button class="btn btn-wa btn-block" type="submit">💬 Send Enquiry on WhatsApp</button>
<span class="hint">After tapping, WhatsApp opens with your details pre-filled. Booking is confirmed only after we reply.</span></div></form>"""

WA_LINK = f"https://wa.me/{WA}?text=Namaste%20Shree%20Ji%20Travels!%20I%20would%20like%20to%20enquire%20about%20a%20cab%20booking."
I = IMG
# ---------------- HOME ----------------
home = f"""
<section class="hero"><div class="hero-bg hero-slides"><img src="{I['hero_home']}" alt="Scenic Uttarakhand highway through the Himalayan mountains" fetchpriority="high"><img data-fallback src="{I['himalaya']}" alt="Himalayan peaks above Haridwar" loading="lazy"><img data-fallback src="{I['mountain_road']}" alt="Mountain road in Uttarakhand" loading="lazy"></div><div class="hero-overlay"></div><div class="hero-dots" role="tablist" aria-label="Hero images"></div>
<div class="container hero-inner"><div class="reveal visible">
<div class="breadcrumb"><span>Shree Ji Travels Haridwar</span></div>
<h1>Your Journey, <span class="accent">Our Responsibility</span></h1>
<p class="hero-sub">Comfortable Cab Services from Haridwar for Local Travel, Outstation Journeys and Char Dham Yatra.</p>
<div class="hero-badges"><span>🚕 One Way Cabs</span><span>🔁 Round Trip</span><span>🛕 Local Haridwar</span><span>⛰️ Outstation</span><span>🙏 Char Dham Yatra</span></div>
<div class="hero-ctas"><a class="btn btn-wa" href="{WA_LINK}" target="_blank" rel="noopener">💬 Book Your Cab on WhatsApp</a><a class="btn btn-light" href="#services">Explore Our Services →</a></div>
<p class="hero-note"><span data-greet>Namaste</span> 🙏 &nbsp;•&nbsp; 📍 SIDCUL, Haridwar &nbsp;•&nbsp; 📞 <a style="color:#fff" href="{TEL}">{PHONE}</a> &nbsp;•&nbsp; Fares &amp; availability confirmed directly on call / WhatsApp.</p>
</div><div class="booking-card reveal visible"><h2>Quick Booking Enquiry</h2><p class="sub">Fill details — we open WhatsApp with everything ready to send.</p>{booking_form("general")}</div>
</div></section>

<section class="section" id="services"><div class="container">
<div class="center reveal"><span class="kicker">Our Services</span><h2>Cab Service in Haridwar, for Every Journey</h2><p class="lead">Choose a service to see details and request a fare. Every enquiry opens on WhatsApp — no advance payment taken online.</p></div>
<div class="cards5" style="margin-top:30px">
<div class="card reveal"><div class="card-img"><img class="nocrop" src="assets/img/cab-front-2.jpg" alt="Shree Ji Travels sedan cab — one way taxi from Haridwar" loading="lazy"></div><div class="card-body"><h3>One Way Cabs</h3><p>Point-to-point drops from Haridwar. Request a quote for your route.</p><a class="card-link" href="one-way-cab.html">Enquire →</a></div></div>
<div class="card reveal"><div class="card-img"><img class="nocrop" src="assets/img/cab-side-2.jpg" alt="Shree Ji Travels sedan cab — round trip cab Haridwar" loading="lazy"></div><div class="card-body"><h3>Round Trip Cabs</h3><p>Onward + return planned together for comfortable journeys.</p><a class="card-link" href="round-trip-cab.html">Enquire →</a></div></div>
<div class="card reveal"><div class="card-img"><img data-fallback src="{I['ghat']}" alt="Local taxi in Haridwar near Ganga ghat" loading="lazy"></div><div class="card-body"><h3>Local Cabs</h3><p>Har Ki Pauri, temples &amp; Rishikesh sightseeing, confirmed in advance.</p><a class="card-link" href="local-cab.html">Enquire →</a></div></div>
<div class="card reveal"><div class="card-img"><img data-fallback src="{I['mountain_road']}" alt="Outstation cab from Haridwar on mountain road" loading="lazy"></div><div class="card-body"><h3>Outstation Cabs</h3><p>Holidays, family visits &amp; business journeys across North India.</p><a class="card-link" href="outstation-cab.html">Enquire →</a></div></div>
<div class="card reveal"><div class="card-img"><img data-fallback src="{I['himalaya']}" alt="Char Dham Yatra cab from Haridwar in Himalayas" loading="lazy"></div><div class="card-body"><h3>Char Dham Yatra</h3><p>Sacred Yamunotri, Gangotri, Kedarnath &amp; Badrinath journeys.</p><a class="card-link" href="char-dham-yatra.html">Enquire →</a></div></div>
</div></div></section>

<section class="section-tight"><div class="container"><div class="split">
<div class="reveal"><span class="kicker">One Way &amp; Round Trip</span><h2>Example Routes from Haridwar</h2><p>Popular enquiry routes. These are <strong>example routes subject to confirmation</strong> — final fare, vehicle and timing are confirmed by us before the trip.</p>
<div class="route-grid" style="grid-template-columns:1fr 1fr;margin-top:18px">
<div class="route"><strong>Haridwar → Dehradun</strong><p>One-way drop enquiry</p><a class="btn btn-outline btn-sm" href="{WA_LINK}%0AInterest%3A%20Haridwar%20to%20Dehradun%20one%20way" target="_blank" rel="noopener">Request Fare</a></div>
<div class="route"><strong>Haridwar → Rishikesh</strong><p>One-way / local enquiry</p><a class="btn btn-outline btn-sm" href="{WA_LINK}%0AInterest%3A%20Haridwar%20to%20Rishikesh" target="_blank" rel="noopener">Request Fare</a></div>
<div class="route"><strong>Haridwar → Delhi</strong><p>One-way / round-trip enquiry</p><a class="btn btn-outline btn-sm" href="{WA_LINK}%0AInterest%3A%20Haridwar%20to%20Delhi" target="_blank" rel="noopener">Request Fare</a></div>
<div class="route"><strong>Haridwar → Chandigarh</strong><p>Long-distance enquiry</p><a class="btn btn-outline btn-sm" href="{WA_LINK}%0AInterest%3A%20Haridwar%20to%20Chandigarh" target="_blank" rel="noopener">Request Fare</a></div>
</div></div>
<div class="reveal"><img class="round nocrop" src="assets/img/cab-rear.jpg" alt="Shree Ji Travels white sedan taxi, full rear photo" loading="lazy">
<div class="trust-row" style="margin-top:14px"><span>✓ Sedan cabs for small groups</span><span>✓ Passenger vans for families</span><span>✓ Fare confirmed before trip</span></div></div>
</div></div></section>

<section class="section-tight"><div class="container"><div class="banner reveal">
<div><span class="kicker" style="color:var(--saffron)">Char Dham Yatra</span><h2>A Sacred Journey Through Uttarakhand</h2><p>Yamunotri • Gangotri • Kedarnath • Badrinath. Road conditions, opening dates, vehicle availability and inclusions are confirmed before booking — request a detailed quote.</p>
<div class="cta-btns" style="justify-content:flex-start;margin-top:18px"><a class="btn btn-saffron" href="char-dham-yatra.html">Plan My Yatra →</a><a class="btn btn-wa" href="{WA_LINK}%0AInterest%3A%20Char%20Dham%20Yatra%20enquiry" target="_blank" rel="noopener">💬 Yatra on WhatsApp</a></div></div>
<div><img class="nocrop" src="assets/img/temple-kedarnath.jpg" alt="Kedarnath Temple — real photo" loading="lazy"></div>
</div></div></section>

<section class="section-tight"><div class="container">
<div class="center reveal"><span class="kicker">Our Cabs — Real Photos</span><h2>Sedan Cabs &amp; Passenger Vans</h2><p class="lead">Actual vehicle photos shared by Shree Ji Travels, SIDCUL Haridwar. Vehicle in your trip is confirmed at booking time.</p></div>
<div class="fleet" style="margin-top:26px">
<div class="fleet-card reveal"><img class="nocrop" src="assets/img/cab-side-2.jpg" alt="White sedan cab side view — Shree Ji Travels real vehicle, full photo" loading="lazy"><div class="pad"><span class="tag">Sedan Cab</span><span class="tag">Ideal for 2–4 passengers</span><h3>Comfortable Sedan Cabs</h3><p style="color:var(--muted)">Clean white sedans suited to one-way drops, local sightseeing and outstation trips. Luggage carrier available on request.</p><a class="card-link" href="contact.html">Request sedan fare →</a></div></div>
<div class="fleet-card reveal"><img class="nocrop poster-full" src="assets/img/poster.jpg" alt="Shree Ji Travels poster showing sedan and passenger van with Haridwar backdrop, full poster" loading="lazy"><div class="pad"><span class="tag">Sedan + Van</span><span class="tag">Family &amp; Yatra groups</span><h3>Sedans &amp; Passenger Vans</h3><p style="color:var(--muted)">From small families to Yatra groups — tell us passengers + luggage and we suggest the right vehicle. Availability confirmed directly.</p><a class="card-link" href="gallery.html">See all photos →</a></div></div>
</div></div></section>

<section class="section-tight"><div class="container">
<div class="center reveal"><span class="kicker">Destinations</span><h2>Popular Destinations Around Haridwar</h2></div>
<div class="dest-grid" style="margin-top:24px">
<div class="dest reveal"><img data-fallback src="{I['ghat']}" alt="Har Ki Pauri Haridwar" loading="lazy"><div><h3>Har Ki Pauri</h3><p>Ganga aarti &amp; ghats</p></div></div>
<div class="dest reveal"><img data-fallback src="{I['ganga_aarti']}" alt="Rishikesh and Ganga river" loading="lazy"><div><h3>Rishikesh</h3><p>Laxman Jhula &amp; ashrams</p></div></div>
<div class="dest reveal"><img data-fallback src="{I['delhi']}" alt="Delhi India Gate" loading="lazy"><div><h3>Delhi</h3><p>Airport &amp; city transfers</p></div></div>
<div class="dest reveal"><img data-fallback src="{I['himalaya']}" alt="Mussoorie and Uttarakhand mountains" loading="lazy"><div><h3>Mussoorie &amp; Hills</h3><p>Weekend mountain trips</p></div></div>
</div></div></section>

<section class="section-tight"><div class="container">
<div class="center reveal"><span class="kicker">How It Works</span><h2>Book in 3 Simple Steps</h2></div>
<div class="steps" style="margin-top:24px">
<div class="step reveal"><div class="num">1</div><h3>Share your trip</h3><p style="color:var(--muted)">Fill the form or tap WhatsApp with pickup, destination, date &amp; passengers.</p></div>
<div class="step reveal"><div class="num">2</div><h3>Get fare &amp; vehicle confirmation</h3><p style="color:var(--muted)">We reply directly with fare, vehicle option and pickup plan.</p></div>
<div class="step reveal"><div class="num">3</div><h3>Travel comfortably</h3><p style="color:var(--muted)">Meet your cab at the confirmed point and enjoy the journey.</p></div>
</div></div></section>

<section class="section-tight"><div class="container">
<div class="center reveal"><span class="kicker">FAQ</span><h2>Common Questions</h2></div>
<div class="faq" style="margin-top:22px">
<div class="faq-item reveal"><button class="faq-q" aria-expanded="false">How can I book a cab?<span class="plus">+</span></button><div class="faq-a"><p>Fill any enquiry form on this website or tap a WhatsApp button. Your details open pre-filled in WhatsApp — send it and we confirm fare and availability directly.</p></div></div>
<div class="faq-item reveal"><button class="faq-q" aria-expanded="false">How are fares confirmed?<span class="plus">+</span></button><div class="faq-a"><p>Fares depend on route, vehicle, dates and halts. Share your trip details and we share the applicable fare before the journey. Nothing is charged online.</p></div></div>
<div class="faq-item reveal"><button class="faq-q" aria-expanded="false">How do I enquire about Char Dham Yatra?<span class="plus">+</span></button><div class="faq-a"><p>Use the Char Dham Yatra page form with travel dates, pilgrims and vehicle preference. Route conditions, opening dates and inclusions are confirmed before booking.</p></div></div>
</div>
<div class="center" style="margin-top:18px"><a class="btn btn-outline" href="faq.html">Read all FAQs →</a></div>
</div></section>

<section class="section-tight"><div class="container"><div class="cta-band reveal">
<h2>Ready to travel from Haridwar?</h2><p>Send your trip on WhatsApp now — we reply with fare and vehicle availability.</p>
<div class="cta-btns"><a class="btn btn-wa" href="{WA_LINK}" target="_blank" rel="noopener">💬 Book Your Cab on WhatsApp</a><a class="btn btn-light" href="{TEL}">📞 Call {PHONE}</a></div>
</div></div></section>
"""
page("index.html","Shree Ji Travels Haridwar | One Way, Round Trip, Local, Outstation & Char Dham Cabs","Shree Ji Travels, SIDCUL Haridwar — cab service in Haridwar for one way taxi, round trip cab, local Haridwar taxi, outstation cabs & Char Dham Yatra. Book on WhatsApp +91 8077274970.","index.html",home)

# ---------------- ONE WAY ----------------
oneway = f"""
<section class="page-hero"><div class="hero-bg"><img src="{I['mountain_road']}" alt="One way taxi from Haridwar on mountain highway"></div><div class="hero-overlay"></div>
<div class="container page-hero-inner"><div>
<div class="breadcrumb"><a href="index.html">Home</a> › <span>One Way Cabs</span></div>
<h1>One Way Cab Service from Haridwar</h1>
<p>Pay for one direction, travel point-to-point. Share your route and date — we confirm the one-way fare, vehicle and pickup plan directly. No fares listed online; every quote is given personally.</p>
<div class="hero-ctas"><a class="btn btn-wa" href="{WA_LINK}%0AJourney%20Type%3A%20One%20Way" target="_blank" rel="noopener">💬 Request One-Way Fare</a><a class="btn btn-light" href="{TEL}">📞 Call {PHONE}</a></div>
</div><div class="page-hero-card"><img class="nocrop" src="assets/img/cab-front-1.jpg" alt="Shree Ji Travels white sedan cab, full front photo"></div></div></section>
<section class="section"><div class="container"><div class="split">
<div class="reveal"><span class="kicker">Why One Way?</span><h2>Benefits of Booking a One-Way Cab</h2>
<ul class="check-list"><li><span class="tick">✓</span><span><strong>No return leg to arrange</strong> — ideal for airport drops, station transfers and single-direction travel.</span></li>
<li><span class="tick">✓</span><span><strong>Clear pickup planning</strong> — confirm pickup point, time and luggage needs with us in advance.</span></li>
<li><span class="tick">✓</span><span><strong>Right-sized vehicle</strong> — sedan cabs for small groups, passenger vans when travelling with family.</span></li>
<li><span class="tick">✓</span><span><strong>Fare shared before the trip</strong> — request a quote; availability and route confirmed by the business.</span></li></ul></div>
<div class="reveal"><div class="booking-card"><h2>One-Way Enquiry</h2><p class="sub">Pickup + drop-off enquiry — opens on WhatsApp.</p>{booking_form("oneway","One Way")}</div></div>
</div></div></section>
<section class="section-tight"><div class="container">
<div class="center reveal"><span class="kicker">Example Routes</span><h2>Popular One-Way Enquiries</h2><p class="lead">Example routes subject to confirmation. Final fare depends on date, vehicle and halts.</p></div>
<div class="route-grid" style="margin-top:22px">
<div class="route reveal"><strong>Haridwar → Dehradun</strong><p>Short intercity drop, incl. airport enquiries.</p><a class="btn btn-outline btn-sm" href="{WA_LINK}%0AJourney%20Type%3A%20One%20Way%0APickup%3A%20Haridwar%0ADestination%3A%20Dehradun" target="_blank" rel="noopener">Request Quote</a></div>
<div class="route reveal"><strong>Haridwar → Rishikesh</strong><p>Nearby transfer &amp; sightseeing drop.</p><a class="btn btn-outline btn-sm" href="{WA_LINK}%0AJourney%20Type%3A%20One%20Way%0APickup%3A%20Haridwar%0ADestination%3A%20Rishikesh" target="_blank" rel="noopener">Request Quote</a></div>
<div class="route reveal"><strong>Haridwar → Delhi</strong><p>Long-distance one-way, incl. airport.</p><a class="btn btn-outline btn-sm" href="{WA_LINK}%0AJourney%20Type%3A%20One%20Way%0APickup%3A%20Haridwar%0ADestination%3A%20Delhi" target="_blank" rel="noopener">Request Quote</a></div>
<div class="route reveal"><strong>Haridwar → Chandigarh</strong><p>Long-distance family &amp; business travel.</p><a class="btn btn-outline btn-sm" href="{WA_LINK}%0AJourney%20Type%3A%20One%20Way%0APickup%3A%20Haridwar%0ADestination%3A%20Chandigarh" target="_blank" rel="noopener">Request Quote</a></div>
</div>
<div class="center" style="margin-top:26px"><a class="btn btn-wa" href="{WA_LINK}%0AJourney%20Type%3A%20One%20Way" target="_blank" rel="noopener">💬 Book One-Way Cab on WhatsApp</a></div>
</div></section>"""
page("one-way-cab.html","One Way Cab Service from Haridwar | Shree Ji Travels","One way taxi from Haridwar to Dehradun, Rishikesh, Delhi & Chandigarh. Request one-way fare on WhatsApp +91 8077274970. Fares confirmed before the trip.","one-way-cab.html",oneway)

# ---------------- ROUND TRIP ----------------
roundtrip = f"""
<section class="page-hero"><div class="hero-bg"><img src="{I['himalaya']}" alt="Round trip cabs for comfortable family journeys in the Himalayas"></div><div class="hero-overlay"></div>
<div class="container page-hero-inner"><div>
<div class="breadcrumb"><a href="index.html">Home</a> › <span>Round Trip Cabs</span></div>
<h1>Round Trip Cabs for Comfortable Journeys</h1>
<p>Arrange onward and return travel together — one vehicle plan, one point of contact. Share departure + return dates and we confirm fare and vehicle availability.</p>
<div class="hero-ctas"><a class="btn btn-wa" href="{WA_LINK}%0AJourney%20Type%3A%20Round%20Trip" target="_blank" rel="noopener">💬 Request Round Trip Fare</a><a class="btn btn-light" href="{TEL}">📞 Call {PHONE}</a></div>
</div><div class="page-hero-card"><img class="nocrop" src="assets/img/cab-front-2.jpg" alt="Shree Ji Travels sedan ready for round trip, full photo"></div></div></section>
<section class="section"><div class="container"><div class="split">
<div class="reveal"><span class="kicker">Why Round Trip?</span><h2>Benefits of Arranging Return Travel in Advance</h2>
<ul class="check-list"><li><span class="tick">✓</span><span><strong>Single coordinated plan</strong> — pickup, halts and return discussed together.</span></li>
<li><span class="tick">✓</span><span><strong>Better for families &amp; pilgrims</strong> — same vehicle understanding for both legs.</span></li>
<li><span class="tick">✓</span><span><strong>Clear communication</strong> — dates, passengers and luggage confirmed before travel.</span></li>
<li><span class="tick">✓</span><span><strong>Fare shared upfront</strong> — request a quote; confirmed directly by the business.</span></li></ul>
<div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:16px"><img class="nocrop" src="assets/img/cab-side-1.jpg" alt="Shree Ji Travels sedan cab side, full photo" loading="lazy" style="border-radius:14px;width:48%;aspect-ratio:4/3;object-fit:contain"><img class="nocrop" src="assets/img/cab-rear.jpg" alt="Shree Ji Travels sedan cab rear, full photo" loading="lazy" style="border-radius:14px;width:48%;aspect-ratio:4/3;object-fit:contain"></div></div>
<div class="reveal"><div class="booking-card"><h2>Round-Trip Enquiry</h2><p class="sub">Include return date &amp; vehicle preference.</p>
<form data-whatsapp-form data-form="roundtrip" novalidate><div class="error-msg" role="alert"></div><div class="form-grid">
<div class="field"><label>Pickup *</label><input name="pickup" placeholder="e.g. Haridwar" required></div>
<div class="field"><label>Destination *</label><input name="destination" placeholder="e.g. Delhi" required></div>
<div class="field"><label>Departure Date *</label><input name="travelDate" type="date" required></div>
<div class="field"><label>Return Date *</label><input name="returnDate" type="date" required></div>
<div class="field"><label>Passengers *</label><input name="passengers" type="number" min="1" max="50" required></div>
<div class="field"><label>Vehicle Preference</label><select name="vehicle"><option value="">No preference</option><option>Sedan Cab</option><option>Passenger Van</option></select></div>
<div class="field"><label>Customer Name *</label><input name="customerName" required></div>
<div class="field"><label>Mobile *</label><input name="mobile" type="tel" required></div>
<div class="field" style="display:none"><input name="journeyType" value="Round Trip"></div>
</div><div class="form-foot"><button class="btn btn-wa btn-block" type="submit">💬 Request Round Trip Fare</button><span class="hint">Booking confirmed only after we reply on WhatsApp.</span></div></form></div></div>
</div></div></section>"""
page("round-trip-cab.html","Round Trip Cab Haridwar | Comfortable Return Journeys","Round trip cab Haridwar for family & return journeys. Share dates & passengers, request round trip fare on WhatsApp +91 8077274970.","round-trip-cab.html",roundtrip)

# ---------------- LOCAL ----------------
local = f"""
<section class="page-hero"><div class="hero-bg"><img src="{I['ghat']}" alt="Haridwar city and Ganga ghat"></div><div class="hero-overlay"></div>
<div class="container page-hero-inner"><div>
<div class="breadcrumb"><a href="index.html">Home</a> › <span>Local Cabs</span></div>
<h1>Explore Haridwar with Local Cab Services</h1>
<p>Local taxi in Haridwar for temple visits, Ganga ghats and nearby Rishikesh. Sightseeing routes, waiting time and availability are confirmed with us before the trip.</p>
<div class="hero-ctas"><a class="btn btn-wa" href="{WA_LINK}%0AJourney%20Type%3A%20Local" target="_blank" rel="noopener">💬 Book Local Cab</a><a class="btn btn-light" href="{TEL}">📞 Call {PHONE}</a></div>
</div><div class="page-hero-card"><img data-fallback src="{I['ganga_aarti']}" alt="Ganga ghat at Haridwar"></div></div></section>
<section class="section"><div class="container"><div class="split">
<div class="reveal"><span class="kicker">Sightseeing</span><h2>Places to Explore</h2>
<ul class="check-list"><li><span class="tick">✓</span><span><strong>Har Ki Pauri</strong> — Ganga ghats, evening aarti and riverside walks.</span></li>
<li><span class="tick">✓</span><span><strong>Mansa Devi Temple</strong> — hilltop temple visit, ropeway or road as available.</span></li>
<li><span class="tick">✓</span><span><strong>Chandi Devi Temple</strong> — hilltop darshan, plan timing with us.</span></li>
<li><span class="tick">✓</span><span><strong>Nearby Rishikesh</strong> — ashrams, ghats and bridges on a local plan.</span></li></ul>
<p style="color:var(--muted)">Sightseeing routes, waiting time and availability must be confirmed. Tell us your must-visit spots and start time — we plan the route.</p></div>
<div class="reveal"><div class="booking-card"><h2>Local Cab Enquiry</h2><p class="sub">City transfer or sightseeing — opens on WhatsApp.</p>{booking_form("local","Local")}</div></div>
</div></div></section>"""
page("local-cab.html","Local Taxi in Haridwar | Har Ki Pauri, Temples & Rishikesh","Local taxi in Haridwar for Har Ki Pauri, Mansa Devi, Chandi Devi & Rishikesh. Confirm sightseeing route & fare on WhatsApp +91 8077274970.","local-cab.html",local)

# ---------------- OUTSTATION ----------------
outstation = f"""
<section class="page-hero"><div class="hero-bg"><img src="{I['mountain_road']}" alt="Outstation cabs from Haridwar on mountain roads"></div><div class="hero-overlay"></div>
<div class="container page-hero-inner"><div>
<div class="breadcrumb"><a href="index.html">Home</a> › <span>Outstation Cabs</span></div>
<h1>Outstation Cabs from Haridwar</h1>
<p>For holidays, family visits, business journeys and personal trips across North India. Choose one-way or return — share dates, passengers and vehicle preference for a quote.</p>
<div class="hero-ctas"><a class="btn btn-wa" href="{WA_LINK}%0AJourney%20Type%3A%20Outstation" target="_blank" rel="noopener">💬 Request Outstation Quote</a><a class="btn btn-light" href="{TEL}">📞 Call {PHONE}</a></div>
</div><div class="page-hero-card"><img data-fallback src="{I['himalaya']}" alt="Scenic Himalayan destination for outstation travel"></div></div></section>
<section class="section"><div class="container"><div class="split">
<div class="reveal"><span class="kicker">Long Distance</span><h2>Travel Your Way</h2>
<ul class="check-list"><li><span class="tick">✓</span><span><strong>Holidays</strong> — hill stations and sightseeing circuits with halts planned.</span></li>
<li><span class="tick">✓</span><span><strong>Family visits</strong> — door-to-door travel with luggage space discussed upfront.</span></li>
<li><span class="tick">✓</span><span><strong>Business journeys</strong> — timed pickups and return options.</span></li>
<li><span class="tick">✓</span><span><strong>Personal trips</strong> — flexible plans confirmed before booking.</span></li></ul>
<div class="route-grid" style="grid-template-columns:1fr 1fr;margin-top:14px">
<div class="route"><strong>Haridwar → Mussoorie</strong><p>Hill-station enquiry</p></div>
<div class="route"><strong>Haridwar → Delhi Airport</strong><p>Airport transfer enquiry</p></div></div></div>
<div class="reveal"><div class="booking-card"><h2>Outstation Enquiry</h2><p class="sub">Add return date if it is a round trip.</p>
<form data-whatsapp-form data-form="outstation" novalidate><div class="error-msg" role="alert"></div><div class="form-grid">
<div class="field"><label>Pickup *</label><input name="pickup" required></div>
<div class="field"><label>Destination *</label><input name="destination" required></div>
<div class="field"><label>Journey Type *</label><select name="journeyType" required><option value="">Select</option><option>One Way</option><option>Round Trip</option><option>Outstation</option></select></div>
<div class="field"><label>Travel Date *</label><input name="travelDate" type="date" required></div>
<div class="field"><label>Return Date (if applicable)</label><input name="returnDate" type="date"></div>
<div class="field"><label>Passengers *</label><input name="passengers" type="number" min="1" max="50" required></div>
<div class="field"><label>Vehicle Preference</label><select name="vehicle"><option value="">No preference</option><option>Sedan Cab</option><option>Passenger Van</option></select></div>
<div class="field"><label>Mobile *</label><input name="mobile" type="tel" required></div>
<div class="field"><label>Customer Name *</label><input name="customerName" required></div>
<div class="field full"><label>Notes</label><textarea name="notes" placeholder="Halts, luggage, timing..."></textarea></div>
</div><div class="form-foot"><button class="btn btn-wa btn-block" type="submit">💬 Request Quote on WhatsApp</button></div></form></div></div>
</div></div></section>"""
page("outstation-cab.html","Outstation Cab from Haridwar | Holidays, Family & Business Trips","Outstation cab from Haridwar for holidays, family visits & business journeys. Request quote on WhatsApp +91 8077274970.","outstation-cab.html",outstation)

# ---------------- CHARDHAM ----------------
chardham = f"""
<section class="page-hero"><div class="hero-bg"><img src="{I['himalaya']}" alt="Himalayan landscapes and pilgrimage roads of Char Dham Yatra"></div><div class="hero-overlay"></div>
<div class="container page-hero-inner"><div>
<div class="breadcrumb"><a href="index.html">Home</a> › <span>Char Dham Yatra</span></div>
<h1>Char Dham Yatra — A Sacred Journey Through Uttarakhand</h1>
<p>Char Dham Yatra cab from Haridwar covering Yamunotri, Gangotri, Kedarnath and Badrinath. Route conditions, opening dates, road access, vehicle availability, travel duration and inclusions must be confirmed before booking.</p>
<div class="hero-ctas"><a class="btn btn-wa" href="{WA_LINK}%0AJourney%20Type%3A%20Char%20Dham%20Yatra" target="_blank" rel="noopener">💬 Enquire for Yatra</a><a class="btn btn-light" href="#yatra-form">Fill Yatra Form ↓</a></div>
</div><div class="page-hero-card"><img class="nocrop" src="assets/img/temple-kedarnath.jpg" alt="Kedarnath Temple — real photo"></div></div></section>
<section class="section"><div class="container">
<div class="center reveal"><span class="kicker">Four Sacred Destinations</span><h2>The Char Dhams</h2><p class="lead">Separate journeys, one sacred circuit. Descriptions are brief introductions — darshan order and halts are planned with you.</p></div>
<div class="cards4" style="margin-top:26px">
<div class="card reveal"><div class="card-img"><img class="nocrop" src="assets/img/temple-yamunotri.jpg" alt="Yamunotri Temple — real photo" loading="lazy"></div><div class="card-body"><h3>Yamunotri</h3><p>Source of the Yamuna, reached via road and trek. Discuss fitness, halts and timing with us.</p></div></div>
<div class="card reveal"><div class="card-img"><img class="nocrop" src="assets/img/temple-gangotri.jpg" alt="Gangotri Temple — real photo" loading="lazy"></div><div class="card-body"><h3>Gangotri</h3><p>Source of the Ganga amid Himalayan valleys. Road access and halts confirmed per season.</p></div></div>
<div class="card reveal"><div class="card-img"><img class="nocrop" src="assets/img/temple-kedarnath.jpg" alt="Kedarnath Temple — real photo" loading="lazy"></div><div class="card-body"><h3>Kedarnath</h3><p>One of the holiest Shiva shrines, with road + trek/transport stages. Conditions vary by season.</p></div></div>
<div class="card reveal"><div class="card-img"><img class="nocrop" src="assets/img/temple-badrinath.jpg" alt="Badrinath Temple — real photo" loading="lazy"></div><div class="card-body"><h3>Badrinath</h3><p>Sacred Vishnu shrine in the high Himalayas. Opening dates and stays confirmed in advance.</p></div></div>
</div>
<p class="hint center" style="margin-top:16px">Temple photos above are real photographs (via Wikimedia Commons contributors).</p></div></section>
<section class="section-tight" id="yatra-form"><div class="container"><div class="split">
<div class="reveal"><span class="kicker">Illustrative Framework</span><h2>How a Yatra Plan Is Discussed</h2>
<p style="color:var(--muted)">This is an <strong>illustrative itinerary framework, not a confirmed package</strong>. We discuss a practical order with you:</p>
<ul class="check-list"><li><span class="tick">1</span><span>Haridwar → Yamunotri region (road + local stages)</span></li>
<li><span class="tick">2</span><span>Yamunotri region → Gangotri region</span></li>
<li><span class="tick">3</span><span>Gangotri region → Kedarnath region</span></li>
<li><span class="tick">4</span><span>Kedarnath region → Badrinath → Haridwar</span></li></ul>
<p style="color:var(--muted)">Halts, darshan time, vehicle choice and duration are fixed only after direct confirmation. No package prices, hotel inclusions, permits or guaranteed darshan are offered online.</p></div>
<div class="reveal"><div class="booking-card"><h2>Char Dham Enquiry</h2><p class="sub">Proposed dates, pilgrims &amp; vehicle — opens on WhatsApp.</p>{booking_form("chardham","Char Dham Yatra",True)}</div></div>
</div></div></section>
<section class="section-tight"><div class="container"><div class="banner reveal">
<div><h2>Planning Your Yatra</h2><p>Carry warm layers, comfortable walking shoes, medicines, ID proofs and extra buffer days. Elderly pilgrims should discuss trek stages and halts with family and us before finalising. Tap below to request a detailed quote.</p>
<div class="cta-btns" style="justify-content:flex-start;margin-top:16px"><a class="btn btn-saffron" href="{WA_LINK}%0AJourney%20Type%3A%20Char%20Dham%20Yatra%0ARequest%3A%20detailed%20quote" target="_blank" rel="noopener">💬 Request a Quote</a></div></div>
<div><img data-fallback src="{I['river']}" alt="Pilgrimage road along Himalayan river" loading="lazy"></div></div></div></section>"""
page("char-dham-yatra.html","Char Dham Yatra Cab from Haridwar | Yamunotri Gangotri Kedarnath Badrinath","Char Dham Yatra cab from Haridwar — Yamunotri, Gangotri, Kedarnath, Badrinath. Request Yatra quote on WhatsApp +91 8077274970. Details confirmed before booking.","char-dham-yatra.html",chardham)

# ---------------- ABOUT ----------------
about = f"""
<section class="page-hero"><div class="hero-bg"><img src="{I['mountain_road']}" alt="Scenic Uttarakhand travel with Shree Ji Travels"></div><div class="hero-overlay"></div>
<div class="container page-hero-inner"><div>
<div class="breadcrumb"><a href="index.html">Home</a> › <span>About</span></div>
<h1>About Shree Ji Travels, Haridwar</h1>
<p>A Haridwar-based cab and travel service in SIDCUL, offering one-way, round-trip, local, outstation and Char Dham Yatra enquiries — with comfortable journeys and clear communication.</p>
<div class="hero-ctas"><a class="btn btn-wa" href="{WA_LINK}" target="_blank" rel="noopener">💬 Contact on WhatsApp</a><a class="btn btn-light" href="contact.html">Contact Details →</a></div>
</div><div class="page-hero-card"><img class="nocrop poster-full" src="assets/img/poster.jpg" alt="Shree Ji Travels business poster, full poster"></div></div></section>
<section class="section"><div class="container"><div class="split">
<div class="reveal"><span class="kicker">Our Approach</span><h2>Comfortable Journeys, Clearly Coordinated</h2>
<p>Families, tourists and pilgrims travel with different needs. We keep the process simple: you share pickup, destination, dates and passengers — we confirm the vehicle option, fare and pickup arrangement directly before the trip.</p>
<ul class="check-list"><li><span class="tick">✓</span><span>One enquiry point on call &amp; WhatsApp: <strong>{PHONE}</strong></span></li>
<li><span class="tick">✓</span><span>Sedan cabs for small groups; passenger vans for larger parties</span></li>
<li><span class="tick">✓</span><span>Local Haridwar knowledge for temples, ghats and Rishikesh plans</span></li>
<li><span class="tick">✓</span><span>Pilgrimage coordination for the Char Dham circuit, confirmed step by step</span></li></ul></div>
<div class="reveal"><img class="round nocrop" src="assets/img/cab-hotel.jpg" alt="Shree Ji Travels sedan cab on duty, full photo"></div>
</div></div></section>"""
page("about.html","About Us | Shree Ji Travels Haridwar — Cab & Yatra Service","Shree Ji Travels is a Haridwar-based cab service in SIDCUL offering one-way, round-trip, local, outstation & Char Dham Yatra enquiries. Call +91 8077274970.","about.html",about)

# ---------------- GALLERY ----------------
gal = f"""
<section class="page-hero"><div class="hero-bg"><img src="{I['himalaya']}" alt="Uttarakhand mountains gallery"></div><div class="hero-overlay"></div>
<div class="container page-hero-inner"><div>
<div class="breadcrumb"><a href="index.html">Home</a> › <span>Gallery</span></div>
<h1>Gallery — Cabs, Haridwar &amp; the Himalayas</h1>
<p>Real cab photos from Shree Ji Travels plus illustrative travel photography of Haridwar, Uttarakhand and the Char Dham region. Tap any photo to view.</p>
</div><div class="page-hero-card"><img class="nocrop" src="assets/img/cab-side-1.jpg" alt="White sedan cab, full photo"></div></div></section>
<section class="section"><div class="container">
<div class="filter-bar reveal"><button class="active" data-filter="all">All</button><button data-filter="sedan">Sedan Cabs</button><button data-filter="van">Passenger Vans</button><button data-filter="haridwar">Haridwar</button><button data-filter="mountains">Uttarakhand Mountains</button><button data-filter="chardham">Char Dham Yatra</button></div>
<div class="g-grid">
<button class="g-item" data-cat="sedan"><img class="nocrop" src="assets/img/cab-front-1.jpg" alt="Shree Ji Travels sedan — front view, full photo" loading="lazy"><figcaption>Sedan Cab • Real Photo</figcaption></button>
<button class="g-item" data-cat="sedan"><img class="nocrop" src="assets/img/cab-rear.jpg" alt="Shree Ji Travels sedan — rear view, full photo" loading="lazy"><figcaption>Sedan Cab • Real Photo</figcaption></button>
<button class="g-item" data-cat="sedan"><img class="nocrop" src="assets/img/cab-front-2.jpg" alt="Sedan cab on highway, full photo" loading="lazy"><figcaption>Sedan Cab • Real Photo</figcaption></button>
<button class="g-item" data-cat="sedan"><img class="nocrop" src="assets/img/cab-side-1.jpg" alt="Sedan cab side profile, full photo" loading="lazy"><figcaption>Sedan Cab • Real Photo</figcaption></button>
<button class="g-item" data-cat="sedan"><img class="nocrop" src="assets/img/cab-side-2.jpg" alt="Sedan cab side view on road, full photo" loading="lazy"><figcaption>Sedan Cab • Real Photo</figcaption></button>
<button class="g-item" data-cat="sedan"><img class="nocrop" src="assets/img/cab-hotel.jpg" alt="Sedan cab parked at hotel, full photo" loading="lazy"><figcaption>Sedan Cab • On Duty</figcaption></button>
<button class="g-item" data-cat="van"><img class="nocrop poster-full" src="assets/img/poster.jpg" alt="Business poster showing sedan and passenger van, full poster" loading="lazy"><figcaption>Sedan + Van • Poster</figcaption></button>
<button class="g-item" data-cat="van"><img class="nocrop" src="assets/img/cab-hotel.jpg" alt="Shree Ji Travels cab on duty, full photo" loading="lazy"><figcaption>Our Cab • On Duty</figcaption></button>
<button class="g-item" data-cat="haridwar"><img data-fallback src="{I['ghat']}" alt="Haridwar Ganga ghat" loading="lazy"><figcaption>Haridwar • Ghats</figcaption></button>
<button class="g-item" data-cat="haridwar"><img data-fallback src="{I['ganga_aarti']}" alt="Ganga river at Haridwar Rishikesh" loading="lazy"><figcaption>Haridwar • Ganga</figcaption></button>
<button class="g-item" data-cat="mountains"><img data-fallback src="{I['hero_home']}" alt="Uttarakhand highway and mountains" loading="lazy"><figcaption>Uttarakhand • Highway</figcaption></button>
<button class="g-item" data-cat="mountains"><img data-fallback src="{I['mountain_road']}" alt="Mountain roads of Uttarakhand" loading="lazy"><figcaption>Uttarakhand • Mountains</figcaption></button>
<button class="g-item" data-cat="mountains"><img data-fallback src="{I['river']}" alt="Himalayan river valley" loading="lazy"><figcaption>Uttarakhand • Valleys</figcaption></button>
<button class="g-item" data-cat="chardham"><img class="nocrop" src="assets/img/temple-yamunotri.jpg" alt="Yamunotri Temple — real photo" loading="lazy"><figcaption>Yamunotri • Real Photo</figcaption></button>
<button class="g-item" data-cat="chardham"><img class="nocrop" src="assets/img/temple-gangotri.jpg" alt="Gangotri Temple — real photo" loading="lazy"><figcaption>Gangotri • Real Photo</figcaption></button>
<button class="g-item" data-cat="chardham"><img class="nocrop" src="assets/img/temple-kedarnath.jpg" alt="Kedarnath Temple — real photo" loading="lazy"><figcaption>Kedarnath • Real Photo</figcaption></button>
<button class="g-item" data-cat="chardham"><img class="nocrop" src="assets/img/temple-badrinath.jpg" alt="Badrinath Temple — real photo" loading="lazy"><figcaption>Badrinath • Real Photo</figcaption></button>
</div>
<p class="hint center" style="margin-top:18px">Cab photos are real Shree Ji Travels vehicles; temple photos are real photographs (via Wikimedia Commons contributors). Vehicle for your trip is confirmed at booking.</p>
</div></section>"""
page("gallery.html","Gallery | Shree Ji Travels — Sedan Cabs, Haridwar & Char Dham Photos","Gallery of Shree Ji Travels: real sedan cab photos, Haridwar, Uttarakhand mountains & Char Dham Yatra region. SIDCUL Haridwar taxi service.","gallery.html",gal)

# ---------------- CONTACT ----------------
contact = f"""
<section class="page-hero"><div class="hero-bg"><img src="{I['ghat']}" alt="Contact Shree Ji Travels for cab booking in Haridwar"></div><div class="hero-overlay"></div>
<div class="container page-hero-inner"><div>
<div class="breadcrumb"><a href="index.html">Home</a> › <span>Contact</span></div>
<h1>Contact &amp; Booking — Shree Ji Travels</h1>
<p>📍 SIDCUL, Haridwar, Uttarakhand, India &nbsp;•&nbsp; 📞 {PHONE} &nbsp;•&nbsp; Tap below to call or WhatsApp. Every form opens WhatsApp with your message ready.</p>
<div class="hero-ctas"><a class="btn btn-wa" href="{WA_LINK}" target="_blank" rel="noopener">💬 WhatsApp Booking</a><a class="btn btn-light" href="{TEL}">📞 Tap to Call</a></div>
</div><div class="page-hero-card"><img class="nocrop poster-full" src="assets/img/poster.jpg" alt="Shree Ji Travels contact poster with phone number, full poster"></div></div></section>
<section class="section"><div class="container contact-grid">
<div class="info-card reveal"><h2>Reach Us Directly</h2>
<div class="info-row"><span class="ic">📞</span><span><strong>Phone</strong><br><a href="{TEL}">{PHONE}</a></span></div>
<div class="info-row"><span class="ic">💬</span><span><strong>WhatsApp</strong><br><a href="https://wa.me/{WA}" target="_blank" rel="noopener">{PHONE} — chat now</a></span></div>
<div class="info-row"><span class="ic">📍</span><span><strong>Location</strong><br>SIDCUL, Haridwar, Uttarakhand, India</span></div>
<div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn btn-wa btn-sm" href="{TEL}">📞 Tap to Call</a><a class="btn btn-saffron btn-sm" href="https://wa.me/{WA}?text=Namaste%20Shree%20Ji%20Travels!%20I%20would%20like%20to%20enquire%20about%20a%20cab%20booking." target="_blank" rel="noopener">💬 WhatsApp Booking</a></div>
<div class="map-wrap"><iframe title="Map — SIDCUL, Haridwar" src="https://www.google.com/maps?q=SIDCUL,+Haridwar,+Uttarakhand&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
</div>
<div class="reveal"><div class="booking-card"><h2>Booking Enquiry Form</h2><p class="sub">Validated — sends via prefilled WhatsApp message.</p>{booking_form("contact")}</div></div>
</div></div></section>"""
page("contact.html","Contact & Booking | Shree Ji Travels SIDCUL Haridwar","Contact Shree Ji Travels, SIDCUL Haridwar. Call or WhatsApp +91 8077274970 for cab booking. Booking enquiry form with tap-to-call & map.","contact.html",contact)

# ---------------- FAQ ----------------
faqs = [("How can I book a cab?","Fill any enquiry form on this site or tap a WhatsApp button. Your trip details open pre-filled in WhatsApp — press send and we reply with fare and availability. A booking is confirmed only after we confirm it."),
("Are one-way cabs available?","Yes, you can request one-way drops from Haridwar to places like Dehradun, Rishikesh, Delhi and Chandigarh (example routes subject to confirmation). Share pickup, destination and date for a quote."),
("Can I book a round-trip taxi?","Yes. Share departure date, return date, destination, passengers and vehicle preference. We confirm the round-trip fare and vehicle directly."),
("Do you offer local Haridwar travel?","Yes — Har Ki Pauri, Mansa Devi Temple, Chandi Devi Temple and nearby Rishikesh. Sightseeing routes, waiting time and availability are confirmed before the trip."),
("Can I request an outstation cab?","Yes — for holidays, family visits, business journeys and personal trips. Share pickup, destination, travel date, return date if applicable, passengers and vehicle preference."),
("How do I enquire about a Char Dham Yatra package?","Use the Char Dham Yatra form with proposed travel dates, number of pilgrims, pickup location, preferred vehicle, trip duration if known, and special requirements. Route conditions, opening dates, road access, vehicle availability, travel duration and inclusions are confirmed before booking."),
("How are fares confirmed?","Fares depend on route, vehicle, dates, halts and season. Send your trip details on WhatsApp or call us — we share the applicable fare before the journey. No fares are charged or fixed online."),
("How do I confirm vehicle availability?","Send your date, route and passenger count. We confirm which vehicle (sedan cab or passenger van) is available and the pickup arrangement. Availability is confirmed only by the business directly.")]
faq_body = '<section class="section"><div class="container"><div class="center reveal"><span class="kicker">Help</span><h1 style="font-size:clamp(2rem,4vw,3rem)">Frequently Asked Questions</h1><p class="lead">Fares, availability, pickup arrangements and package details are confirmed directly by Shree Ji Travels on call / WhatsApp.</p></div><div class="faq-search reveal"><input id="faqSearch" type="search" placeholder="🔍 Search questions… e.g. one-way, fare, Yatra" aria-label="Search frequently asked questions"></div><p class="faq-empty" id="faqEmpty">No matching question — try “fare”, “Char Dham” or ask us on WhatsApp below.</p><div class="faq" style="margin-top:26px">'
for q,a in faqs:
    faq_body += f'<div class="faq-item reveal"><button class="faq-q" aria-expanded="false">{q}<span class="plus">+</span></button><div class="faq-a"><p>{a}</p></div></div>'
faq_body += f'</div><div class="center" style="margin-top:26px"><a class="btn btn-wa" href="{WA_LINK}" target="_blank" rel="noopener">💬 Ask on WhatsApp</a> <a class="btn btn-outline" href="contact.html">Contact Page →</a></div></div></section>'
page("faq.html","FAQ | Shree Ji Travels Haridwar — Booking, Fares & Yatra","FAQs: how to book a cab, one-way & round-trip taxi, local Haridwar travel, outstation cabs, Char Dham Yatra enquiries, fare & availability. +91 8077274970.","faq.html",faq_body)

# ---------------- PRIVACY / TERMS / 404 ----------------
page("privacy-policy.html","Privacy Policy | Shree Ji Travels","Privacy policy of Shree Ji Travels website: enquiry data shared via WhatsApp only; no online payments or accounts.","privacy-policy.html",
'<section class="section"><div class="container" style="max-width:820px"><span class="kicker">Legal</span><h1>Privacy Policy</h1><p>Shree Ji Travels, SIDCUL Haridwar, operates this website to receive cab enquiries over phone and WhatsApp.</p><h3>What we collect</h3><p>Only what you type into an enquiry form (name, pickup, destination, dates, passengers, mobile) — which <strong>you choose to send via WhatsApp</strong> to +91 8077274970. We do not operate accounts, online payments or a database on this site.</p><h3>How it is used</h3><p>Your message is used solely to respond with fare and availability and to coordinate your trip.</p><h3>Cookies &amp; analytics</h3><p>This static site sets no tracking cookies of its own. Embedded content (maps, fonts, images) may be subject to those providers\u2019 policies.</p><h3>Contact</h3><p>For privacy questions, call or WhatsApp us at +91 8077274970.</p></div></section>')
page("terms.html","Terms of Service | Shree Ji Travels","Terms of using Shree Ji Travels website and requesting cab enquiries: quotes, confirmation and conduct.","terms.html",
'<section class="section"><div class="container" style="max-width:820px"><span class="kicker">Legal</span><h1>Terms of Service</h1><p>By using this website or sending an enquiry, you agree to the following.</p><h3>Enquiries, not automatic bookings</h3><p>Forms open WhatsApp with a pre-filled message. A trip is booked only after Shree Ji Travels confirms fare, vehicle and pickup directly.</p><h3>Fares &amp; availability</h3><p>All fares, routes, waiting time, vehicle allocation and Yatra details are quoted and confirmed by the business per trip. Example routes and illustrative itineraries are not guarantees.</p><h3>Conduct</h3><p>Please share accurate pickup details, passenger counts and contact numbers so we can coordinate smoothly.</p><h3>Contact</h3><p>SIDCUL, Haridwar, Uttarakhand • +91 8077274970.</p></div></section>')
page("404.html","Page Not Found | Shree Ji Travels","The page you requested could not be found. Return to Shree Ji Travels home or book on WhatsApp.","index.html",
f'<section class="nf"><div class="container"><span class="kicker">404</span><h1>Destination not found</h1><p class="lead" style="margin:0 auto 22px">The road you took doesn\u2019t exist — but Haridwar\u2019s finest journeys do. Let\u2019s get you back on route.</p><div class="cta-btns"><a class="btn btn-primary" href="index.html">← Back to Home</a><a class="btn btn-wa" href="{WA_LINK}" target="_blank" rel="noopener">💬 WhatsApp Us</a></div></div></section>')

# sitemap + robots
open(os.path.join(BASE,"sitemap.xml"),"w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>/{p}</loc></url>" for p in ["index.html","about.html","one-way-cab.html","round-trip-cab.html","local-cab.html","outstation-cab.html","char-dham-yatra.html","gallery.html","contact.html","faq.html"]) + "</urlset>")
open(os.path.join(BASE,"robots.txt"),"w").write("User-agent: *\nAllow: /\nSitemap: /sitemap.xml\n")
print("done")
