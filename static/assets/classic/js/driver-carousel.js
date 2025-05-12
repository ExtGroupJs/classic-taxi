document.addEventListener("DOMContentLoaded", function () {
  const initVehicledrivercarousel = () => {
    const driverCrouselContainer = document.querySelector(".carousel-driver");
    // driverCrouselContainer.empty();
    if (!driverCrouselContainer) {
      console.error(
        "No se encontró el contenedor del driver driverrusel (.drivercarousel-driver)"
      );
      return;
    }

    // Función para cargar y renderizar los vehículos
    const loadDriver = async () => {
      try {
        lang = localStorage.getItem("userLanguage") || "es";

        const response = await axios.get(
          "/business-gestion/drivers?lang=" + lang
        );
        const drivers = response.data.results;

        if (drivers.length === 0) {
          driverCrouselContainer.innerHTML =
            "<p>No hay conductores disponibles</p>";
          return;
        }

        // Crear el HTML para todos los vehículos
        const driversHTML = drivers
          .map(
            (driver) => `
          <div class="item">
                <div class="testimony-wrap rounded text-center py-4 pb-5">
                  <div class="user-img mb-2" style="background-image: url('${driver.main_picture}');">
                  </div>
                  <div class="text pt-4">
                    <p class="mb-4">${driver.extra_info}</p>
                     <p class="name">${driver.name}</p>
                    <span class="position">Driving since ${driver.licence_year} </span>
                  </div>
                </div>
              </div>
        `
          )
          .join("");
        //     (driver) => `
        //   <div class="item">
        //     <div class="driver-wrap rounded ftco-animate">
        //       <div class="img rounded d-flex align-items-end" style="background-image: url('${driver.main_picture}');">
        //       </div>
        //       <div class="text">
        //         <h2 class="mb-0"><a href="#">${driver.name}</a></h2>
        //         <div class="d-flex mb-3">
        //           <span class="cat">${driver.year}</span>
        //           <p class="price ml-auto">${driver.seats} <span>/Seats</span></p>
        //         </div>
        //         <p class="d-flex mb-0 d-block">
        //           <a  class="whatsapp btn btn-primary py-2 mr-1" "
        //              data-driver-name="${driver.model_name}">Book now</a>
        //           <a  class="btn btn-secondary py-2 ml-1" data-driver-name="${driver.id}" onclick='detalles(${driver.id})'>Details</a>
        //         </p>
        //       </div>
        //     </div>
        //   </div>
        // `
        //   )

        // Insertar el HTML en el contenedor
        driverCrouselContainer.innerHTML = driversHTML;

        //Inicializar Owl drivercarousel
        $(driverCrouselContainer).owlCarousel({
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

        // Reinicializar AOS para las animaciones
        if (typeof AOS !== "undefined") {
          AOS.refresh();
        }
      } catch (error) {
        console.log("✌️error --->", error);
        console.error("Error al cargar los vehículos:", error);
        driverCrouselContainer.innerHTML =
          "<p>Error al cargar los vehículos</p>";
      }
    };

    // Iniciar la dcarga de vehículos
    loadDriver();
  };

  // Ejecutar la inicialización
  initVehicledrivercarousel();
});
