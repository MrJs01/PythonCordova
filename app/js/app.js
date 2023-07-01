document.addEventListener('deviceready', onDeviceReady.bind(this), false);





var app = new Framework7({
	root: '#app',
	name: 'AppPrefab',
	id: 'crom.appprefab',
	panel: {
		swipe: 'left',
	},
	routes: [{
			path: '/index/',
			url: 'index.html',
			on: {
				pageInit: function (event, page) {
					app.views.main.router.navigate('/home/');
					setTimeout(() => {

					}, 5000);
				}
			}
		},
		{
			path: '/home/',
			url: './pages/home.html',
			on: {
				pageInit: function (event, page) {

					$.ajax({
						url: "/list_projects",
						dataType: "json",

					}).done(function (data) {
						for (let i = 0; i < data.length; i++) {
							const element = data[i];

							$("#result_list").append(`<a class="list-group-item" href="/project?name=${element}">${element}</a>`)


						}
					}).fail(function (a, b, c) {
						console.log(a, b, c)
					})


				}
			}
		},
		{
			path: '/project/',
			url: './pages/project.html',
			on: {
				pageInit: function (event, page) {

					$.ajax({
						url: "/project",
						data: {
							cmd: $("#cmd").val()
						},
						dataType: "json",

					}).done(function (data) {
						console.log(data)
					}).fail(function (a, b, c) {
						console.log(a, b, c)
					})

					$('#btt_cmd').click(function () {
						$.ajax({
							url: "/cmd_cordova",
							data: {
								cmd: $("#cmd").val(),
								name: name_project
							},
							dataType: "json",

						}).done(function (data) {
							console.log(data)
						}).fail(function (a, b, c) {
							console.log(a, b, c)
						})
					})


				}
			}
		},
		{
			path: '(.*)',
			url: './pages/404.html',
		},
	],
});

function onDeviceReady() {
	var mainView = app.views.create('.view-main', {
		url: '/index/'
	});
	document.addEventListener("backbutton", onBackKeyDown, false);

	function onBackKeyDown() {
		var currentRoute = app.views.main.router.currentRoute;

		if (currentRoute.url === '/home/') {
			app.views.main.router.navigate('/index/');
		} else {
			app.views.main.router.back();
		}
	}

}