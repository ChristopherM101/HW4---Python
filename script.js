function loadTruckingCompanies() {
  const file = (document.getElementById('jsonFile').value || '').trim();
  const err  = document.getElementById('errorMessage');
  err.textContent = '';
  
  if (!file || !/\.json$/i.test(file)) { 
    err.textContent = 'Please enter a valid .json filename.'; return; 
  }

  fetch(`/cgi-bin/server.py?file=${encodeURIComponent(file)}`)
    .then(r => r.text())
    .then(html => {
      const w = window.open('', '', 'width=900,height=650,scrollbars=yes');
      if (!w) { err.textContent = 'Popup blocked—allow popups for this site.'; return; }
      w.document.open(); w.document.write(html); w.document.close();
    })
    .catch(e => err.textContent = 'Request failed: ' + e.message);
}
document.getElementById('go').addEventListener('click', loadTruckingCompanies);
