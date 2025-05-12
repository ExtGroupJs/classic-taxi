document.addEventListener("DOMContentLoaded", function () {
  const langLinks = document.querySelectorAll(".dropdown-item[data-lang]");
  const dropdownToggle = document.querySelector(
    '.dropdown-toggle[data-toggle="dropdown"]'
  );

  // Configuración inicial
  const defaultLanguage = "es"; // Idioma por defecto
  let currentLanguage = localStorage.getItem("userLanguage") || defaultLanguage;

  // Función para resaltar el idioma activo
  function highlightActiveLanguage(lang) {
    // Remover clase 'active' de todos los items
    langLinks.forEach((link) => {
      link.classList.remove("active");
      link.classList.remove("font-weight-bold");
    });

    // Añadir clase 'active' al idioma actual
    const activeLink = document.querySelector(
      `.dropdown-item[data-lang="${lang}"]`
    );
    if (activeLink) {
      activeLink.classList.add("active");
      activeLink.classList.add("font-weight-bold");

      // Actualizar texto del botón dropdown
      if (dropdownToggle) {
        const langNames = {
          es: "Español",
          en: "English",
          fr: "Français",
        };
        dropdownToggle.innerHTML = langNames[lang] || "Idioma";
      }
    }
  }

  // Función para cambiar el idioma
  function setLanguage(lang) {
    currentLanguage = lang;
    localStorage.setItem("userLanguage", lang);
    // Disparar evento personalizado
    // document.dispatchEvent(
    //   new CustomEvent("languageChanged", {
    //     detail: { language: lang },
    //   })
    // );
    highlightActiveLanguage(lang);

    // Aquí puedes añadir la lógica para notificar al backend
    console.log("Idioma cambiado a:", lang);
  }

  // Inicializar mostrando el idioma actual
  highlightActiveLanguage(currentLanguage);

  // Manejar clicks en los enlaces de idioma
  langLinks.forEach((link) => {
    link.addEventListener("click", function (e) {
      e.preventDefault();
      const lang = this.getAttribute("data-lang");
      setLanguage(lang);

      // Opcional: Recargar la página si es necesario
      window.location.reload();
    });
  });
});

// Función auxiliar para obtener cookies (necesaria para CSRF token en Django)
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
