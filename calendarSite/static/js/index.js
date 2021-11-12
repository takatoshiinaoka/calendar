var app = new Vue({
  delimiters: ['[[', ']]'],
  el: '#app',
  data: {
    response_data: 'hello vueJS!!',
  },
  methods: {
    getData: function (num) {
      axios
        .get('/myapp/get_tasks/'+num)
        .then(response => (this.response_data = response.data))
        .catch(error => console.log(error))
    }
  }
})