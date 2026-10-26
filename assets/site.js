/* Roof and Chimney Doctor — shared behaviour.
   Degrades gracefully: without GSAP or Lenis everything is still visible and usable. */
(function () {
  /* ===== EDIT CONTACT DETAILS HERE (updates every page) ===== */
  var CONFIG = {
    phone: '083 121 3251', phoneHref: 'tel:+353831213251',
    whatsapp: 'https://wa.me/353831213251',
    email: 'roofandchimneydoctor@gmail.com',
    address: 'Dublin, Ireland',
    // Paste a Web3Forms access key here (free at web3forms.com) to have forms send straight to the inbox.
    // Left blank, forms open the visitor's email app with everything filled in.
    formEndpoint: 'https://api.web3forms.com/submit',
    formKey: ''
  };
  /* ============================================================ */
  const html = document.documentElement;
  html.classList.add('js');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fine = matchMedia('(pointer: fine)').matches;
  const touch = !fine;
  const G = typeof gsap !== 'undefined';
  const ST = G && typeof ScrollTrigger !== 'undefined';
  if (ST) gsap.registerPlugin(ScrollTrigger);
  if (touch) html.classList.add('touch');
  if (G && ST && !touch && !reduce) html.classList.add('gsap');
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const rand = (a, b) => a + Math.random() * (b - a);

  /* config fill */
  $$('[data-cfg]').forEach(el => {
    const k = el.dataset.cfg;
    if (k === 'phone') { el.textContent = CONFIG.phone; if (el.tagName === 'A') el.href = CONFIG.phoneHref; }
    else if (k === 'email') { el.textContent = CONFIG.email; if (el.tagName === 'A') el.href = 'mailto:' + CONFIG.email; }
    else if (k === 'year') el.textContent = new Date().getFullYear();
    else if (k in CONFIG) el.textContent = CONFIG[k];
  });
  $$('a[data-href="phone"]').forEach(a => a.href = CONFIG.phoneHref);
  $$('a[data-href="whatsapp"]').forEach(a => a.href = CONFIG.whatsapp);
  $$('a[data-href="email"]').forEach(a => a.href = 'mailto:' + CONFIG.email);

  /* smooth scroll (desktop only) */
  let lenis = null;
  if (!reduce && fine && typeof Lenis !== 'undefined') {
    lenis = new Lenis({ lerp: 0.1, smoothWheel: true });
    if (G) { lenis.on('scroll', () => ST && ScrollTrigger.update()); gsap.ticker.add(t => lenis.raf(t * 1000)); gsap.ticker.lagSmoothing(0); }
    else { const raf = t => { lenis.raf(t); requestAnimationFrame(raf); }; requestAnimationFrame(raf); }
  }
  const lockScroll = on => { if (lenis) on ? lenis.stop() : lenis.start(); };

  /* header */
  const hdr = $('.hdr');
  const onScroll = () => hdr && hdr.classList.toggle('solid', scrollY > 40);
  addEventListener('scroll', onScroll, { passive: true }); onScroll();

  /* mobile menu */
  const burger = $('.burger');
  if (burger) burger.addEventListener('click', () => {
    const open = html.classList.toggle('menu-open');
    burger.setAttribute('aria-expanded', open); lockScroll(open);
  });
  $$('.mnav a').forEach(a => a.addEventListener('click', () => { html.classList.remove('menu-open'); lockScroll(false); }));

  /* quote drawer */
  const qd = $('#qd');
  const openQ = e => { if (!qd) return; if (e) e.preventDefault(); html.classList.remove('menu-open'); html.classList.add('qd-open'); lockScroll(true); setTimeout(() => { const f = $('input:not(.hp)', qd); if (f && fine) f.focus(); }, 350); };
  const closeQ = () => { html.classList.remove('qd-open'); lockScroll(false); };
  $$('[data-quote]').forEach(b => b.addEventListener('click', openQ));
  $$('[data-close]').forEach(b => b.addEventListener('click', closeQ));
  addEventListener('keydown', e => { if (e.key === 'Escape') { closeQ(); closeLb(); } });

  /* forms */
  $$('form[data-form]').forEach(form => {
    const msg = $('.fmsg', form);
    const say = (t, ok) => { if (!msg) return; msg.textContent = t; msg.className = 'fmsg ' + (ok ? 'ok' : 'err'); };
    form.addEventListener('submit', async e => {
      e.preventDefault();
      let bad = null;
      $$('[required]', form).forEach(f => {
        const ok = f.value.trim() && f.checkValidity();
        f.closest('label').classList.toggle('bad', !ok);
        if (!ok && !bad) bad = f;
      });
      if (bad) { say('Please fill in the highlighted fields.'); bad.focus(); return; }
      if ($('.hp', form) && $('.hp', form).value) return;
      const data = Object.fromEntries(new FormData(form).entries()); delete data.botcheck;
      const subject = 'Website enquiry: ' + (data.service || 'Roofing quote') + ' – ' + (data.name || '');
      const body = Object.entries(data).filter(([, v]) => v).map(([k, v]) => k.charAt(0).toUpperCase() + k.slice(1) + ': ' + v).join('\n');
      const btn = $('button[type=submit]', form); const label = btn.innerHTML;
      if (CONFIG.formEndpoint && CONFIG.formKey) {
        btn.disabled = true; btn.textContent = 'Sending…';
        try {
          const r = await fetch(CONFIG.formEndpoint, { method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' }, body: JSON.stringify({ access_key: CONFIG.formKey, subject, from_name: 'Roof and Chimney Doctor website', ...data }) });
          const j = await r.json().catch(() => ({}));
          if (!r.ok || j.success === false) throw new Error();
          form.reset(); say('Thanks, we have your request. We aim to respond within 24 hours. If it’s urgent, call ' + CONFIG.phone + '.', true);
        } catch (err) { say('Sorry, that didn’t send. Please call ' + CONFIG.phone + ' or email ' + CONFIG.email + '.'); }
        btn.disabled = false; btn.innerHTML = label;
      } else {
        location.href = 'mailto:' + CONFIG.email + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
        say('Your email app should now open with your details filled in. Just press send. Or call us on ' + CONFIG.phone + '.', true);
      }
    });
    $$('input,select,textarea', form).forEach(f => f.addEventListener('input', () => f.closest('label') && f.closest('label').classList.remove('bad')));
  });

  /* before / after sliders: drag anywhere on the photo (mouse or finger) */
  $$('.compare').forEach(c => {
    const r = $('input', c);
    const set = v => { r.value = v; c.style.setProperty('--p', v + '%'); };
    r.addEventListener('input', () => set(r.value)); set(r.value);
    let drag = false, sx = 0, sy = 0, lock = null;
    const at = x => { const b = c.getBoundingClientRect(); set(Math.round(Math.min(Math.max((x - b.left) / b.width, 0), 1) * 1000) / 10); };
    c.addEventListener('pointerdown', e => { drag = true; sx = e.clientX; sy = e.clientY; lock = e.pointerType === 'mouse' ? 'x' : null; if (lock) { at(e.clientX); c.setPointerCapture(e.pointerId); } e.preventDefault(); });
    c.addEventListener('pointermove', e => {
      if (!drag) return;
      if (!lock) { const dx = Math.abs(e.clientX - sx), dy = Math.abs(e.clientY - sy); if (dx < 6 && dy < 6) return; lock = dx > dy ? 'x' : 'y'; if (lock === 'x') c.setPointerCapture(e.pointerId); }
      if (lock === 'x') at(e.clientX);
    });
    const end = e => { if (drag && !lock && e.type === 'pointerup') at(e.clientX); drag = false; lock = null; };
    c.addEventListener('pointerup', end); c.addEventListener('pointercancel', end);
  });

  /* photo viewer: tap any photo to see it full size */
  const photos = [...$$('.gal a').map(a => ({ src: a.href, alt: ($('img', a) || {}).alt || '', el: a })),
    ...$$('.collage img, .ph img').map(img => ({ src: img.currentSrc || img.src, alt: img.alt, el: img }))];
  let lb = $('.lb'), lbI = 0;
  if (photos.length && !lb) {
    lb = document.createElement('div'); lb.className = 'lb'; lb.setAttribute('role', 'dialog'); lb.setAttribute('aria-label', 'Photo viewer');
    const ic = d => `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="${d}"/></svg>`;
    lb.innerHTML = `<button class="x" aria-label="Close">${ic('M18 6L6 18M6 6l12 12')}</button><button class="pv" aria-label="Previous">${ic('M15 18l-6-6 6-6')}</button><img alt=""><button class="nx" aria-label="Next">${ic('M9 18l6-6-6-6')}</button>`;
    document.body.appendChild(lb);
  }
  function showLb(i) { lbI = (i + photos.length) % photos.length; const im = $('img', lb); im.src = photos[lbI].src; im.alt = photos[lbI].alt; }
  function closeLb() { if (lb && lb.classList.contains('on')) { lb.classList.remove('on'); lockScroll(false); } }
  if (lb && photos.length) {
    photos.forEach((ph, i) => { ph.el.classList.add('zoom'); ph.el.addEventListener('click', e => { e.preventDefault(); showLb(i); lb.classList.add('on'); lockScroll(true); }); });
    $('.x', lb).addEventListener('click', closeLb);
    $('.pv', lb).addEventListener('click', () => showLb(lbI - 1));
    $('.nx', lb).addEventListener('click', () => showLb(lbI + 1));
    lb.addEventListener('click', e => { if (e.target === lb) closeLb(); });
    addEventListener('keydown', e => { if (!lb.classList.contains('on')) return; if (e.key === 'ArrowLeft') showLb(lbI - 1); if (e.key === 'ArrowRight') showLb(lbI + 1); });
    let tx0 = null; lb.addEventListener('touchstart', e => tx0 = e.touches[0].clientX, { passive: true });
    lb.addEventListener('touchend', e => { if (tx0 == null) return; const dx = e.changedTouches[0].clientX - tx0; if (Math.abs(dx) > 50) showLb(lbI + (dx < 0 ? 1 : -1)); tx0 = null; });
  }

  /* rain */
  function rainOn(host, o = {}) {
    if (reduce) return null;
    const cv = document.createElement('canvas'); cv.className = 'rain'; cv.setAttribute('aria-hidden', 'true');
    host.insertBefore(cv, host.firstElementChild ? host.firstElementChild.nextSibling : null);
    const ctx = cv.getContext('2d'); let w, h, drops = [], vis = true, raf;
    const dpr = Math.min(devicePixelRatio || 1, 2);
    const size = () => { w = cv.clientWidth; h = cv.clientHeight; cv.width = w * dpr; cv.height = h * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      const n = Math.round(w * h / 10000 * (o.density || 1)); drops = Array.from({ length: n }, () => ({ x: rand(0, w), y: rand(0, h), l: rand(10, 24), v: rand(9, 16) * (o.speed || 1), a: rand(.08, .28) * (o.alpha || 1) })); };
    size(); addEventListener('resize', size);
    const tick = () => {
      ctx.clearRect(0, 0, w, h); ctx.lineWidth = 1;
      for (const d of drops) {
        ctx.strokeStyle = (o.color || 'rgba(170,215,255,') + d.a + ')';
        ctx.beginPath(); ctx.moveTo(d.x, d.y); ctx.lineTo(d.x - d.l * .18, d.y + d.l); ctx.stroke();
        d.y += d.v; d.x -= d.v * .18;
        if (d.y > h) { d.y = -d.l; d.x = rand(0, w * 1.15); }
      }
      if (vis || o.always) raf = requestAnimationFrame(tick);
    };
    if (!o.always) new IntersectionObserver(es => { const was = vis; vis = es[0].isIntersecting; if (vis && !was) raf = requestAnimationFrame(tick); }).observe(host);
    raf = requestAnimationFrame(tick);
    return () => cancelAnimationFrame(raf);
  }
  $$('[data-rain]').forEach(el => rainOn(el));

  /* ---------- intro: lightning strikes the logo, then the page lifts up ---------- */
  const loader = $('#loader');
  let stopIntroRain = null;
  function finishIntro() { if (stopIntroRain) stopIntroRain(); if (loader) loader.remove(); html.classList.remove('intro', 'intro-out'); heroIn(); if (ST) ScrollTrigger.refresh(); }
  function boltPath(x0, y0, x1, y1, rough) {
    // midpoint displacement gives a natural jagged bolt
    let pts = [[x0, y0], [x1, y1]], d = rough;
    for (let k = 0; k < 6; k++) {
      const nx = [];
      for (let i = 0; i < pts.length - 1; i++) {
        const [ax, ay] = pts[i], [bx, by] = pts[i + 1];
        nx.push(pts[i], [(ax + bx) / 2 + rand(-d, d), (ay + by) / 2 + rand(-d, d) * .3]);
      }
      nx.push(pts[pts.length - 1]); pts = nx; d *= .55;
    }
    return pts;
  }
  const toD = pts => 'M' + pts.map(p => p[0].toFixed(1) + ' ' + p[1].toFixed(1)).join(' L');
  function runIntro() {
    try { sessionStorage.setItem('rcd_intro', '1'); } catch (e) {}
    if (!loader || !html.classList.contains('intro') || reduce) { finishIntro(); return; }
    stopIntroRain = rainOn(loader, { always: true, density: 5, speed: 1.5, alpha: 1.5 });
    const svg = $('svg.bolt', loader), flash = $('.flash', loader), logo = $('.logo', loader);
    const W = innerWidth, H = innerHeight;
    svg.setAttribute('viewBox', `0 0 ${W} ${H}`);
    const r = logo.getBoundingClientRect();
    const pt = k => loader.dataset[k].split(',').map(Number);
    const [ax, ay] = pt('apex'), tx = r.left + r.width * ax, ty = r.top + r.height * ay; // the roof peak of the logo
    $$('.ring, .glow', loader).forEach(el => { el.style.left = tx + 'px'; el.style.top = ty + 'px'; });
    const flashTo = (o, ms) => { flash.style.transition = `opacity ${ms}ms ease-out`; flash.style.opacity = o; };
    const addBolt = (pts, wd, cls) => {
      const d = toD(pts);
      const g = document.createElementNS('http://www.w3.org/2000/svg', 'g'); g.setAttribute('class', cls || '');
      g.innerHTML = `<path d="${d}" stroke="rgba(99,192,242,.55)" stroke-width="${wd * 7}" filter="url(#glow)"/><path d="${d}" stroke="#d9f1ff" stroke-width="${wd * 2.2}"/><path d="${d}" stroke="#fff" stroke-width="${wd}"/>`;
      svg.appendChild(g);
      $$('path', g).forEach(p => { const L = p.getTotalLength(); p.style.strokeDasharray = L; p.style.strokeDashoffset = L; p.getBoundingClientRect(); p.style.transition = 'stroke-dashoffset .16s cubic-bezier(.6,0,.9,.5)'; p.style.strokeDashoffset = 0; });
      return g;
    };
    // distant flicker first
    setTimeout(() => { flashTo(.12, 60); setTimeout(() => flashTo(0, 300), 70); }, 250);
    setTimeout(() => { flashTo(.06, 40); setTimeout(() => flashTo(0, 200), 50); }, 480);
    // the strike
    setTimeout(() => {
      const sx = tx + rand(-W * .18, W * .18);
      const main = boltPath(sx, -20, tx, ty, Math.max(60, W * .07));
      const groups = [addBolt(main, 2.6)];
      // forks off the main bolt
      for (let b = 0; b < 3; b++) {
        const i = Math.floor(rand(main.length * .2, main.length * .7)), [bx, by] = main[i];
        groups.push(addBolt(boltPath(bx, by, bx + rand(-W * .22, W * .22), by + rand(H * .08, H * .22), 30), 1.1, 'fork'));
      }
      setTimeout(() => {
        flashTo(.9, 30); loader.classList.add('struck');
        // sparks from the peak
        for (let s = 0; s < 26; s++) {
          const sp = document.createElement('i'); sp.className = 'spark'; sp.style.left = tx + 'px'; sp.style.top = ty + 'px'; loader.appendChild(sp);
          const a = rand(Math.PI * 1.05, Math.PI * 1.95), dist = rand(60, 220);
          sp.animate([{ transform: 'translate(0,0) scale(1)', opacity: 1 }, { transform: `translate(${Math.cos(a) * dist}px,${Math.sin(a) * dist * .6 + rand(40, 120)}px) scale(.2)`, opacity: 0 }], { duration: rand(500, 900), easing: 'cubic-bezier(.2,.7,.3,1)', fill: 'forwards' });
        }
        setTimeout(() => flashTo(0, 450), 60);
        // electricity crackles down both slopes of the logo's roof
        const [lx, ly] = pt('l'), [rx, ry] = pt('r'), L = [r.left + r.width * lx, r.top + r.height * ly], R = [r.left + r.width * rx, r.top + r.height * ry];
        [0, 140, 300].forEach(t => setTimeout(() => {
          const arcs = [addBolt(boltPath(tx, ty, L[0], L[1], 14), .8, 'fork'), addBolt(boltPath(tx, ty, R[0], R[1], 14), .8, 'fork')];
          setTimeout(() => arcs.forEach(g => g.remove()), 110);
        }, t));
        // bolt flickers out
        const fl = [[120, .25], [190, 1], [260, .4], [330, 0]];
        fl.forEach(([t, o]) => setTimeout(() => groups.forEach(g => g.style.opacity = o), t));
        setTimeout(() => { flashTo(.55, 20); setTimeout(() => flashTo(0, 380), 40); }, 200);
      }, 150);
    }, 750);
    // lift the whole intro up to reveal the home page
    setTimeout(() => { html.classList.add('intro-out'); heroIn(); setTimeout(finishIntro, 850); }, 2700);
  }

  /* split headings into words */
  function splitWords(el) {
    if (el.dataset.splitDone) return $$('.w > span', el);
    const walk = node => {
      [...node.childNodes].forEach(n => {
        if (n.nodeType === 3) {
          const frag = document.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach(part => {
            if (!part) return;
            if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(' ')); return; }
            const w = document.createElement('span'); w.className = 'w'; w.style.cssText = 'display:inline-block;overflow:hidden;vertical-align:bottom;padding-bottom:.08em;margin-bottom:-.08em';
            const i = document.createElement('span'); i.style.display = 'inline-block'; i.textContent = part;
            w.appendChild(i); frag.appendChild(w);
          });
          node.replaceChild(frag, n);
        } else if (n.nodeType === 1 && !n.classList.contains('w')) walk(n);
      });
    };
    walk(el); el.dataset.splitDone = '1';
    return $$('.w > span', el);
  }

  /* hero entrance */
  let heroDone = false;
  function heroIn() {
    if (heroDone) return; heroDone = true;
    const hero = $('.hero, .phero'); if (!hero) return;
    $$('video', hero).forEach(v => v.play().catch(() => {}));
    if (!G || reduce) return;
    const tl = gsap.timeline({ defaults: { ease: 'power3.out' } });
    const h = $('h1', hero);
    if (h) { if (touch) tl.from(h, { opacity: 0, y: 26, duration: 0.9, clearProps: 'all' }, 0.1); else tl.from(splitWords(h), { yPercent: 110, duration: 1, stagger: 0.045, clearProps: 'all' }, 0.05); }
    const gb = $('.gbadge', hero); if (gb) tl.from(gb, { opacity: 0, y: -12, scale: 0.96, duration: 0.7, clearProps: 'all' }, 0);
    const eb = $('.eyebrow, .crumb', hero); if (eb) tl.from(eb, { opacity: 0, x: -20, duration: 0.8, clearProps: 'all' }, 0.1);
    const lead = $('.lead', hero); if (lead) tl.from(lead, { opacity: 0, y: 20, duration: 0.9, clearProps: 'all' }, 0.45);
    const btns = $$('.btn-row .btn', hero); if (btns.length) tl.from(btns, { opacity: 0, y: 16, duration: 0.7, stagger: 0.1, clearProps: 'all' }, 0.6);
    const trust = $('.trust', hero); if (trust) tl.from(trust, { opacity: 0, y: 14, duration: 0.8, clearProps: 'all' }, 0.85);
    const vc = $('.vcard', hero); if (vc) tl.from(vc, { clipPath: 'inset(45% 0 45% 0 round 28px)', scale: 0.97, duration: 1.2, ease: 'power4.inOut', clearProps: 'all' }, 0.15);
    const fr = $('.vwrap .frame', hero); if (fr) tl.from(fr, { opacity: 0, scale: 1.05, duration: 1, clearProps: 'all' }, 0.9);
    const pill = $('.vwrap .pill', hero); if (pill) tl.from(pill, { opacity: 0, y: 20, scale: 0.92, duration: 0.7, ease: 'back.out(1.6)', clearProps: 'all' }, 1.2);
    const tag = $('.vwrap .tag', hero); if (tag) tl.from(tag, { opacity: 0, x: -14, duration: 0.6, clearProps: 'all' }, 1.1);
    const bg = $('img.bg', hero); if (bg && !touch) tl.from(bg, { scale: 1.12, duration: 1.8, ease: 'power2.out', clearProps: 'transform' }, 0);
    const sc = $('.scroll', hero); if (sc) tl.from(sc, { opacity: 0, duration: 0.8 }, 1.3);
  }

  /* scroll animations */
  function ioFx() {
    const els = $$('[data-reveal]').filter(el => !el.closest('.hero, .phero'));
    const io = new IntersectionObserver(es => es.forEach(e => {
      if (!e.isIntersecting) return; const el = e.target;
      if (el.dataset.reveal === 'group') [...el.children].forEach((c, i) => { c.style.transitionDelay = (i * 70) + 'ms'; });
      el.classList.add('in'); io.unobserve(el);
    }), { rootMargin: '0px 0px -6% 0px', threshold: 0.01 });
    els.forEach(el => io.observe(el));
    $$('[data-reveal]').filter(el => el.closest('.hero, .phero')).forEach(el => el.classList.add('in'));
  }
  function scrollFx() {
    if (reduce) { $$('[data-reveal]').forEach(el => el.classList.add('in')); return; }
    if (touch || !ST) { ioFx(); return; }
    gsap.defaults({ ease: 'power3.out' });
    $$('[data-reveal]').forEach(el => {
      el.classList.add('in');
      if (el.closest('.hero, .phero')) return;
      if (el.dataset.reveal === 'group') gsap.from(el.children, { y: 44, opacity: 0, duration: 1, stagger: 0.1, clearProps: 'transform,opacity', scrollTrigger: { trigger: el, start: 'top 88%' } });
      else gsap.from(el, { y: 44, opacity: 0, duration: 1, clearProps: 'transform,opacity', scrollTrigger: { trigger: el, start: 'top 90%' } });
    });
    $$('[data-split]').forEach(el => { if (el.closest('.hero, .phero')) return; gsap.from(splitWords(el), { yPercent: 110, duration: 0.9, stagger: 0.03, clearProps: 'all', scrollTrigger: { trigger: el, start: 'top 86%' } }); });
    $$('[data-clip]').forEach(el => {
      const img = $('img', el);
      const tl = gsap.timeline({ scrollTrigger: { trigger: el, start: 'top 85%' } });
      tl.from(el, { clipPath: 'inset(0 0 100% 0 round 24px)', duration: 1.2, ease: 'power4.inOut', clearProps: 'clipPath' }, 0);
      if (img) tl.from(img, { scale: 1.2, duration: 1.6, ease: 'power3.out', clearProps: 'transform' }, 0);
    });
    $$('.weather .big').forEach(el => gsap.to(el, { xPercent: -14, ease: 'none', scrollTrigger: { trigger: el.parentElement, start: 'top bottom', end: 'bottom top', scrub: true } }));
    $$('[data-count]').forEach(el => { const n = +el.dataset.count; const o = { v: 0 }; gsap.to(o, { v: n, duration: 1.6, ease: 'power2.out', onUpdate: () => el.textContent = Math.round(o.v), scrollTrigger: { trigger: el, start: 'top 90%' } }); });
  }

  scrollFx();
  runIntro();
})();
