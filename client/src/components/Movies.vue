<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Filmes</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
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
                  <button type="button"
                  class="btn btn-warning btn-sm"
                  v-b-modal.movie-update-modal
                  @click="editMovie(movie)">
                  Modificar
                  </button>
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
<b-modal ref="editMovieModal"
         id="movie-update-modal"
         title="Update"
         hide-footer>
  <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
  <b-form-group id="form-title-edit-group"
                label="Titulo:"
                label-for="form-title-edit-input">
      <b-form-input id="form-title-edit-input"
                    type="text"
                    v-model="editForm.title"
                    required
                    placeholder="Introduza o titulo">
      </b-form-input>
    </b-form-group>
    <b-form-group id="form-author-edit-group"
                  label="Autor:"
                  label-for="form-author-edit-input">
        <b-form-input id="form-author-edit-input"
                      type="text"
                      v-model="editForm.author"
                      required
                      placeholder="Introduza autor">
        </b-form-input>
      </b-form-group>
    <b-form-group id="form-read-edit-group">
      <b-form-checkbox-group v-model="editForm.saw" id="form-checks">
        <b-form-checkbox value="true">Visto?</b-form-checkbox>
      </b-form-checkbox-group>
    </b-form-group>
    <b-button-group>
      <b-button type="submit" variant="primary">Actualizar</b-button>
      <b-button type="reset" variant="danger">Cancelar</b-button>
    </b-button-group>
  </b-form>
</b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from '@/components/Alert.vue';

export default {
  data() {
    return {
      movies: [],
      addMovieForm: {
        title: '',
        author: '',
        saw: [],
      },
      editForm: {
        id: '',
        title: '',
        author: '',
        saw: [],
      },
      message: '',
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
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
          this.message = 'Filme Adicionado!';
          this.showMessage = true;
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
      this.editForm.id = '';
      this.editForm.title = '';
      this.editForm.author = '';
      this.editForm.saw = [];
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
    editMovie(movie) {
      this.editForm = movie;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editMovieModal.hide();
      let saw = false;
      if (this.editForm.saw[0]) saw = true;
      console.log(saw);
      const payload = {
        title: this.editForm.title,
        author: this.editForm.author,
        saw,
      };
      this.updateMovie(payload, this.editForm.id);
    },
    updateMovie(payload, movieID) {
      const path = `http://localhost:5000/filmes/${movieID}`;
      axios.put(path, payload)
        .then(() => {
          this.getMovies();
          this.message = 'Filme actualizado!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getMovies();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editMovieModal.hide();
      this.initForm();
      this.getMovies();
    },
  },
  created() {
    this.getMovies();
  },
};
</script>
