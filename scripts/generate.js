// scripts/generate.js
const fs = require("fs");
const path = require("path");

// --- CONFIG ---
const DATA_DIR = path.join(__dirname, "..", "data");
const TEMPLATES_DIR = path.join(__dirname, "..", "templates");
const DIST_DIR = path.join(__dirname, "..", "dist");

const KEYWORDS_FILE = "keywords.csv";
const TEMPLATE_FILE = "page.html";

// --- AFFILIATE LINKS ---
const AFFILIATES = {
  booking: (city) => `https://www.booking.com/searchresults.html?ss=${city}&aid=8132800`,
};

// --- HELPERS ---
function slugify(str) {
  return str
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
}

function ensureDir(dir) {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
}

// --- 3000+ WORD CONTENT BUILDER ---
function generateContent(topic, city, subtopic) {
  const themes = [
    `Why stay in {{CITY}} for {{TOPIC}} travelers`,
    `Best neighborhoods for {{SUBTOPIC}} in {{CITY}}`,
    `How to find {{TOPIC}} hotels in {{CITY}} under good prices`,
    `Booking strategies for last‑minute {{SUBTOPIC}} stays`,
    `Family, business, and solo tips for {{CITY}}`,
  ];

  const paragraphs = [];

  for (let i = 0; i < 30; i++) {
    const theme = themes[i % themes.length];

    const para = `
{{THEME}}: In {{CITY}}, the key is choosing the right area and hotel type.
For {{SUBTOPIC}}, focus on central districts with easy access to public transport and attractions.
Always compare prices across networks, check recent reviews, and read the description.
Use filters for guest rating, breakfast included, and free cancellation.
Consider the time of year, local events, and airport proximity.
Early bookings often secure better rates, while last‑minute deals can surprise you.
National holidays and festivals can double prices; plan ahead or accept higher costs.
For business trips, prioritize location, WiFi quality, and quiet rooms.
For families, look for spacious rooms, child‑friendly policies, and nearby parks or attractions.
If you’re arriving late or leaving early, confirm check‑in and check‑out rules and ask about baggage storage.
Finally, trust your instincts; if a deal looks too good to be true, double‑check photos and reviews.
    `.trim();

    paragraphs.push(
      para
        .replace(/\{\{THEME\}\}/g, theme)
        .replace(/\{\{TOPIC\}\}/g, topic)
        .replace(/\{\{SUBTOPIC\}\}/g, subtopic)
        .replace(/\{\{CITY\}\}/g, city)
    );
  }

  return paragraphs.join(" ");
}

// --- TEMPLATE LOADER ---
function loadTemplate() {
  const templatePath = path.join(TEMPLATES_DIR, TEMPLATE_FILE);
  return fs.readFileSync(templatePath, "utf8");
}

function generatePageHtml(template, row) {
  const city = row.city;
  const keyword = row.keyword;
  const topic = row.topic;
  const subtopic = row.subtopic;

  const content = generateContent(topic, city, subtopic);
  const booking = AFFILIATES.booking(encodeURIComponent(city));
  const link = `<a href="${booking}" class="btn">Check Hotels in ${city}</a>`;

  return template
    .replace(/\{\{KEYWORD\}\}/g, keyword)
    .replace(/\{\{CITY\}\}/g, city)
    .replace(/\{\{CONTENT_3000_WORDS\}\}/g, content)
    .replace(/\{\{BOOKING_COM_LINK\}\}/g, booking)
    .replace(/\{\{AFFILIATE_WIDGET\}\}/g, link);
}

// --- CSV READER ---
function readKeywords() {
  const data = fs.readFileSync(path.join(DATA_DIR, KEYWORDS_FILE));
  const lines = data.toString().split("\n").map(line => line.trim());
  if (lines.length < 2) throw new Error("Empty or invalid CSV");

  const headers = lines[0].split(",").map(h => h.trim());
  return lines.slice(1).filter(line => line).map(line => {
    const values = line.split(",").map(v => v.trim());
    const row = {};
    headers.forEach((h, i) => {
      row[h] = values[i] || "";
    });
    return row;
  });
}

// --- MAIN ---
function run() {
  console.log("Starting 3000‑word page generator...");
  ensureDir(DATA_DIR);
  ensureDir(TEMPLATES_DIR);
  ensureDir(DIST_DIR);

  const rows = readKeywords();
  console.log(`Generating ${rows.length} pages (each ~3000+ words)...`);

  rows.forEach((row, i) => {
    const slug = slugify(row.keyword);
    const pageDir = path.join(DIST_DIR, "slugs", slug);
    const indexPath = path.join(pageDir, "index.html");

    ensureDir(pageDir);

    const html = generatePageHtml(loadTemplate(), row);
    fs.writeFileSync(indexPath, html, "utf8");

    if (i % 10 === 0) process.stdout.write(`.`);
  });

  console.log("\n✅ Pages written to /dist/ (ready for GitHub Pages).");
}

run();
