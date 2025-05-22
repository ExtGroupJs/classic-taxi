window.carData = window.carData || {};
const initVehicleCarousel = () => {
  const carouselContainer = document.querySelector(".carousel-car");
  // carouselContainer.empty();
  if (!carouselContainer) {
    console.error("No se encontró el contenedor del carrusel (.carousel-car)");
    return;
  }

  // Función para cargar y renderizar los vehículos
  const loadVehicles = async () => {
    try {
      // lang = localStorage.getItem("userLanguage") || "es";
      const response = await axios.get("/business-gestion/cars/");
      const cars = response.data.results;
      mybanner(cars);
      if (cars.length === 0) {
        carouselContainer.innerHTML = "<p>No hay vehículos disponibles</p>";
        return;
      }

      // Crear el HTML para todos los vehículos
      const carsHTML = cars
        .map(
          (car) => `
          <div class="item">
            <div class="car-wrap rounded ftco-animate">
              <div class="img rounded d-flex align-items-end" style="background-image: url('${car.main_picture}');">
              </div>
              <div class="text">
                <h2 class="mb-0"><a href="#">${car.model_name}</a></h2>
                <div class="d-flex mb-3">
                  <span class="cat">${car.year}</span>
                  <p class="price ml-auto">${car.seats} <span>/Seats</span></p>
                </div>
                <p class="d-flex mb-0 d-block">
                  <a  class="whatsapp btn btn-primary py-2 mr-1" "
                     data-car-name="${car.model_name}">Book now</a> 
                  <a  class="btn btn-secondary py-2 ml-1" data-car-name="${car.id}" onclick='detalles(${car.id})'>Details</a>
                </p>
              </div>
            </div>
          </div>
        `
        )
        .join("");

      // Insertar el HTML en el contenedor
      carouselContainer.innerHTML = carsHTML;

      //Inicializar Owl Carousel
      $(carouselContainer).owlCarousel({
        center: true,
        loop: true,
        margin: 30,
        autoplay: true,
        autoplayHoverPause: true,
        autoplayTimeout: 4000,
        nav: true,
        navText: [
          '<span class="ion-ios-arrow-back"></span>',
          '<span class="ion-ios-arrow-forward"></span>',
        ],
        responsive: {
          0: {
            items: 1,
            nav: false,
          },
          600: {
            items: 2,
            nav: false,
          },
          1000: {
            items: 3,
            nav: true,
          },
        },
      });

      // $('.carousel-car').owlCarousel({
      //   center: true,
      //   loop: true,
      //   autoplay: true,
      //   items:1,
      //   margin: 30,
      //   stagePadding: 0,
      //   nav: false,
      //   navText: ['<span class="ion-ios-arrow-back">', '<span class="ion-ios-arrow-forward">'],
      //   responsive:{
      //     0:{
      //       items: 1
      //     },
      //     600:{
      //       items: 2
      //     },
      //     1000:{
      //       items: 3
      //     }
      //   }
      // });

      // Reinicializar AOS para las animaciones
      if (typeof AOS !== "undefined") {
        AOS.refresh();
      }
    } catch (error) {
      console.error("Error al cargar los vehículos:", error);
      carouselContainer.innerHTML = "<p>Error al cargar los vehículos</p>";
    }
  };

  // Iniciar la carga de vehículos
  loadVehicles();
};
document.addEventListener("DOMContentLoaded", function () {
  initVehicleCarousel();
});

function detalles(id) {
  localStorage.setItem("carid", id);
  window.location = "/carsdetail/";
}
