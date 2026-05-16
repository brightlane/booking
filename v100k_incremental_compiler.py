import os
import glob
import urllib.parse
from datetime import datetime

# ==========================================
# 1. ENTERPRISE SYSTEM CONFIGURATION
# ==========================================
BASE_URL = "https://brightlane.github.io/booking/matrix-router.html"
SITEMAP_LIMIT = 45000  # Strict crawl threshold ceiling for optimal indexing
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")

# Unique runtime hash identifier to isolate this run's files from older runs
RUN_TIMESTAMP = datetime.now().strftime("%Y%m%d-%H%M")

# 100 Target ISO Language Codes
LANGUAGES_100 = [
    "en", "es", "fr", "de", "it", "pt", "nl", "pl", "sv", "da",
    "no", "fi", "ru", "zh", "ja", "ko", "ar", "tr", "he", "el",
    "cs", "hu", "ro", "bg", "sk", "sl", "hr", "sr", "uk", "et",
    "lv", "lt", "th", "vi", "id", "ms", "hi", "bn", "ta", "te",
    "mr", "gu", "kn", "ml", "pa", "ur", "fa", "az", "ka", "hy",
    "be", "kk", "uz", "tk", "ky", "tg", "mn", "ms", "fil", "is",
    "ga", "cy", "gd", "kw", "br", "co", "fy", "lb", "af", "zu",
    "xh", "st", "tn", "sw", "yo", "ig", "ha", "am", "ti", "so",
    "om", "mg", "ln", "kg", "bi", "ch", "fj", "sm", "to", "mi",
    "haw", "my", "km", "lo", "ne", "si", "dz", "bo", "sq", "mk"
]

# 150 High-Density Global Travel Destinations
GLOBAL_CITIES = [
    "london", "paris", "berlin", "madrid", "rome", "amsterdam", "barcelona", "vienna", "lisbon", "munich",
    "milan", "dublin", "manchester", "lyon", "marseille", "seville", "valencia", "florence", "venice", "bologna",
    "porto", "birmingham", "edinburgh", "glasgow", "liverpool", "bristol", "leeds", "nice", "toulouse", "bordeaux",
    "frankfurt", "hamburg", "stuttgart", "cologne", "dusseldorf", "malaga", "alicante", "ibiza", "mallorca", "naples",
    "turin", "palermo", "genoa", "pisa", "brussels", "antwerp", "bruges", "geneva", "zurich", "basel",
    "copenhagen", "oslo", "stockholm", "helsinki", "reykjavik", "warsaw", "krakow", "prague", "budapest", "bucharest",
    "new-york", "los-angeles", "chicago", "houston", "phoenix", "philadelphia", "san-antonio", "san-diego", "dallas", "san-jose",
    "austin", "jacksonville", "fort-worth", "columbus", "san-francisco", "charlotte", "indianapolis", "seattle", "denver", "washington",
    "boston", "el-paso", "nashville", "detroit", "las-vegas", "portland", "memphis", "oklahoma-city", "louisville", "baltimore",
    "milwaukee", "albuquerque", "tucson", "fresno", "sacramento", "mesa", "atlanta", "kansas-city", "colorado-springs", "miami",
    "raleigh", "omaha", "long-beach", "virginia-beach", "oakland", "minneapolis", "tulsa", "arlington", "tampa", "new-orleans",
    "toronto", "vancouver", "montreal", "calgary", "ottawa", "edmonton", "quebec-city", "winnipeg", "cancun", "mexico-city",
    "tokyo", "osaka", "kyoto", "seoul", "busan", "bangkok", "phuket", "pattaya", "singapore", "kuala-lumpur",
    "jakarta", "bali", "manila", "ho-chi-minh", "hanoi", "mumbai", "delhi", "bangalore", "hyderabad", "chennai",
    "kolkata", "dubai", "abu-dhabi", "doha", "riyadh", "jeddah", "tel-aviv", "jerusalem", "istanbul", "antalya",
    "sydney", "melbourne", "brisbane", "perth", "adelaide", "auckland", "wellington", "christchurch", "hong-kong", "shanghai",
    "sao-paulo", "rio-de-janeiro", "buenos-aires", "lima", "bogota", "santiago", "caracas", "quito", "medellin", "cali",
    "johannesburg", "cape-town", "durban", "nairobi", "cairo", "alexandria", "casablanca", "marrakech", "tunis", "lagos"
]

# 20 Niche Intent Modifiers
INTENT_MODIFIERS = [
    "reservations", "allocations", "wholesale-rates", "direct-deals", "premium-tier", 
    "hidden-inventory", "exclusive-discounts", "last-minute-lock", "business-travel", "holiday-rentals", 
    "corporate-rates", "verified-properties", "top-rated-lodging", "discount-vouchers", "secret-deals",
    "member-rates", "flash-sale", "early-bird", "weekend-specials", "low-latency-booking"
]

# 35 Architectural Property Style Modifiers (Pushes each language block straight past 100,000 unique layers)
PROPERTY_STYLES = [
    "hotels", "suites", "rooms", "accommodation", "stay", "boutique-stay", "luxury-suites", "budget-rooms",
    "motel-deals", "resort-booking", "apartments-online", "lodging", "penthouses", "villas", "hostels",
    "cabins", "inns", "guesthouses", "studios", "lofts", "flats", "rentals", "beach-houses",
    "manors", "estates", "cottages", "chalets", "bungalows", "b-and-b", "lodges", "quarters",
    "hideaways", "residences", "habitats", "sanctuaries", "pavilions", "apart-hotels", "eco-lodges"
]

# ==========================================
# 2. RUNTIME GENERATION PIPELINE
# ==========================================
def run_v100k_incremental_compiler():
    print("="*80)
    print("🤖 INITIALIZING VULTURE 100K MAX-SCALE INCREMENTAL COMPILER")
    print(f"• Target Batch Runtime Stamp: {RUN_TIMESTAMP}")
    print("="*80)
    
    # Structural Combinatorial Calculations
    urls_per_language = len(GLOBAL_CITIES) * len(INTENT_MODIFIERS) * len(PROPERTY_STYLES)
    projected_total_urls = urls_per_language * len(LANGUAGES_100)
    
    print(f"• Languages Stacked: {len(LANGUAGES_100)}")
    print(f"• Target Metric Verified: {urls_per_language:,} URLs calculated per language node")
    print(f"• Matrix Network Volume for Current Run: {projected_total_urls:,} global URLs")
    print("-"*80)

    current_url_buffer = []
    sitemap_index_tracker = 1
    running_url_total = 0

    # 4-Dimensional Array Processing Loop
    for lang in LANGUAGES_100:
        for city in GLOBAL_CITIES:
            for mod in INTENT_MODIFIERS:
                for style in PROPERTY_STYLES:
                    # Compile systemic semantic pattern structures
                    keyword_phrase = f"{city}-{style}-{mod}"
                    url_safe_slug = urllib.parse.quote(keyword_phrase)
                    
                    # Format dynamic routing request targeting the main hub
                    parameterized_url = f"{BASE_URL}?lang={lang}&amp;q={url_safe_slug}"
                    current_url_buffer.append(parameterized_url)
                    running_url_total += 1

                    # Write buffer array down to a node segment when hitting maximum load limits
                    if len(current_url_buffer) >= SITEMAP_LIMIT:
                        map_filename = f"sitemap-v10k-node-{RUN_TIMESTAMP}-{sitemap_index_tracker}.xml"
                        commit_buffer_to_xml(map_filename, current_url_buffer)
                        sitemap_index_tracker += 1
                        current_url_buffer = []

    # Clear remaining URLs sitting inside the active pipeline buffer
    if current_url_buffer:
        map_filename = f"sitemap-v10k-node-{RUN_TIMESTAMP}-{sitemap_index_tracker}.xml"
        commit_buffer_to_xml(map_filename, current_url_buffer)

    # Re-compile global manifest index to bridge prior runs with new ones
    compile_master_registry_index()
    
    print("\n" + "="*80)
    print("🚀 BATCH COMPILED SUCCESSFULLY - TARGET CRITERIA REALIZED")
    print(f"  » URLs Mapped in This Single Run: {running_url_total:,}")
    print(f"  » Prior Sitemaps Intact and Maintained.")
    print(f"  » Next Step: Deploy files and point webmaster panels to 'sitemap-index.xml'")
    print("="*80)

# ==========================================
# 3. FILE SYSTEM OUTPUT CONTROLLERS
# ==========================================
def commit_buffer_to_xml(filename, url_set):
    """Writes standard web architecture sitemap XML tracking sheets to disk."""
    xml_header = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]
    
    for link in url_set:
        xml_header.append("  <url>")
        xml_header.append(f"    <loc>{link}</loc>")
        xml_header.append(f"    <lastmod>{CURRENT_DATE}</lastmod>")
        xml_header.append("    <changefreq>daily</changefreq>")
        xml_header.append("    <priority>0.6</priority>")
        xml_header.append("  </url>")
        
    xml_header.append('</urlset>')
    
    with open(filename, "w", encoding="utf-8") as file_stream:
        file_stream.write("\n".join(xml_header))
    print(f" ✓ Node written: {filename} ({len(url_set):,} URLs mapping to grid)")

def compile_master_registry_index():
    """Scans folder for ALL historical and current nodes and maps them into one index."""
    filename = "sitemap-index.xml"
    
    # Isolate root directory string from the core routing configuration path
    base_directory_path = BASE_URL.replace("matrix-router.html", "")
    
    # Capture absolutely every node file present in the workspace directory
    all_active_sitemaps = sorted(glob.glob("sitemap-v10k-node-*.xml"))
    
    index_markup = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]
    
    for sitemap_file in all_active_sitemaps:
        index_markup.append("  <sitemap>")
        index_markup.append(f"    <loc>{base_directory_path}{sitemap_file}</loc>")
        index_markup.append(f"    <lastmod>{CURRENT_DATE}</lastmod>")
        index_markup.append("  </sitemap>")
        
    index_markup.append('</sitemapindex>')
    
    with open(filename, "w", encoding="utf-8") as file_stream:
        file_stream.write("\n".join(index_markup))
    print(f"\n ✓ Master Crawl Registry Verified. Monitoring {len(all_active_sitemaps)} total node clusters.")

if __name__ == "__main__":
    run_v100k_incremental_compiler()
