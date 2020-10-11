var app = new Vue({
    el: '#app',
    data: {
      message: 'Hello CINS 465!'
    }
  })

var app2 = new Vue({
  el: '#app-2',
  data: {
    message: 'You loaded this page on ' + new Date().toLocaleString()
  }
})

var app4 = new Vue({
  el: '#app-4',
  data: {
    suggestions: [],
    seen:true,
    unseen:false,
  },
  created:function(){
    this.fetchSuggestionList();
    this.timer = setInterval(this.fetchSuggestionList, 10000);
  },

  methods: {
    fetchSuggestionList: function(){
      axios
        .get('/suggestions/')
        //.then(response => console.log(response.data))
        .then(response => (this.suggestions = response.data.suggestions))
      console.log(this.suggestions)
      this.seen=false
      this.unseen=true
    },
    cancelAutoUpdate: function() { clearInterval(this.timer) }
  },
  beforeDestroy(){
    this.cancelAutoUpdate();
  }
})

var app6 = new Vue({
  el: '#app-6',
  data: {
    message: 'Text Box Feature'
  }
})
