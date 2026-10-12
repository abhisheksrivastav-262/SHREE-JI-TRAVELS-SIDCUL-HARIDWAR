/* Shree Ji Travels — dynamic behaviours (slider, scroll UI, smart forms, FAQ search) */
(function () {
  'use strict';
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- Hero slider (home) ---- */
  const slides = Array.from(document.querySelectorAll('.hero-slides img'));
  const dotsWrap = document.querySelector('.hero-dots');
  if (slides.length > 1) {
    let i = 0, timer = null;
    slides[0].classList.add('on');
    if (dotsWrap) {
      slides.forEach((_, n) => {
        const d = document.createElement('button');
        d.type = 'button';
        d.setAttribute('aria-label', 'Show slide ' + (n + 1));
        if (n === 0) d.classList.add('on');
        d.addEventListener('click', () => go(n, true));
        dotsWrap.appendChild(d);
      });
    }
    const dots = Array.from(dotsWrap ? dotsWrap.children : []);
    function go(n, manual) {
      slides[i].classList.remove('on');
      if (dots[i]) dots[i].classList.remove('on');
      i = (n + slides.length) % slides.length;
      slides[i].classList.add('on');
      if (dots[i]) dots[i].classList.add('on');
      if (manual) restart();
    }
    function restart() { if (!reduceMotion) { clearInterval(timer); timer = setInterval(() => go(i + 1), 6000); } }
    restart();
    const hero = document.querySelector('.hero');
    if (hero) {
      hero.addEventListener('pointerenter', () => clearInterval(timer));
      hero.addEventListener('pointerleave', restart);
    }
  }

  /* ---- Shrinking header + back-to-top ---- */
  const head = document.querySelector('.site-header');
  const toTop = document.querySelector('.to-top');
  function onScroll() {
    const y = window.scrollY || 0;
    if (head) head.classList.toggle('scrolled', y > 24);
    if (toTop) toTop.classList.toggle('show', y > 700);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
  if (toTop) toTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' }));

  /* ---- Smart booking forms ---- */
  document.querySelectorAll('form[data-whatsapp-form]').forEach((form) => {
    // Travel-date can't be in the past
    const today = new Date().toISOString().split('T')[0];
    form.querySelectorAll('input[type="date"]').forEach((d) => { if (!d.min) d.min = today; });
    // Show return-date only when relevant
    const jt = form.querySelector('[name="journeyType"]');
    const retField = form.querySelector('[data-return-field]');
    const retInput = retField ? retField.querySelector('input') : null;
    function syncReturn() {
      if (!jt || !retField) return;
      const need = /round trip|outstation/i.test(jt.value);
      retField.style.display = need ? '' : 'none';
      if (retInput) { retInput.required = need; if (!need) retInput.value = ''; }
    }
    if (jt && retField) { jt.addEventListener('change', syncReturn); syncReturn(); }
    // Live character count for notes/requirements
    form.querySelectorAll('textarea').forEach((ta) => {
      ta.setAttribute('maxlength', '600');
      const c = document.createElement('div');
      c.className = 'char-counter';
      ta.after(c);
      const upd = () => { c.textContent = ta.value.length + ' / 600'; };
      ta.addEventListener('input', upd); upd();
    });
    // Auto-set destination hint for one-way/round-trip fixed forms
    const dest = form.querySelector('[name="destination"]');
    if (dest && !dest.placeholder) dest.placeholder = 'e.g. Delhi / Dehradun';
  });

  /* ---- FAQ live search ---- */
  const search = document.querySelector('#faqSearch');
  if (search) {
    const items = Array.from(document.querySelectorAll('.faq-item'));
    const empty = document.querySelector('#faqEmpty');
    search.addEventListener('input', () => {
      const q = search.value.trim().toLowerCase();
      let visible = 0;
      items.forEach((it) => {
        const hit = !q || it.textContent.toLowerCase().includes(q);
        it.style.display = hit ? '' : 'none';
        if (hit) visible++;
      });
      if (empty) empty.classList.toggle('show', visible === 0);
    });
  }

  /* ---- Time-aware greeting in hero note ---- */
  const greet = document.querySelector('[data-greet]');
  if (greet) {
    const h = new Date().getHours();
    greet.textContent = h < 12 ? 'Good morning' : h < 17 ? 'Good afternoon' : 'Good evening';
  }
})();
