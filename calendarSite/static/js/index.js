var app = new Vue({
  delimiters: ['[[', ']]'],
  el: '#app',
  data: {
    response_data: 'hello vueJS!!',
  },
  methods: {
    getData: function (subject) {
      axios
        .get('/app/get_tasks?subject='+subject)
        .then(response => (this.response_data = response.data))
        .catch(error => console.log(error))
    },
    getTask: function (subject,task) {
      axios
        .get('/app/get_tasks?subject='+subject+'&task='+task)
        .then(response => (this.response_data = response.data))
        .catch(error => console.log(error))
    }
  }
})

