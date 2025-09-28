async function search(){
  const q = document.getElementById('q').value.trim();
  if(!q) return alert('Please enter a soil or crop name');
  document.getElementById('results').innerHTML = '<p class="small">Searching...</p>';

  try{
    const res = await fetch('/api/search?q='+encodeURIComponent(q));
    const data = await res.json();
    renderResults(data);
  }catch(err){
    console.error(err);
    document.getElementById('results').innerHTML = '<p class="small">Server error</p>';
  }
}

function renderResults(data){
  const container = document.getElementById('results');
  container.innerHTML = '';

  if(data.soils && data.soils.length){
    data.soils.forEach(s => {
      const div = document.createElement('div');
      div.className='card';
      div.innerHTML = `
        <h3>${s.name} <span class="badge">Soil</span></h3>
        <img src="${s.image || '/static/placeholder-soil.jpg'}" alt="${s.name}" />
        <p class="small"><strong>Notes:</strong> ${s.notes || 'No details available'}</p>
        <p class="small"><strong>Recommended crops:</strong></p>
        ${s.recommended_crops.length ? s.recommended_crops.map(c=>`<div class="small">• <strong>${c.name}</strong> — ${c.short_note}</div>`).join('') : '<div class="small">No recommended crops found.</div>'}
      `;
      container.appendChild(div);
    });
  }

  if(data.crops && data.crops.length){
    data.crops.forEach(c => {
      const div = document.createElement('div');
      div.className='card';
      div.innerHTML = `
        <h3>${c.name} <span class="badge">Crop</span></h3>
        <img src="${c.image || '/static/placeholder-crop.jpg'}" alt="${c.name}" />
        <p class="small"><strong>Soil:</strong> ${c.soil_preference || 'General'}</p>
        <p class="small"><strong>Growth notes:</strong> ${c.short_note || 'No notes'}</p>
        <p class="small"><strong>Fertilizer (N-P-K):</strong> ${c.fertilizer || 'Varies'}</p>
      `;
      container.appendChild(div);
    });
  }

  if((!data.soils || data.soils.length===0) && (!data.crops || data.crops.length===0)){
    container.innerHTML = '<p class="small">No matches found</p>';
  }
}

document.getElementById('searchBtn').addEventListener('click', search);
document.getElementById('q').addEventListener('keydown', (e)=>{ if(e.key==='Enter') search(); });