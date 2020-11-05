var app3 = new Vue({
	el: '#app-3',
	data: {
		show: false
	}
})

var app2 = new Vue({
	el: '#app-2',
	data: {
		show: false
	}
})

var app5 = new Vue({
	el: '#app-5',
	data: {
		friends: [],
	},
	//Adapted from https://stackoverflow.com/questions/36572540/vue-js-auto-reload-refresh-data-with-timer
	created: function() {
		this.fetchFriendList();
		this.timer = setInterval(this.fetchFriendList, 30000);
	},
	methods: {
		fetchFriendList: function() {
			axios
				.get('/friends/')
				.then(response => (this.friends = response.data.friends))
			console.log(this.friends)
		},
		cancelAutoUpdate: function() { clearInterval(this.timer) }
	},
	beforeDestroy() {
		clearInterval(this.timer)
	}

})

var app6 = new Vue({
	el: '#app-6',
	data: {
		statuses: [],
	},
	//Adapted from https://stackoverflow.com/questions/36572540/vue-js-auto-reload-refresh-data-with-timer
	created: function() {
		this.fetchStatusList();
		this.timer = setInterval(this.fetchStatusList, 30000);
	},
	methods: {
		fetchStatusList: function() {
			axios
				.get('/statuses/')
				.then(response => (this.statuses = response.data.statuses))
			console.log(this.friends)
		},
		cancelAutoUpdate: function() { clearInterval(this.timer) }
	},
	beforeDestroy() {
		clearInterval(this.timer)
	}

})
