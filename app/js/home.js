var popupDark;
var imgs_banners = [];
var imgs_thumb = [];
var popupDark_product;

function GetBanners() {
    $.ajax({
        url: URLAPI + 'GetBanners.php',
        type: "POST",

    }).done(function (data) {
        swiper_banner = app.swiper.get(".demo-swiper-multiple");


        for (var i = 0; i < data.length; i++) {
            swiper_banner.appendSlide(`<swiper-slide>
            <img src="${URLASSETS + "banners/"+ data[i].img}"
                alt="" class="img">
        </swiper-slide>`)

            imgs_banners.push({
                url: URLASSETS + "banners/" + data[i].img,
                caption: ""
            });

            imgs_thumb.push(URLASSETS + "banners/" + data[i].img);
        }

        popupDark = app.photoBrowser.create({
            photos: imgs_banners,
            thumbs: imgs_thumb,
            type: 'popup',
            theme: 'dark',
        });

        $(".demo-swiper-multiple").click(function () {
            popupDark.open();
        })




    }).fail(function (a, b, c) {
        console.log(a, b, c);

    })
}

function GetCart() {
    $.ajax({
        url: URLAPI + 'GetProducts.php',
        type: "POST",

    }).done(function (data) {
        LoadCart();
        for (var i = 0; i < data.length; i++) {

            CreateGetProductHTML("result_products", data[i].id, data[i].img, data[i].title, data[i].description, data[i].price);
        }





    }).fail(function (a, b, c) {
        console.log(a, b, c);

    })
}

function LoadHome() {
    GetCart();

    GetBanners();
    GetCategorysHome();
    GetUser();

    checkCart();
    

}

function GetCategorysHome() {
    $.ajax({
        url: URLAPI + 'GetCategorys.php',
        type: "POST",
    }).done(function (data) {
        console.log(data);
        for (var i = 0; i < data.length; i++) {
            var category = data[i];
            $("#result_categorys_home").append(`
            <div class="chip">
								<a class="chip-label" href="/category/${category.name}/${category.products}">${category.name}</a>
							</div>
            `)
        }
    }).fail(function (a, b, c) {
        console.log(a, b, c);
    })

}