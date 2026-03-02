document.addEventListener('DOMContentLoaded', function() {

    $('.slider-for').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        fade: true,
        asNavFor: '.slider-nav',
        infinite: true,
        speed: 300,
        adaptiveHeight: true
    });

    $('.slider-nav').slick({
        slidesToShow: 5,
        slidesToScroll: 1,
        asNavFor: '.slider-for',
        dots: false,
        arrows: true,
        focusOnSelect: true,
        infinite: true,
        prevArrow: '<button type="button" class="slick-prev"></button>',
        nextArrow: '<button type="button" class="slick-next"></button>',
        responsive: [
            {
                breakpoint: 992,
                settings: {
                    slidesToShow: 4,
                }
            },
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 3,
                    arrows: false,
                    draggable: true,
                    swipe: true,
                    touchMove: true
                }
            },
            {
                breakpoint: 576,
                settings: {
                    slidesToShow: 2,
                    arrows: false,
                    draggable: true,
                    swipe: true,
                    touchMove: true
                }
            }
        ]
    });

    $('.slider-for').on('afterChange', function(event, slick, currentSlide) {
        $(this).css('height', 'auto');
        $(this).find('.slick-track').css('height', 'auto');
        $(this).find('.slick-list').css('height', 'auto');

        $(this).slick('resize');

        console.log('Slide changed to:', currentSlide, 'Height:', $(this).height());
    });

    if (typeof Fancybox !== 'undefined') {
        Fancybox.bind('[data-fancybox="gallery"]', {
            loop: true,
            keyboard: true,
            arrows: true,
            Toolbar: {
                display: {
                    left: ["infobar"],
                    middle: [],
                    right: ["slideshow", "thumbs", "close"],
                },
            },
        });
    }

    $('.slider-for-item').on('click', 'img', function() {
        const currentIndex = $('.slider-for').slick('slickCurrentSlide');

        const images = [];
        $('.slider-for-item img').each(function() {
            images.push({
                src: $(this).attr('src'),
                caption: ''
            });
        });

        if (images.length > 0 && typeof Fancybox !== 'undefined') {
            Fancybox.show(images, {
                startIndex: currentIndex,
                loop: true,
            });
        }
    });

    let resizeTimer;
    window.addEventListener('resize', function() {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(function() {
            $('.slider-for').slick('resize');
            $('.slider-nav').slick('resize');
        }, 250);
    });
});