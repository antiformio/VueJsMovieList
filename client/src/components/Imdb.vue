<template>
  <div class="container">
    <table class="table table-hover">
      <thead>
        <tr>
          <th scope="col">Ano</th>
          <th scope="col">Nota</th>
          <th scope="col">Genero</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>{{ ano }}</td>
          <td>{{ nota }}</td>
          <td>{{ genero }}</td>
        </tr>
      </tbody>
    </table>
    <i>"<b>{{ shortPlotDescription }}</b>"</i>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: {
    title: String,
    id: String,
  },
  name: 'Imdb',
  data() {
    return {
      searchTitle: '',
      ano: '',
      nota: '',
      genero: '',
      plot: '',
      poster: '',
    };
  },
  methods: {
    fixString() {
      this.searchTitle = encodeURIComponent(this.title.trim());
    },
    getFilme() {
      const path = `https://www.omdbapi.com/?apikey=77ad7f8d&t=${this.searchTitle}`;
      axios
        .get(path)
        .then((res) => {
          this.ano = res.data.Year;
          this.genero = res.data.Genre;
          this.nota = res.data.imdbRating;
          this.plot = res.data.Plot;
          this.poster = res.data.Poster;
          this.passUrl();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    passUrl() {
      this.$emit('urlForCard', this.$props.id, this.poster);
    },
  },
  computed: {
    shortPlotDescription() {
      // eslint-disable-next-line prefer-template
      return this.plot.substring(0, 120) + '...';
    },
  },
  mounted() {
    this.fixString();
    this.getFilme();
  },
};
</script>
