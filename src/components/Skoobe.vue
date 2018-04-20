<template>
  <div class="risk_type_detail">
    <div class="container">
    <h3>Following results fetched for query: {{search_query}}</h3>
    </div><br/><br/>
    <div class="container-fluid">
        <div class="col-md-6">
           <ul class="list-group">
            <li class="list-group-item" v-for="book in top_publishers">
             <b>Book Title:</b><em> {{book.title}}</em><br/>
             <b>Book Publisher:</b><em> {{book.publisher_name}}</em><br/>
             <b>Book Genre:</b><em> {{book.genre_name}}</em><br/>
             <b>Book Link:</b><em> {{book.hyperlink}}</em><br/>
             <b>Book Picture:</b><em> {{book.picture_url}}</em>
           </li>
          </ul>
        </div>
        <div class="col-md-6">
           <ul class="list-group">
      <li class="list-group-item" v-for="book in low_publishers">
         <b>Book Title:</b><em> {{book.title}}</em><br/>
         <b>Book Publisher:</b><em> {{book.publisher_name}}</em><br/>
         <b>Book Genre:</b><em> {{book.genre_name}}</em><br/>
         <b>Book Link:</b><em> {{book.hyperlink}}</em><br/>
         <b>Book Picture:</b><em> {{book.picture_url}}</em>
      </li>
      </ul>
        </div>
       
</div>

      
      
    </div>    
  </div>
</template>

<script>
export default {
  name: 'RiskTypeDetail',
  data () {
    return {
      top_publishers: [],
      low_publishers: [],
      search_query: '',
    }
  },
  methods:{
  greet: function(greeting){
      alert(greeting);
  },
  presskey: function(){
      console.log('Pressed');
  },
  hitEnter: function(){
      console.log('You Hit Enter');
  }
  },
  created: function(){
    this.$http.get('http://localhost:5000/v1/search/'+this.$route.params.search_query)
	.then(function(response) {
            console.log("Created");
            this.top_publishers = response.data.top_publishers
            this.low_publishers = response.data.low_publishers
            this.search_query = this.$route.params.search_query
	    console.log(response.data.top_publishers)
            console.log(response.data.low_publishers)
	})
	.catch((err) => {
	    console.log(err)
	})
      }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
