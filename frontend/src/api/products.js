const API = import.meta.env.VITE_API_URL || 'http://localhost:5000/api';
export async function fetchProducts() {
const res = await fetch(`${API}/products`);
return res.json();
}