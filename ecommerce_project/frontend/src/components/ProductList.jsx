import React, { useEffect, useState } from 'react';
import { fetchProducts } from '../api/products';
import ProductCard from './ProductCard';

export default function ProductList(){
  const [products, setProducts] = useState([]);
  const [q, setQ] = useState('');

  useEffect(()=>{
    fetchProducts(q).then(setProducts).catch(err=>console.error(err));
  },[q]);

  return (
    <div>
      <div style={{marginBottom:10}}>
        <input placeholder='Buscar...' value={q} onChange={e=>setQ(e.target.value)} />
      </div>
      <div style={{display:'grid', gridTemplateColumns:'repeat(auto-fit,minmax(220px,1fr))', gap:12}}>
        {products.map(p => <ProductCard key={p.id} product={p} />)}
      </div>
    </div>
  )
}
