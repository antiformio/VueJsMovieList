<template>
  <div class="container">
    <img class="netflix-logo" src="@/assets/netflix.png"/>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: {
    title: String,
  },
  name: 'Netflix',
  data() {
    return {
      searchTitle: '',
      hasIt: Boolean,
      url: '',
    };
  },
  methods: {
    checkIt() {
      const searchTitle = this.title;
      axios({
        method: 'get',
        url: 'https://utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com/lookup',
        params: {
          term: searchTitle,
          country: 'es',
        },
        headers: {
          'content-type': 'application/octet-stream',
          'x-rapidapi-host': 'utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com',
          'x-rapidapi-key': '99fa5a5205msh97b4c6d9706f294p1720c5jsnd5c47f14dd37',
        },
      })
        .then((res) => {
          console.log(res.data.results[0].locations);
          if (res.data.results[0].locations){
              iterateArray(res.data.results[0].locations);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    iterateArray(locations) {
      locations.forEach(function (arrayItem) {
        const netflixSpain = 'NetflixIVAES';
        if (arrayItem.name === netflixSpain) {
            this.hasIt = true;
            this.url = arrayItem.url;
        }
        },
    },
  },
  created() {
    this.checkIt();
  },
};
</script>

<style scoped>
.netflix-logo {
    width: 35px;
    height: 35px;
}
</style>
