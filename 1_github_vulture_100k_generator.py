import os
import urllib.parse
from datetime import datetime

# Master GitHub Pages Repository Configuration (Updated to match brightlane/booking)
BASE_URL = "https://brightlane.github.io/booking/"
OUTPUT_DIR = "."
SITEMAP_LIMIT = 40000  # Standard search console safe ceiling per index file

# Base Core Arrays Cross-Multiplied to reach 100,000 unique variations
CITIES = [
    "New York", "Los Angeles", "London", "Paris", "Tokyo", "Miami", "Las Vegas", 
    "Barcelona", "Rome", "Sydney", "Toronto", "Vancouver", "Mexico City", "Guadalajara",
    "Monterrey", "Dallas", "Houston", "Atlanta", "Boston", "Chicago", "Seattle", 
    "San Francisco", "Austin", "Denver", "Phoenix", "Philadelphia", "Orlando", "Nashville"
]

STADIUMS_VENUES = [
    "MetLife Stadium Area", "SoFi Stadium Suites", "Hard Rock Stadium Hub", "ATandT Stadium Zone", 
    "Wembley Stadium District", "Mercedes Benz Stadium Arena", "Allegiant Stadium Strips",
    "Estadio Azteca Core", "BC Place Accommodations", "Lumen Field Quarters", "Arrowhead Hub",
    "Gillette Stadium Stays", "Levi Stadium District", "Lincoln Financial Field Allocations"
]

HOTEL_MODIFIERS = [
    "Luxury Resort Allocations", "Premium Boutique Stays", "Genius Tier Elite Stays", 
    "Mobile Only Inventory Hidden Deals", "Last Minute Room Lock", "Five Star Suite Sniper",
    "Business Class Accommodations", "Budget Friendly Modern Rooms", "Extended Stay Suites",
    "Downtown Penthouse Inventory", "Waterfront View Allocations", "Airport Transit Rooms"
]

def build_100k_matrix():
    print("⚡ Starting Vulture 100K GitHub Cross-Multiplication Engine...")
    generated_targets = set()
    
    # Cross-multiply basic permutations to create dynamic search queries
    for city in CITIES:
        for venue in STADIUMS_VENUES:
            for modifier in HOTEL_MODIFIERS:
                generated_targets.add(f"{venue} {city} {modifier}")
                generated_targets.add(f"{city} {modifier} Near {venue}")
                generated_targets.add(f"{modifier} at {venue} {city}")

    # Programmatic padding block to guarantee exactly 100,000 clean target outputs
    counter = 1
    while len(generated_targets) < 100000:
        city_seed = CITIES[counter % len(CITIES)]
        venue_seed = STADIUMS_VENUES[(counter * 3) % len(STADIUMS_VENUES)]
        modifier_seed = HOTEL_MODIFIERS[(counter * 7) % len(HOTEL_MODIFIERS)]
        
        generated_targets.add(f"Variant Allocation {counter} {modifier_seed} {city_seed} {venue_seed}")
        counter += 1

    return list(generated_targets)[:100000]

def write_sitemaps(targets):
    print(f"📦 Matrix compiled with {len(targets)} parameters. Generating sitemaps...")
    current_date = datetime.utcnow().strftime('%Y-%m-%d')
    sitemap_files = []
    
    # Split the 100,000 links into clean chunks
    chunks = [targets[i:i + SITEMAP_LIMIT] for i in range(0, len(targets), SITEMAP_LIMIT)]
    
    for index, chunk in enumerate(chunks):
        filename = f"sitemap-matrix-{index + 1}.xml"
        sitemap_files.append(filename)
        
        xml_lines = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        ]
        
        if index == 0:
            xml_lines.append('  <url>')
            xml_lines.append(f'    <loc>{BASE_URL}</loc>')
            xml_lines.append(f'    <lastmod>{current_date}</lastmod>')
            xml_lines.append('    <changefreq>always</changefreq>')
            xml_lines.append('    <priority>1.0</priority>')
            xml_lines.append('  </url>')
            
        for item in chunk:
            safe_query = urllib.parse.quote_plus(item)
            full_url = f"{BASE_URL}?ss={safe_query}"
            
            xml_lines.append('  <url>')
            xml_lines.append(f'    <loc>{full_url}</loc>')
            xml_lines.append(f'    <lastmod>{current_date}</lastmod>')
            xml_lines.append('    <changefreq>weekly</changefreq>')
            xml_lines.append('    <priority>0.8</priority>')
            xml_lines.append('  </url>')
            
        xml_lines.append('</urlset>')
        
        with open(os.path.join(OUTPUT_DIR, filename), 'w', encoding='utf-8') as f:
            f.write('\n'.join(xml_lines))
        print(f"   ↳ Written: {filename} ({len(chunk)} target nodes)")

    # Generate Master Sitemap Index File (sitemap.xml)
    print("🗂️ Assembling main sitemap index anchor file...")
    index_xml = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]
    
    for sitemap in sitemap_files:
        index_xml.append('  <sitemap>')
        index_xml.append(f'    <loc>{BASE_URL}{sitemap}</loc>')
        index_xml.append(f'    <lastmod>{current_date}</lastmod>')
        index_xml.append('  </sitemap>')
        
    index_xml.append('</sitemapindex>')
    
    with open(os.path.join(OUTPUT_DIR, "sitemap.xml"), 'w', encoding='utf-8') as f:
        f.write('\n'.join(index_xml))
        
    print("✅ Success: sitemap.xml index master initialized completely.")

if __name__ == "__main__":
    matrix_data = build_100k_matrix()
    write_sitemaps(matrix_data)
