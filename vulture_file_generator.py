#!/usr/bin/env python3
"""
VULTURE 10K ENGINE: Zero-Competition File Matrix Compiler
Generates paired HTML index wrappers and physical download CSV payloads.
Targeting high-intent, unsummarizable localized infrastructure datasets.
"""

import os
import csv
import re

# ----------------------------------------------------------------------
# MATRIX CONFIGURATION: Expansion Nodes
# ----------------------------------------------------------------------
TARGET_DATASET_NODES = [
    {
        "geo": "Miami FL", 
        "niche": "florist-wholesale", 
        "keyword": "Wholesale Florist Commercial Distributors",
        "records": [
            ["FL-WF-301", "Miami Flower Exchange", "Import Terminal 4", "Active Distribution", "21885"],
            ["FL-WF-302", "Biscayne Floral Logistics", "Bayfront Suite B", "Priority Broker", "21885"]
        ]
    },
    {
        "geo": "Austin TX", 
        "niche": "roofing-permit", 
        "keyword": "Residential MasterRib Steel Panel Setback Guidelines",
        "records": [
            ["TX-RP-901", "Travis Co. Structural Code Sec 4", "Charcoal MasterRib Minimums", "Zoning Clearance", "8132800"],
            ["TX-RP-902", "Austin Municipal Drainage Transition", "2-Foot Ridge Flashing Caps", "Zoning Clearance", "8132800"]
        ]
    },
    {
        "geo": "Los Angeles CA", 
        "niche": "stadium-vendor", 
        "keyword": "Stadium Perimeter Commercial Supplier Directory",
        "records": [
            ["CA-SV-501", "LA Sports Hub Catering Zone", "Gate 7 Vendor Conduit", "Compliance Verified", "8132800"],
            ["CA-SV-502", "Pacific Arena Logistics Matrix", "Loading Bay 3 Access", "Compliance Verified", "8132800"]
        ]
    }
]

# ----------------------------------------------------------------------
# THE HIGH-CONVERTING LANDING HUB TEMPLATE
# ----------------------------------------------------------------------
HTML_LAYOUT_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="robots" content="index, follow">
    <title>Download {KEYWORD} Data Sheet (.CSV) - {GEO}</title>
    <meta name="description" content="Direct system export for {KEYWORD} in {GEO}. Includes encrypted node reference verification strings for regional verification.">
    
    <!-- Modern Tailwind UI Layer -->
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    <style>
        .matrix-mesh {{ background: radial-gradient(circle at 50% 50%, #0f172a 0%, #020617 100%); }}
    </style>
</head>
<body class="matrix-mesh text-slate-100 font-sans min-h-screen flex flex-col justify-between antialiased">

    <!-- Top Infrastructure Header Bar -->
    <header class="border-b border-slate-900 w-full bg-slate-950/80 backdrop-blur-md sticky top-0 z-50">
        <div class="max-w-5xl mx-auto px-6 py-4 flex justify-between items-center">
            <div class="flex items-center space-x-2">
                <span class="bg-amber-500 text-slate-950 font-mono font-black px-2 py-0.5 rounded text-xs">V10K</span>
                <span class="font-mono text-xs font-bold tracking-tight text-slate-400">FILE_SERVER_NODE_INDEX</span>
            </div>
            <div class="text-[10px] font-mono bg-emerald-950/40 border border-emerald-900/60 text-emerald-400 px-2.5 py-1 rounded flex items-center space-x-1.5">
                <span class="h-1.5 w-1.5 rounded-full bg-emerald-400 animate-ping"></span>
                <span>DATASTREAM ANCHOR VERIFIED</span>
            </div>
        </div>
    </header>

    <!-- Main File Container Module -->
    <main class="max-w-4xl mx-auto px-4 py-16 text-center flex-grow flex flex-col justify-center">
        <span class="text-xs font-mono font-bold tracking-widest text-amber-500 uppercase">SYSTEM ASSET RECORD</span>
        <h1 class="text-3xl md:text-5xl font-black tracking-tight text-slate-200 mt-2 max-w-2xl mx-auto leading-tight">
            {KEYWORD}
        </h1>
        <p class="text-sm font-mono text-slate-400 mt-3 bg-slate-900/50 border border-slate-800/60 inline-block px-3 py-1 rounded-full mx-auto">
            📍 Target Operational Perimeter: <span class="text-slate-200 font-bold">{GEO}</span>
        </p>

        <!-- Dynamic Download Prompt Card Component -->
        <div class="mt-10 bg-slate-900/90 border border-slate-800/80 p-8 rounded-2xl max-w-md mx-auto shadow-2xl backdrop-blur-sm w-full">
            <div class="flex justify-center mb-4 text-slate-600">
                <!-- SVG Spreadsheet Icon Asset -->
                <svg class="h-12 w-12 text-amber-500/80" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z" />
                </svg>
            </div>
            <div class="text-[10px] font-mono text-slate-500 uppercase tracking-widest">Format: Structured Comma-Separated Values</div>
            <h3 class="font-bold text-slate-200 mt-1 font-mono text-sm break-all">{NICHE}_master_ledger_{CLEAN_GEO}.csv</h3>
            
            <a href="./{NICHE}_master_ledger_{CLEAN_GEO}.csv" download 
               class="mt-6 block w-full bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-400 hover:to-orange-400 text-slate-950 font-black py-4 rounded-xl transition-all shadow-lg shadow-amber-500/20 uppercase text-xs tracking-widest cursor-pointer">
                Download Raw Structured Dataset
            </a>
            
            <div class="mt-4 text-[10px] text-slate-500 leading-relaxed">
                *File contains full programmatic indices, compliance statuses, and handshake tags mapped to active distribution servers.*
            </div>
        </div>

        <!-- High-Authority Preview Window for Bot Scrapers -->
        <div class="mt-16 text-left max-w-2xl mx-auto w-full">
            <h3 class="text-xs font-mono font-bold text-slate-400 uppercase tracking-widest mb-3 flex items-center space-x-2">
                <span>📊 Top-Tier Live Records Index Preview</span>
            </h3>
            <div class="overflow-x-auto border border-slate-900 rounded-xl bg-slate-950/60 backdrop-blur-sm">
                <table class="w-full text-xs font-mono text-slate-400">
                    <thead class="bg-slate-900 text-slate-200 font-bold text-left border-b border-slate-800">
                        <tr>
                            <th class="p-3.5">Record ID</th>
                            <th class="p-3.5">Operational Node Name</th>
                            <th class="p-3.5">Validation Loop</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-900/60">
                        {PREVIEW_ROWS}
                    </tbody>
                </table>
            </div>
        </div>
    </main>

    <!-- Invisible Authority Semantic Context Block (For Advanced Search Query Crawling) -->
    <section class="max-w-4xl mx-auto px-6 py-12 opacity-25 text-xs text-left border-t border-slate-900/60 w-full">
        <h4 class="font-bold mb-1 uppercase tracking-tight text-slate-400">System Log: Data Extraction Vector For {GEO}</h4>
        <p class="mb-2 leading-relaxed">Parsing architecture maps incoming local user sessions dynamically across targeted structural coordinates. This layout forces exact data match identification parameters down to client index endpoints without using standard text wrappers.</p>
        <p>The companion file {NICHE}_master_ledger_{CLEAN_GEO}.csv maintains persistence structures for verification requirements inside the {GEO} dataset node.</p>
    </section>

    <!-- Footer Terminal Info -->
    <footer class="bg-slate-950/80 border-t border-slate-900 py-6 text-center text-[10px] font-mono text-slate-600">
        <div>Vulture File Compiler Engine v4.9.2 // Global Stay Matrix Deployment Protocols</div>
        <div class="mt-1">&copy; 2026 Database Archive Terminal Network. All Rights Reserved.</div>
    </footer>

</body>
</html>
"""

# ----------------------------------------------------------------------
# EXECUTION ENGINE LOGIC
# ----------------------------------------------------------------------
def execute_compilation():
    output_dir = "file_matrix_output"
    os.makedirs(output_dir, exist_ok=True)
    
    print("🚀 Vulture 10K System initializing file generation routine...")
    print(f"📁 Destination output path defined: ./{output_dir}/")
    print("-" * 65)

    for structure in TARGET_DATASET_NODES:
        geo_name = structure["geo"]
        niche_slug = structure["niche"]
        keyword_string = structure["keyword"]
        records_pool = structure["records"]
        
        # Format a clean filename variation for asset outputs
        clean_geo = re.sub(r'[^a-z0-9]', '_', geo_name.lower()).strip('_')
        
        # 1. Build and Compile the Associated CSV Payload File
        csv_filename = f"{niche_slug}_master_ledger_{clean_geo}.csv"
        csv_dest_path = os.path.join(output_dir, csv_filename)
        
        with open(csv_dest_path, mode='w', newline='', encoding='utf-8') as data_file:
            csv_writer = csv.writer(data_file)
            
            # Formulate structural headers with integrated handshake targets
            csv_writer.writerow([
                "System_Record_ID", 
                "Geographic_Scope", 
                "Target_Node_Context", 
                "Validation_Parameters", 
                "Network_Partner_Handshake_ID"
            ])
            
            # Loop dataset matrix metrics row by row into the file storage
            for row in records_pool:
                csv_writer.writerow([row[0], geo_name, row[1], row[2], f"TRACKING_TAG_{row[3]}"])
        
        print(f"📄 Compiled Data Payload -> {csv_filename}")

        # 2. Render HTML Preview Table Rows for Search Crawler Discovery
        table_preview_rows = ""
        for row in records_pool:
            table_preview_rows += f"""
                        <tr>
                            <td class="p-3.5 text-amber-500 font-bold">{row[0]}</td>
                            <td class="p-3.5 text-slate-300 font-semibold">{row[1]} ({row[2]})</td>
                            <td class="p-3.5"><span class="bg-emerald-950/80 text-emerald-400 border border-emerald-900 px-2 py-0.5 rounded text-[10px] font-bold">{row[3]}</span></td>
                        </tr>"""

        # 3. Inject Values into Master Layout and Save
        html_filename = f"{niche_slug}_{clean_geo}.html"
        html_dest_path = os.path.join(output_dir, html_filename)
        
        compiled_html_payload = HTML_LAYOUT_TEMPLATE.format(
            KEYWORD=keyword_string,
            GEO=geo_name,
            NICHE=niche_slug,
            CLEAN_GEO=clean_geo,
            PREVIEW_ROWS=table_preview_rows
        )
        
        with open(html_dest_path, mode='w', encoding='utf-8') as web_file:
            web_file.write(compiled_html_payload)
            
        print(f"🌐 Compiled Landing Hub  -> {html_filename}")
        print("." * 65)

    print(f"\n✅ Build complete. {len(TARGET_DATASET_NODES)} zero-competition file matrices loaded directly into the directory.")

if __name__ == "__main__":
    execute_compilation()
