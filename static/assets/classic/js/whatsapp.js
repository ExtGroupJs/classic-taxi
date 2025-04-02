document.addEventListener('DOMContentLoaded', function() {
  function getWhatsAppUrl(phone, message) {
    return `https://wa.me/${phone}?text=${encodeURIComponent(message)}`;
  }

  // Usar delegación de eventos en un contenedor padre que existe en el DOM
  document.addEventListener('click', function(event) {
    const whatsappButton = event.target.closest('.whatsapp');
    
    if (whatsappButton) {
      event.preventDefault();
      
      // Obtener datos del botón usando dataset
      const phoneNumber = '1234567890';
      const carModelName = whatsappButton.dataset.carName || '';
      console.log('%c⧭', 'color: #0088cc', carModelName);
      let message=""
      if(carModelName || carModelName!=''){ message = `¡Hola! Me gustaría obtener más información sobre el ${carModelName}.`;}
      else{ message = `¡Hola! Me gustaría obtener más información sobre el Alquiler de los coches.`;}
      // Crear mensaje personalizado con los datos del carro
     
    

      const whatsappUrl = getWhatsAppUrl(phoneNumber, message);
      window.open(whatsappUrl, '_blank');
    }
  });
}); 