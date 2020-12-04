var auto_refresh = new Vue({
  el: '#auto_refresh',
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