const API = import.meta.env.VITE_API_URL || 'http://localhost:5000/api';
export async function fetchProducts(q = '') {
  const url = `${API}/products${q?`?q=${encodeURIComponent(q)}`:''}`;
  const res = await fetch(url);
  if (!res.ok) throw new Error('Failed to fetch products');
  return res.json();
}
