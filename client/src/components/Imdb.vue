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
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: {
    title: String,
  },
  name: 'Imdb',
  data() {
    return {
      searchTitle: '',
      ano: '',
      nota: '',
      genero: '',
    };
  },
  methods: {
    fixString() {
      this.searchTitle = encodeURIComponent(this.title.trim());
    },
    getFilme() {
      const path = `http://www.omdbapi.com/?apikey=77ad7f8d&t=${this.searchTitle}`;
      axios.get(path)
        .then((res) => {
          this.ano = res.data.Year;
          this.genero = res.data.Genre;
          this.nota = res.data.imdbRating;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.fixString();
    this.getFilme();
  },
};
</script>
