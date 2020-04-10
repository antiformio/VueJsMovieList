<template>
    <a v-if="videoId" :href="url" target="_blank">
     <font-awesome-icon :icon="[ 'fab', 'youtube' ]" class="fa-2x"/>
    </a>
</template>>

<script>
import axios from 'axios';

export default {
  props: {
    title: String,
  },
  name: 'YoutubeTrailer',
  data() {
    return {
      url: '',
      videoId: '',
    };
  },
  methods: {
    getTrailer() {
      const key = 'AIzaSyAlOO5JRUA5jSmK0rWo71Fq1buFzPcmeUo';
      const part = 'snippet';
      const maxResults = 1;
      const q = this.$props.title;
      const type = 'video';

      const path = `https://www.googleapis.com/youtube/v3/search?key=${key}&part=${part}&maxResults=${maxResults}&q=${q}&type=${type}`;

      axios
        .get(path)
        .then((res) => {
          this.buildUrl(res.data.items[0].id.videoId);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    buildUrl(videoId) {
      // eslint-disable-next-line prefer-template
      this.url = 'https://www.youtube.com/watch?v=' + videoId;
      this.videoId = videoId;
    },
  },
  mounted() {
    this.getTrailer();
  },
};
</script>

<style scoped>
.fa-youtube {
  color: red;
  size: 3em;
}

</style>
