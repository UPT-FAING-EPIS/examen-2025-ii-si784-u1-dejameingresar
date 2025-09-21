import React from 'react';

export default function ProductCard({product}){
  return (
    <div style={{border:'1px solid #ddd', padding:12, borderRadius:8}}>
      <img src={product.imageUrl || 'https://via.placeholder.com/300'} alt={product.name} style={{width:'100%', height:150, objectFit:'cover'}} />
      <h3>{product.name}</h3>
      <p>{product.description}</p>
      <div><strong>S/ {product.price}</strong></div>
    </div>
  )
}
