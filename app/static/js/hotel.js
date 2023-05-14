class Review {

   static last_review_id = 0

   review_id
   user_id
   service_id
   rating
   content
   status

   submit_review() {
      var form = document.getElementById("contact-form");

      this.review_id = this.last_review_id++
      this.user_id = 1

      let name = form.querySelector("input[name='name']").value;
      this.user_id = form.querySelector("input[name='email']").value;
      this.rating = form.querySelector("input[name='number']").value;
      this.content = form.querySelector("textarea[name='msg']").value;
      
      window.location.href = "mailto:drakensang47@gmail.com" + "?subject=REVIEW:" + name + "&body=" + this.content;
   }
}

let navbar = document.querySelector('.header .navbar');

// document.querySelector('#menu-btn').onclick = () =>{
//    navbar.classList.toggle('active');
// }

window.onscroll = () =>{
   navbar.classList.remove('active');
}

document.querySelectorAll('.contact .row .faq .box h3').forEach(faqBox => {
   faqBox.onclick = () =>{
      faqBox.parentElement.classList.toggle('active');
   }
});

function sendMail() {
   review = new Review()
   review.submit_review()
}

var swiper = new Swiper(".home-slider", {
   loop:true,
   effect: "coverflow",
   spaceBetween: 30,
   grabCursor: true,
   coverflowEffect: {
      rotate: 50,
      stretch: 0,
      depth: 100,
      modifier: 1,
      slideShadows: false,
   },
   navigation: {
     nextEl: ".swiper-button-next",
     prevEl: ".swiper-button-prev",
   },
});

var swiper = new Swiper(".gallery-slider", {
   loop:true,
   effect: "coverflow",
   slidesPerView: "auto",
   centeredSlides: true,
   grabCursor: true,
   coverflowEffect: {
      rotate: 0,
      stretch: 0,
      depth: 100,
      modifier: 2,
      slideShadows: true,
   },
   pagination: {
      el: ".swiper-pagination",
    },
});

var swiper = new Swiper(".reviews-slider", {
   loop:true,
   slidesPerView: "auto",
   grabCursor: true,
   spaceBetween: 30,
   pagination: {
      el: ".swiper-pagination",
   },
   breakpoints: {
      768: {
        slidesPerView: 1,
      },
      991: {
        slidesPerView: 2,
      },
   },
});