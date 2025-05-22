document.addEventListener("DOMContentLoaded", function () {
  const langLinks = document.querySelectorAll(".dropdown-item[data-lang]");
  const dropdownToggle = document.querySelector(
    '.dropdown-toggle[data-toggle="dropdown"]'
  );

  const defaultLanguage = "es"; // Idioma por defecto
  setLanguage(localStorage.getItem("userLanguage") || defaultLanguage);

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

  function setLanguage(lang) {
    localStorage.setItem("userLanguage", lang);
    document.cookie = "django_language=" + lang;
    localStorage.setItem("django_language", lang);
    highlightActiveLanguage(lang);
  }

  // Manejar clicks en los enlaces de idioma
  langLinks.forEach((link) => {
    link.addEventListener("click", function (e) {
      e.preventDefault();
      const lang = this.getAttribute("data-lang");
      setLanguage(lang);

      // Recargar la página
      window.location.reload();
    });
  });
});
