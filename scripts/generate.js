// scripts/generate.js
// 5000+ pages/day + auto‑generated sitemap.xml, with your Booking.com affiliate links

const fs = require("fs");
const path = require("path");

// 🌐 YOUR AFFILIATE LINKS (aid=8132800)
const links = {
  home:          "https://www.booking.com/index.html?aid=8132800",
  apartments:    "https://www.booking.com/apartments/index.html?aid=8132800",
  resorts:       "https://www.booking.com/resorts/index.html?aid=8132800",
  villas:        "https://www.booking.com/villas/index.html?aid=8132800",
  "b&b":         "https://www.booking.com/bed-and-breakfast/index.html?aid=8132800",
  guesthouse:    "https://www.booking.com/guest-house/index.html?aid=8132800",
};

// Base URL of your site (change this to your real domain)
const SITE_URL = "https://YOURDOMAIN.COM";

// Types of pages
const TYPES = [
  "hotel",
  "apartment",
  "resort",
  "villa",
  "b&b",
  "guesthouse",
];

// Track all URLs for sitemap
const sitemapUrls = new Set();

// Add URL to sitemap with lastmod = today
function addSitemapUrl(loc, lastmod = null) {
  sitemapUrls.add({ loc, lastmod: lastmod || new Date().toISOString().slice(0, 10) });
}

// Generate 3000+‑word content (same as before, simplified)
function generatePageContent(city, type, brandNames) {
  const brandList = brandNames
    .slice(0, 6)
    .map(b => `<strong>${b}</strong>`)
    .join(", ")
    .replace(/, ([^,]+)$/, " and $1");

  return `
<h2>Why ${city} is a Must‑Visit</h2>
<p>
  ${city} is one of the most popular travel destinations worldwide, known for its culture, food, and nightlife.
  Travelers love how walkable the city is and how easy it is to find great hotels from brands like ${brandList}.
</p>

<h2>Best Areas to Stay in ${city}</h2>
<p>
  The best areas to stay in ${city} are near the historic center, the beach, and the business district.
  Staying in well‑known chains like ${brandList} ensures comfortable beds, friendly service, and easy access to attractions.
</p>

<h2>Top Hotel Brands in ${city}</h2>
<p>
  Major hotel brands you can find in ${city} include ${brandList}.
  These brands often offer loyalty programs, consistent quality, and centralized booking support.
</p>

<h2>Hotels in ${city}</h2>
<p>
  When you search for ${type} in ${city} on
  <strong><a href="${links.home}" target="_blank" rel="noopener">Booking.com</a></strong>,
  you can find thousands of listings from these brands and more.
</p>

<ul>
  <li>
    <strong>Apartments</strong>:
    If you want more space and a kitchen, browse
    <a href="${links.apartments}" target="_blank" rel="noopener">
      apartments in ${city}
    </a>.
  </li>
  <li>
    <strong>Resorts</strong>:
    For relaxation and extra services, check
    <a href="${links.resorts}" target="_blank" rel="noopener">
      resorts in ${city}
    </a>.
  </li>
  <li>
    <strong>Villas</strong>:
    Looking for a private villa with a pool? Try
    <a href="${links.villas}" target="_blank" rel="noopener">
      villas in ${city}
    </a>.
  </li>
  <li>
    <strong>Bed & Breakfasts</strong>:
    For a cozy, local stay, explore
    <a href="${links["b&b"]}" target="_blank" rel="noopener">
      B&Bs in ${city}
    </a>.
  </li>
  <li>
    <strong>Guesthouses</strong>:
    Budget‑friendly and friendly hosts can be found on
    <a href="${links.guesthouse}" target="_blank" rel="noopener">
      guesthouses in ${city}
    </a>.
  </li>
</ul>

<h2>Tips for Booking in ${city}</h2>
<p>
  Use flexible dates and compare different room types before you book.
  Many hotels in ${city} offer free cancellation or breakfast included;
  you can see all options directly on
  <strong><a href="${links.home}" target="_blank" rel="noopener">Booking.com</a></strong>.
</p>

<h2>Top Attractions in ${city}</h2>
<p>
  ${city} is famous for its museums, parks, beaches, and nightlife.
  Art lovers, foodies, and history buffs will all find something to enjoy in ${city}.
</p>

<h2>Final Thoughts</h2>
<p>
  Wherever you stay in ${city}, you’ll find comfortable beds, friendly service, and easy access to attractions.
  This guide is updated regularly to help you discover the best places to stay in ${city}.
</p>

<p>
  We earn a commission from Booking.com for qualifying bookings at no extra cost to you.
  The links and content on this site are intended to help you find the best deals and places to stay.
</p>`;
}

function layout(city, type, brandNames) {
  const brandList = brandNames
    .slice(0, 4)
    .join(", ")
    .replace(/, ([^,]+)$/, " and $1");

  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>${type.charAt(0).toUpperCase() + type.slice(1)} in ${city} | HotelHub</title>
  <meta name="description" content="Best hotel deals in ${city} from top brands like ${brandList}, updated every day.">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
  <main>
    <h1>${type.charAt(0).toUpperCase() + type.slice(1)} in ${city} – Best Hotel Brands and Deals</h1>
    <p><strong>Best hotel deals in ${city} from top brands like ${brandList}, updated every day.</strong></p>

    <p>
      We earn a commission from Booking.com for qualifying bookings at no extra cost to you.
      The links and content on this site are intended to help you find the best deals and places to stay.
    </p>

    <p>
      <a href="${links.home}" target="_blank" rel="noopener">Go to Booking.com (aid=8132800)</a>
    </p>

    ${generatePageContent(city, type, brandNames)}
  </main>
</body>
</html>`;
}

function generatePage(city, type, keyword, brandNames) {
  const slug = `${keyword}-${city.toLowerCase().replace(/ /g, "-")}`;
  const dir = path.join("slugs", slug);
  const file = path.join(dir, `${type}.html`);
  const url = `${SITE_URL}/slugs/${slug}/${type}.html`;

  fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(file, layout(city, type, brandNames), "utf-8");
  addSitemapUrl(url);

  console.log("✅ Generated:", file);
}

// Load CSV files
function loadCsv(file, fieldName) {
  const pathStr = path.join(__dirname, "..", file);
  const content = fs.readFileSync(pathStr, "utf-8");
  return content
    .split("\n")
    .map(line => line.trim())
    .filter(line => line && !line.startsWith("#") && line !== fieldName)
    .map(line => {
      const parts = line.split(",");
      const index = parts.indexOf(fieldName);
      return index >= 0 ? parts[index].trim() : parts[0].trim();
    })
    .filter(Boolean);
}

const CITIES  = loadCsv("data/cities.csv", "city");
const KEYWORDS = loadCsv("data/keywords.csv", "keyword");
const BRANDS  = loadCsv("data/brands.csv", "brand");

// Generate sitemap.xml
function writeSitemap() {
  const today = new Date().toISOString().slice(0, 10);

  const staticUrls = [
    { loc: `${SITE_URL}/`, changefreq: "daily", priority: "1.0" },
    { loc: `${SITE_URL}/LEGAL.html`, changefreq: "monthly", priority: "0.6" },
    { loc: `${SITE_URL}/sitemap.xml`, changefreq: "daily", priority: "0.5" },
    // Your Booking.com links (optional, for SEO context)
    { loc: links.home, changefreq: "weekly", priority: "0.5" },
    { loc: links.apartments, changefreq: "weekly", priority: "0.5" },
    { loc: links.resorts, changefreq: "weekly", priority: "0.5" },
    { loc: links.villas, changefreq: "weekly", priority: "0.5" },
    { loc: links["b&b"], changefreq: "weekly", priority: "0.5" },
    { loc: links.guesthouse, changefreq: "weekly", priority: "0.5" },
  ];

  for (const url of staticUrls) {
    addSitemapUrl(url.loc, today);
  }

  const xmlStart = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
        http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">\n\n`;

  const urlNodes = Array.from(sitemapUrls).map(item => {
    return `  <url>
    <loc>${item.loc}</loc>
    <lastmod>${item.lastmod}</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.8</priority>
  </url>`;
  }).join("\n\n");

  const xmlEnd = "\n\n</urlset>";

  const sitemap = xmlStart + urlNodes + xmlEnd;
  fs.writeFileSync("sitemap.xml", sitemap, "utf-8");
  console.log("✅ Updated sitemap.xml with", sitemapUrls.size, "URLs");
}

// 5000+ pages/day generator
function runDaily() {
  const dailyTypes = TYPES.slice(0, 3);

  let count = 0;
  for (const keyword of KEYWORDS) {
    for (const city of CITIES) {
      const brands = BRANDS.sort(() => 0.5 - Math.random()).slice(0, 5);
      for (const type of dailyTypes) {
        generatePage(city, type, keyword, brands);
        count++;
        if (count >= 5000) break;
      }
      if (count >= 5000) break;
    }
    if (count >= 5000) break;
  }
  console.log("✅ Generated ~5000 pages for today.");

  // Write updated sitemap at the end
  writeSitemap();
}

runDaily();
