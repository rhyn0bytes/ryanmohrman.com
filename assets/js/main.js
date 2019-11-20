(function($) {
  "use strict"; // Start of use strict

  // Hide Profile Image after scrolling
  $(window).scroll(function() {
    if ($(".navbar").offset().top > 50 || $("#navbarCollapse").hasClass("show")) { // added check for navbar collapse to prevent profile from showing when collapsing on mobile
        $(".profile-container").hide(); 
    } else {
        $(".profile-container").show();
    }
  });

  // On mobile, hide the avatar when expanding the navbar menu
  $('#navbarCollapse').on('show.bs.collapse', function () {
    $(".profile-container").hide();
  });
  $('#navbarCollapse').on('hidden.bs.collapse', function () {
    if($(".navbar").offset().top >50) { // added check for scroll position to prevent profile from showing when collapsing on mobile
      $(".profile-container").hide();
    } else {
      $(".profile-container").show();
    }
  });

})(jQuery); // End of use strict
