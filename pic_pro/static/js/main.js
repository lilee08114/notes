$(document).ready(function(){
	"use strict";
		$('.top-news-slide').owlCarousel({
			items: 1,
		    nav:true,
		    loop: true,
		    pagination: false,
		    dots: false,
		    navSpeed: 2000,
		    navText: ['<i class="fa fa-angle-left">','<i class="fa fa-angle-right">']
	    });

	    $('.main-slider').owlCarousel({
			items: 1,
			autoplay: true,
			autoplaySpeed: 2000,
		    nav:true,
		    loop: true,
		    dots: false,
		    navSpeed: 2000,
		    navText: ['<i class="fa fa-angle-left fa-lg">','<i class="fa fa-angle-right fa-lg">']
	    });

	    $('.high-slider').owlCarousel({
			items: 1,
		    nav:true,
		    loop: true,
		    dots: false,
		    navSpeed: 2000,
		    navText: ['<i class="fa fa-angle-left">','<i class="fa fa-angle-right">']
	    });

	     $('.new-steps').owlCarousel({
	        items:1,
	        loop:false,
	        URLhashListener:true,
	        startPosition: 'URLHash',
	        dots: false
    	});

	     $('.trending-slider').owlCarousel({
			items: 1,
		    nav:true,
		    loop: true,
		    dots: false,
		    navSpeed: 2000,
		    navText: ['<i class="fa fa-angle-left fa-lg">','<i class="fa fa-angle-right fa-lg">']
	    });

	    $('.latest-videos').owlCarousel({
	        items:1,
	        loop:false,
	        URLhashListener:true,
	        startPosition: 'URLHash',
	        dots: false
    	});

    	$('.mn-news').owlCarousel({
	        items:1,
	        loop:true,
	        URLhashListener:true,
	        startPosition: 'URLHash',
	        dots: false,
	        nav: true,
	        navText: ['<i class="fa fa-angle-left fa-lg">','<i class="fa fa-angle-right fa-lg">']
    	});

    	$('.f-news-slider').owlCarousel({
	        items: 1,
            loop:false,
            center:true,
            margin:10,
            info:true,
            lazyLoad:false,
            URLhashListener:true,
            autoplayHoverPause:true,
            startPosition: 'URLHash'
    	});

		$('.popular-videos').owlCarousel({
			items: 1,
		    nav:true,
		    loop: true,
		    dots: false,
		    navSpeed: 200,
		    navText: ['<i class="fa fa-angle-up fa-lg">','<i class="fa fa-angle-down fa-lg">'],
		    animateOut: 'slideOutUp',
  			animateIn: 'slideInUp'
	    });

	    $('#popular-post-1').owlCarousel({
			items: 1,
		    nav:true,
		    loop: true,
		    dots: false,
		    navSpeed: 200,
		    navText: ['<i class="fa fa-angle-up fa-lg">','<i class="fa fa-angle-down fa-lg">'],
		    animateOut: 'slideOutUp',
  			animateIn: 'slideInUp'
	    });
	    $('#popular-post-2').owlCarousel({
			items: 1,
		    nav:true,
		    loop: true,
		    dots: false,
		    navSpeed: 200,
		    navText: ['<i class="fa fa-angle-up fa-lg">','<i class="fa fa-angle-down fa-lg">'],
		    animateOut: 'slideOutUp',
  			animateIn: 'slideInUp',
  			onInitialized: function(e) {
  				$('#month').removeClass('active');
  			}
	    });
	    $('#popular-post-3').owlCarousel({
			items: 1,
		    nav:true,
		    loop: true,
		    dots: false,
		    navSpeed: 200,
		    navText: ['<i class="fa fa-angle-up fa-lg">','<i class="fa fa-angle-down fa-lg">'],
		    animateOut: 'slideOutUp',
  			animateIn: 'slideInUp',
  			onInitialized: function(e) {
  				$('#all').removeClass('active');
  			}
	    });




	    $('.pp, popular-videos').owlCarousel({
			items: 1,
		    nav:true,
		    loop: true,
		    dots: false,
		    navSpeed: 200,
		    navText: ['<i class="fa fa-angle-up fa-lg">','<i class="fa fa-angle-down fa-lg">'],
		    animateOut: 'slideOutUp',
  			animateIn: 'slideInUp'
	    });
		$('.latest-videos a.fa.fa-play').on("click", function(){
			"use strict";
			$('.video-img > img, .video-img > .overlay, .video-img > .video-overlay ').css("opacity","0");
			$('.video-play').css("display","block");


		});
		$('.v-nav').on( "click" , function(){
			"use strict";
			$('.video-img > img, .video-img > .overlay, .video-img > .video-overlay ').css("opacity","1");
			$('.video-play').css("display","none");
			$("#biker").vimeo("play");

		});

});