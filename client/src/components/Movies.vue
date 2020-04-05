<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Filmes</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.movie-modal>
        Adicionar Filme
        </button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Titulo</th>
              <th scope="col">Autor</th>
              <th scope="col">Visto?</th>
              <th scope="col">Nota</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(movie, index) in movies" :key="index">
              <td>{{ movie.title }}</td>
              <td>{{ movie.author }}</td>
              <td>
                <span v-if="movie.saw">Sim</span>
                <span v-else>Nao</span>
              </td>
              <td>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm">Modificar</button>
                  <button type="button" class="btn btn-danger btn-sm">Apagar</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addMovieModal"
         id="movie-modal"
         title="Adicionar novo filme"
         hide-footer>
    <b-form @submit="onSubmit" @reset="onReset" class="w-100">
    <b-form-group id="form-title-group"
                label="Title:"
                label-for="form-title-input">
                  <b-form-input id="form-title-input"
                            type="text"
                            v-model="addMovieForm.title"
                            required
                            placeholder="Introduz o titulo">
                  </b-form-input>
    </b-form-group>
    <b-form-group id="form-author-group"
                  label="Author:"
                  label-for="form-author-input">
                  <b-form-input id="form-author-input"
                                type="text"
                                v-model="addMovieForm.author"
                                required
                                placeholder="Introduz autor">
                  </b-form-input>
    </b-form-group>
    <b-form-group id="form-saw-group">
      <b-form-checkbox-group v-model="addMovieForm.saw" id="form-checks">
        <b-form-checkbox value="true">Visto?</b-form-checkbox>
      </b-form-checkbox-group>
    </b-form-group>
    <b-button type="submit" variant="primary">Submeter</b-button>
    <b-button type="reset" variant="danger">Reset</b-button>
  </b-form>
</b-modal>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      movies: [],
      addMovieForm: {
        title: '',
        author: '',
        saw: [],
      },
    };
  },
  methods: {
    getMovies() {
      const path = 'http://localhost:5000/filmes';
      axios.get(path)
        .then((res) => {
          this.movies = res.data.movies;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addMovie(payload) {
      const path = 'http://localhost:5000/filmes';
      axios.post(path, payload)
        .then(() => {
          this.getMovies();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getMovies();
        });
    },
    initForm() {
      this.addMovieForm.title = '';
      this.addMovieForm.author = '';
      this.addMovieForm.saw = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addMovieModal.hide();
      let saw = false;
      if (this.addMovieForm.saw[0]) saw = true;
      const payload = {
        title: this.addMovieForm.title,
        author: this.addMovieForm.author,
        saw, // property shorthand
      };
      this.addMovie(payload); // chamar o metodo de adicionar filme
      this.initForm(); // fazer reset ao formulario
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addMovieModal.hide();
      this.initForm();
    },
  },
  created() {
    this.getMovies();
  },
};
</script>
