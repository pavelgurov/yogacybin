// Cleanse program pages: show one day at a time and remember where the reader left off.
(function () {
  var root = document.documentElement;
  var days = document.querySelectorAll('.day');
  var links = document.querySelectorAll('.daynav a');
  var prev = document.getElementById('prev');
  var next = document.getElementById('next');
  var all = document.getElementById('all');
  var key = 'cleanse-day:' + location.pathname;
  var current = 1;

  function saved() {
    try { return parseInt(localStorage.getItem(key), 10) || 1; } catch (e) { return 1; }
  }

  function show(n, scroll) {
    current = Math.min(Math.max(n, 1), days.length);
    days.forEach(function (d) { d.classList.toggle('on', +d.dataset.day === current); });
    links.forEach(function (a) {
      var on = +a.dataset.day === current;
      a.classList.toggle('on', on);
      if (on) {
        a.setAttribute('aria-current', 'true');
        a.parentNode.scrollLeft = a.offsetLeft - a.parentNode.clientWidth / 2 + a.offsetWidth / 2;
      } else {
        a.removeAttribute('aria-current');
      }
    });
    prev.disabled = current === 1;
    next.disabled = current === days.length;
    try { localStorage.setItem(key, current); } catch (e) {}
    if (scroll) document.getElementById('day-' + current).scrollIntoView();
  }

  function go(n) {
    history.replaceState(null, '', '#day-' + n);
    show(n, true);
  }

  // Opening a guide link (#oleation etc.) expands that entry
  function openTarget() {
    var m = location.hash.match(/^#day-(\d+)$/);
    if (m) { show(+m[1], true); return; }
    var el = location.hash && document.getElementById(location.hash.slice(1));
    if (el && el.tagName === 'DETAILS') el.open = true;
  }

  root.classList.add('js');
  links.forEach(function (a) {
    a.addEventListener('click', function (e) { e.preventDefault(); go(+a.dataset.day); });
  });
  prev.addEventListener('click', function () { go(current - 1); });
  next.addEventListener('click', function () { go(current + 1); });
  all.addEventListener('click', function () {
    var on = root.classList.toggle('show-all');
    all.textContent = on ? 'Show one day' : 'Show all days';
  });
  window.addEventListener('hashchange', openTarget);

  show(saved(), false);
  openTarget();
})();
