var app = new Vue({
  delimiters: ['[[', ']]'],
  el: '#app',
  data: {
    response_data: 'hello vueJS!!',
  },
  methods: {
    getData: function (num) {
      axios
        .get('/app/get_tasks/'+num)
        .then(response => (this.response_data = response.data))
        .catch(error => console.log(error))
    },
    getTask: function (task) {
      axios
        .get('/app/get_task/'+task)
        .then(response => (this.response_data = response.data))
        .catch(error => console.log(error))
    }
  }
})

