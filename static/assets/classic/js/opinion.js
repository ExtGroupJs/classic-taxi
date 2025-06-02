function enviarOpinion() {
  const opinionForm = document.getElementById('opinionForm');
  const opinionMsg = document.getElementById('opinionMsg');
  const formData = new FormData(opinionForm);

  const data = {
    first_name: formData.get('first_name') || '',
    last_name: formData.get('last_name') || '',
    email: formData.get('email') || '',
    opinion: formData.get('opinion') || '',
    enabled: true
  };

  // Obtener el token CSRF del input oculto o meta tag
  // const token = document.querySelector('input[name="csrfmiddlewaretoken"]')?.value ||
  //               document.querySelector('meta[name="csrf-token"]')?.getAttribute('content') || '';

  axios.post('/business-gestion/clients/', data, {
    headers: {
      'X-Requested-With': 'XMLHttpRequest',
      'X-CSRFToken': getCSRFToken()
    }
  })
  .then(response => {
    if (response.status === 201 || response.status === 200) {
      opinionMsg.style.display = 'block';
      opinionForm.reset();
    }
  });
}


document.addEventListener('DOMContentLoaded', function() {
  let page = 1;
  let loading = false;
  let hasMore = true;
  const carousel = document.getElementById('testimonials-carousel');

  function loadTestimonials() {
    if (loading || !hasMore) return;
    loading = true;
    axios.get(`/business-gestion/clients/?page=${page}`)
      .then(function(response) {
        const testimonials = response.data.results.filter(c => c.enabled && c.opinion && c.first_name);
        testimonials.forEach(function(client) {
          const item = document.createElement('div');
          item.className = 'item';
          item.innerHTML = `
            <div class="testimony-wrap rounded text-center py-4 pb-5">
              <div class="user-img mb-2" style="background-image: url('/static_output/assets/classic/images/avatar${Math.floor(Math.random() * 5) + 1}.png');"></div>
              <div class="text pt-4">
                <p class="mb-4">${client.opinion}</p>
                <p class="name">${client.first_name} ${client.last_name || ''}</p>
              </div>
            </div>
          `;
          carousel.appendChild(item);
        });
        if (typeof $ !== 'undefined' && typeof $.fn.owlCarousel === 'function' && page === 1) {
          $('#testimonials-carousel').owlCarousel({
            loop: true,
            margin: 30,
            nav: false,
            dots: true,
            autoplay: true,
            items: 1,
            responsive: { 0: { items: 1 }, 600: { items: 1 }, 1000: { items: 2 } }
          });
        }
        hasMore = !!response.data.next;
        if (hasMore) page++;
        loading = false;
      })
      .catch(function() {
        loading = false;
      });
  }

  if (carousel) {
    loadTestimonials();
    carousel.addEventListener('scroll', function() {
      if (carousel.scrollLeft + carousel.clientWidth >= carousel.scrollWidth - 10) {
        loadTestimonials();
      }
    });
  }
});