#!/usr/bin/env python3
"""Build the Social Media Masters website.

Each file in src/pages/ starts with a small header block:

    ---
    title: Page title
    description: Meta description
    nav: home
    ---
    <main html...>

The script wraps every page in the shared layout (head, header, footer,
WhatsApp button) and writes the finished site to public/.

Run:  python3 build.py
"""
import pathlib
import re
import shutil

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "src" / "pages"
OUT = ROOT / "public"
SITE = "https://socialmediamasters.in"
WA_NUMBER = "919911941474"

NAV = [
    ("home", "/", "Home"),
    ("services", "/services/", "Services & Pricing"),
    ("about", "/about/", "About"),
    ("contact", "/contact/", "Contact"),
]

WA_ICON = (
    '<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M16 3C8.8 3 3 8.7 3 15.8c0 2.5.7 4.9 2 7L3 29l6.4-2c2 1.1 4.3 1.7 6.6 1.7 7.2 0 13-5.7 13-12.8S23.2 3 16 3zm0 23.4c-2.1 0-4.1-.6-5.8-1.6l-.4-.2-3.8 1.2 1.2-3.7-.3-.4c-1.2-1.8-1.8-3.8-1.8-5.9C5.1 9.9 10 5.1 16 5.1s10.9 4.8 10.9 10.7S22 26.4 16 26.4zm6-8c-.3-.2-1.9-.9-2.2-1-.3-.1-.5-.2-.7.2-.2.3-.8 1-1 1.2-.2.2-.4.2-.7.1-.3-.2-1.4-.5-2.6-1.6-1-.9-1.6-1.9-1.8-2.2-.2-.3 0-.5.1-.7l.5-.6c.2-.2.2-.4.3-.6.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.2 1.1-1.2 2.8s1.2 3.2 1.4 3.4c.2.2 2.4 3.6 5.8 5 .8.3 1.4.5 1.9.7.8.3 1.6.2 2.2.1.7-.1 1.9-.8 2.2-1.5.3-.7.3-1.4.2-1.5-.1-.2-.3-.3-.6-.4z"/></svg>'
)


def layout(meta, body, path):
    title = meta["title"]
    desc = meta["description"]
    nav_key = meta.get("nav", "")
    url = SITE + path
    links = "".join(
        f'<li><a href="{href}"{" aria-current=page" if key == nav_key else ""}>{label}</a></li>'
        for key, href, label in NAV
    )
    robots = '<meta name="robots" content="noindex">' if meta.get("noindex") else ""
    return f"""<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
{robots}
<meta name="theme-color" content="#0A1A33">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Social Media Masters">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/img/favicon-32.png">
<link rel="icon" type="image/svg+xml" href="/assets/img/icon-ring.svg">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400;1,500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"ProfessionalService","name":"Social Media Masters","url":"{SITE}","slogan":"Brands That Outlast the Feed.","telephone":"+91-99119-41474","email":"socialmediamasters.in@gmail.com","address":{{"@type":"PostalAddress","addressLocality":"Delhi","addressCountry":"IN"}},"sameAs":["https://www.instagram.com/socialmediamasters.in/"]}}</script>
</head>
<body>
<header class="site-header">
  <nav class="wrap nav" aria-label="Main">
    <a class="brand" href="/" aria-label="Social Media Masters home"><img src="/assets/img/mark-champagne.svg" alt="" width="35" height="30"><span>SOCIAL MEDIA MASTERS</span></a>
    <button class="menu-btn" aria-label="Open menu" aria-expanded="false"><span></span></button>
    <ul class="nav-links">{links}<li><a class="btn btn-gold" href="/free-audit/">Free audit</a></li></ul>
  </nav>
</header>
{body}
<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <img src="/assets/img/mark-champagne.svg" alt="Social Media Masters" width="51" height="44">
        <div class="n">SOCIAL MEDIA MASTERS</div>
        <div class="t">Brands That Outlast the Feed.</div>
      </div>
      <div>
        <h4>Pages</h4>
        <ul><li><a href="/">Home</a></li><li><a href="/services/">Services &amp; Pricing</a></li><li><a href="/about/">About</a></li><li><a href="/free-audit/">Free Audit</a></li><li><a href="/contact/">Contact</a></li></ul>
      </div>
      <div>
        <h4>Legal</h4>
        <ul><li><a href="/terms/">Terms of Service</a></li><li><a href="/privacy/">Privacy Policy</a></li></ul>
      </div>
      <div>
        <h4>Reach us</h4>
        <ul>
          <li><a href="https://wa.me/{WA_NUMBER}" target="_blank" rel="noopener">WhatsApp +91 99119 41474</a></li>
          <li><a href="https://www.instagram.com/socialmediamasters.in/" target="_blank" rel="noopener">@socialmediamasters.in</a></li>
          <li><a href="mailto:socialmediamasters.in@gmail.com">socialmediamasters.in@gmail.com</a></li>
          <li>Delhi, India</li>
        </ul>
      </div>
    </div>
    <div class="foot-bottom"><span>&copy; <span data-year>2026</span> Social Media Masters. All rights reserved.</span><span>All prices + GST.</span></div>
  </div>
</footer>
<a class="wa-float" href="https://wa.me/{WA_NUMBER}?text={'Hi%20Social%20Media%20Masters%2C%20I%27d%20like%20to%20know%20more.'}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{WA_ICON}</a>
<script src="/assets/js/main.js" defer></script>
</body>
</html>
"""


def parse(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    meta = {}
    for line in m.group(1).splitlines():
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip()
    return meta, text[m.end():]


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(ROOT / "assets", OUT / "assets")
    urls = []
    for page in sorted(SRC.glob("*.html")):
        meta, body = parse(page.read_text(encoding="utf-8"))
        slug = page.stem
        if slug == "index":
            path, dest = "/", OUT / "index.html"
        elif slug == "404":
            path, dest = "/404.html", OUT / "404.html"
        else:
            path, dest = f"/{slug}/", OUT / slug / "index.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(layout(meta, body, path), encoding="utf-8")
        if slug != "404":
            urls.append(path)
    sitemap = "".join(f"<url><loc>{SITE}{u}</loc></url>" for u in urls)
    (OUT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sitemap}</urlset>\n',
        encoding="utf-8",
    )
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
    print(f"Built {len(urls) + 1} pages into {OUT}")


if __name__ == "__main__":
    main()
