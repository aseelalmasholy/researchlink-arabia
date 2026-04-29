
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
