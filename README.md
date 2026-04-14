# HotelHub Website

HotelHub is a static information site for travelers and hospitality professionals.

## Overview

This repository contains a static website served via GitHub Pages. It provides:

- Descriptive pages about hotels and travel in selected cities.  
- Basic navigation, styling, and layout to support readability.  
- Standard SEO‑friendly structure (semantic HTML, `robots.txt`, `sitemap.xml`).

The site is not a booking platform; it only links out to established travel services for actual reservations.

## Core files

- `index.html` – main landing page  
- `legal.html` – legal and compliance page  
- `robots.txt` – search‑engine instructions  
- `sitemap.xml` – XML sitemap for indexing  
- `404.html` – custom error page  
- Various HTML pages under the generated sections (for example, city‑specific guides)  
- CSS‑style design embedded in the templates to maintain a consistent dark‑blue theme

All content is produced manually and reviewed for quality and structure. No external automation systems are directly exposed in this repository.

## How to run locally

1. Clone the repo:

   ```bash
   git clone https://github.com/your-username/hotel-mega-site.git
   cd hotel-mega-site
   ```

2. Serve the site with a local static‑server (example):

   ```bash
   npx serve
   ```

Open `index.html` in the browser to view the site locally.

## How to deploy

This project is hosted with GitHub Pages:

- The `main` branch serves as the publishing source.  
- The site is updated whenever new HTML or assets are committed.

## License

This repository is provided for educational and reference purposes. It is not a commercial booking service. The content and design are intended for learning and experimentation.
