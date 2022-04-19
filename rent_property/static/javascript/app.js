
var radio = document.getElementById('radio')



var label = radio.getElementsByClassName("not-active");

for (var i = 0; i < label.length; i++) {
  label[i].addEventListener("click", function () {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
}

$(document).ready(function () {
  $('.carousel').slick({
    slidesToShow: 5,
    centerMode: true,
    autoplay: true,
    infinite: true,
    responsive: [
      {
        breakpoint: 1600,
        settings: {
          slidesToShow: 4,
          slidesToScroll: 2,
          infinite: true,
        }
      },
      {
        breakpoint: 1400,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 2,
          infinite: true,
        }
      },
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 3,
          infinite: true,
        }
      },
      {
        breakpoint: 700,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          variableWidth: true
        }
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 2,
          arrows: false,
          variableWidth: true
        }
      }
    ]
  });
});



document.addEventListener("DOMContentLoaded", function () {
  var lazyloadImages;

  if ("IntersectionObserver" in window) {
    lazyloadImages = document.querySelectorAll(".lazy");
    var imageObserver = new IntersectionObserver(function (entries, observer) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          var image = entry.target;
          image.classList.remove("lazy");
          imageObserver.unobserve(image);
        }
      });
    });

    lazyloadImages.forEach(function (image) {
      imageObserver.observe(image);
    });
  } else {
    var lazyloadThrottleTimeout;
    lazyloadImages = document.querySelectorAll(".lazy");

    function lazyload() {
      if (lazyloadThrottleTimeout) {
        clearTimeout(lazyloadThrottleTimeout);
      }

      lazyloadThrottleTimeout = setTimeout(function () {
        var scrollTop = window.pageYOffset;
        lazyloadImages.forEach(function (img) {
          if (img.offsetTop < (window.innerHeight + scrollTop)) {
            img.src = img.dataset.src;
            img.classList.remove('lazy');
          }
        });
        if (lazyloadImages.length == 0) {
          document.removeEventListener("scroll", lazyload);
          window.removeEventListener("resize", lazyload);
          window.removeEventListener("orientationChange", lazyload);
        }
      }, 20);
    }

    document.addEventListener("scroll", lazyload);
    window.addEventListener("resize", lazyload);
    window.addEventListener("orientationChange", lazyload);
  }
})





const sidebar = document.querySelector('.pop-up-form');
const overlay = document.querySelector('.pop-up-overlay');
const timess = document.querySelector('.timess');
const bars = document.querySelector('.add');
const login = document.querySelector('.login');



bars.addEventListener('click', function () {
  sidebar.classList.toggle('show');
  overlay.classList.add('show')
});

login.addEventListener('click', function () {
  sidebar.classList.toggle('show');
  overlay.classList.add('show');
  document.querySelector('.sidebar').classList.remove('showSidebar');
  document.querySelector('.side-lay').classList.remove('showSidebar');
});

overlay.addEventListener('click', function () {
  sidebar.classList.remove('show');
  sidebar.style.transition = '0.3s ease-in'
  overlay.classList.remove('show')
})


timess.addEventListener('click', function () {
  sidebar.classList.remove('show');
  sidebar.style.transition = '0.3s ease-in'
  overlay.classList.remove('show')
})



$(document).ready(function () {
  $('.customer-logos').slick({
    slidesToShow: 5,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 1000,
    arrows: false,
    dots: false,
    pauseOnHover: false,
    responsive: [{
      breakpoint: 768,
      settings: {
        slidesToShow: 3
      }
    }, {
      breakpoint: 520,
      settings: {
        slidesToShow: 2
      }
    }]
  });
});






function run() {
  document.querySelector('.sidebar').classList.add('showSidebar');
  document.querySelector('.side-lay').classList.add('showSidebar');
};


document.querySelector('.side-lay').addEventListener('click', function () {

  document.querySelector('.sidebar').classList.remove('showSidebar');
  document.querySelector('.side-lay').classList.remove('showSidebar');
})





document.querySelector('.btn').addEventListener('click', function () {
  document.querySelector('.hms').classList.toggle('show');

  document.querySelector('.hms1').classList.remove('show');
  document.querySelector('.hms2').classList.remove('show');
})
document.querySelector('.btn1').addEventListener('click', function () {
  document.querySelector('.hms1').classList.toggle('show');

  document.querySelector('.hms').classList.remove('show');
  document.querySelector('.hms2').classList.remove('show');
})
document.querySelector('.btn2').addEventListener('click', function () {
  document.querySelector('.hms2').classList.toggle('show');

  document.querySelector('.hms').classList.remove('show');
  document.querySelector('.hms1').classList.remove('show');
})





//radio

var radio = document.getElementById('radio')


var label = radio.getElementsByClassName("not-active");

for (var i = 0; i < label.length; i++) {
  label[i].addEventListener("click", function () {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
}


const wrap = document.querySelector(".embla");
const viewPort = wrap.querySelector(".embla__viewport");
const prevBtn = wrap.querySelector(".embla__button--prev");
const nextBtn = wrap.querySelector(".embla__button--next");
const setupPrevNextBtns = (prevBtn, nextBtn, embla) => {
  prevBtn.addEventListener("click", embla.scrollPrev, false);
  nextBtn.addEventListener("click", embla.scrollNext, false);
};

const disablePrevNextBtns = (prevBtn, nextBtn, embla) => {
  return () => {
    if (embla.canScrollPrev()) prevBtn.removeAttribute("disabled");
    else prevBtn.setAttribute("disabled", "disabled");

    if (embla.canScrollNext()) nextBtn.removeAttribute("disabled");
    else nextBtn.setAttribute("disabled", "disabled");
  };
};

const embla = EmblaCarousel(viewPort, {
  dragFree: true,
  containScroll: "trimSnaps"
});
const disablePrevAndNextBtns = disablePrevNextBtns(
  prevBtn,
  nextBtn,
  embla
);

setupPrevNextBtns(prevBtn, nextBtn, embla);

embla.on("select", disablePrevAndNextBtns);
embla.on("init", disablePrevAndNextBtns);




