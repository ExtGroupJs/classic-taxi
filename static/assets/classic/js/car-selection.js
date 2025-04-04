function mybanner(cars) { 
  const headDiv = document.getElementById("headdiv");
  const headName = document.getElementById("headname");
  const headDescription = document.getElementById("headdescription");

  // Seleccionar un coche aleatoriamente
  const randomCar = cars[Math.floor(Math.random() * cars.length)];
  // Actualizar el contenido de la página
  headDiv.style.backgroundImage = `url('${randomCar.main_picture}')`;
  headName.textContent = `${randomCar.model_name} ${randomCar.year}`;
  headDescription.textContent = randomCar.extra_info;
}
