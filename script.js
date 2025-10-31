document.getElementById('go').addEventListener('click', async () => {
  const err = document.getElementById('errorMessage');
  err.textContent = '';

  const file = (document.getElementById('jsonFile').value || '').trim();
  if (!file || !/\.json$/i.test(file)) {
    err.textContent = 'Please enter a valid JSON filename, like truckinglist.json.';
    return;
  }

  try {// send the filename to Python script (fetch)
    const res = await fetch(`/cgi-bin/trucks.py?file=${encodeURIComponent(file)}`, {
      method: 'GET',
      headers: { 'Accept': 'text/html' }
    });

    const html = await res.text();
    
    const w = window.open('', '', 'width=900,height=650,scrollbars=yes');
    if (!w) {
      err.textContent = 'Popup blocked — allow popups for this site.';
      return;
    }
    w.document.open();
    w.document.write(html);
    w.document.close();
  } catch (e) {
    err.textContent = 'Request failed: ' + e.message;
  }
});
