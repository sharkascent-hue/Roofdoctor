#!/usr/bin/env python3
"""Builds the Roof and Chimney Doctor site: every page shares one header, footer and set of sections.
Edit the content below, then run:  python3 build.py   (writes the .html files next to this script)."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = 'https://roofandchimneydoctor.ie'
PHONE, TEL, EMAIL = '083 121 3251', 'tel:+353831213251', 'roofandchimneydoctor@gmail.com'

# ---------- icons ----------
def svg(body, cls=''):
    c = f' class="{cls}"' if cls else ''
    return f'<svg{c} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{body}</svg>'
I = {
    'arrow': svg('<path d="M5 12h14M13 6l6 6-6 6"/>', 'arr'),
    'arrowup': svg('<path d="M7 17L17 7M8 7h9v9"/>'),
    'phone': svg('<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>'),
    'mail': svg('<rect x="2" y="4" width="20" height="16" rx="2"/><path d="M22 6l-10 7L2 6"/>'),
    'pin': svg('<path d="M12 22s-8-6.6-8-12a8 8 0 0 1 16 0c0 5.4-8 12-8 12z"/><circle cx="12" cy="10" r="3"/>'),
    'check': svg('<path d="M20 6L9 17l-5-5"/>'),
    'chev': svg('<path d="M6 9l6 6 6-6"/>'),
    'x': svg('<path d="M18 6L6 18M6 6l12 12"/>'),
    'left': svg('<path d="M15 18l-6-6 6-6"/>'),
    'right': svg('<path d="M9 18l6-6-6-6"/>'),
    'bolt': svg('<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>'),
    'shield': svg('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>'),
    'quote': svg('<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/>'),
    'star': svg('<path d="M12 2l3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/>'),
    'clock': svg('<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>'),
    'house': svg('<path d="M3 11l9-8 9 8"/><path d="M5 9.5V21h14V9.5"/><path d="M10 21v-6h4v6"/>'),
    'wrench': svg('<path d="M14.7 6.3a4 4 0 0 0 5 5L22 14l-8 8-2.3-2.3a4 4 0 0 0-5-5L2 10l8-8z" transform="scale(.9) translate(1.3 1.3)"/>'),
    'layers': svg('<path d="M12 2l10 5-10 5L2 7z"/><path d="M2 17l10 5 10-5M2 12l10 5 10-5"/>'),
    'drop': svg('<path d="M12 2.7l5.7 5.6a8 8 0 1 1-11.4 0z"/>'),
    'chimney': svg('<path d="M3 12l9-8 9 8"/><path d="M15 6.5V3h3v6"/><path d="M5 10.5V21h14V10.5"/>'),
    'gutter': svg('<path d="M3 6h18v3a3 3 0 0 1-3 3H6a3 3 0 0 1-3-3z"/><path d="M17 12v9M7 15v2M11 15v4"/>'),
    'storm': svg('<path d="M19 16.9A5 5 0 0 0 18 7h-1.3A8 8 0 1 0 4 15.3"/><path d="M13 11l-4 6h6l-4 6"/>'),
    'roof': svg('<path d="M2 12L12 3l10 9"/><path d="M6 8.5V5h3"/><path d="M5 12v9h14v-9"/>'),
    'hammer': svg('<path d="M15 12l-8.5 8.5a2.1 2.1 0 0 1-3-3L12 9"/><path d="M17.6 15L22 10.6M20.9 11.7l-4.6-4.6a3 3 0 0 0-2.1-.9h-1.8L10 4l1.8-1.8h3.5a6 6 0 0 1 4.2 1.8l2.6 2.6"/>'),
    'chat': svg('<path d="M21 11.5a8.4 8.4 0 0 1-12.3 7.4L3 21l2-5.4A8.4 8.4 0 1 1 21 11.5z"/>'),
    'search': svg('<circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/>'),
    'broom': svg('<path d="M19.4 2.6l-7.8 7.8"/><path d="M11 9l4 4-3.5 8.5L3 13z"/><path d="M7 17l-2 2"/>'),
    'fb': svg('<path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>'),
}
WA = '<svg viewBox="0 0 32 32" fill="currentColor" aria-hidden="true"><path d="M16 3a13 13 0 0 0-11.2 19.6L3 29l6.6-1.7A13 13 0 1 0 16 3zm0 23.7c-2 0-4-.5-5.7-1.6l-.4-.2-3.9 1 1-3.8-.3-.4A10.7 10.7 0 1 1 16 26.7zm5.9-8c-.3-.2-1.9-1-2.2-1s-.5-.2-.7.2-.8 1-1 1.2-.4.2-.7 0a8.8 8.8 0 0 1-4.4-3.8c-.3-.6.3-.5 1-1.7.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6a1.2 1.2 0 0 0-.9.4 3.7 3.7 0 0 0-1.1 2.7 6.4 6.4 0 0 0 1.3 3.4 14.7 14.7 0 0 0 5.7 5c2.1.9 2.9 1 4 .8a3.4 3.4 0 0 0 2.2-1.6 2.8 2.8 0 0 0 .2-1.6c0-.2-.3-.3-.6-.5z"/></svg>'
HOUSE_SVG = '<svg class="house" viewBox="0 0 400 260" fill="none" stroke="#fff" stroke-width="22" stroke-linejoin="miter"><path d="M10 250L170 40l160 210"/><path d="M215 60l45-35 130 225"/><path d="M290 70V20h34v95"/></svg>'
I['search'] = svg('<circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/>')
I['euro'] = svg('<path d="M17 6.5A7 7 0 1 0 17 17.5"/><path d="M4 10h9M4 14h9"/>')
I['users'] = svg('<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>')
I['leaf'] = svg('<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.5 19 2c1 2 2 4.2 2 8 0 5.5-4.8 10-10 10z"/><path d="M2 21c0-3 1.9-5.4 5.1-6"/>')
I['heart'] = svg('<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8L12 21.2l8.8-8.8a5.5 5.5 0 0 0 0-7.8z"/>')
I['fire'] = svg('<path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.4-.5-2-1-3-1.1-2.1-.2-4 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.2.4-2.3 1-3.4.2 1.6 1.5 2.9 2.5 2.9z"/>')
I['trend'] = svg('<path d="M23 6l-9.5 9.5-5-5L1 18"/><path d="M17 6h6v6"/>')
I['sun'] = svg('<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>')
I['wind'] = svg('<path d="M9.6 4.6A2 2 0 1 1 11 8H2M12.6 19.4A2 2 0 1 0 14 16H2M17.7 7.7A2.5 2.5 0 1 1 19.5 12H2"/>')
I['sparkle'] = svg('<path d="M12 3l1.9 5.8L20 11l-6.1 2.2L12 19l-1.9-5.8L4 11l6.1-2.2z"/>')

# ---------- content ----------
def svc(slug, name, icon, card, imgs, h1, tag, intro, how, benefits, faqs):
    return dict(slug=slug, name=name, icon=icon, card=card, imgs=imgs, h1=h1, tag=tag, intro=intro, how=how, benefits=benefits, faqs=faqs)

SERVICES = [
    svc('service/roof-repairs', 'Roof Repairs', 'hammer', 'roofing.jpg', ('roof-repair.jpg', 'roofing.jpg'),
        'Roof repairs.', 'Fast, lasting protection for your home.',
        'At Roof and Chimney Doctor, we provide fast and effective roof repair solutions to protect your property from leaks, weather damage, and structural issues. Whether it’s a few missing shingles, storm damage, or persistent leaks, our skilled team diagnoses the problem and delivers lasting repairs. We focus on restoring your roof’s strength, safety, and appearance—helping you avoid costly replacements in the future.',
        [('Detailed Roof Inspection', 'We carefully examine your roof to identify the cause of the problem.'),
         ('Clear Repair Plan & Quote', 'You’ll receive a transparent explanation of what needs to be done and the costs involved.'),
         ('High-Quality Repairs', 'From fixing leaks to replacing damaged shingles or flashing, we use durable materials and proven techniques.'),
         ('Weatherproofing', 'We ensure your roof is sealed against future weather damage.'),
         ('Final Quality Check', 'We inspect our work to guarantee the repair is solid and your property is safe.')],
        [('shield', 'Prevent Major Damage', 'Stop small issues from becoming costly roof replacements.'),
         ('house', 'Protect Your Home', 'Prevent water leaks, mold growth, and structural damage.'),
         ('trend', 'Extend Roof Lifespan', 'Regular maintenance keeps your roof in good condition for years longer.'),
         ('euro', 'Save Money', 'Timely repairs are far more affordable than full replacements.')],
        [('How quickly can you respond to a roof repair emergency?', 'We offer prompt service and aim to attend to emergency repairs within 24 hours whenever possible.'),
         ('Can you repair any type of roof?', 'Yes, we work on slate, tile, asphalt shingles, flat roofs, and more.'),
         ('How do I know if my roof needs repair?', 'Signs include leaks, missing or broken tiles, water stains on ceilings, or visible damage after a storm.'),
         ('Will repairing my roof affect its warranty?', 'Our repair methods follow manufacturer guidelines, so your warranty remains intact in most cases.')]),
    svc('service/roof-inspection', 'Roof Inspection', 'search', 'roof-inspection.jpg', ('roof-inspection.jpg', 'flat-roof.jpg'),
        'Roof inspection.', 'Expert checks for safety, longevity, and peace of mind.',
        'At Roof and Chimney Doctor, we offer professional roof inspection services to help homeowners detect issues early, prevent costly repairs, and extend the life of their roof. Our inspections cover every aspect of your roof—from shingles and flashing to gutters and structural integrity. Whether you’re buying a new home, preparing for bad weather, or simply ensuring your roof is in good shape, our detailed assessments give you the knowledge and confidence to make the right decisions.',
        [('Visual Assessment', 'We examine the entire roof for visible signs of damage, wear, or aging.'),
         ('Structural Check', 'We assess the roof’s structure for sagging, weakness, or potential hazards.'),
         ('Material Inspection', 'We check shingles, tiles, flashing, and sealants for cracks, leaks, or deterioration.'),
         ('Gutter & Drainage Review', 'We ensure water flows correctly and there are no blockages or damage.'),
         ('Detailed Report & Recommendations', 'You receive a clear summary of our findings and advice on any necessary repairs or maintenance.')],
        [('search', 'Early Problem Detection', 'Catch small issues before they turn into expensive repairs.'),
         ('trend', 'Longer Roof Lifespan', 'Proper care extends the durability of your roofing materials.'),
         ('shield', 'Improved Safety', 'Identifies structural weaknesses that could become dangerous.'),
         ('heart', 'Peace of Mind', 'Know the exact condition of your roof year-round.')],
        [('How often should I have my roof inspected?', 'At least once a year, ideally in spring or autumn, and after major storms.'),
         ('Do you inspect all types of roofs?', 'Yes, we inspect pitched, flat, metal, slate, tile, and shingle roofs.'),
         ('Will you provide photos of any problems found?', 'Yes, our inspection reports include clear photos so you can see exactly what needs attention.'),
         ('How long does a roof inspection take?', 'Most inspections take between 1–2 hours, depending on the roof size and condition.')]),
    svc('service/roof-installation', 'Roof Installation', 'roof', 'roof-installation-1.jpg', ('roof-installation.jpg', 'roof-install.jpg'),
        'New roof installation.', 'Built to last, designed for your home.',
        'At Roof and Chimney Doctor, we specialize in professional new roof installations that provide your property with lasting protection and curb appeal. Whether you’re building a new home or replacing an aging, damaged roof, our expert team delivers high-quality craftsmanship using durable materials. We ensure every new roof meets the highest standards of safety, weather resistance, and style—giving you peace of mind for years to come.',
        [('Initial Inspection & Consultation', 'We assess your property’s needs, discuss roofing options, and provide a transparent quote.'),
         ('Material Selection', 'Choose from a wide range of premium materials such as slate, tile, asphalt shingles, or metal roofing.'),
         ('Preparation & Safety Setup', 'We prepare the site, ensure safety measures, and protect your property during the work.'),
         ('Professional Installation', 'Our skilled roofers install your new roof with precision and care, following industry best practices.'),
         ('Final Inspection & Cleanup', 'We check every detail for quality, remove debris, and leave your property spotless.')],
        [('shield', 'Enhanced Protection', 'Safeguards your home against leaks, weather damage, and structural issues.'),
         ('trend', 'Increased Property Value', 'Boosts curb appeal and resale value.'),
         ('sun', 'Energy Efficiency', 'Modern roofing materials help regulate indoor temperature, reducing energy bills.'),
         ('heart', 'Peace of Mind', 'A properly installed roof means less maintenance and fewer repairs in the future.')],
        [('How long does a new roof installation take?', 'Most new roof projects are completed within 2–5 days, depending on size and weather conditions.'),
         ('How do I know if I need a new roof instead of repairs?', 'Signs include frequent leaks, missing shingles, sagging areas, or a roof older than 20–25 years. We offer inspections to help you decide.'),
         ('What roofing materials do you recommend?', 'We work with slate, tile, asphalt shingles, and metal roofing—each with its own style, durability, and price range.'),
         ('Is there a warranty on your new roof installations?', 'Yes, we offer both manufacturer warranties on materials and our own workmanship guarantee.')]),
    svc('service/chimney-repairs', 'Chimney Repairs', 'chimney', 'chimney-repairs.jpg', ('chimney-repair-1.jpg', 'chimney-repair-2.jpg'),
        'Chimney repairs.', 'Restoring safety, strength, and style.',
        'At Roof and Chimney Doctor, we provide expert chimney repair services to keep your home safe, warm, and structurally sound. From cracked bricks and damaged mortar to leaning structures or water leaks, we address all types of chimney issues with precision. Our skilled team ensures your chimney not only looks great but also functions safely—protecting your home from fire hazards, water damage, and structural deterioration.',
        [('Comprehensive Chimney Inspection', 'We check for cracks, leaks, loose bricks, and structural weaknesses.'),
         ('Repair Plan & Estimate', 'You’ll receive a clear explanation of the work needed and the associated costs.'),
         ('Brick & Mortar Restoration', 'We replace damaged bricks, repoint mortar joints, and seal gaps to prevent water penetration.'),
         ('Structural & Safety Repairs', 'We stabilize leaning chimneys, repair crowns, and fix flashing to keep your chimney secure.'),
         ('Finishing & Waterproofing', 'We apply protective coatings to extend your chimney’s lifespan and prevent future damage.')],
        [('fire', 'Fire Safety', 'Reduces the risk of chimney fires caused by cracks and blockages.'),
         ('drop', 'Water Damage Prevention', 'Seals leaks to protect your home from internal damage.'),
         ('sun', 'Improved Heating Efficiency', 'Ensures smoke and gases exit properly, improving fireplace performance.'),
         ('trend', 'Extended Lifespan', 'Keeps your chimney strong and functional for many more years.')],
        [('How do I know if my chimney needs repairs?', 'Look for cracks in bricks, loose mortar, water stains, leaning structure, or difficulty with smoke ventilation.'),
         ('Can you repair both modern and traditional chimneys?', 'Yes, we repair all types of chimneys, from traditional brick to more modern designs.'),
         ('Do chimney repairs require scaffolding?', 'For major repairs or tall chimneys, scaffolding may be required to ensure safety and precision.'),
         ('How often should I have my chimney inspected?', 'We recommend at least once a year, ideally before winter, to ensure it’s safe and functional.')]),
    svc('service/guttering', 'Guttering', 'gutter', 'gutter.jpg', ('guttering-2.jpg', 'gutter.jpg'),
        'Guttering services.', 'Protecting your home from water damage.',
        'At Roof and Chimney Doctor, we provide professional gutter installation, repair, and maintenance to ensure your home stays safe from water damage. Gutters play a crucial role in directing rainwater away from your roof and foundation, preventing costly issues like leaks, dampness, and structural damage. Whether you need a brand-new gutter system, repairs to an existing one, or a thorough clean, our team delivers reliable, high-quality results that stand the test of time.',
        [('Inspection & Assessment', 'We examine your current guttering system to identify damage, blockages, or areas needing improvement.'),
         ('Custom Solutions', 'We recommend the best gutter type and material for your property, such as uPVC, aluminum, or steel.'),
         ('Professional Installation or Repairs', 'We fit or fix your gutters with precision, ensuring correct slope and secure fittings.'),
         ('Cleaning & Maintenance', 'We clear debris, leaves, and moss to keep your gutters working efficiently.'),
         ('Final Quality Check', 'We test the flow of water to ensure your system is fully functional and leak-free.')],
        [('drop', 'Prevents Water Damage', 'Directs rainwater away from your home’s foundation and walls.'),
         ('shield', 'Protects Roof & Fascia', 'Stops water overflow from rotting timber or damaging your roof edges.'),
         ('wind', 'Reduces Mold & Dampness', 'Keeps moisture away from your property’s interior.'),
         ('sparkle', 'Enhances Home Appearance', 'A clean, well-installed gutter system improves curb appeal.')],
        [('How often should gutters be cleaned?', 'We recommend cleaning at least twice a year, especially after autumn and spring.'),
         ('Can you replace only a section of damaged guttering?', 'Yes, we can repair or replace sections without changing the entire system.'),
         ('What gutter materials do you work with?', 'We install and repair uPVC, aluminum, steel, and cast iron guttering.'),
         ('How do I know if my gutters need replacing?', 'Signs include sagging, leaks, rust, cracks, or frequent blockages despite regular cleaning.')]),
    svc('service/fascia-soffit', 'Fascia & Soffit', 'layers', 'fascia-soffit.jpg', ('fascia-soffit-2.jpg', 'fascia-soffit-3.jpg'),
        'Fascia &amp; soffit services.', 'Strong, stylish, and built to protect.',
        'At Roof and Chimney Doctor, we provide expert fascia and soffit installation, repair, and replacement services to protect your roofline and improve your property’s appearance. Fascias and soffits are essential parts of your home’s roofing system—working together to support the guttering, protect the roof’s edge, and keep out moisture, pests, and debris. Whether your existing boards are damaged, worn, or outdated, our skilled team delivers high-quality, weather-resistant solutions that last for years.',
        [('Inspection & Assessment', 'We check the condition of your existing fascia and soffit for signs of rot, cracks, or weather damage.'),
         ('Material & Style Selection', 'Choose from durable uPVC, aluminum, or timber in various colours and finishes.'),
         ('Professional Removal', 'We safely remove old boards without damaging your roof structure.'),
         ('Precise Installation', 'We fit new fascia and soffit boards with exact alignment and secure fixings.'),
         ('Finishing Touches', 'We seal edges, check ventilation, and ensure your roofline looks neat and stylish.')],
        [('shield', 'Protects Your Roof', 'Prevents water from entering and damaging the roof structure.'),
         ('gutter', 'Supports Guttering', 'Provides a strong base for your gutter system.'),
         ('wind', 'Improves Ventilation', 'Soffits allow airflow into the roof space, reducing moisture buildup.'),
         ('trend', 'Low Maintenance & Long-Lasting', 'Modern materials require minimal upkeep and withstand harsh weather.')],
        [('How do I know if my fascia or soffit needs replacing?', 'Signs include peeling paint, rotting wood, water leaks near the roofline, or sagging gutters.'),
         ('What’s the best material for fascia and soffits?', 'uPVC is a popular choice due to its durability, weather resistance, and low maintenance needs, but timber and aluminum are also options.'),
         ('Do you offer matching colours for my existing roofline?', 'Yes, we can match your fascia and soffits to your home’s style and colour scheme.'),
         ('How long do fascia and soffits last?', 'With proper care, modern fascia and soffits can last 20–30 years or more.')]),
]
SUMMARY = {
    'service/roof-repairs': 'Fast and effective roof repairs for leaks, storm damage, missing tiles and flashing. We diagnose the problem and deliver lasting repairs.',
    'service/roof-inspection': 'Professional roof inspections to detect issues early, prevent costly repairs and extend the life of your roof, with photos of everything we find.',
    'service/roof-installation': 'New roof installations that give your property lasting protection and curb appeal, in slate, tile, shingle or metal.',
    'service/chimney-repairs': 'Expert chimney repairs for cracked bricks, damaged mortar, leaning stacks, flashing and leaks, keeping your home safe and warm.',
    'service/guttering': 'Gutter installation, repair, cleaning and maintenance to direct rainwater safely away from your roof and foundations.',
    'service/fascia-soffit': 'Fascia and soffit installation, repair and replacement in uPVC, aluminium or timber to protect and smarten your roofline.',
}
BA = {
    1: ('roof-repair.jpg', 'roofing.jpg', 'Project 01', 'Tile roof replaced'),
    2: ('roof-inspection.jpg', 'roofing-1.jpg', 'Project 02', 'Full re-roof'),
}
REVIEWS = [
    ('Patrick O’Connor', 'Dublin', 'Fantastic service from start to finish. The team arrived on time, worked efficiently, and left everything spotless. Highly recommend!'),
    ('Siobhán Murphy', 'Cork', 'They repaired my roof after a storm, and it’s been perfect ever since. Professional, friendly, and reasonably priced.'),
]
WHY = [('euro', 'Affordable Prices', 'Quality roofing and chimney services at fair, competitive rates — giving you lasting value without breaking your budget.'),
       ('users', 'Expert Team', 'Skilled and experienced professionals dedicated to delivering top-quality roofing and chimney solutions every time.'),
       ('leaf', 'Sustainable Practices', 'Environmentally responsible methods and materials that protect your home while caring for the planet.'),
       ('heart', 'Customer Focus', 'Personalized service and clear communication to ensure your needs are met and your expectations exceeded.')]
SERVICE_OPTS = ['Roof Repairs', 'Roof Inspection', 'Roof Installation', 'Chimney Repairs', 'Guttering', 'Fascia & Soffit', 'Other']
GALLERY = ['roofing-1.jpg', 'chimney-repair-2.jpg', 'roofing.jpg', 'roof-installation-1.jpg', 'roof-repair.jpg', 'flat-roof.jpg']

# ---------- building blocks ----------
def head(p, title, desc, path):
    canon = SITE + '/' + path
    return f'''<!doctype html>
<html lang="en-IE">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#061a30">
<meta property="og:type" content="website"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/img/roofing-1.jpg"><meta property="og:url" content="{canon}"><meta property="og:locale" content="en_IE">
<link rel="icon" href="{p}img/icon-192.png"><link rel="apple-touch-icon" href="{p}img/icon-192.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@500;600;700;800&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/style.css?v=1">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"RoofingContractor","name":"Roof and Chimney Doctor","url":"{SITE}/","telephone":"+353831213251","email":"{EMAIL}","image":"{SITE}/img/roofing-1.jpg","logo":"{SITE}/img/logo.png","address":{{"@type":"PostalAddress","addressLocality":"Dublin","addressCountry":"IE"}},"areaServed":"Ireland"}}</script>'''

def header(p, active):
    def on(k): return ' class="on" aria-current="page"' if k == active else ''
    menu = ''.join(f'<a href="{p}{s["slug"]}/"><i>{I[s["icon"]]}</i>{s["name"]}</a>' for s in SERVICES)
    subs = ''.join(f'<a href="{p}{s["slug"]}/">{s["name"]}</a>' for s in SERVICES)
    svc_on = ' class="on"' if active == 'services' else ''
    return f'''<header class="hdr"><div class="wrap">
<a class="brand" href="{p}" aria-label="Roof and Chimney Doctor home"><img src="{p}img/logo-white.png" alt="Roof and Chimney Doctor" width="824" height="372"></a>
<nav class="nav" aria-label="Main">
<a href="{p}"{on('home')}>Home</a>
<div class="dd"><a href="{p}services/"{svc_on}>Services {I['chev']}</a><div class="menu">{menu}</div></div>
<a href="{p}projects/"{on('projects')}>Projects</a>
<a href="{p}contact/"{on('contact')}>Contact</a>
</nav>
<a class="tel" href="{TEL}">{I['phone']}<span data-cfg="phone">{PHONE}</span></a>
<a class="btn btn-blue" href="#quote" data-quote>Get a free quote</a>
<button class="burger" aria-label="Menu" aria-expanded="false"><span></span><span></span></button>
</div></header>
<nav class="mnav" aria-label="Mobile">
<a class="ml" href="{p}">Home <small>01</small></a>
<a class="ml" href="{p}services/">Services <small>02</small></a>
<div class="subs">{subs}</div>
<a class="ml" href="{p}projects/">Projects <small>03</small></a>
<a class="ml" href="{p}contact/">Contact <small>04</small></a>
<a class="btn btn-blue" href="#quote" data-quote>Get a free quote</a>
<a class="btn btn-ghost" href="{TEL}" style="margin-top:12px">{I['phone']} Call {PHONE}</a>
<div class="mfoot">Dublin, Ireland · 15+ years’ experience</div>
</nav>'''

def select(name='service'):
    return f'<select name="{name}" required><option value="">Choose a service</option>' + ''.join(f'<option>{o}</option>' for o in SERVICE_OPTS) + '</select>'

def form(p, kind='quote', title='Get a free quote', sub='Free, no-obligation quotation. Tell us what you need and we’ll get back to you quickly.'):
    email_req = ' required' if kind == 'full' else ''
    fields = f'''<label class="f"><span>Name</span><input name="name" autocomplete="name" required></label>
<label class="f"><span>Phone</span><input name="phone" type="tel" autocomplete="tel" required></label>
<label class="f"><span>Email</span><input name="email" type="email" autocomplete="email"{email_req}></label>
<label class="f"><span>Service</span>{select()}</label>
<label class="f full"><span>Message</span><textarea name="message" placeholder="Tell us about your roof or chimney" required></textarea></label>'''
    return f'''<form class="formcard" data-form novalidate>
<h3>{title}</h3><p class="sub">{sub}</p>
<div class="fmsg" role="status"></div>
<div class="fgrid">{fields}</div>
<input class="hp" name="botcheck" tabindex="-1" autocomplete="off" aria-hidden="true">
<button class="btn btn-blue" type="submit">Send request {I['arrow']}</button>
<p class="fnote">Your details are kept private. See our <a href="{p}privacy-policy/">privacy policy</a>.</p>
</form>'''

def quote_drawer(p):
    f = form(p).replace('<form class="formcard"', '<form class="formcard" id="quote"').replace('<h3>', f'<button class="x" type="button" data-close aria-label="Close">{I["x"]}</button><h3>', 1)
    return f'<div class="qd" id="qd" role="dialog" aria-modal="true" aria-label="Request a quote"><div class="scrim" data-close></div>{f}</div>'

def footer(p):
    svcs = ''.join(f'<li><a href="{p}{s["slug"]}/">{s["name"]}</a></li>' for s in SERVICES)
    return f'''<footer class="ftr"><div class="wrap">
<div class="cols">
<div><img class="fl" src="{p}img/logo-white.png" alt="Roof and Chimney Doctor" width="824" height="372" loading="lazy">
<p>Roof and Chimney Doctor – your trusted specialists for repairs, installations, and maintenance across Ireland. Quality workmanship, fair pricing, and reliable service — from the top down.</p>
<span class="h247">{I['star'].replace('<svg', '<svg width="14" height="14"')} 15+ YEARS’ EXPERIENCE</span></div>
<div><h4>Quick Links</h4><ul><li><a href="{p}">Home</a></li><li><a href="{p}services/">Services</a></li><li><a href="{p}projects/">Projects</a></li><li><a href="{p}contact/">Contact</a></li></ul></div>
<div><h4>Services</h4><ul>{svcs}</ul></div>
<div><h4>Contact</h4><ul class="ci">
<li>{I['pin']}<span>Dublin, Ireland</span></li>
<li>{I['phone']}<a href="{TEL}" data-cfg="phone">{PHONE}</a></li>
<li>{I['mail']}<a href="mailto:{EMAIL}" data-cfg="email" style="word-break:break-all">{EMAIL}</a></li></ul></div>
</div>
<div class="base"><span>Copyright © <span data-cfg="year">2026</span> Roof and Chimney Doctor. All rights reserved.</span>
<nav><a href="{p}privacy-policy/">Privacy Policy</a></nav></div>
</div></footer>
<div class="fab"><a class="ph" href="{TEL}" aria-label="Call {PHONE}">{I['phone']}</a><a class="wa" href="https://wa.me/353831213251" data-href="whatsapp" target="_blank" rel="noopener" aria-label="WhatsApp us">{WA}</a></div>'''

def scripts(p):
    return f'''<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" defer></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js" defer></script>
<script src="https://cdn.jsdelivr.net/npm/lenis@1.1.18/dist/lenis.min.js" defer></script>
<script src="{p}assets/site.js?v=1" defer></script>'''

def page(path, active, title, desc, body, intro=False):
    p = '../' * path.count('/')
    head_html = head(p, title, desc, path)
    loader = ''
    if intro:
        head_html += '\n<script>try{if(!sessionStorage.getItem("rcd_intro")||/[?&]intro/.test(location.search))document.documentElement.classList.add("intro")}catch(e){document.documentElement.classList.add("intro")}</script>'
        # data-apex: the roof peak of the logo the bolt strikes; data-l / data-r: where the crackles run to
        loader = f'''<div id="loader" aria-hidden="true" data-apex="0.307,0.02" data-l="0.05,0.44" data-r="0.55,0.42"><div class="sky"></div><i class="glow"></i>
<i class="ring"></i><i class="ring r2"></i>
<div class="box"><div class="logo"><img class="off" src="{p}img/logo-white.png" alt=""><img class="on" src="{p}img/logo-white.png" alt=""></div><div class="lt">From the top down</div></div>
<svg class="bolt"><defs><filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6"/></filter></defs></svg>
<div class="flash"></div></div>'''
    html = f'''{head_html}
</head>
<body>
{loader}
{header(p, active)}
<main>
{body(p)}
</main>
{footer(p)}
{quote_drawer(p)}
{scripts(p)}
</body>
</html>
'''
    out = os.path.join(ROOT, path, 'index.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html)
    print('wrote', os.path.relpath(out, ROOT))

# ---------- sections ----------
def phero(p, crumb, h1, lead, img, extra=''):
    trail = ''.join(f'<span>/</span><a href="{p}{u}">{t}</a>' for t, u in crumb[:-1])
    return f'''<section class="phero" data-rain>
<img class="bg" src="{p}img/{img}" alt="" fetchpriority="high">
<div class="wrap">
<div class="crumb"><a href="{p}">Home</a>{trail}<span>/</span><b>{crumb[-1][0]}</b></div>
<h1>{h1}</h1>
<p class="lead">{lead}</p>
{extra}
</div></section>'''

def hero_btns(p):
    return f'<div class="btn-row"><a class="btn btn-blue" href="#quote" data-quote>Get a free quote {I["arrow"]}</a><a class="btn btn-ghost" href="{TEL}">{I["phone"]} Call {PHONE}</a></div>'

def marquee():
    items = ['Roof repairs', 'Chimney repairs', 'Roof inspections', 'New roof installations', 'Guttering', 'Fascia & soffits', '15+ years’ experience', 'Free quotes']
    s = ''.join(f'<span>{t}</span>' for t in items)
    return f'<div class="marquee" aria-hidden="true"><div class="track">{s}{s}</div></div>'

def why(soft=True):
    c = ''.join(f'<div class="card"><span class="ico">{I[a]}</span><h3>{b}</h3><p>{t}</p></div>' for a, b, t in WHY)
    return f'''<section class="sec{' soft' if soft else ''}"><div class="wrap">
<div class="center" style="margin-bottom:48px"><span class="eyebrow">Why choose us</span><h2 data-split>Quality work, fair prices, real care.</h2></div>
<div class="cards" data-reveal="group">{c}</div></div></section>'''

def services_grid(p, title='Our services.', head=True):
    cards = ''
    for i, s in enumerate(SERVICES, 1):
        cards += f'''<a class="scard" href="{p}{s['slug']}/"><img src="{p}img/{s['card']}" alt="{s['name']} by Roof and Chimney Doctor" loading="lazy">
<span class="num">0{i}</span><span class="go">{I['arrow']}</span>
<h3>{s['name']}</h3><p>{SUMMARY[s['slug']]}</p><span class="tlink">View service {I['arrow']}</span></a>'''
    hd = f'''<div class="sec-head"><div><span class="eyebrow">What we do</span><h2 data-split>{title}</h2></div>
<a class="btn btn-line" href="{p}services/">All services {I['arrow']}</a></div>''' if head else ''
    return f'<section class="sec" id="services"><div class="wrap">{hd}<div class="sgrid" data-reveal="group">{cards}</div></div></section>'

def compare(p, n):
    b, a, t, s = BA[n]
    return f'''<figure class="ba"><div class="compare"><img class="after" src="{p}img/{a}" alt="{s}: after, by Roof and Chimney Doctor" loading="lazy"><img class="before" src="{p}img/{b}" alt="{s}: before" loading="lazy">
<span class="tag l">Before</span><span class="tag r">After</span><span class="handle"></span>
<input type="range" min="0" max="100" value="50" aria-label="Drag to compare before and after"></div>
<figcaption>{t}<span>{s}</span></figcaption></figure>'''

def before_after(p, soft=False):
    items = ''.join(compare(p, n) for n in BA)
    return f'''<section class="sec{' soft' if soft else ''}" id="work"><div class="wrap">
<div class="sec-head"><div><span class="eyebrow">Before &amp; after</span><h2 data-split>See the difference we make.</h2></div>
<p>Drag the slider across each photo to see the roof before and after our work.</p></div>
<div class="ba-grid" data-reveal="group">{items}</div></div></section>'''

def gallery(p, title='Our stunning projects.', soft=True, link=False):
    g = ''.join(f'<a href="{p}img/{x}"><img src="{p}img/{x}" alt="Roofing and chimney project by Roof and Chimney Doctor" loading="lazy"></a>' for x in GALLERY)
    btn = f'<a class="btn btn-line" href="{p}projects/">View projects {I["arrow"]}</a>' if link else '<p>Tap a photo to see it full size.</p>'
    return f'''<section class="sec{' soft' if soft else ''}"><div class="wrap">
<div class="sec-head"><div><span class="eyebrow">Recent work</span><h2 data-split>{title}</h2></div>{btn}</div>
<div class="gal">{g}</div></div></section>'''

def reviews():
    r = ''.join(f'''<div class="review"><div class="stars" aria-label="5 stars">★★★★★</div><q>{t}</q>
<div class="who"><span class="av">{n[0]}</span><div><b>{n}</b><span>{loc}</span></div></div></div>''' for n, loc, t in REVIEWS)
    return f'''<section class="sec deep" data-rain><div class="wrap split" style="position:relative;z-index:2;align-items:start">
<div><span class="eyebrow">Our customers say…</span><h2 data-split>Trusted by homeowners across Ireland.</h2>
<p>Every project is backed by our passion for craftsmanship and our dedication to customer satisfaction.</p>
<a class="btn btn-blue" href="#quote" data-quote style="margin-top:10px">Get a free quote {I['arrow']}</a></div>
<div class="rgrid r2" data-reveal="group">{r}</div></div></section>'''

def cta(p):
    return f'''<section class="cta">{HOUSE_SVG}<div class="wrap">
<div><span class="eyebrow">Get in touch</span><h2 data-split>Need expert roofing or chimney services?</h2>
<p>Contact us today to schedule a consultation or to learn more about our services.</p></div>
<div class="btn-row"><a class="btn btn-white" href="{p}contact/">Get a free quote {I['arrow']}</a><a class="btn btn-ghost" href="{TEL}">{I['phone']} {PHONE}</a></div>
</div></section>'''

# ---------- pages ----------
def home(p):
    trust = ''.join(f'<li>{I["check"]}{t}</li>' for t in ['15+ years’ experience', 'Free, no-obligation quotes', 'Quality materials, lasting results'])
    return f'''<section class="hero" data-rain>
<img class="bg" src="{p}img/roof-installation.jpg" alt="" fetchpriority="high">
<div class="wrap">
<div>
<div class="gbadge"><span class="stars">★★★★★</span><b>15+ years</b> Roofing &amp; chimney specialists</div>
<span class="eyebrow">Dublin · Ireland</span>
<h1>Roof &amp; chimney excellence, backed by <span class="blue">experience.</span></h1>
<p class="lead">With over 15 years of proven experience in roofing and chimney services, we provide expert repairs, precision installations, and long-lasting solutions to keep your home safe, secure, and weatherproof.</p>
<div class="btn-row"><a class="btn btn-blue" href="#quote" data-quote>Get a free quote {I['arrow']}</a><a class="btn btn-ghost" href="{p}projects/">View projects</a></div>
<ul class="trust">{trust}</ul>
</div>
<div class="vwrap"><span class="frame"></span>
<div class="vcard"><img src="{p}img/roofing.jpg" alt="Newly tiled roof by Roof and Chimney Doctor"></div>
<span class="tag"><i></i>Recent work</span>
<div class="pill"><i>{I['chimney']}</i><div><b>Roof &amp; chimney</b><span>Repairs · installs · inspections</span></div></div>
</div>
</div>
<div class="scroll">Scroll</div>
</section>
{marquee()}
<section class="sec"><div class="wrap split">
<div>
<span class="eyebrow">Who we are</span>
<h2 data-split>Committed to protecting your home from the top down.</h2>
<p class="lead" style="color:var(--ink)">If you are looking for a trusted, experienced team to handle all your roofing and chimney needs, you’ve come to the right place.</p>
<p>With over 15 years of hands-on experience, we specialize in delivering reliable repairs, precise installations, and thorough maintenance to keep your home safe, dry, and looking its best.</p>
<p>We pride ourselves on combining skilled craftsmanship with quality materials, ensuring every project meets the highest standards of durability and safety. Whether it’s a simple chimney cleaning or a complete roof replacement, our goal is to provide solutions that stand the test of time — giving you peace of mind in every season.</p>
<div class="callrow"><a class="btn btn-blue" href="#quote" data-quote>Get a free quote {I['arrow']}</a>
<div><small>Prefer to call?</small><a class="num" href="{TEL}">{PHONE}</a></div></div>
</div>
<div class="collage">
<figure data-clip><img src="{p}img/roofing-1.jpg" alt="New roof completed by Roof and Chimney Doctor" loading="lazy"></figure>
<figure data-clip><img src="{p}img/chimney-repair-2.jpg" alt="Rebuilt brick chimney" loading="lazy"></figure>
<figure data-clip><img src="{p}img/flat-roof.jpg" alt="Flat roof" loading="lazy"></figure>
<figure data-clip><img src="{p}img/roof-installation-1.jpg" alt="Roofer laying new slates" loading="lazy"></figure>
</div>
</div></section>
<section class="sec tight soft"><div class="wrap"><div class="stats" data-reveal="group">
<div><b>15+</b><span>Years’ experience</span></div>
<div><b>6</b><span>Specialist services</span></div>
<div><b>100%</b><span>Free, no-obligation quotes</span></div>
<div><b>5★</b><span>Customer rated</span></div>
</div></div></section>
{services_grid(p, 'Roofing &amp; chimney services, done right.')}
{before_after(p, soft=True)}
<section class="sec dark weather" data-rain><div class="big" aria-hidden="true">FROM THE TOP DOWN</div><div class="wrap split rev">
<div>
<span class="eyebrow">About us</span>
<h2 data-split>Your home deserves the very best protection.</h2>
<p>At Roof and Chimney Doctor, we believe your home deserves the very best protection — starting from the top. With over 15 years of dedicated experience in roofing and chimney services, we’ve built a reputation for delivering high-quality workmanship, reliable service, and lasting results.</p>
<p>We handle everything from routine maintenance and repairs to complete installations, using only top-grade materials and proven techniques to ensure durability and safety.</p>
<p>Our commitment goes beyond just fixing problems — we focus on preventing them, keeping your home safe, weatherproof, and looking great for years to come.</p>
<div class="callrow"><a class="btn btn-blue" href="{p}contact/">Contact us {I['arrow']}</a>
<div><small>Prefer to call?</small><a class="num" href="{TEL}">{PHONE}</a></div></div>
</div>
<div class="ph tall" data-clip><img src="{p}img/team-roof.jpg" alt="Clay tile roof with new ridge" loading="lazy"><span class="chip">{I['shield']}Top-grade materials, proven techniques</span></div>
</div></section>
{why()}
{gallery(p, 'View some of our recent projects.', soft=False, link=True)}
{reviews()}
{cta(p)}'''

def services_page(p):
    details = ''
    for i, s in enumerate(SERVICES, 1):
        details += f'''<div class="sdetail"><div class="ph" data-clip><img src="{p}img/{s['card']}" alt="{s['name']}" loading="lazy"></div>
<div><div class="bign">0{i}</div><h2 style="font-size:clamp(1.6rem,2.6vw,2.2rem)">{s['name']}</h2><p>{SUMMARY[s['slug']]}</p>
<ul class="ticks">{''.join(f"<li>{I['check']}{b[1]}</li>" for b in s['benefits'])}</ul>
<a class="btn btn-blue" href="{p}{s['slug']}/">View service {I['arrow']}</a></div></div>'''
    return f'''{phero(p, [('Services', 'services/')], 'Our services.', 'Explore our comprehensive range of roofing and chimney services designed to protect, enhance, and extend the life of your home.', 'roof-installation-2.jpg', hero_btns(p))}
{services_grid(p, 'Our full range of services.', head=False)}
<section class="sec deep"><div class="wrap">
<div class="center" style="margin-bottom:60px"><span class="eyebrow">In detail</span><h2 data-split>Everything your roof and chimney need.</h2></div>
{details}</div></section>
{why()}
{cta(p)}'''

def service_page(s):
    def body(p):
        steps_html = ''.join(f'<div class="step"><div class="n">0{i}</div><h3>{a}</h3><p>{b}</p></div>' for i, (a, b) in enumerate(s['how'], 1))
        ben = ''.join(f'<div class="card"><span class="ico">{I[a]}</span><h3>{b}</h3><p>{c}</p></div>' for a, b, c in s['benefits'])
        faq = ''.join(f'<details class="faq"><summary>{q}<i>{I["chev"]}</i></summary><p>{a}</p></details>' for q, a in s['faqs'])
        others = ''.join(f'''<a class="scard" href="{p}{o['slug']}/" style="min-height:300px"><img src="{p}img/{o['card']}" alt="" loading="lazy"><span class="go">{I['arrow']}</span><h3>{o['name']}</h3><span class="tlink">View service {I['arrow']}</span></a>''' for o in SERVICES if o is not s)
        a, b = s['imgs']
        return f'''{phero(p, [('Services', 'services/'), (s['name'], s['slug'] + '/')], s['h1'], s['tag'], s['card'], hero_btns(p))}
{marquee()}
<section class="sec"><div class="wrap split">
<div><span class="eyebrow">{s['name']}</span><h2 data-split>{s['tag']}</h2><p>{s['intro']}</p>
<div class="callrow"><a class="btn btn-blue" href="#quote" data-quote>Get a free quote {I['arrow']}</a><div><small>Prefer to call?</small><a class="num" href="{TEL}">{PHONE}</a></div></div></div>
<div class="duo"><div class="ph" data-clip><img src="{p}img/{a}" alt="{s['name']} by Roof and Chimney Doctor" loading="lazy"></div><div class="ph" data-clip><img src="{p}img/{b}" alt="{s['name']} work" loading="lazy"></div></div>
</div></section>
<section class="sec soft"><div class="wrap">
<div class="center" style="margin-bottom:48px"><span class="eyebrow">How we do it</span><h2 data-split>Our process, step by step.</h2></div>
<div class="steps s5" data-reveal="group">{steps_html}</div></div></section>
<section class="sec"><div class="wrap">
<div class="center" style="margin-bottom:48px"><span class="eyebrow">Benefits</span><h2 data-split>Why it’s worth doing properly.</h2></div>
<div class="cards" data-reveal="group">{ben}</div></div></section>
<section class="sec soft"><div class="wrap split" style="align-items:start">
<div><span class="eyebrow">FAQs</span><h2 data-split>Questions we get asked.</h2><div class="faqs">{faq}</div></div>
<div data-reveal>{form(p)}</div></div></section>
<section class="sec"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">Other services</span><h2 data-split>More ways we can help.</h2></div><a class="btn btn-line" href="{p}services/">All services {I['arrow']}</a></div>
<div class="sgrid others" data-reveal="group">{others}</div></div></section>
{cta(p)}'''
    return body

def projects_page(p):
    return f'''{phero(p, [('Projects', 'projects/')], 'Our projects.', 'Real roofs and chimneys we’ve repaired, rebuilt and installed for homeowners across Ireland.', 'roofing-1.jpg', hero_btns(p))}
{before_after(p)}
{gallery(p)}
{cta(p)}'''

def contact_page(p):
    return f'''{phero(p, [('Contact', 'contact/')], 'Contact us.', 'Locate and visit us or send us a message for your next project!', 'roof-install.jpg')}
<section class="sec" style="padding-top:0"><div class="wrap">
<div class="info" data-reveal="group">
<div class="ic"><span class="ico">{I['pin']}</span><div><h3>Address</h3><p>Dublin, Ireland</p></div></div>
<a href="{TEL}"><span class="ico">{I['phone']}</span><div><h3>Call Us</h3><p data-cfg="phone">{PHONE}</p></div></a>
<a href="mailto:{EMAIL}"><span class="ico">{I['mail']}</span><div><h3>Email Us</h3><p data-cfg="email" style="word-break:break-all">{EMAIL}</p></div></a>
</div>
<div class="split" style="margin-top:80px;align-items:start">
<div><span class="eyebrow">Find us on Google</span><h2 data-split>Send us a message.</h2>
<p>Tell us about your roof or chimney and we’ll get back to you with advice and a free quote. Or call us on <a class="blue" href="{TEL}"><b>{PHONE}</b></a>.</p>
<div class="map" style="margin-top:28px"><iframe title="Roof and Chimney Doctor location map" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://maps.google.com/maps?q=Dublin%2C%20Ireland&amp;t=m&amp;z=11&amp;output=embed"></iframe></div></div>
<div data-reveal>{form(p, 'full', 'Send us a message', 'Fill in the form and we’ll be in touch shortly.')}</div>
</div></div></section>
{cta(p)}'''

def privacy_page(p):
    return f'''{phero(p, [('Privacy Policy', 'privacy-policy/')], 'Privacy policy.', 'How Roof and Chimney Doctor collects, uses and protects your personal information.', 'guttering.jpg')}
<section class="sec"><div class="wrap article">
<p>Roof and Chimney Doctor (“we”, “us”) respects your privacy. This policy explains what personal information we collect through this website and how we use it, in line with the GDPR and Irish data protection law.</p>
<h2>Who we are</h2><p>Roof and Chimney Doctor, Dublin, Ireland. Email <a class="blue" href="mailto:{EMAIL}">{EMAIL}</a>, phone <a class="blue" href="{TEL}">{PHONE}</a>.</p>
<h2>What we collect</h2><p>When you send a quote request or message, we collect the details you give us: your name, phone number, email address, the service you are interested in and your message. We do not collect any other personal information through this website.</p>
<h2>How we use it</h2><ul><li>To respond to your enquiry and arrange an inspection or quotation.</li><li>To carry out and follow up on work you have asked us to do.</li><li>To keep records required for accounting and legal purposes.</li></ul>
<p>We never sell your information or use it for unrelated marketing.</p>
<h2>How long we keep it</h2><p>Enquiries that do not lead to work are deleted within 12 months. Records relating to completed work are kept for as long as required by law.</p>
<h2>Cookies</h2><p>This website does not set analytics or advertising cookies. It stores one item in your browser’s session storage so the opening animation only plays once per visit. The map on the contact page is provided by Google, which may set its own cookies.</p>
<h2>Your rights</h2><p>You can ask to access, correct or delete your personal data, or object to how we use it, by contacting us. You can also complain to the Data Protection Commission (dataprotection.ie).</p>
</div></section>
{cta(p)}'''

if __name__ == '__main__':
    T = ' - Roof and Chimney Doctor'
    page('', 'home', 'Roof and Chimney Doctor | Roof & Chimney Repairs Dublin', 'Roof and Chimney Doctor: over 15 years of roofing and chimney experience. Roof repairs, inspections, new roofs, chimney repairs, guttering, fascia and soffits. Free quotes.', home, intro=True)
    page('services/', 'services', 'Our Services' + T, 'Roof repairs, roof inspections, new roof installations, chimney repairs, guttering, fascia and soffits.', services_page)
    for s in SERVICES:
        page(s['slug'] + '/', 'services', s['name'] + T, SUMMARY[s['slug']], service_page(s))
    page('projects/', 'projects', 'Our Projects' + T, 'Recent roofing and chimney projects by Roof and Chimney Doctor.', projects_page)
    page('contact/', 'contact', 'Contact Us' + T, 'Contact Roof and Chimney Doctor. Call 083 121 3251 or email roofandchimneydoctor@gmail.com for a free quote.', contact_page)
    page('privacy-policy/', '', 'Privacy Policy' + T, 'How Roof and Chimney Doctor handles your personal information.', privacy_page)
