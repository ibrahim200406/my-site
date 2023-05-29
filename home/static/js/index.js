document.addEventListener("click", function (event) {
  var menu = document.getElementById("navbar-collapse-toggle");
  var toggleButton = document.getElementById("navbar-toggler");
  var targetElement = event.target; // Tıklanan öğe

  // Tıklanan öğe menü veya menü düğmesi değilse menüyü kapat
  if (!menu.contains(targetElement) && targetElement !== toggleButton) {
    menu.classList.remove("show");
    toggleButton.setAttribute("aria-expanded", "false");
  }
});



window.onscroll = function () {
  var navbar = document.getElementById("navbar");

  if (window.pageYOffset > 0) {
    navbar.classList.add("black");
  } else {
    navbar.classList.remove("black");
  }
};



// JavaScript
function setActiveNav() {
  var sections = document.querySelectorAll('section'); // Tüm bölümleri seçin

  // Kaydırma olayını dinleyin
  window.addEventListener('scroll', function() {
    var currentScrollPos = window.pageYOffset; // Geçerli kaydırma konumu

    // Her bir bölümü döngüye alın
    sections.forEach(function(section) {
      var sectionTop = section.offsetTop - 100; // Bölümün üst konumu (100 piksel kaydırma payı)

      if (currentScrollPos >= sectionTop) {
        var sectionId = section.getAttribute('id');
        var activeLink = document.querySelector('#navlink li a[href="#' + sectionId + '"]');

        if (activeLink) {
          // Tüm navbar linklerinden aktif sınıfı kaldır
          document.querySelectorAll('#navlink li a').forEach(function(link) {
            link.classList.remove('acitve');
          });

          // Geçerli bölüme ait navbar linkine aktif sınıfı ekle
          activeLink.classList.add('acitve');
        }
      }
    });
  });
}

setActiveNav();
