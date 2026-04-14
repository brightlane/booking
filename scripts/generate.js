// scripts/generate.js - uses your Booking.com affiliate links

const fs = require("fs");
const path = require("path");

// 🌐 YOUR AFFILIATE LINKS (aid=8132800 used everywhere)
const links = {
  home:          "https://www.booking.com/index.html?aid=8132800",
  apartments:    "https://www.booking.com/apartments/index.html?aid=8132800",
  resorts:       "https://www.booking.com/resorts/index.html?aid=8132800",
  villas:        "https://www.booking.com/villas/index.html?aid=8132800",
  "b&b":         "https://www.booking.com/bed-and-breakfast/index.html?aid=8132800",
  guesthouse:    "https://www.booking.com/guest-house/index.html?aid=8132800",
};

// Basic HTML layout
function layout(title, content) {
  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>${title}</title>
  <meta name="description" content="Hotel, apartment, resort, villa, B&B, and guesthouse guide with Booking.com links.">
</head>
<body>
  <main>
    <h1>${title}</h1>
    ${content}
  </main>
</body>
</html>`;
}

// Generate main index page with your Booking.com home link
function generateIndex() {
  const html = layout(
    "HotelHub",
    `
    <p>
      Find hotels, apartments, resorts, villas, B&Bs, and guesthouses worldwide.
    </p>
    <ul>
      <li><a href="${links.home}" target="_blank" rel="noopener">Hotels</a></li>
      <li><a href="${links.apartments}" target="_blank" rel="noopener">Apartments</a></li>
      <li><a href="${links.resorts}" target="_blank" rel="noopener">Resorts</a></li>
      <li><a href="${links.villas}" target="_blank" rel="noopener">Villas</a></li>
      <li><a href="${links["b&b"]}" target="_blank" rel="noopener">Bed & Breakfasts</a></li>
      <li><a href="${links.guesthouse}" target="_blank" rel="noopener">Guesthouses</a></li>
    </ul>`
  );

  const outFile = path.join("dist", "index.html");
  fs.mkdirSync(path.dirname(outFile), { recursive: true });
  fs.writeFileSync(outFile, html, "utf-8");
  console.log("✅ Generated main index:", outFile);
}

// Generate a city page for a category (e.g., apartment, resort)
function generateCityPage(city, category, bookingLink) {
  const label = category.charAt(0).toUpperCase() + category.slice(1);
  const html = layout(
    `${label} in ${city}`,
    `
    <p>Explore ${label}s in ${city} on Booking.com.</p>
    <p>
      <a href="${bookingLink}" target="_blank" rel="noopener">
        See ${label}s in ${city} on Booking.com
      </a>
    </p>`
  );

  const dir = path.join("dist", category);
  const file = path.join(dir, city.toLowerCase().replace(/ /g, "-") + ".html");
  fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(file, html, "utf-8");
  console.log("✅ Generated:", file);
}

// Example cities list (change this later if you want)
const cities = ["Alice Springs", "Sydney", "Melbourne", "Brisbane", "Perth"];

// Generate all pages
function run() {
  // Main page
  generateIndex();

  // Apartments in each city
  cities.forEach((city) => {
    generateCityPage(city, "apartment", links.apartments);
  });

  // Resorts in each city
  cities.forEach((city) => {
    generateCityPage(city, "resort", links.resorts);
  });

  // Villas in each city
  cities.forEach((city) => {
    generateCityPage(city, "villa", links.villas);
  });

  // B&Bs in each city
  cities.forEach((city) => {
    generateCityPage(city, "bedbreakfast", links["b&b"]);
  });

  // Guesthouses in each city
  cities.forEach((city) => {
    generateCityPage(city, "guesthouse", links.guesthouse);
  });
}

// Run generator
run();
