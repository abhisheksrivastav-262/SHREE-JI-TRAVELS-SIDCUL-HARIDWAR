/* Shree Ji Travels — shared interactions v1.0 */
const WA_NUMBER = '918077274970';
const $ = (s, c = document) => c.querySelector(s);
const $$ = (s, c = document) => Array.from(c.querySelectorAll(s));

/* Mobile panel */
function toggleMobile(open) {
  const p = $('#mobilePanel');
  if (!p) return;
  p.classList.toggle('open', open === undefined ? !p.classList.contains('open') : open);
  document.body.style.overflow = p.classList.contains('open') ? 'hidden' : '';
}
document.addEventListener('click', (e) => {
  const hb = e.target.closest('[data-open-menu]');
  if (hb) { toggleMobile(true); return; }
  if (e.target.closest('[data-close-menu]')) { toggleMobile(false); return; }
  const db = e.target.closest('.drop-btn');
  if (db) {
    const wrap = db.closest('.has-dropdown');
    const was = wrap.classList.contains('open');
    $$('.has-dropdown.open').forEach(d => d.classList.remove('open'));
    if (!was) wrap.classList.add('open');
    db.setAttribute('aria-expanded', String(!was));
    return;
  }
  if (!e.target.closest('.has-dropdown')) $$('.has-dropdown.open').forEach(d => d.classList.remove('open'));
});
document.addEventListener('keydown', (e) => { if (e.key === 'Escape') { toggleMobile(false); closeLightbox(); } });

/* Reveal on scroll */
const io = new IntersectionObserver((entries) => {
  entries.forEach(en => { if (en.isIntersecting) { en.target.classList.add('visible'); io.unobserve(en.target); } });
}, { threshold: 0.12 });
$$('.reveal').forEach(el => io.observe(el));

/* FAQ accordion */
$$('.faq-q').forEach(btn => {
  btn.addEventListener('click', () => {
    const item = btn.closest('.faq-item');
    const open = item.classList.contains('open');
    $$('.faq-item.open').forEach(i => { i.classList.remove('open'); i.querySelector('.faq-q').setAttribute('aria-expanded', 'false'); });
    if (!open) { item.classList.add('open'); btn.setAttribute('aria-expanded', 'true'); }
  });
});

/* Image fallback — keeps layout premium even if a CDN image fails */
const FALLBACK_IMG = 'data:image/svg+xml;utf8,' + encodeURIComponent(`<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="800"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#073B70"/><stop offset="1" stop-color="#071B33"/></linearGradient></defs><rect width="1200" height="800" fill="url(#g)"/><g fill="none" stroke="#F49B20" stroke-width="6" opacity="0.9"><path d="M120 620 L480 300 L640 470 L780 330 L1080 620"/></g><circle cx="880" cy="220" r="60" fill="#F49B20"/><text x="600" y="700" text-anchor="middle" font-family="Georgia" font-size="52" fill="#fff">Shree Ji Travels</text></svg>`);
$$('img[data-fallback]').forEach(img => {
  img.addEventListener('error', () => { if (img.src !== FALLBACK_IMG) img.src = FALLBACK_IMG; }, { once: true });
});

/* Gallery filter + lightbox */
$$('.filter-bar button').forEach(btn => {
  btn.addEventListener('click', () => {
    $$('.filter-bar button').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    const f = btn.dataset.filter;
    $$('.g-item').forEach(it => { it.style.display = (f === 'all' || it.dataset.cat === f) ? '' : 'none'; });
  });
});
let lbList = [], lbIndex = 0;
function openLightbox(src, alt) {
  lbList = $$('.g-item').filter(el => el.style.display !== 'none').map(el => ({ src: el.querySelector('img').src, alt: el.querySelector('img').alt }));
  lbIndex = Math.max(0, lbList.findIndex(x => x.src === src));
  const lb = $('#lightbox'); if (!lb) return;
  $('#lbImg').src = src; $('#lbImg').alt = alt || 'Gallery photo';
  lb.classList.add('open'); document.body.style.overflow = 'hidden';
}
function closeLightbox() { const lb = $('#lightbox'); if (lb) lb.classList.remove('open'); if (!$('#mobilePanel')?.classList.contains('open')) document.body.style.overflow = ''; }
function lbStep(d) {
  if (!lbList.length) return;
  lbIndex = (lbIndex + d + lbList.length) % lbList.length;
  $('#lbImg').src = lbList[lbIndex].src; $('#lbImg').alt = lbList[lbIndex].alt;
}
document.addEventListener('click', (e) => {
  const g = e.target.closest('.g-item');
  if (g) { const im = g.querySelector('img'); openLightbox(im.src, im.alt); return; }
  if (e.target.closest('[data-lb-close]')) closeLightbox();
  if (e.target.closest('[data-lb-prev]')) lbStep(-1);
  if (e.target.closest('[data-lb-next]')) lbStep(1);
  const lb = $('#lightbox');
  if (lb && e.target === lb) closeLightbox();
});

/* ---------- WhatsApp form handling ---------- */
function markInvalid(field, bad) { field.classList.toggle('invalid', bad); return !bad; }
function validPhone(v) { const d = v.replace(/\D/g, ''); return d.length >= 10 && d.length <= 13; }
function encodeMsg(lines) { return encodeURIComponent(lines.join('\n')); }
function openWA(msg) { window.open(`https://wa.me/${WA_NUMBER}?text=${encodeMsg(msg)}`, '_blank', 'noopener'); }
function showFormError(form, text) {
  let box = form.querySelector('.error-msg');
  if (!box) return;
  box.textContent = text; box.classList.add('show');
  box.scrollIntoView({ behavior: 'smooth', block: 'center' });
}
function clearFormError(form) { form.querySelector('.error-msg')?.classList.remove('show'); }

function handleBookingForm(form) {
  form.addEventListener('submit', (e) => {
    e.preventDefault(); clearFormError(form);
    const v = (n) => (form.querySelector(`[name="${n}"]`)?.value || '').trim();
    let ok = true;
    const req = ['pickup', 'destination', 'journeyType', 'travelDate', 'passengers', 'customerName', 'mobile'];
    if (form.dataset.form === 'chardham') req.push('pilgrims');
    const retInput = form.querySelector('[name="returnDate"]');
    if (retInput && retInput.required) req.push('returnDate');
    req.forEach(n => {
      const f = form.querySelector(`[name="${n}"]`)?.closest('.field');
      const val = v(n);
      let bad = !val;
      if (n === 'mobile' && val) bad = !validPhone(val);
      if (f) ok = markInvalid(f, bad) && ok;
    });
    const mobile = v('mobile');
    if (mobile && !validPhone(mobile)) { showFormError(form, 'Please enter a valid 10-digit mobile number.'); return; }
    const missing = req.filter(n => !v(n));
    if (missing.length || !ok) { showFormError(form, 'Please fill all required fields correctly, then tap “Send on WhatsApp”.'); return; }
    const L = ['Namaste Shree Ji Travels! I would like to enquire about a cab booking.', ''];
    const push = (k, val) => { if (val) L.push(`${k}: ${val}`); };
    push('Name', v('customerName')); push('Pickup', v('pickup')); push('Destination', v('destination'));
    push('Journey Type', v('journeyType')); push('Travel Date', v('travelDate'));
    if (v('returnDate')) push('Return Date', v('returnDate'));
    push('Passengers', v('passengers') || v('pilgrims'));
    if (v('pilgrims')) push('Pilgrims', v('pilgrims'));
    push('Vehicle Preference', v('vehicle')); push('Mobile', mobile);
    if (v('duration')) push('Trip Duration', v('duration'));
    if (v('requirements')) push('Special Requirements', v('requirements'));
    if (v('notes')) push('Notes', v('notes'));
    L.push('', 'Please share the fare and availability.');
    openWA(L);
  });
  form.addEventListener('input', (e) => { e.target.closest('.field')?.classList.remove('invalid'); });
}
$$('form[data-whatsapp-form]').forEach(handleBookingForm);

/* Footer year */
const yr = $('#year'); if (yr) yr.textContent = new Date().getFullYear();
