function enviarOpinion() {
  const opinionForm = document.getElementById('opinionForm');
  const opinionMsg = document.getElementById('opinionMsg');
  fetch(opinionForm.action || window.location.href, {
    method: 'POST',
    body: new FormData(opinionForm),
    headers: {
      'X-Requested-With': 'XMLHttpRequest'
    }
  })
  .then(response => {
    if (response.ok) {
      opinionMsg.style.display = 'block';
      opinionForm.reset();
    }
  });
}