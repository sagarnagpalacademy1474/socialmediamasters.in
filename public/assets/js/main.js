(function () {
  var WA = '919911941474';

  // Header turns solid on scroll
  var header = document.querySelector('.site-header');
  function onScroll() { if (header) header.classList.toggle('solid', window.scrollY > 30); }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Mobile menu
  var menuBtn = document.querySelector('.menu-btn');
  if (menuBtn) {
    menuBtn.addEventListener('click', function () {
      var open = document.body.classList.toggle('menu-open');
      menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.querySelectorAll('.nav-links a').forEach(function (a) {
      a.addEventListener('click', function () { document.body.classList.remove('menu-open'); });
    });
  }

  // Reveal on scroll
  var items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: 0.12 });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('in'); });
  }

  // Price toggle (monthly / 3-month / 6-month)
  var toggle = document.querySelector('.toggle');
  if (toggle) {
    toggle.addEventListener('click', function (e) {
      var b = e.target.closest('button');
      if (!b) return;
      var term = b.getAttribute('data-term');
      toggle.querySelectorAll('button').forEach(function (x) { x.classList.toggle('on', x === b); });
      document.querySelectorAll('[data-m]').forEach(function (el) {
        var v = el.getAttribute('data-' + term);
        var plan = el.closest('.plan');
        var na = plan && plan.querySelector('.na');
        if (v) {
          el.textContent = v; el.style.display = '';
          if (na) na.style.display = 'none';
          var per = plan && plan.querySelector('.per');
          if (per) per.textContent = term === 'm' ? 'per month + GST · no commitment' : 'per month + GST · ' + (term === 't' ? '3-month plan' : '6-month plan') + ', paid upfront';
        } else {
          el.style.display = 'none';
          if (na) na.style.display = '';
          var per2 = plan && plan.querySelector('.per');
          if (per2) per2.textContent = 'Monthly plan only';
        }
      });
    });
  }

  // Chips (multi-select)
  document.querySelectorAll('.chips').forEach(function (g) {
    g.addEventListener('click', function (e) {
      var b = e.target.closest('button');
      if (!b) return;
      if (g.hasAttribute('data-single')) g.querySelectorAll('button').forEach(function (x) { if (x !== b) x.classList.remove('on'); });
      b.classList.toggle('on');
    });
  });

  // Step-by-step form
  document.querySelectorAll('.step-form form').forEach(function (form) {
    var steps = form.querySelectorAll('.sf-step');
    var bars = form.querySelectorAll('.sf-prog i');
    var cur = 0;
    function show(i) {
      steps.forEach(function (s, k) { s.hidden = k !== i; });
      bars.forEach(function (b, k) { b.classList.toggle('on', k <= i); });
      cur = i;
      var first = steps[i].querySelector('input');
      if (first && i > 0) first.focus();
    }
    function valid(i) {
      var ok = true;
      steps[i].querySelectorAll('input[required]').forEach(function (f) {
        var bad = !f.value.trim();
        f.classList.toggle('bad', bad);
        if (bad && ok) { f.focus(); ok = false; }
      });
      return ok;
    }
    form.addEventListener('input', function (e) { if (e.target.value.trim()) e.target.classList.remove('bad'); });
    form.querySelectorAll('.sf-next').forEach(function (b) {
      b.addEventListener('click', function () { if (valid(cur)) show(cur + 1); });
    });
    form.querySelectorAll('.sf-back').forEach(function (b) {
      b.addEventListener('click', function () { show(cur - 1); });
    });
    form.addEventListener('keydown', function (e) {
      if (e.key !== 'Enter' || e.target.tagName !== 'INPUT') return;
      var ins = Array.prototype.slice.call(steps[cur].querySelectorAll('input'));
      var i = ins.indexOf(e.target);
      if (i > -1 && i < ins.length - 1) { e.preventDefault(); ins[i + 1].focus(); return; }
      if (cur < steps.length - 1) { e.preventDefault(); if (valid(cur)) show(cur + 1); }
    });
    form.addEventListener('submit', function (e) {
      if (!valid(cur)) { e.preventDefault(); e.stopImmediatePropagation(); }
    }, true);
    show(0);
  });

  document.querySelectorAll('form[data-wa]').forEach(function (form) {
    form.addEventListener('input', function (e) { if (e.target.value.trim()) e.target.classList.remove('bad'); });
  });

  // Forms open WhatsApp with the details filled in
  document.querySelectorAll('form[data-wa]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.closest('.step-form')) {
        var bad = null;
        form.querySelectorAll('[required]').forEach(function (f) {
          var b = !f.value.trim(); f.classList.toggle('bad', b); if (b && !bad) bad = f;
        });
        if (bad) { bad.focus(); return; }
      }
      var lines = [form.getAttribute('data-wa')];
      form.querySelectorAll('input, textarea').forEach(function (f) {
        if (f.value.trim()) lines.push(f.getAttribute('data-label') + ': ' + f.value.trim());
      });
      form.querySelectorAll('.chips').forEach(function (g) {
        var picked = Array.prototype.map.call(g.querySelectorAll('button.on'), function (b) { return b.textContent; });
        if (picked.length) lines.push(g.getAttribute('data-label') + ': ' + picked.join(', '));
      });
      var url = 'https://wa.me/' + WA + '?text=' + encodeURIComponent(lines.join('\n'));
      window.open(url, '_blank', 'noopener');
      var ok = form.parentNode.querySelector('.form-ok');
      if (ok) { form.style.display = 'none'; ok.style.display = 'block'; }
    });
  });

  // Year
  document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
