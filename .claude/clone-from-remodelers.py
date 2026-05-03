"""Clone remodelers-website -> tree-removal-website
 - jsDelivr repo URL: remodelers-website -> tree-removal-website
 - Image extensions: .png -> .jpg
 - Navy accent (#4870A8) -> dark forest green (#3D7A5C)
 - Kitchen/bath service content -> tree removal service content
 - GHL slug paths /home /about /services etc. (already in remodelers)
"""
import os, re, shutil

REM = os.path.expanduser('~/Downloads/Claude/remodelers-website')
DST = os.path.expanduser('~/Downloads/Claude/tree-removal-website')

PAGES = ['index.html','about.html','services.html','service-areas.html',
         'gallery.html','testimonials.html','faq.html','contact.html',
         'quote.html','privacy.html','terms.html','404.html']

# 1. Copy + recolor CSS
with open(os.path.join(REM, 'assets/css/styles.css'), encoding='utf-8') as f:
    css = f.read()

css = css.replace('REMODELERS — Dark Premium + Brass Accent',
                  'TREE REMOVAL — Dark Premium + Forest Green')
css = css.replace('warm brass accent (kitchen/bath fixtures)',
                  'forest green accent (tree service trade)')
css = css.replace('--brass:        #4870A8', '--brass:        #3D7A5C')
css = css.replace('--brass-bright: #6090C8', '--brass-bright: #5A9D7C')
css = css.replace('--brass-deep:   #2D4F7E', '--brass-deep:   #25503C')
css = css.replace('rgba(72, 112, 168, 0.5)',  'rgba(61, 122, 92, 0.5)')
css = css.replace('rgba(72, 112, 168, 0.1)',  'rgba(61, 122, 92, 0.1)')
css = css.replace('rgba(72, 112, 168, 0.45)', 'rgba(61, 122, 92, 0.45)')
css = css.replace('rgba(72, 112, 168, 0.3)',  'rgba(61, 122, 92, 0.3)')
css = css.replace('rgba(72, 112, 168, 0.04) 1px',
                  'rgba(61, 122, 92, 0.04) 1px')
css = css.replace('rgba(96, 144, 200, 0.32)', 'rgba(90, 157, 124, 0.32)')
css = css.replace('#9DC0E8', '#A8D9BD')
css = css.replace('annasfilig-max/remodelers-website',
                  'annasfilig-max/tree-removal-website')
css = css.replace('hero.png', 'hero.jpg')
css = css.replace('#4870A8', '#3D7A5C')

with open(os.path.join(DST, 'assets/css/styles.css'), 'w', encoding='utf-8', newline='\n') as f:
    f.write(css)
print('  CSS copied + navy -> forest green #3D7A5C')

# 2. Copy main.js verbatim
shutil.copy(os.path.join(REM, 'assets/js/main.js'),
            os.path.join(DST, 'assets/js/main.js'))
print('  main.js copied')

# 3. HTML content swaps
SWAPS = [
    # repo URL
    ('annasfilig-max/remodelers-website', 'annasfilig-max/tree-removal-website'),
    # image extensions
    ('.png\'', '.jpg\''),
    ('.png"', '.jpg"'),
    # tagline
    ('Kitchen &amp; Bath Remodels', 'Tree Removal &amp; Tree Care'),
    ('Kitchen &middot; Bath &middot; Whole-Home Remodels',
     'Tree Removal &middot; Trimming &middot; Stump Grinding'),
    # SEO
    ('Kitchen &amp; Bath Remodelers in [City, State]',
     'Tree Removal Service in [City, State]'),
    ('design-build kitchen and bath remodelers',
     'licensed tree removal &amp; care experts'),
    ('Custom cabinetry, countertops, tile, and full renovations.',
     'Tree removal, trimming, stump grinding, storm cleanup, lot clearing &mdash; 24/7 emergency.'),
    ('Remodels Done Right', 'Tree Work Done Right'),
    ('Design-build kitchen and bath remodels by a local crew that finishes on time and on budget.',
     'Trees down, lawns clean, hauled away &mdash; same-day for emergencies, scheduled for the rest.'),
    # Nav label
    ('<a href="/gallery">Portfolio</a>',
     '<a href="/gallery">Gallery</a>'),
    # Hero
    ('Kitchens &amp; Baths<br><em>Built To Last.</em>',
     'Trees Down.<br><em>Lawns Clean.</em>'),
    ("Design-build remodels by a local crew that doesn't ghost mid-project. Measured, designed, built, and warrantied &mdash; start to reveal in one trade.",
     "Tree removal, trimming, and stump grinding by a crew that shows up insured, climbs safely, and hauls away every branch &mdash; even after the worst storm."),
    ('Book a Design Visit', 'Get a Free Quote'),
    ('View Portfolio', 'Call [Phone Number]'),
    ('Years Building', 'Years Climbing'),
    ('Rooms Done', 'Trees Removed'),
    ('Houzz / Google', 'Avg Google'),
    ('Featured Build<br>[Project Name]', 'On Call<br>24/7 Storm Crew'),
    # Marquee badges
    ('NKBA Member Designers', 'ISA Certified Arborists'),
    ('NARI Certified Builders', 'Crane &amp; Bucket Equipped'),
    ('Free In-Home Design Visits', '24/7 Storm Emergency'),
    ('15-Year Workmanship Warranty', 'Fully Licensed &amp; Insured'),
    ('Lead-Safe EPA RRP Certified', 'BBB A+ Rated'),
    ('On-Time, On-Budget', 'Free Estimates'),
    # Services section header
    ('Six Specialties.<br>One Crew On Site.',
     'Six Services.<br>One Crew On Site.'),
    ('Design + Build, In-House', 'Climb &middot; Cut &middot; Cleanup'),
    # Service slug anchors
    ('href="/services#kitchen"', 'href="/services#removal"'),
    ('href="/services#bath"', 'href="/services#trimming"'),
    ('href="/services#cabinets"', 'href="/services#stump"'),
    ('href="/services#counters"', 'href="/services#emergency"'),
    ('href="/services#tile"', 'href="/services#clearing"'),
    ('href="/services#design"', 'href="/services#crane"'),
    ('id="kitchen"',  'id="removal"'),
    ('id="bath"',     'id="trimming"'),
    ('id="cabinets"', 'id="stump"'),
    ('id="counters"', 'id="emergency"'),
    ('id="tile"',     'id="clearing"'),
    ('id="design"',   'id="crane"'),
    # Service card titles
    ('01 / Signature</span>\n          <h3>Kitchen Remodels</h3>',
     '01 / Removal</span>\n          <h3>Tree Removal</h3>'),
    ('02 / Signature</span>\n          <h3>Bath Remodels</h3>',
     '02 / Care</span>\n          <h3>Tree Trimming</h3>'),
    ('03 / Cabinetry</span>\n          <h3>Cabinets &amp; Refacing</h3>',
     '03 / Stump</span>\n          <h3>Stump Grinding</h3>'),
    ('04 / Surfaces</span>\n          <h3>Countertops &amp; Stone</h3>',
     '04 / Storm</span>\n          <h3>Emergency Storm Cleanup</h3>'),
    ('05 / Tile</span>\n          <h3>Custom Tile &amp; Stone</h3>',
     '05 / Clearing</span>\n          <h3>Lot &amp; Land Clearing</h3>'),
    ('06 / Design</span>\n          <h3>Design Consultation</h3>',
     '06 / Crane</span>\n          <h3>Crane-Assist Removal</h3>'),
    # Card descriptions
    ('Full-gut to refresh. Cabinets, counters, lighting, flooring &mdash; one crew, one timeline, one warranty.',
     'Hazardous, dead, or just in the way &mdash; we drop it safely, even tight against the house.'),
    ('Spa-grade primary baths to clean second-bath refreshes. Tile, plumbing, vanities, glass &mdash; in-house.',
     'Crown lifts, deadwood removal, structural pruning &mdash; done by trained climbers, not chainsaw cowboys.'),
    ('Custom, semi-custom, or refacing. Tight joinery, real wood, finishes that hold &mdash; sized and installed in-house.',
     'Grind to 6 inches below grade. Chips left, hauled, or used as mulch &mdash; your call.'),
    ('Quartz, granite, marble, butcher block. Templated, fabricated, installed &mdash; without the markup games.',
     'Storm hit overnight? We dispatch 24/7. Trees off houses, cars, driveways &mdash; insurance paperwork too.'),
    ('Backsplashes, shower walls, floors. Hand-laid by tile specialists &mdash; not the lowest-bid sub.',
     'New build site, expansion, view-clearing &mdash; we strip, grind, and haul any size lot.'),
    ('3D visualization, material selection, and an honest budget &mdash; before any demo starts.',
     'Tight access? Big tree? Crane crew &amp; certified rigger on staff &mdash; no sub-contracted guesswork.'),
    ('Explore Kitchens &rarr;', 'Tree Removal &rarr;'),
    ('Explore Baths &rarr;',    'Trimming &rarr;'),
    ('See Cabinetry &rarr;',    'Stump Grinding &rarr;'),
    ('See Surfaces &rarr;',     'Storm Cleanup &rarr;'),
    ('See Tile Work &rarr;',    'Lot Clearing &rarr;'),
    ('Book a Design Visit &rarr;', 'Crane Removal &rarr;'),
    # Portfolio
    ('Recent<br>Transformations.', 'Recent Jobs.<br>Real Trees.'),
    ('[##]+ Builds Delivered', '4,800+ Trees Down'),
    ('Kitchen', 'Big Oak'),
    ('Primary Bath', 'Storm Cleanup'),
    ('Cabinetry', 'Crane Lift'),
    ('Custom Tile', 'Stump Grind'),
    ('Open-Plan', 'Lot Clear'),
    ('Powder Room', 'Trimming'),
    ('Quartz Counters', 'Hazard Drop'),
    ('See Full Portfolio &rarr;', 'See Full Gallery &rarr;'),
    # About
    ('A Crew That<br>Treats Your Home<br>Like Their Own.',
     'A Crew That<br>Treats Your Yard<br>Like Their Own.'),
    ("Family-owned since [Year]. Built on the idea that homeowners shouldn't have to be afraid of contractors &mdash; no mystery invoices, no high-pressure sales, no leaving you on hold for three weeks while we finish someone else's job.",
     "Family-owned since [Year]. Built on the idea that homeowners shouldn't have to be afraid of tree guys &mdash; no mystery invoices, no high-pressure sales, no leaving stumps and limbs in the yard."),
    ('Background-checked, drug-tested crew', 'ISA-certified, climber-tested crew'),
    ('Fixed-price quotes &mdash; the invoice matches the quote', 'Flat-rate quotes &mdash; the invoice matches the quote'),
    ('Floors covered, daily cleanup, debris hauled', 'Drop cloths over flowerbeds, every chip hauled'),
    ('15-year workmanship warranty on every job', 'Fully insured &mdash; we cover the worst case so you never have to'),
    # Process
    ('Sketch.<br>Build. Reveal.', 'Quote.<br>Drop. Cleanup.'),
    ('Discovery Call', 'Free Estimate'),
    ('15 minutes on the phone &mdash; scope, ballpark budget, and whether we\'re a fit.',
     'On-site walkthrough &mdash; scope, hazards, and a flat-rate quote in writing.'),
    ('Design &amp; Quote', 'Schedule'),
    ('In-home measure, 3D plans, material selections, fixed-price quote &mdash; before any demo.',
     "Lock in a date that works &mdash; or call after-hours if it's a storm emergency."),
    ('Build It Right', 'Drop It Safely'),
    ('Code-correct framing, plumbing, electrical, finishing &mdash; daily updates, no ghosts.',
     'Climber + ground crew + spotter on every job. Tight rigging, controlled drops, no surprises.'),
    ('Reveal &amp; Warranty', 'Cleanup &amp; Haul'),
    ('Walkthrough, punch list, 15-year workmanship warranty, clean job site at handoff.',
     'Every chip raked, every limb hauled, every stump ground &mdash; yard cleaner than we found it.'),
    # Big quote
    ('Quoted in week one, demoed in week three, finished in week six &mdash; all within a hundred bucks of the original number. Every contractor we\'d hired before would have laughed at this kind of timeline. They actually delivered.',
     "Storm dropped a giant oak across our driveway at midnight. They had a crew on site by 6 a.m., tree gone by noon, driveway swept by 2 p.m. The price matched the quote on the spot. Calling them every time."),
    ('Full Kitchen Remodel &middot; [City]', 'Storm Removal &middot; [City]'),
    ('Janet &amp; David M.', 'David R.'),
    # Service areas
    ('Where We Build.', 'Where We Cut.'),
    # CTA
    ('Ready To<br><em>Sketch It?</em>', 'Tree Down?<br><em>We&#39;re On The Way.</em>'),
    ('Free in-home design visit. Fixed-price quote within five business days. No high-pressure sales script &mdash; just an honest scope and number.',
     '24/7 storm emergency dispatch across [Service Region]. Most calls answered in under 60 seconds. Scheduled jobs get free on-site quotes within 48 hours.'),
    # Form
    ('Full kitchen remodel', 'Tree removal'),
    ('Full bath remodel', 'Tree trimming / pruning'),
    ('Cabinets / refacing', 'Stump grinding'),
    ('Countertops / surfaces', 'Storm / emergency cleanup'),
    ('Custom tile work', 'Lot / land clearing'),
    ('Design consultation only', 'Crane-assist removal'),
    ('Whole-home renovation', 'Other &mdash; not sure'),
    ("Square footage, age of home, what you're hoping to change&hellip;",
     "Tree species, height, location relative to house/wires&hellip;"),
    # Footer
    ('Specialties', 'Services'),
    ('Kitchen Remodels', 'Tree Removal'),
    ('Bath Remodels', 'Tree Trimming'),
    ('Cabinets &amp; Refacing', 'Stump Grinding'),
    ('Countertops', 'Storm Cleanup'),
    ('Custom Tile', 'Lot Clearing'),
    ('Design Consultation', 'Crane Removal'),
    ('Mon&ndash;Fri 8a&ndash;6p<br>Free In-Home Design Visits',
     'Mon&ndash;Fri 7a&ndash;6p &middot; Sat 8a&ndash;2p<br>24/7 Storm Emergency Dispatch'),
    ('Design-build remodelers serving [Service Region]. Fixed-price quotes, real timelines, and a 15-year workmanship warranty on every job.',
     'Family-owned tree removal &amp; care company serving [Service Region]. Licensed, insured, and 24/7 for storm emergencies.'),
    # Social
    ('aria-label="Houzz"', 'aria-label="Google"'),
    # Schema type
    ('"@type": "GeneralContractor"', '"@type": "LocalBusiness"'),
]

for p in PAGES:
    src = os.path.join(REM, p)
    dst = os.path.join(DST, p)
    with open(src, encoding='utf-8') as fh: html = fh.read()
    for old, new in SWAPS:
        html = html.replace(old, new)
    with open(dst, 'w', encoding='utf-8', newline='\n') as fh: fh.write(html)
    print(f'  built {p:25s}  {len(html):6d}b')

# Sitemap
with open(os.path.join(DST, 'sitemap.xml'), 'w', encoding='utf-8', newline='\n') as fh:
    fh.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
             ''.join(f'  <url><loc>[https://yourdomain.com]/{p}</loc><lastmod>2026-05-03</lastmod><changefreq>monthly</changefreq><priority>{pri}</priority></url>\n'
                     for p, pri in [('index.html','1.0'),('about.html','0.8'),('services.html','0.9'),
                                    ('service-areas.html','0.8'),('gallery.html','0.7'),
                                    ('testimonials.html','0.7'),('faq.html','0.7'),
                                    ('contact.html','0.9'),('quote.html','0.9'),
                                    ('privacy.html','0.3'),('terms.html','0.3')]) +
             '</urlset>\n')

# Delete blog files (not used)
for f in ['blog.html']:
    p = os.path.join(DST, f)
    if os.path.exists(p): os.remove(p); print(f'  deleted {f}')
import shutil as sh
blogdir = os.path.join(DST, 'blog')
if os.path.isdir(blogdir): sh.rmtree(blogdir); print('  deleted blog/')

print('\nDone.')
