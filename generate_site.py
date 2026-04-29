from pathlib import Path
import textwrap, json, html

ROOT = Path('/mnt/data/researchlink-arabia')
ASSETS = ROOT / 'assets'
ASSETS.mkdir(exist_ok=True)

SITE = {
    'name_en': 'ResearchLink Arabia',
    'name_ar': 'رابط الباحثين',
    'domain': 'https://researchlinkarabia.com',
    'email': 'info@researchlinkarabia.com',
    'phone': '+966 55 000 0000',
    'whatsapp': '966550000000'
}

NAV = [
    ('الرئيسية', 'index.html'),
    ('من نحن', 'about.html'),
    ('الفرص البحثية', 'research-opportunities.html'),
    ('الخدمات', 'services.html'),
    ('التدريب', 'research-training.html'),
    ('المدونة', 'blog.html'),
    ('الأسئلة الشائعة', 'faq.html'),
    ('تواصل معنا', 'contact.html'),
]

pages = []

def slug_to_url(slug):
    return SITE['domain'] + '/' + ('' if slug == 'index.html' else slug)

def layout(title, description, keywords, slug, body, extra_head='', schema=None):
    canonical = slug_to_url(slug)
    nav_html = ''.join(f'<a href="{href}" class="nav-link">{label}</a>' for label, href in NAV)
    schema_json = ''
    org_schema = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": SITE['name_en'],
        "alternateName": SITE['name_ar'],
        "url": SITE['domain'],
        "logo": SITE['domain'] + "/assets/logo.svg",
        "contactPoint": {
            "@type": "ContactPoint",
            "contactType": "customer support",
            "email": SITE['email'],
            "availableLanguage": ["Arabic", "English"]
        }
    }
    breadcrumb_schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type":"ListItem", "position":1, "name":"الرئيسية", "item": SITE['domain'] + "/"},
            {"@type":"ListItem", "position":2, "name": title.split('|')[0].strip(), "item": canonical}
        ]
    }
    schemas = [org_schema, breadcrumb_schema]
    if schema:
        schemas.append(schema)
    schema_json = '\n'.join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schemas)
    return f'''<!doctype html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(description)}">
  <meta name="keywords" content="{html.escape(keywords)}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{canonical}">
  <meta property="og:title" content="{html.escape(title)}">
  <meta property="og:description" content="{html.escape(description)}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:locale" content="ar_AR">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" type="image/svg+xml" href="assets/favicon.svg">
  <link rel="preload" href="assets/styles.css" as="style">
  <link rel="stylesheet" href="assets/styles.css">
  {extra_head}
  {schema_json}
</head>
<body>
  <a class="skip-link" href="#main">تخطي إلى المحتوى</a>
  <header class="site-header" id="top">
    <div class="container nav-wrap">
      <a href="index.html" class="brand" aria-label="ResearchLink Arabia home">
        <img src="assets/logo.svg" alt="شعار ResearchLink Arabia" width="46" height="46">
        <span><strong>{SITE['name_ar']}</strong><small>{SITE['name_en']}</small></span>
      </a>
      <button class="menu-toggle" aria-expanded="false" aria-controls="site-nav">☰</button>
      <nav class="site-nav" id="site-nav" aria-label="القائمة الرئيسية">
        {nav_html}
        <a href="contact.html" class="btn btn-primary btn-small">انضم الآن</a>
      </nav>
    </div>
  </header>
  <main id="main">
    {body}
  </main>
  <footer class="site-footer">
    <div class="container footer-grid">
      <div>
        <a href="index.html" class="footer-brand"><img src="assets/logo.svg" alt="" width="42" height="42"><span>{SITE['name_ar']}</span></a>
        <p>منصة عربية متخصصة في ربط الأطباء وطلاب الطب والباحثين الصحيين بفرص بحثية منظمة وخدمات دعم النشر العلمي.</p>
      </div>
      <div>
        <h3>روابط سريعة</h3>
        <a href="research-opportunities.html">الفرص البحثية</a>
        <a href="services.html">الخدمات البحثية</a>
        <a href="scientific-publication.html">النشر العلمي</a>
        <a href="faq.html">الأسئلة الشائعة</a>
      </div>
      <div>
        <h3>خدمات متخصصة</h3>
        <a href="saudi-board-research.html">البورد السعودي والبحث العلمي</a>
        <a href="smle-research.html">SMLE والبحث الطبي</a>
        <a href="statistical-analysis.html">التحليل الإحصائي</a>
        <a href="systematic-review-service.html">المراجعات المنهجية</a>
      </div>
      <div>
        <h3>تواصل</h3>
        <p>البريد: <a href="mailto:{SITE['email']}">{SITE['email']}</a></p>
        <p>واتساب: <a href="https://wa.me/{SITE['whatsapp']}">{SITE['phone']}</a></p>
        <div class="footer-actions"><a href="contact.html" class="btn btn-light">اطلب استشارة</a></div>
      </div>
    </div>
    <div class="container footer-bottom">
      <span>© 2026 {SITE['name_en']}. جميع الحقوق محفوظة.</span>
      <span><a href="privacy-policy.html">سياسة الخصوصية</a> · <a href="terms.html">الشروط والأحكام</a></span>
    </div>
  </footer>
  <a href="https://wa.me/{SITE['whatsapp']}" class="whatsapp-float" aria-label="تواصل عبر واتساب">واتساب</a>
  <script src="assets/script.js"></script>
</body>
</html>'''

def section_header(eyebrow, h1, lead, actions=None):
    actions_html = ''
    if actions:
        actions_html = '<div class="hero-actions">' + ''.join(f'<a href="{href}" class="btn {cls}">{label}</a>' for label, href, cls in actions) + '</div>'
    return f'''
<section class="page-hero">
  <div class="container hero-content slim">
    <span class="eyebrow">{eyebrow}</span>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
    {actions_html}
  </div>
</section>
'''

def card_grid(items, cols='three'):
    return '<div class="card-grid '+cols+'">' + ''.join(f'''
      <article class="info-card">
        <div class="card-icon">{icon}</div>
        <h3>{title}</h3>
        <p>{desc}</p>
      </article>''' for icon,title,desc in items) + '</div>'

def write_page(slug, title, description, keywords, body, extra_head='', schema=None):
    (ROOT / slug).write_text(layout(title, description, keywords, slug, body, extra_head, schema), encoding='utf-8')
    pages.append((slug, title, description))

# Assets
(ASSETS / 'logo.svg').write_text('''<svg width="128" height="128" viewBox="0 0 128 128" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect width="128" height="128" rx="28" fill="#0B2742"/>
<path d="M34 68C34 51.4315 47.4315 38 64 38H93V50H64C54.0589 50 46 58.0589 46 68C46 77.9411 54.0589 86 64 86H94V98H64C47.4315 98 34 84.5685 34 68Z" fill="#47D6C8"/>
<path d="M34 30H74C89.464 30 102 42.536 102 58C102 73.464 89.464 86 74 86H55V74H74C82.837 74 90 66.837 90 58C90 49.163 82.837 42 74 42H34V30Z" fill="#F4C95D"/>
<circle cx="64" cy="68" r="8" fill="white"/>
</svg>''', encoding='utf-8')

(ASSETS / 'favicon.svg').write_text('''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg"><rect width="64" height="64" rx="14" fill="#0B2742"/><path d="M17 34C17 25.7 23.7 19 32 19H47V25H32C26.5 25 22 29.5 22 35C22 40.5 26.5 45 32 45H48V51H32C23.7 51 17 44.3 17 36V34Z" fill="#47D6C8"/><path d="M17 14H37C45.8 14 53 21.2 53 30C53 38.8 45.8 46 37 46H28V40H37C42.5 40 47 35.5 47 30C47 24.5 42.5 20 37 20H17V14Z" fill="#F4C95D"/><circle cx="32" cy="35" r="4" fill="white"/></svg>''', encoding='utf-8')

(ASSETS / 'styles.css').write_text(r'''
:root{
  --navy:#0B2742; --navy-2:#123A5B; --teal:#47D6C8; --teal-dark:#19AFA2; --gold:#F4C95D; --paper:#F8FBFC; --white:#fff; --ink:#102033; --muted:#5D6B7A; --line:#DDE8EE; --shadow:0 18px 45px rgba(11,39,66,.12); --radius:24px; --radius-sm:16px;
}
*{box-sizing:border-box} html{scroll-behavior:smooth} body{margin:0;font-family:"Tahoma","Arial",sans-serif;background:var(--paper);color:var(--ink);line-height:1.8} a{color:inherit;text-decoration:none} img{max-width:100%;height:auto}.container{width:min(1160px,calc(100% - 32px));margin-inline:auto}.skip-link{position:absolute;top:-80px;right:20px;background:#fff;padding:10px 14px;border-radius:10px;z-index:99}.skip-link:focus{top:14px}.site-header{position:sticky;top:0;background:rgba(248,251,252,.88);backdrop-filter:blur(18px);border-bottom:1px solid rgba(221,232,238,.8);z-index:50}.nav-wrap{display:flex;align-items:center;justify-content:space-between;min-height:82px}.brand,.footer-brand{display:flex;align-items:center;gap:12px}.brand strong{display:block;font-size:1.12rem}.brand small{display:block;color:var(--muted);font-size:.78rem;direction:ltr;text-align:right}.site-nav{display:flex;align-items:center;gap:6px}.nav-link{padding:9px 11px;border-radius:12px;color:#263B50;font-weight:700;font-size:.94rem}.nav-link:hover{background:#EAF4F7;color:var(--navy)}.menu-toggle{display:none;background:var(--navy);color:#fff;border:0;border-radius:14px;padding:10px 14px;font-size:1.2rem}.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;border-radius:999px;padding:13px 22px;font-weight:800;border:1px solid transparent;transition:.2s ease;cursor:pointer}.btn-primary{background:linear-gradient(135deg,var(--teal),#25B7AA);color:#06283A;box-shadow:0 10px 24px rgba(71,214,200,.28)}.btn-primary:hover{transform:translateY(-2px);box-shadow:0 18px 36px rgba(71,214,200,.32)}.btn-secondary{background:var(--navy);color:#fff}.btn-outline{border-color:#B9D2DC;background:#fff;color:var(--navy)}.btn-light{background:#fff;color:var(--navy)}.btn-small{padding:9px 16px;font-size:.9rem}.hero{position:relative;overflow:hidden;background:radial-gradient(circle at 15% 20%,rgba(71,214,200,.25),transparent 25%),linear-gradient(135deg,#F7FCFD 0%,#EAF5F8 100%);padding:84px 0 68px}.hero::after{content:"";position:absolute;inset:auto -120px -180px auto;width:420px;height:420px;background:rgba(244,201,93,.25);border-radius:50%;filter:blur(6px)}.hero-grid{display:grid;grid-template-columns:1.1fr .9fr;gap:44px;align-items:center;position:relative;z-index:1}.eyebrow{display:inline-flex;align-items:center;gap:8px;background:#E8FFFC;color:#087F76;border:1px solid #C6F5EF;padding:7px 14px;border-radius:999px;font-size:.88rem;font-weight:800}.hero h1,.page-hero h1{font-size:clamp(2rem,5vw,4.1rem);line-height:1.22;margin:20px 0 16px;color:var(--navy);letter-spacing:-1.2px}.lead{font-size:1.12rem;color:var(--muted);max-width:760px}.hero-actions{display:flex;gap:12px;flex-wrap:wrap;margin-top:28px}.hero-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:34px}.stat-card{background:rgba(255,255,255,.82);border:1px solid var(--line);border-radius:18px;padding:16px;box-shadow:0 12px 28px rgba(11,39,66,.07)}.stat-card strong{display:block;color:var(--navy);font-size:1.5rem}.visual-card{background:var(--white);border:1px solid var(--line);border-radius:32px;padding:24px;box-shadow:var(--shadow);position:relative}.research-panel{background:linear-gradient(160deg,var(--navy),#16506E);color:#fff;border-radius:26px;padding:24px;min-height:360px;position:relative;overflow:hidden}.research-panel::before{content:"";position:absolute;width:230px;height:230px;border:46px solid rgba(71,214,200,.18);border-radius:50%;left:-60px;top:-80px}.panel-top{position:relative;z-index:1;display:flex;justify-content:space-between;gap:16px;align-items:flex-start}.badge{background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.2);border-radius:999px;padding:7px 12px;font-size:.85rem}.project-list{position:relative;z-index:1;display:grid;gap:14px;margin-top:30px}.project-item{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.14);border-radius:18px;padding:16px}.project-item span{display:block;color:#B9F4EE;font-size:.85rem}.section{padding:72px 0}.section.alt{background:#fff}.section-title{max-width:780px;margin:0 auto 36px;text-align:center}.section-title h2{font-size:clamp(1.8rem,3.2vw,2.7rem);line-height:1.3;margin:10px 0;color:var(--navy)}.section-title p{color:var(--muted);margin:0}.card-grid{display:grid;gap:18px}.card-grid.three{grid-template-columns:repeat(3,1fr)}.card-grid.two{grid-template-columns:repeat(2,1fr)}.info-card,.service-card,.article-card,.opportunity-card,.faq-card{background:#fff;border:1px solid var(--line);border-radius:var(--radius);padding:24px;box-shadow:0 12px 30px rgba(11,39,66,.06);transition:.2s ease}.info-card:hover,.service-card:hover,.article-card:hover,.opportunity-card:hover{transform:translateY(-4px);box-shadow:var(--shadow)}.card-icon{width:46px;height:46px;border-radius:16px;display:flex;align-items:center;justify-content:center;background:#E8FFFC;color:#0B8C82;font-size:1.4rem;margin-bottom:12px}.info-card h3,.service-card h3,.article-card h3,.opportunity-card h3{color:var(--navy);margin:6px 0 8px;font-size:1.18rem}.info-card p,.service-card p,.article-card p,.opportunity-card p,.faq-card p{color:var(--muted);margin:0}.split{display:grid;grid-template-columns:1fr 1fr;gap:36px;align-items:center}.feature-list{display:grid;gap:14px}.feature-item{display:flex;gap:14px;align-items:flex-start;background:#fff;border:1px solid var(--line);border-radius:18px;padding:16px}.check{flex:none;width:28px;height:28px;border-radius:50%;background:var(--teal);color:var(--navy);display:flex;align-items:center;justify-content:center;font-weight:900}.timeline{counter-reset:step;display:grid;gap:18px}.step{counter-increment:step;position:relative;background:#fff;border:1px solid var(--line);border-radius:22px;padding:22px 78px 22px 22px;box-shadow:0 10px 28px rgba(11,39,66,.05)}.step::before{content:counter(step);position:absolute;right:22px;top:22px;width:38px;height:38px;border-radius:14px;background:var(--navy);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:900}.cta{background:linear-gradient(135deg,var(--navy),#144969);color:#fff;border-radius:32px;padding:42px;display:grid;grid-template-columns:1fr auto;gap:20px;align-items:center;overflow:hidden;position:relative}.cta h2{margin:0 0 10px;font-size:2rem}.cta p{margin:0;color:#D6E9EF}.page-hero{background:linear-gradient(135deg,#F7FCFD,#EAF5F8);padding:66px 0 50px;border-bottom:1px solid var(--line)}.hero-content.slim{max-width:900px}.breadcrumb{font-size:.9rem;color:var(--muted);margin-bottom:12px}.content-section{padding:56px 0}.prose{background:#fff;border:1px solid var(--line);border-radius:var(--radius);padding:32px;box-shadow:0 12px 30px rgba(11,39,66,.05)}.prose h2,.prose h3{color:var(--navy)}.prose p,.prose li{color:#4A5969}.service-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.tag-list{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}.tag{background:#F0F7FA;border:1px solid #D8E8EF;border-radius:999px;padding:6px 10px;color:#31546A;font-size:.85rem;font-weight:700}.filters{display:flex;gap:10px;flex-wrap:wrap;margin:0 0 20px}.filter-btn{border:1px solid var(--line);background:#fff;border-radius:999px;padding:9px 14px;cursor:pointer;font-weight:800;color:var(--navy)}.filter-btn.active{background:var(--navy);color:#fff}.opportunities-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.opportunity-meta{display:flex;gap:8px;flex-wrap:wrap;margin:12px 0}.meta{background:#F0F7FA;border-radius:999px;padding:5px 10px;font-size:.82rem;color:#365C70}.status{display:inline-flex;padding:6px 10px;border-radius:999px;background:#E8FFFC;color:#087F76;font-weight:800;font-size:.82rem}.faq-list{display:grid;gap:14px}.faq-card button{width:100%;background:none;border:0;text-align:right;font:inherit;font-weight:900;color:var(--navy);cursor:pointer;display:flex;justify-content:space-between;gap:16px;padding:0}.faq-card .answer{display:none;margin-top:10px}.faq-card.open .answer{display:block}.contact-grid{display:grid;grid-template-columns:.85fr 1.15fr;gap:22px}.contact-box{background:#fff;border:1px solid var(--line);border-radius:24px;padding:24px;box-shadow:0 12px 30px rgba(11,39,66,.05)}.form-grid{display:grid;gap:14px}.input-group{display:grid;gap:7px}.input-group label{font-weight:800;color:var(--navy)}input,select,textarea{width:100%;border:1px solid #CFE0E7;border-radius:14px;padding:13px 14px;font:inherit;background:#fff;color:var(--ink)}textarea{min-height:140px;resize:vertical}.site-footer{background:var(--navy);color:#D8E7EE;padding:52px 0 18px}.footer-grid{display:grid;grid-template-columns:1.2fr .8fr .9fr 1fr;gap:30px}.footer-brand span{font-weight:900;color:#fff;font-size:1.2rem}.site-footer h3{color:#fff;margin-top:0}.site-footer a{display:block;color:#D8E7EE;margin:7px 0}.site-footer p{color:#C5DAE4}.footer-bottom{margin-top:32px;padding-top:20px;border-top:1px solid rgba(255,255,255,.14);display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}.footer-bottom a{display:inline}.whatsapp-float{position:fixed;left:18px;bottom:18px;background:#19B569;color:#fff;padding:13px 18px;border-radius:999px;font-weight:900;box-shadow:0 12px 28px rgba(25,181,105,.35);z-index:40}.table-wrap{overflow:auto;background:#fff;border:1px solid var(--line);border-radius:22px}table{width:100%;border-collapse:collapse;min-width:680px}th,td{text-align:right;padding:15px;border-bottom:1px solid var(--line)}th{background:#F0F7FA;color:var(--navy)}tr:last-child td{border-bottom:0}.article-card a{color:var(--navy)}.blog-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.notice{background:#FFF8E6;border:1px solid #F2D580;color:#664D00;padding:16px 18px;border-radius:18px}.success-message{display:none;background:#E8FFFC;border:1px solid #AFEDE6;color:#096B64;border-radius:16px;padding:14px;margin-top:12px}
@media (max-width: 960px){.hero-grid,.split,.contact-grid,.cta{grid-template-columns:1fr}.card-grid.three,.service-grid,.opportunities-grid,.blog-grid,.footer-grid{grid-template-columns:repeat(2,1fr)}.cta{padding:28px}.site-nav{position:fixed;inset:82px 16px auto 16px;background:#fff;border:1px solid var(--line);box-shadow:var(--shadow);border-radius:22px;padding:16px;display:none;flex-direction:column;align-items:stretch}.site-nav.open{display:flex}.menu-toggle{display:block}.nav-link{text-align:center}.hero{padding-top:54px}.hero-stats{grid-template-columns:1fr 1fr}}
@media (max-width: 640px){.container{width:min(100% - 22px,1160px)}.card-grid.three,.card-grid.two,.service-grid,.opportunities-grid,.blog-grid,.footer-grid{grid-template-columns:1fr}.hero-stats{grid-template-columns:1fr}.hero h1,.page-hero h1{font-size:2.05rem}.visual-card{padding:12px}.research-panel{min-height:300px}.section{padding:50px 0}.footer-bottom{display:block}.brand small{display:none}.step{padding:22px}.step::before{position:static;margin-bottom:12px}.whatsapp-float{left:12px;bottom:12px;padding:11px 14px}.hero-actions .btn{width:100%}}
''', encoding='utf-8')

(ASSETS / 'script.js').write_text(r'''
const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('#site-nav');
if (toggle && nav) {
  toggle.addEventListener('click', () => {
    const isOpen = nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', String(isOpen));
  });
}

document.querySelectorAll('.faq-card button').forEach(btn => {
  btn.addEventListener('click', () => {
    const card = btn.closest('.faq-card');
    card.classList.toggle('open');
  });
});

document.querySelectorAll('[data-filter]').forEach(btn => {
  btn.addEventListener('click', () => {
    const value = btn.dataset.filter;
    document.querySelectorAll('[data-filter]').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    document.querySelectorAll('[data-category]').forEach(card => {
      card.style.display = value === 'all' || card.dataset.category === value ? '' : 'none';
    });
  });
});

const contactForm = document.querySelector('#contact-form');
if(contactForm){
  contactForm.addEventListener('submit', function(e){
    e.preventDefault();
    const msg = document.querySelector('.success-message');
    if(msg) msg.style.display = 'block';
    contactForm.reset();
  });
}
''', encoding='utf-8')

# Home page
home_body = '''
<section class="hero">
  <div class="container hero-grid">
    <div>
      <span class="eyebrow">منصة بحثية طبية عربية</span>
      <h1>ابنِ مسيرتك البحثية مع فرص طبية موثوقة</h1>
      <p class="lead">رابط الباحثين منصة تساعد الأطباء وطلاب الطب والباحثين الصحيين على الوصول إلى فرص بحثية منظمة، فرق بحثية متخصصة، تدريب عملي، ودعم في النشر العلمي داخل السعودية والخليج.</p>
      <div class="hero-actions">
        <a href="research-opportunities.html" class="btn btn-primary">استعرض الفرص البحثية</a>
        <a href="how-it-works.html" class="btn btn-outline">كيف تعمل المنصة؟</a>
      </div>
      <div class="hero-stats" aria-label="مؤشرات المنصة">
        <div class="stat-card"><strong>+120</strong><span>فرصة بحثية سنويًا</span></div>
        <div class="stat-card"><strong>15</strong><span>تخصصًا صحيًا</span></div>
        <div class="stat-card"><strong>عن بُعد</strong><span>مشاركة مرنة</span></div>
      </div>
    </div>
    <div class="visual-card">
      <div class="research-panel">
        <div class="panel-top">
          <div><span class="badge">فرص مفتوحة الآن</span><h2>مشاريع بحثية حسب التخصص والخبرة</h2></div>
          <span class="badge">2026</span>
        </div>
        <div class="project-list">
          <div class="project-item"><span>Systematic Review</span><strong>جودة الرعاية الصحية وسلامة المرضى</strong></div>
          <div class="project-item"><span>Cross-sectional Study</span><strong>الصحة الرقمية وتجربة المرضى</strong></div>
          <div class="project-item"><span>Data Analysis</span><strong>تحليل بيانات سريرية وبحثية</strong></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-title"><span class="eyebrow">لماذا نحن؟</span><h2>منصة مصممة لتسهيل البحث العلمي الطبي</h2><p>نربط الباحثين بالفرص المناسبة ونوفر مسارًا واضحًا من الفكرة إلى النشر.</p></div>
    ''' + card_grid([
      ('🔬','فرص بحثية منظمة','فرص مصنفة حسب التخصص، نوع الدراسة، ومستوى الخبرة حتى تختار المشروع المناسب لك.'),
      ('👥','فرق بحثية متعددة التخصصات','تواصل مع أطباء وباحثين ومشرفين لبناء تعاون علمي احترافي.'),
      ('📊','دعم منهجي وإحصائي','مساعدة في تصميم الدراسة، جمع البيانات، التحليل الإحصائي، وكتابة النتائج.'),
      ('📚','دعم النشر العلمي','إرشاد في تحسين المخطوطات واختيار المجلات المناسبة ومتطلبات التقديم.'),
      ('🎓','تدريب بحثي عملي','برامج قصيرة تساعد المبتدئين على فهم خطوات البحث الطبي والنشر.'),
      ('✅','مناسب للبورد والسيرة العلمية','يساعد الأطباء والطلاب على بناء خبرة بحثية منظمة وقابلة للعرض في السيرة الذاتية.')
    ]) + '''
  </div>
</section>

<section class="section alt">
  <div class="container split">
    <div>
      <span class="eyebrow">الخدمات</span>
      <h2>حلول بحثية متكاملة في مكان واحد</h2>
      <p class="lead">سواء كنت تبدأ أول بحث أو تعمل على نشر دراسة متقدمة، نقدم خدمات تساعدك في كل مرحلة.</p>
      <div class="hero-actions"><a href="services.html" class="btn btn-primary">عرض جميع الخدمات</a><a href="contact.html" class="btn btn-outline">استشارة مجانية</a></div>
    </div>
    <div class="feature-list">
      <div class="feature-item"><span class="check">✓</span><div><strong>إعداد مقترح بحثي</strong><p>صياغة سؤال البحث، الأهداف، المنهجية، وخطة جمع البيانات.</p></div></div>
      <div class="feature-item"><span class="check">✓</span><div><strong>مراجعات منهجية</strong><p>دعم في البحث، الفرز، استخراج البيانات، وتقييم جودة الدراسات.</p></div></div>
      <div class="feature-item"><span class="check">✓</span><div><strong>تحليل إحصائي</strong><p>اختيار الاختبارات المناسبة وتفسير النتائج بطريقة أكاديمية واضحة.</p></div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-title"><span class="eyebrow">كيف تبدأ؟</span><h2>رحلة بحثية واضحة في خمس خطوات</h2></div>
    <div class="timeline">
      <div class="step"><h3>أنشئ حسابك أو تواصل معنا</h3><p>أرسل تخصصك ومستوى خبرتك واهتماماتك البحثية.</p></div>
      <div class="step"><h3>اختر الفرصة المناسبة</h3><p>نرشح لك فرصًا حسب التخصص ونوع البحث والوقت المتاح.</p></div>
      <div class="step"><h3>انضم للفريق البحثي</h3><p>تبدأ العمل مع فريق واضح المهام والمخرجات.</p></div>
      <div class="step"><h3>نفّذ البحث بجودة أكاديمية</h3><p>تعمل على جمع البيانات، التحليل، الكتابة، والمراجعة.</p></div>
      <div class="step"><h3>جهّز البحث للنشر</h3><p>يتم تحسين المخطوط واختيار المجلة أو المؤتمر المناسب.</p></div>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="container">
    <div class="cta">
      <div><h2>جاهز تبدأ أول خطوة بحثية؟</h2><p>أرسل لنا تخصصك واهتماماتك، وسنساعدك على اختيار المسار البحثي المناسب.</p></div>
      <a href="contact.html" class="btn btn-light">انضم الآن</a>
    </div>
  </div>
</section>
'''
write_page('index.html', 'فرص بحثية طبية ونشر علمي للأطباء | ResearchLink Arabia', 'منصة رابط الباحثين تربط الأطباء وطلاب الطب والباحثين بفرص بحثية طبية، دعم النشر العلمي، التحليل الإحصائي، والتدريب البحثي في السعودية والخليج.', 'فرص بحثية طبية, نشر بحث علمي, البورد السعودي, SMLE, أبحاث طبية, تدريب بحثي', home_body)

# About page
about_body = section_header('من نحن', 'منصة عربية لدعم البحث العلمي الطبي', 'نساعد الأطباء وطلاب الطب والباحثين الصحيين على الوصول إلى فرص بحثية منظمة وبناء خبرة علمية عملية قابلة للتطوير.', [('تواصل معنا','contact.html','btn-primary'),('الخدمات','services.html','btn-outline')]) + '''
<section class="content-section"><div class="container split"><div class="prose"><h2>رؤيتنا</h2><p>أن تكون رابط الباحثين منصة عربية رائدة في تسهيل التعاون البحثي الطبي، وتمكين الباحثين من إنتاج أبحاث ذات جودة علمية وتأثير مهني واضح.</p><h2>رسالتنا</h2><p>توفير بيئة منظمة تجمع بين الباحثين، الفرق البحثية، والخبرات الأكاديمية، مع تقديم دعم عملي في التصميم البحثي، التحليل، الكتابة، والنشر.</p></div><div class="feature-list"><div class="feature-item"><span class="check">✓</span><div><strong>مصداقية</strong><p>نركز على فرص واضحة ومخرجات قابلة للقياس.</p></div></div><div class="feature-item"><span class="check">✓</span><div><strong>تعلم عملي</strong><p>المشاركة لا تقتصر على الاسم، بل على اكتساب مهارات بحثية حقيقية.</p></div></div><div class="feature-item"><span class="check">✓</span><div><strong>جودة أكاديمية</strong><p>نعتمد خطوات منظمة تناسب طبيعة الدراسات الطبية والصحية.</p></div></div></div></div></section>
<section class="section alt"><div class="container"><div class="section-title"><h2>من نخدم؟</h2><p>الفئات المستفيدة من المنصة</p></div>'''+card_grid([('🩺','طلاب الطب','لبناء أساس بحثي مبكر ومهارات أكاديمية قوية.'),('🏥','أطباء الامتياز والمقيمون','للمشاركة في أبحاث تدعم المسار المهني والتقديمات الأكاديمية.'),('🔬','الباحثون الصحيون','للتعاون في مشاريع متعددة التخصصات وتوسيع شبكة البحث.'),('🎓','المهتمون بالبورد السعودي','لتطوير خبرة بحثية منظمة تساعد في السيرة العلمية.'),('📈','فرق البحث','للوصول إلى مشاركين ومهارات بحثية مكملة.'),('🌍','الباحثون في الخليج','لتسهيل التعاون عن بعد في مشاريع صحية مشتركة.')]) + '</div></section>'
write_page('about.html', 'من نحن | ResearchLink Arabia', 'تعرف على منصة رابط الباحثين، رؤيتنا ورسالتنا في دعم البحث العلمي الطبي وربط الباحثين بفرص بحثية موثوقة في السعودية والخليج.', 'منصة بحثية طبية, تعاون بحثي, أطباء باحثون, السعودية الخليج', about_body)

# Opportunities
opps = [
    ('مراجعة منهجية حول سلامة المرضى','systematic','Systematic Review','مفتوحة','مناسبة للمبتدئين','دراسة تقارن العوامل المؤثرة في سلامة المرضى وجودة الرعاية في المستشفيات.'),
    ('الصحة الرقمية وتجربة المرضى','clinical','Cross-sectional','مفتوحة','متوسط','فرصة لدراسة استخدام التطبيقات الصحية وتأثيرها على رضا المرضى.'),
    ('تحليل بيانات سريرية','data','Data Analysis','قريبًا','متقدم','مشروع يعتمد على تحليل بيانات سريرية واستخراج نتائج قابلة للنشر.'),
    ('مراجعة حول الذكاء الاصطناعي في التشخيص','systematic','Scoping Review','مفتوحة','متوسط','رصد الاتجاهات البحثية في تطبيقات الذكاء الاصطناعي في التشخيص الطبي.'),
    ('بحث حول تدريب طلاب الطب','clinical','Survey Study','مفتوحة','مبتدئ','استبيان أكاديمي حول مهارات البحث العلمي لدى طلاب الطب.'),
    ('Meta-analysis في الصحة العامة','systematic','Meta-analysis','قريبًا','متقدم','مشروع متخصص يتطلب خبرة في التحليل الإحصائي وتجميع النتائج.')
]
opps_html = ''.join(f'''<article class="opportunity-card" data-category="{cat}"><span class="status">{status}</span><h3>{title}</h3><p>{desc}</p><div class="opportunity-meta"><span class="meta">{typ}</span><span class="meta">{level}</span></div><a href="contact.html" class="btn btn-outline btn-small">التقديم على الفرصة</a></article>''' for title,cat,typ,status,level,desc in opps)
opp_schema = {"@context":"https://schema.org","@type":"CollectionPage","name":"فرص بحثية طبية","description":"قائمة فرص بحثية طبية للأطباء وطلاب الطب والباحثين الصحيين."}
opp_body = section_header('الفرص البحثية', 'استعرض أحدث الفرص البحثية الطبية', 'فرص بحثية مصنفة حسب نوع الدراسة، مستوى الخبرة، والتخصص الصحي، مع إمكانية المشاركة عن بعد في مشاريع مختارة.') + f'''
<section class="content-section"><div class="container"><div class="filters" aria-label="تصفية الفرص"><button class="filter-btn active" data-filter="all">الكل</button><button class="filter-btn" data-filter="systematic">مراجعات منهجية</button><button class="filter-btn" data-filter="clinical">دراسات ميدانية</button><button class="filter-btn" data-filter="data">تحليل بيانات</button></div><div class="opportunities-grid">{opps_html}</div></div></section>
<section class="section alt"><div class="container"><div class="cta"><div><h2>لم تجد الفرصة المناسبة؟</h2><p>أرسل تخصصك واهتماماتك وسنخبرك عند توفر مشروع مناسب.</p></div><a href="contact.html" class="btn btn-light">سجل اهتمامك</a></div></div></section>
'''
write_page('research-opportunities.html', 'فرص بحثية طبية للأطباء وطلاب الطب | ResearchLink Arabia', 'استعرض فرص بحثية طبية في تخصصات متعددة، وانضم إلى فرق بحثية مناسبة للأطباء وطلاب الطب وأطباء الامتياز والمقيمين.', 'فرص بحثية, فرص بحثية طبية, بحث طبي, أطباء امتياز, طلاب الطب', opp_body, schema=opp_schema)

# Services
service_items = [
('🔎','فرص بحثية','ربط الباحثين بمشاريع بحثية قائمة حسب التخصص والخبرة.','research-opportunities.html'),
('📝','إعداد مقترح بحثي','تطوير سؤال البحث والأهداف والمنهجية وخطة العمل.','services.html#proposal'),
('📊','تحليل إحصائي','تحليل البيانات، اختيار الاختبارات المناسبة، وتفسير النتائج.','statistical-analysis.html'),
('📚','المراجعات المنهجية','دعم في Systematic Review وMeta-analysis وScoping Review.','systematic-review-service.html'),
('🧾','دعم النشر العلمي','تحسين المخطوطات، اختيار المجلات، وتجهيز متطلبات التقديم.','scientific-publication.html'),
('🎓','التدريب البحثي','ورش عملية في أساسيات البحث الطبي والكتابة الأكاديمية.','research-training.html')
]
services_body = section_header('الخدمات البحثية', 'خدمات بحثية متكاملة للقطاع الصحي', 'من الفكرة وحتى النشر، نقدم خدمات تساعد الباحث على تنفيذ مشروعه بجودة أكاديمية واضحة.') + '<section class="content-section"><div class="container"><div class="service-grid">' + ''.join(f'''<article class="service-card"><div class="card-icon">{icon}</div><h3>{title}</h3><p>{desc}</p><a href="{href}" class="btn btn-outline btn-small">تفاصيل الخدمة</a></article>''' for icon,title,desc,href in service_items) + '</div></div></section>' + '''
<section class="section alt" id="proposal"><div class="container split"><div class="prose"><h2>ماذا تشمل خدماتنا؟</h2><ul><li>تحديد فكرة بحثية قابلة للتنفيذ.</li><li>صياغة أهداف البحث وأسئلته.</li><li>تصميم المنهجية واختيار العينة والأدوات.</li><li>خطة جمع البيانات وتحليلها.</li><li>كتابة النتائج والمناقشة بطريقة أكاديمية.</li><li>تجهيز البحث للنشر أو العرض في مؤتمر.</li></ul></div><div class="prose"><h2>لمن تناسب؟</h2><p>الخدمات مناسبة للطلاب، أطباء الامتياز، المقيمين، الباحثين الصحيين، والفرق البحثية التي تحتاج إلى دعم منظم في مرحلة محددة من المشروع أو في كامل المسار البحثي.</p><div class="hero-actions"><a href="contact.html" class="btn btn-primary">اطلب الخدمة</a></div></div></div></section>
'''
write_page('services.html', 'الخدمات البحثية الطبية | ResearchLink Arabia', 'خدمات بحثية تشمل الفرص البحثية، إعداد المقترحات، التحليل الإحصائي، المراجعات المنهجية، دعم النشر، والتدريب البحثي.', 'خدمات بحثية طبية, تحليل إحصائي, مراجعة منهجية, نشر علمي, مقترح بحثي', services_body)

# Scientific Publication
pub_body = section_header('النشر العلمي', 'دعم احترافي للنشر في المجلات العلمية', 'نساعد الباحثين في تحسين المخطوطات البحثية، اختيار المجلات المناسبة، وفهم متطلبات التقديم الأكاديمي.', [('اطلب دعم النشر','contact.html','btn-primary')]) + '''
<section class="content-section"><div class="container split"><div class="prose"><h2>مراحل دعم النشر</h2><ol><li>مراجعة جاهزية البحث للنشر.</li><li>تحسين الهيكل الأكاديمي واللغة العلمية.</li><li>اختيار قائمة مجلات مناسبة حسب التخصص والنطاق.</li><li>تجهيز خطاب التقديم والملفات المطلوبة.</li><li>مراجعة ملاحظات المحكمين عند الحاجة.</li></ol></div><div class="prose"><h2>تنبيه أخلاقي مهم</h2><p>لا نضمن قبول البحث في مجلة علمية، لأن قرار النشر يعود للمجلة والمحكمين. دورنا هو تحسين جودة المخطوط وتجهيزه بطريقة أكاديمية تزيد فرص المراجعة الجادة.</p></div></div></section>
<section class="section alt"><div class="container"><div class="section-title"><h2>ما الذي تحصل عليه؟</h2></div>'''+card_grid([('✅','تقييم المخطوط','ملاحظات عملية حول نقاط القوة والضعف.'),('🎯','ترشيح مجلات','اقتراح مجلات مناسبة لنطاق البحث.'),('🧾','تجهيز الملفات','تنظيم المتطلبات الأساسية للتقديم.'),('🔁','دعم بعد التحكيم','مساعدة في الرد على ملاحظات المحكمين عند الحاجة.')], 'two') + '</div></section>'
write_page('scientific-publication.html', 'دعم النشر العلمي الطبي في المجلات المحكمة | ResearchLink Arabia', 'نساعد الباحثين في تجهيز الأبحاث الطبية للنشر، تحسين جودة المخطوطات، اختيار المجلات المناسبة، ومراجعة المتطلبات الأكاديمية.', 'نشر علمي, مجلة محكمة, بحث طبي, Manuscript, نشر بحث طبي', pub_body)

# Saudi Board
sb_body = section_header('البورد السعودي', 'البحث العلمي ودوره في مسيرة أطباء البورد السعودي', 'صفحة مخصصة للأطباء والطلاب المهتمين ببناء سجل بحثي منظم يدعم سيرتهم العلمية ومسارهم المهني.', [('ابدأ مسارك البحثي','contact.html','btn-primary')]) + '''
<section class="content-section"><div class="container split"><div class="prose"><h2>كيف تساعدك المنصة؟</h2><p>توفر رابط الباحثين فرصًا بحثية منظمة، تدريبًا عمليًا، ودعمًا في إعداد الدراسات بما يساعد الطبيب على بناء خبرة بحثية واضحة قابلة للعرض في السيرة الذاتية والمقابلات الأكاديمية.</p><h3>أمثلة مسارات مناسبة</h3><ul><li>المشاركة في مراجعة منهجية.</li><li>تصميم دراسة استبيانية في تخصص صحي.</li><li>تحليل بيانات سريرية.</li><li>إعداد ملخص بحثي لمؤتمر.</li></ul></div><div class="prose"><h2>المهارات التي تبنيها</h2><ul><li>صياغة سؤال بحثي واضح.</li><li>قراءة الدراسات وتقييمها.</li><li>جمع البيانات وتنظيمها.</li><li>كتابة النتائج والمناقشة.</li><li>فهم أخلاقيات البحث والنشر.</li></ul></div></div></section>
'''
write_page('saudi-board-research.html', 'البورد السعودي والبحث العلمي للأطباء | ResearchLink Arabia', 'تعرف على أهمية البحث العلمي للأطباء المتقدمين للبورد السعودي وكيف تساعدك المنصة في بناء خبرة بحثية منظمة.', 'البورد السعودي, البحث العلمي, أطباء مقيمين, فرص بحثية للأطباء', sb_body)

# SMLE
smle_body = section_header('SMLE والبحث الطبي', 'طوّر ملفك الأكاديمي إلى جانب الاستعداد للاختبار', 'المنصة تساعد طلاب الطب وأطباء الامتياز على دخول البحث العلمي مبكرًا بطريقة منظمة لا تتعارض مع الدراسة والاستعداد للاختبارات.', [('سجل اهتمامك','contact.html','btn-primary')]) + '''
<section class="content-section"><div class="container"><div class="prose"><h2>لماذا يهتم طلاب الطب بالبحث؟</h2><p>المشاركة البحثية المبكرة تساعد الطالب على فهم الطب المبني على الدليل، تحسين السيرة الأكاديمية، وتطوير مهارات القراءة النقدية والكتابة العلمية.</p><div class="table-wrap"><table><thead><tr><th>المسار</th><th>مناسب لمن؟</th><th>المخرجات المتوقعة</th></tr></thead><tbody><tr><td>بحث استبياني بسيط</td><td>المبتدئون</td><td>تجربة عملية في جمع البيانات والكتابة</td></tr><tr><td>مراجعة منهجية</td><td>طلاب لديهم وقت للقراءة والتحليل</td><td>مهارة بحثية قوية ومخطوط قابل للتطوير</td></tr><tr><td>ملخص مؤتمر</td><td>من لديه مشروع قائم</td><td>Abstract أو Poster أكاديمي</td></tr></tbody></table></div></div></div></section>
'''
write_page('smle-research.html', 'SMLE والبحث الطبي لطلاب الطب | ResearchLink Arabia', 'صفحة مخصصة لطلاب الطب وأطباء الامتياز المهتمين ببناء خبرة بحثية بجانب الاستعداد لاختبار SMLE.', 'SMLE, البحث الطبي, طلاب الطب, أطباء امتياز, فرص بحثية', smle_body)

# Training
training_body = section_header('التدريب البحثي', 'تدريب عملي في أساسيات البحث العلمي الطبي', 'ورش قصيرة ومباشرة تساعدك على فهم خطوات البحث من اختيار الفكرة إلى كتابة المخطوط.', [('احجز مقعدك','contact.html','btn-primary')]) + '''
<section class="content-section"><div class="container"><div class="service-grid"><article class="service-card"><div class="card-icon">1</div><h3>مدخل إلى البحث الطبي</h3><p>فهم أنواع الدراسات، صياغة السؤال البحثي، والأخلاقيات.</p></article><article class="service-card"><div class="card-icon">2</div><h3>كتابة المقترح البحثي</h3><p>الأهداف، المنهجية، العينة، الأدوات، وخطة التحليل.</p></article><article class="service-card"><div class="card-icon">3</div><h3>قراءة وتقييم الأبحاث</h3><p>مهارات القراءة النقدية وتقييم جودة الدراسات.</p></article><article class="service-card"><div class="card-icon">4</div><h3>أساسيات التحليل الإحصائي</h3><p>اختيار الاختبار، فهم p-value، والجداول والرسوم.</p></article><article class="service-card"><div class="card-icon">5</div><h3>الكتابة الأكاديمية</h3><p>تنظيم المقدمة والمنهجية والنتائج والمناقشة.</p></article><article class="service-card"><div class="card-icon">6</div><h3>النشر العلمي</h3><p>اختيار مجلة مناسبة وتجهيز ملفات التقديم.</p></article></div></div></section>
'''
write_page('research-training.html', 'التدريب البحثي الطبي للأطباء وطلاب الطب | ResearchLink Arabia', 'ورش تدريبية في البحث العلمي الطبي، إعداد المقترحات، التحليل الإحصائي، والكتابة الأكاديمية للأطباء وطلاب الطب.', 'تدريب بحثي, دورة بحث علمي, أطباء, طلاب الطب, كتابة أكاديمية', training_body)

# Statistical analysis
stat_body = section_header('التحليل الإحصائي', 'تحليل بيانات الأبحاث الطبية بطريقة واضحة', 'نساعدك في اختيار الاختبارات الإحصائية المناسبة، تنظيم البيانات، تفسير النتائج، وتجهيز الجداول البحثية.', [('اطلب تحليل بيانات','contact.html','btn-primary')]) + '''
<section class="content-section"><div class="container split"><div class="prose"><h2>ما الذي نقدمه؟</h2><ul><li>تنظيف البيانات وتجهيزها.</li><li>اختيار الاختبار الإحصائي المناسب.</li><li>تحليل وصفي واستدلالي.</li><li>تفسير النتائج بلغة بحثية.</li><li>إعداد جداول قابلة للإدراج في البحث.</li></ul></div><div class="prose"><h2>أنواع الدراسات المدعومة</h2><p>دراسات مقطعية، استبيانات، دراسات قبل وبعد، مقارنات بين مجموعات، مشاريع جودة، ومشاريع مراجعة منهجية تحتاج إلى Meta-analysis.</p></div></div></section>
'''
write_page('statistical-analysis.html', 'التحليل الإحصائي للأبحاث الطبية | ResearchLink Arabia', 'خدمة تحليل إحصائي للأبحاث الطبية تشمل تنظيف البيانات، اختيار الاختبارات، تفسير النتائج، وتجهيز الجداول البحثية.', 'تحليل إحصائي, SPSS, R, أبحاث طبية, تحليل بيانات', stat_body)

# Systematic review
sys_body = section_header('المراجعات المنهجية', 'دعم Systematic Review وMeta-analysis', 'نساعدك في بناء مراجعة منهجية منظمة بداية من سؤال البحث وحتى استخراج البيانات وكتابة النتائج.', [('ابدأ مراجعتك','contact.html','btn-primary')]) + '''
<section class="content-section"><div class="container"><div class="timeline"><div class="step"><h3>تحديد السؤال البحثي</h3><p>صياغة PICO أو الإطار المناسب حسب نوع المراجعة.</p></div><div class="step"><h3>بناء استراتيجية البحث</h3><p>تحديد قواعد البيانات والكلمات المفتاحية ومعايير الإدراج والاستبعاد.</p></div><div class="step"><h3>فرز الدراسات</h3><p>تنظيم العناوين والملخصات والنصوص الكاملة.</p></div><div class="step"><h3>استخراج البيانات وتقييم الجودة</h3><p>تصميم نموذج استخراج البيانات وتطبيق أدوات التقييم المناسبة.</p></div><div class="step"><h3>الكتابة والتحليل</h3><p>عرض النتائج بطريقة منهجية وإجراء Meta-analysis عند توفر الشروط.</p></div></div></div></section>
'''
write_page('systematic-review-service.html', 'خدمة المراجعات المنهجية وMeta-analysis | ResearchLink Arabia', 'دعم كامل في Systematic Review وMeta-analysis وScoping Review للأبحاث الطبية والصحية.', 'Systematic Review, Meta-analysis, Scoping Review, مراجعة منهجية, بحث طبي', sys_body)

# How it works
how_body = section_header('كيف تعمل المنصة؟', 'ابدأ رحلتك البحثية بخطوات بسيطة', 'صممنا المنصة لتكون واضحة وسهلة، من تسجيل الاهتمامات إلى الانضمام للمشروع وتجهيز المخرجات البحثية.') + '''
<section class="content-section"><div class="container"><div class="timeline"><div class="step"><h3>أرسل بياناتك واهتماماتك</h3><p>التخصص، المرحلة الدراسية أو المهنية، الخبرة البحثية، والوقت المتاح.</p></div><div class="step"><h3>نرشح فرصًا مناسبة</h3><p>يتم اختيار الفرص بناءً على المستوى ونوع البحث والتخصص.</p></div><div class="step"><h3>تتضح المهام من البداية</h3><p>كل مشروع يحتوي على أدوار ومخرجات ومسار زمني تقريبي.</p></div><div class="step"><h3>تبدأ المشاركة والمتابعة</h3><p>يتم توزيع المهام، مراجعة التقدم، وتقديم الدعم عند الحاجة.</p></div><div class="step"><h3>تجهيز المخرجات</h3><p>مخطوط بحثي، ملخص مؤتمر، Poster، أو تقرير تحليلي حسب طبيعة المشروع.</p></div></div></div></section>
<section class="section alt"><div class="container"><div class="cta"><div><h2>ابدأ الآن</h2><p>لا تحتاج خبرة كبيرة للبدء؛ المهم اختيار فرصة تناسب مستواك.</p></div><a href="contact.html" class="btn btn-light">تواصل معنا</a></div></div></section>
'''
write_page('how-it-works.html', 'كيف تعمل منصة ResearchLink Arabia؟', 'تعرف على خطوات الانضمام إلى المنصة، اختيار الفرص البحثية، المشاركة في الفرق البحثية، وتطوير خبرتك العلمية.', 'كيف تعمل منصة بحثية, فرص بحثية, انضمام باحثين, بحث طبي', how_body)

# Blog
articles = [
('كيف تبدأ في البحث العلمي الطبي؟','دليل مبسط للمبتدئين لفهم أول خطوة في اختيار الفكرة وصياغة سؤال البحث.','blog-start-medical-research.html'),
('الفرق بين Systematic Review وMeta-analysis','شرح مختصر للفروقات الأساسية ومتى يستخدم كل نوع في البحث الطبي.','blog-systematic-review-vs-meta-analysis.html'),
('كيف تكتب Research Proposal قوي؟','عناصر المقترح البحثي الناجح من العنوان وحتى خطة التحليل.','blog-research-proposal.html'),
('أهمية البحث العلمي للأطباء وطلاب الطب','كيف يساعد البحث العلمي في تطوير السيرة الأكاديمية والمهارات المهنية.','blog-importance-medical-research.html'),
('أخطاء شائعة في كتابة الأبحاث الطبية','أخطاء في المقدمة والمنهجية والنتائج وكيفية تجنبها.','blog-common-research-mistakes.html'),
('كيف تختار مجلة مناسبة للنشر؟','خطوات عملية لتقييم نطاق المجلة ومتطلبات التقديم.','blog-choose-journal.html')
]
blog_body = section_header('المدونة', 'مقالات تعليمية في البحث الطبي والنشر العلمي', 'محتوى تعليمي يساعد الأطباء وطلاب الطب والباحثين على فهم البحث العلمي بطريقة مبسطة وعملية.') + '<section class="content-section"><div class="container"><div class="blog-grid">' + ''.join(f'''<article class="article-card"><span class="tag">مقال تعليمي</span><h3><a href="{href}">{title}</a></h3><p>{desc}</p><a href="{href}" class="btn btn-outline btn-small">قراءة المقال</a></article>''' for title,desc,href in articles) + '</div></div></section>'
write_page('blog.html', 'مدونة البحث العلمي الطبي | ResearchLink Arabia', 'مقالات تعليمية حول البحث العلمي الطبي، النشر الأكاديمي، المراجعات المنهجية، والتحليل الإحصائي للأطباء وطلاب الطب.', 'مدونة بحث علمي, بحث طبي, نشر علمي, مقالات طبية', blog_body)

article_contents = {
'blog-start-medical-research.html': ('كيف تبدأ في البحث العلمي الطبي؟','ابدأ بفكرة واضحة ومشكلة قابلة للقياس. بعد ذلك حوّل الفكرة إلى سؤال بحثي، حدد نوع الدراسة، واختر عينة مناسبة وأداة جمع بيانات واضحة. لا تبدأ بجمع البيانات قبل مراجعة الأدبيات والتأكد من الأخلاقيات البحثية.'),
'blog-systematic-review-vs-meta-analysis.html': ('الفرق بين Systematic Review وMeta-analysis','المراجعة المنهجية تبحث وتقيّم الدراسات بطريقة منظمة للإجابة عن سؤال محدد. أما Meta-analysis فهو تحليل إحصائي يجمع نتائج الدراسات المتشابهة كميًا. ليس كل Systematic Review يحتاج إلى Meta-analysis، لأن ذلك يعتمد على تجانس الدراسات والبيانات.'),
'blog-research-proposal.html': ('كيف تكتب Research Proposal قوي؟','المقترح البحثي الجيد يحتوي على عنوان واضح، خلفية مختصرة، مشكلة البحث، الأهداف، المنهجية، خطة العينة، أدوات جمع البيانات، خطة التحليل، والاعتبارات الأخلاقية. يجب أن يكون السؤال البحثي قابلًا للتنفيذ ضمن الوقت والموارد المتاحة.'),
'blog-importance-medical-research.html': ('أهمية البحث العلمي للأطباء وطلاب الطب','البحث العلمي يساعد الطبيب على فهم الأدلة العلمية، تحسين القرارات السريرية، وتطوير مهارات القراءة النقدية والكتابة الأكاديمية. كما يدعم بناء السيرة العلمية والمشاركة في المؤتمرات والمشاريع الصحية.'),
'blog-common-research-mistakes.html': ('أخطاء شائعة في كتابة الأبحاث الطبية','من الأخطاء الشائعة: عنوان عام جدًا، أهداف غير قابلة للقياس، منهجية غير واضحة، نتائج بلا تفسير، ومناقشة لا تربط النتائج بالدراسات السابقة. الحل هو اتباع هيكل أكاديمي واضح ومراجعة البحث قبل الإرسال.'),
'blog-choose-journal.html': ('كيف تختار مجلة مناسبة للنشر؟','اختر مجلة تتوافق مع تخصص البحث ونطاقه، وتحقق من تعليمات المؤلفين، نوع المقالات المقبولة، مدة المراجعة، والرسوم. تجنب المجلات غير الموثوقة، ولا ترسل البحث إلى أكثر من مجلة في نفس الوقت إلا إذا كانت السياسة تسمح بذلك.')
}
for slug,(title_art,text) in article_contents.items():
    body = section_header('مقال تعليمي', title_art, 'محتوى مبسط يساعد الباحثين المبتدئين على فهم خطوات البحث العلمي الطبي.') + f'''<section class="content-section"><div class="container"><article class="prose"><p>{text}</p><h2>نقاط عملية</h2><ul><li>ابدأ بخطة واضحة قبل التنفيذ.</li><li>استخدم مصادر علمية موثوقة.</li><li>وثق كل خطوة في البحث.</li><li>اطلب مراجعة من شخص لديه خبرة بحثية.</li></ul><div class="notice">هذا المقال تعليمي عام ولا يغني عن إشراف أكاديمي أو مراجعة لجنة أخلاقيات البحث عند الحاجة.</div><div class="hero-actions"><a href="blog.html" class="btn btn-outline">العودة للمدونة</a><a href="contact.html" class="btn btn-primary">اطلب مساعدة بحثية</a></div></article></div></section>'''
    write_page(slug, f'{title_art} | مدونة ResearchLink Arabia', f'{title_art} - مقال تعليمي في البحث العلمي الطبي من منصة رابط الباحثين.', 'بحث علمي طبي, نشر علمي, تدريب بحثي', body)

# FAQ
faqs = [
('هل أحتاج خبرة بحثية سابقة؟','لا، توجد فرص مناسبة للمبتدئين وفرص أخرى للباحثين ذوي الخبرة. يتم ترشيح الفرصة حسب مستواك.'),
('هل المشاركة في الفرص البحثية عن بعد؟','نعم، كثير من الفرص يمكن المشاركة فيها عن بعد، لكن بعض المشاريع قد تحتاج إلى جمع بيانات ميداني.'),
('هل تضمنون نشر البحث؟','لا يمكن ضمان قبول البحث في مجلة، لأن القرار للمجلة والمحكمين. نساعدك في تحسين الجودة وتجهيز الملفات.'),
('هل المنصة مناسبة لأطباء البورد السعودي؟','نعم، المنصة تساعد الأطباء على بناء خبرة بحثية منظمة، لكن يجب مراجعة متطلبات الجهة الرسمية بشكل مستقل.'),
('هل توجد شهادات مشاركة؟','يمكن إصدار خطاب أو شهادة مشاركة حسب طبيعة المشروع ودور الباحث بعد إكمال المهام المطلوبة.'),
('كيف يتم اختيار المشروع المناسب؟','يتم النظر إلى التخصص، الخبرة، الوقت المتاح، ونوع البحث المفضل لديك.'),
('هل تقدمون تحليلًا إحصائيًا فقط؟','نعم، يمكن طلب خدمة التحليل الإحصائي بشكل مستقل لمشروع قائم.'),
('هل تدعمون المراجعات المنهجية؟','نعم، ندعم Systematic Review وScoping Review وMeta-analysis حسب نوع المشروع والبيانات المتوفرة.')
]
faq_schema = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]}
faq_html = ''.join(f'''<div class="faq-card"><button type="button">{q}<span>+</span></button><div class="answer"><p>{a}</p></div></div>''' for q,a in faqs)
faq_body = section_header('الأسئلة الشائعة', 'إجابات واضحة عن الفرص البحثية والخدمات', 'جمعنا أهم الأسئلة التي يطرحها الأطباء وطلاب الطب قبل الانضمام إلى منصة بحثية.') + f'<section class="content-section"><div class="container"><div class="faq-list">{faq_html}</div></div></section>'
write_page('faq.html', 'الأسئلة الشائعة حول الفرص البحثية والنشر العلمي | ResearchLink Arabia', 'إجابات عن أهم الأسئلة حول الانضمام للفرص البحثية، النشر العلمي، الرسوم، الإشراف، ومتطلبات المشاركة.', 'أسئلة شائعة, فرص بحثية, نشر علمي, أطباء باحثون', faq_body, schema=faq_schema)

# Contact
contact_body = section_header('تواصل معنا', 'ابدأ رحلتك البحثية اليوم', 'أرسل لنا بياناتك وسنساعدك في اختيار الخدمة أو الفرصة البحثية المناسبة.') + f'''
<section class="content-section"><div class="container contact-grid"><aside class="contact-box"><h2>بيانات التواصل</h2><p>البريد الإلكتروني:</p><strong>{SITE['email']}</strong><p>واتساب:</p><strong>{SITE['phone']}</strong><div class="hero-actions"><a href="https://wa.me/{SITE['whatsapp']}" class="btn btn-primary">تواصل واتساب</a></div><hr><p class="notice">يمكن تعديل رقم الجوال والبريد بسهولة من ملفات المشروع قبل النشر.</p></aside><div class="contact-box"><h2>نموذج طلب الخدمة</h2><form id="contact-form" class="form-grid"><div class="input-group"><label for="name">الاسم الكامل</label><input id="name" name="name" required placeholder="اكتب اسمك"></div><div class="input-group"><label for="email">البريد الإلكتروني</label><input id="email" type="email" name="email" required placeholder="name@example.com"></div><div class="input-group"><label for="stage">المرحلة أو الصفة</label><select id="stage" name="stage"><option>طالب طب</option><option>طبيب امتياز</option><option>طبيب مقيم</option><option>باحث صحي</option><option>فريق بحثي</option></select></div><div class="input-group"><label for="service">نوع الطلب</label><select id="service" name="service"><option>فرصة بحثية</option><option>تحليل إحصائي</option><option>مراجعة منهجية</option><option>نشر علمي</option><option>تدريب بحثي</option></select></div><div class="input-group"><label for="message">تفاصيل الطلب</label><textarea id="message" name="message" placeholder="اكتب تخصصك واهتماماتك البحثية"></textarea></div><button class="btn btn-primary" type="submit">إرسال الطلب</button><div class="success-message">تم إرسال النموذج تجريبيًا. لربطه فعليًا استخدم Formspree أو Google Forms أو API خاص.</div></form></div></div></section>
'''
write_page('contact.html', 'تواصل معنا | ResearchLink Arabia', 'تواصل مع منصة رابط الباحثين للاستفسار عن الفرص البحثية، خدمات النشر العلمي، التحليل الإحصائي، والتدريب البحثي.', 'تواصل بحث علمي, استشارة بحثية, فرص بحثية طبية', contact_body)

# Privacy
privacy_body = section_header('سياسة الخصوصية', 'سياسة الخصوصية واستخدام البيانات', 'توضح هذه الصفحة كيفية التعامل مع بيانات المستخدمين عند استخدام منصة رابط الباحثين.') + '''
<section class="content-section"><div class="container"><article class="prose"><h2>البيانات التي نجمعها</h2><p>قد نجمع الاسم، البريد الإلكتروني، رقم الجوال، التخصص، المرحلة المهنية، والاهتمامات البحثية عند تعبئة نموذج التواصل.</p><h2>كيف نستخدم البيانات؟</h2><p>تستخدم البيانات للتواصل مع المستخدم، ترشيح الفرص البحثية المناسبة، تحسين الخدمات، والرد على الاستفسارات.</p><h2>مشاركة البيانات</h2><p>لا نبيع بيانات المستخدمين. قد تتم مشاركة بيانات محدودة مع فريق بحثي عند موافقة المستخدم وانضمامه لمشروع معين.</p><h2>أمان البيانات</h2><p>نستخدم إجراءات تنظيمية معقولة لحماية البيانات، ويُنصح بعدم مشاركة أي معلومات حساسة أو سرية عبر نموذج التواصل.</p><h2>تحديث السياسة</h2><p>قد يتم تحديث هذه السياسة من وقت لآخر، ويُعد استمرار استخدام الموقع موافقة على التحديثات.</p></article></div></section>
'''
write_page('privacy-policy.html', 'سياسة الخصوصية | ResearchLink Arabia', 'سياسة الخصوصية لمنصة رابط الباحثين وكيفية جمع واستخدام بيانات المستخدمين.', 'سياسة الخصوصية, بيانات المستخدم, منصة بحثية', privacy_body)

# Terms
terms_body = section_header('الشروط والأحكام', 'شروط استخدام منصة رابط الباحثين', 'توضح هذه الصفحة القواعد العامة لاستخدام الموقع والخدمات البحثية.') + '''
<section class="content-section"><div class="container"><article class="prose"><h2>طبيعة الخدمة</h2><p>تقدم المنصة خدمات ربط ودعم بحثي وتدريب ونشر علمي، ولا تضمن قبول الأبحاث في المجلات أو الجهات الأكاديمية.</p><h2>مسؤولية المستخدم</h2><p>يلتزم المستخدم بتقديم معلومات صحيحة، واحترام أخلاقيات البحث العلمي، وعدم استخدام الخدمات لأي غرض مخالف للأنظمة أو النزاهة الأكاديمية.</p><h2>الملكية الفكرية</h2><p>حقوق التأليف والمساهمة البحثية تحدد حسب دور كل مشارك وسياسات المشروع أو المجلة أو الجهة البحثية.</p><h2>إخلاء مسؤولية</h2><p>المحتوى الموجود في الموقع لأغراض تعليمية وتنظيمية عامة، ولا يغني عن استشارة أكاديمية أو قانونية عند الحاجة.</p><h2>التعديل على الشروط</h2><p>يحق للمنصة تعديل الشروط عند الحاجة، ويُنشر آخر تحديث على هذه الصفحة.</p></article></div></section>
'''
write_page('terms.html', 'الشروط والأحكام | ResearchLink Arabia', 'شروط وأحكام استخدام منصة رابط الباحثين وخدماتها البحثية والتدريبية.', 'الشروط والأحكام, منصة بحثية, حقوق البحث العلمي', terms_body)

# sitemap and robots and readme
sitemap = ['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for slug,_,_ in pages:
    loc = SITE['domain'] + '/' + ('' if slug == 'index.html' else slug)
    sitemap.append(f'  <url><loc>{loc}</loc><changefreq>weekly</changefreq><priority>{"1.0" if slug=="index.html" else "0.8"}</priority></url>')
sitemap.append('</urlset>')
(ROOT / 'sitemap.xml').write_text('\n'.join(sitemap), encoding='utf-8')
(ROOT / 'robots.txt').write_text(f'''User-agent: *
Allow: /

Sitemap: {SITE['domain']}/sitemap.xml
''', encoding='utf-8')

(ROOT / 'README.md').write_text(f'''# ResearchLink Arabia - رابط الباحثين

مشروع موقع ثابت كامل لمنصة فرص بحثية طبية، مصمم باللغة العربية RTL مع صفحات مفهرسة SEO.

## الملفات المهمة

- `index.html` الصفحة الرئيسية
- `about.html` من نحن
- `research-opportunities.html` الفرص البحثية
- `services.html` الخدمات
- `scientific-publication.html` النشر العلمي
- `saudi-board-research.html` البورد السعودي والبحث العلمي
- `smle-research.html` SMLE والبحث الطبي
- `research-training.html` التدريب البحثي
- `statistical-analysis.html` التحليل الإحصائي
- `systematic-review-service.html` المراجعات المنهجية
- `how-it-works.html` كيف تعمل المنصة
- `blog.html` المدونة + مقالات داخلية
- `faq.html` الأسئلة الشائعة مع FAQ Schema
- `contact.html` تواصل معنا
- `privacy-policy.html` سياسة الخصوصية
- `terms.html` الشروط والأحكام
- `sitemap.xml` خريطة الموقع
- `robots.txt` ملف الزحف

## التعديل قبل النشر

افتح ملف `generate_site.py` أو ملفات HTML مباشرة وعدّل:

- اسم المنصة
- الدومين
- البريد الإلكتروني
- رقم الواتساب
- محتوى الخدمات والأسعار إن وجدت

## طريقة النشر السريعة

يمكن رفع الملفات على GitHub Pages أو Netlify أو Render Static Site.

## ملاحظات

نموذج التواصل تجريبي في الواجهة فقط. لربطه فعليًا استخدم Formspree أو Google Forms أو API خاص.
''', encoding='utf-8')

print(f'Generated {len(pages)} HTML pages at {ROOT}')
