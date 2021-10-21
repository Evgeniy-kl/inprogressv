new Vue ({
    el: '#articles_id',
    data: {
        articles: []
    },
    created: function() {
        const vm = this;
        axios.get('/api/v1/articles/')
        .then(function (response){
        vm.articles = response.data
        })
    }
}
)

