const route = location.pathname.replace(/\/+$/, '');
const segment = route.split('/').filter(Boolean).at(-1);
const params = new URLSearchParams(location.search);
const requested = params.get('variant')?.toLowerCase();
const storageKey = `vereda-ab-${segment}`;
let variant = requested === 'a' || requested === 'b' ? requested : localStorage.getItem(storageKey);

if (variant !== 'a' && variant !== 'b') {
  const random = new Uint32Array(1);
  crypto.getRandomValues(random);
  variant = random[0] % 2 === 0 ? 'a' : 'b';
}

localStorage.setItem(storageKey, variant);
params.delete('variant');
const query = params.toString();
location.replace(`${route}/${variant}/${query ? `?${query}` : ''}${location.hash}`);
