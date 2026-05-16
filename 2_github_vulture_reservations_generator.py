import os
import urllib.parse
from datetime import datetime

# Master Configuration (Targets your active booking repository)
BASE_URL = "https://brightlane.github.io/booking/"
OUTPUT_DIR = "."
SITEMAP_LIMIT = 40000 

# High-Intent Geography Targets
CITIES = [
    "New York", "Los Angeles", "London", "Paris", "Tokyo", "Miami", "Las Vegas", 
    "Barcelona", "Rome", "Sydney", "Toronto", "Vancouver", "Orlando", "Chicago"
]

# Core Asset Targets
PROPERTIES = [
    "Luxury Resort", "Boutique Hotel", "Five Star Suites", "Plaza Hotel",
    "Grand Central Inn", "Waterfront Resort", "Stadium View Hotel", "Convention Center Hotel",
    "Elite Tier Resort", "Skyline Suites", "Downtown Hub Hotel", "Airport Express Inn"
]

# HIGH-INTENT KEYWORDS: Explicitly engineered to catch users with credit cards out
BUYER_PHRASES = [
    "Reservations At",
    "Hotel Reservations",
    "Book A Room At",
    "Room Booking Available",
    "Direct Reservations Only",
    "Check Availability At",
    "Secure Room Booking",
    "Discount Reservations Only"
]

def build_reservation_matrix():
    print("💰 Creating separate high-intent transactional reservation matrix...")
    generated_targets = set()
    
    # Cross-multiply lists to create targeted booking searches
    for city in CITIES:
        for prop in PROPERTIES:
            for phrase in BUYER_PHRASES:
                # Variant 1: "Reservations At Miami Luxury Resort"
                generated_targets.add(f"{phrase} {city} {prop}")
                # Variant 2: "London Boutique Hotel Hotel Reservations"
                generated_targets.add(f"{city} {prop} {phrase}")
                # Variant 3: "Book A Room At The Skyline Suites Tokyo"
                generated_targets.add(f"{phrase} The {prop} {city}")

    # Fallback padding system to scale index metrics to target limits safely
    counter = 1
    while len(generated_targets) < 100000:
        city_seed = CITIES[counter % len(CITIES)]
        prop_seed = PROPERTIES[(counter * 3) % len(PROPERTIES)]
        phrase_seed = BUYER_PHRASES[(counter * 7) % len(BUYER_PHRASES)]
        
        generated_targets.add(f"Secure Online {phrase_seed} {city_seed} {prop_seed} Node {counter}")
        counter += 1

    return list(generated_targets)[:100000]

def write_reservation_sitemaps(targets):
    print(f"📦 Matrix compiled with {len(targets)} booking keys. Writing configuration chunks...")
    current_date = datetime.utcnow().strftime('%Y-%m-%d')
    sitemap_files = []
    
    # Split the massive layout array into manageable index slices
    chunks = [targets[i:i + SITEMAP_LIMIT] for i in range(0, len(targets), SITEMAP_LIMIT)]
    
    for index, chunk in enumerate(chunks):
        # We name these differently so they do NOT overwrite your first script's sitemaps!
        filename = f"sitemap-reservations-{index + 1}.xml"
        sitemap_files.append(filename)
        
        xml_lines = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        ]
        
        # Add root index reference logic to chunk 1
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
        print(f"   ↳ Written: {filename} ({len(chunk)} commercial nodes compiled)")

    # Generate a dedicated Master Index File for the Reservations system
    print("🗂️ Assembling main reservations sitemap index file...")
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
    
    # We save this as sitemap-reservations.xml to keep it entirely separate
    with open(os.path.join(OUTPUT_DIR, "sitemap-reservations.xml"), 'w', encoding='utf-8') as f:
        f.write('\n'.join(index_xml))
        
    print("✅ Complete: sitemap-reservations.xml built successfully.")

if __name__ == "__main__":
    matrix_data = build_reservation_matrix()
    write_reservation_sitemaps(matrix_data)
