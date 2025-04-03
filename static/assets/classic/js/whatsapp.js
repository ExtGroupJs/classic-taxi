document.addEventListener('DOMContentLoaded', function() {
  function getWhatsAppUrl(phone, message) {
    return `https://wa.me/${phone}?text=${encodeURIComponent(message)}`;
  }

  // Usar delegación de eventos en un contenedor padre que existe en el DOM
  document.addEventListener('click', function(event) {
    const whatsappButton = event.target.closest('.whatsapp');
    
    if (whatsappButton) {
      event.preventDefault();
      
      // Acceder a los datos de los coches desde el objeto global
      const cars = window.carData.cars || [];
      const carId = whatsappButton.dataset.carId;
      
      // Encontrar el coche específico si existe
      const selectedCar = cars.find(car => car.id === carId);
      
      const phoneNumber = '1234567890';
      const carModelName = selectedCar ? selectedCar.name : whatsappButton.dataset.carName || '';
      console.log('%c⧭', 'color: #0088cc', carModelName);
      
      let message = carModelName ? 
        `¡Hola! Me gustaría obtener más información sobre el ${carModelName}.` :
        `¡Hola! Me gustaría obtener más información sobre el Alquiler de los coches.`;

      const whatsappUrl = getWhatsAppUrl(phoneNumber, message);
      window.open(whatsappUrl, '_blank');
    }
  });
}); 