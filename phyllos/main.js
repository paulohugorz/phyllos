// Cursor
const cursor = document.getElementById('cursor');
if (cursor) {
  document.addEventListener('mousemove', e => {
    cursor.style.left = e.clientX + 'px';
    cursor.style.top = e.clientY + 'px';
  });
  document.querySelectorAll('a, button, .product-card, .cat-card, .size, .material-card, .collection-feature').forEach(el => {
    el.addEventListener('mouseenter', () => cursor.classList.add('hover'));
    el.addEventListener('mouseleave', () => cursor.classList.remove('hover'));
  });
}

// Nav scroll
window.addEventListener('scroll', () => {
  const nav = document.getElementById('mainNav');
  if (nav) nav.classList.toggle('scrolled', window.scrollY > 40);
});

// Active nav link
(function() {
  const page = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a').forEach(a => {
    if (a.getAttribute('href') === page) a.classList.add('active');
  });
})();

// Cart state
let cartNum = parseInt(document.getElementById('cartCount')?.textContent || '0');

function toggleCart() {
  const drawer = document.getElementById('cartDrawer');
  const overlay = document.getElementById('overlay');
  if (drawer) drawer.classList.toggle('open');
  if (overlay) overlay.classList.toggle('show');
}

function closeCart() {
  const drawer = document.getElementById('cartDrawer');
  const overlay = document.getElementById('overlay');
  if (drawer) drawer.classList.remove('open');
  if (overlay) overlay.classList.remove('show');
}

function addToCart(e) {
  cartNum++;
  const countEl = document.getElementById('cartCount');
  if (countEl) countEl.textContent = cartNum;
  const card = e.currentTarget;
  card.style.outline = '1px solid rgba(184,154,106,0.4)';
  setTimeout(() => { card.style.outline = ''; }, 600);
}

// Attach addToCart to product cards
document.querySelectorAll('.product-card').forEach(card => {
  card.addEventListener('click', addToCart);
});

// Wishlist toggle
document.querySelectorAll('.product-wish').forEach(btn => {
  btn.addEventListener('click', e => {
    e.stopPropagation();
    btn.textContent = btn.textContent === '♡' ? '♥' : '♡';
  });
});

// Mobile nav
function toggleMobileNav() {
  const nav = document.getElementById('mainNav');
  if (!nav) return;
  nav.classList.toggle('nav-mobile-open');
  const spans = document.querySelectorAll('.nav-hamburger span');
  const open = nav.classList.contains('nav-mobile-open');
  if (open) {
    spans[0].style.transform = 'translateY(6px) rotate(45deg)';
    spans[1].style.opacity = '0';
    spans[2].style.transform = 'translateY(-6px) rotate(-45deg)';
  } else {
    spans.forEach(s => { s.style.transform = ''; s.style.opacity = ''; });
  }
}

function checkMobile() {
  const hb = document.getElementById('hamburger');
  const nav = document.getElementById('mainNav');
  if (!hb || !nav) return;
  if (window.innerWidth <= 768) { hb.style.display = 'flex'; }
  else { hb.style.display = 'none'; nav.classList.remove('nav-mobile-open'); }
}
checkMobile();
window.addEventListener('resize', checkMobile);
