

document.addEventListener('DOMContentLoaded', function() {
  
  const headDiv = document.getElementById('headdiv');
  const headName = document.getElementById('headname');
  const headDescription = document.getElementById('headdescription');

  axios.get('/business-gestion/cars/')
    .then(response => {     
      const cars = response.data.results;
      if (cars.length === 0) return;

      // Seleccionar un coche aleatoriamente
      const randomCar = cars[Math.floor(Math.random() * cars.length)];
      // Actualizar el contenido de la página
      headDiv.style.backgroundImage = `url('${randomCar.main_picture}')`;
      headName.textContent = `${randomCar.model_name} ${randomCar.year}`;
      headDescription.textContent = randomCar.extra_info;
    })
    .catch(error => {
      console.error('Error fetching car data:', error);
    });
}); 