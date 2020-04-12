<template>
  <div class="container">
    <navBar @filter="filterMovies"></navBar>


    <br />
    <b-row>
      <div class="card-single" v-for="movie in movies" :key="movie.id">

        <b-card v-if="filterStatus === 'viewed' && movie.saw === true ||
          filterStatus === 'notViewed' && movie.saw === false ||
          filterStatus === null"
          :title="movie.title | capitalize"
          :img-src="movie.url"
          img-alt="Image"
          img-top
          tag="article"
          style="max-width: 20rem;"
          class="ml-2 mr-2 mt-5"
        >

          <b-card-text>
            <span v-if="movie.saw">
              <h5><b-badge pill variant="success">Visto</b-badge></h5>
            </span>

            <span v-else>
              <h5><b-badge pill variant="secondary">Por ver</b-badge></h5>
            </span>
          </b-card-text>

          <b-card-text>
            <div class="author mb-7">
              <b>Director: </b>
              <i>{{ movie.author }}</i>
            </div>

            <imdb
            :title="movie.title"
            :id="movie.id"
            :key="movie.url"
            @urlForCard="urlForCard">
            </imdb>
          </b-card-text>

          <youtube class="mb-4 mt-4" :title="movie.title"></youtube>

          <netflix class="mb-4" :title="movie.title"></netflix>

          <div>
            <b-button
            pill
            variant="outline-secondary"
            size="sm"
            v-b-modal.movie-update-modal @click="editMovie(movie)"
            >Modificar
            </b-button>

            <b-button
            pill
            variant="outline-danger"
            size="sm"
            @click="onDeleteMovie(movie)"
            >Apagar
            </b-button>

          </div>
        </b-card>
      </div>
    </b-row>

    <b-modal ref="addMovieModal" id="movie-modal" title="Adicionar novo filme" hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-title-group" label="Title:" label-for="form-title-input">
          <b-form-input
            id="form-title-input"
            type="text"
            v-model="addMovieForm.title"
            required
            placeholder="Introduz o titulo"
          ></b-form-input>
        </b-form-group>

        <b-form-group id="form-author-group" label="Author:" label-for="form-author-input">
          <b-form-input
            id="form-author-input"
            type="text"
            v-model="addMovieForm.author"
            required
            placeholder="Introduz autor"
          ></b-form-input>
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
    <b-modal ref="editMovieModal" id="movie-update-modal" title="Modificar" hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
        <b-form-group id="form-title-edit-group" label="Titulo:" label-for="form-title-edit-input">
          <b-form-input
            id="form-title-edit-input"
            type="text"
            v-model="editForm.title"
            required
            placeholder="Introduza o titulo"
          ></b-form-input>
        </b-form-group>

        <b-form-group id="form-author-edit-group" label="Autor:" label-for="form-author-edit-input">
          <b-form-input
            id="form-author-edit-input"
            type="text"
            v-model="editForm.author"
            required
            placeholder="Introduza autor"
          ></b-form-input>
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
// import Alert from '@/components/Alert.vue';
import Header from '@/components/Header.vue';
import Imdb from '@/components/Imdb.vue';
import NetflixCheck from '@/components/NetflixCheck.vue';
import YoutubeTrailer from '@/components/YoutubeTrailer.vue';

export default {
  data() {
    return {
      movies: [],
      filterStatus: null,
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
  filters: {
    capitalize: (value) => {
      if (!value) return '';
      const res = value.toString();
      return res.charAt(0).toUpperCase() + res.slice(1);
    },
  },
  components: {
    // alert: Alert,
    navBar: Header,
    imdb: Imdb,
    netflix: NetflixCheck,
    youtube: YoutubeTrailer,
  },
  methods: {
    getMovies() {
      // const path = 'http://localhost:5000/filmes';
      const path = '/filmes';
      axios
        .get(path)
        .then((res) => {
          this.movies = res.data.movies;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addMovie(payload) {
      // const path = 'http://localhost:5000/filmes';
      const path = '/filmes';
      axios
        .post(path, payload)
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
      const payload = {
        title: this.editForm.title,
        author: this.editForm.author,
        saw,
      };
      this.updateMovie(payload, this.editForm.id);
    },
    updateMovie(payload, movieID) {
      const path = `/filmes/${movieID}`;
      axios
        .put(path, payload)
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
    removeMovie(movieID) {
      const path = `/filmes/${movieID}`;
      axios
        .delete(path)
        .then(() => {
          this.getMovies();
          this.message = 'Filme Apagado!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getMovies();
        });
    },
    onDeleteMovie(movie) {
      this.removeMovie(movie.id);
    },
    urlForCard(id, urlOfCover) {
      const index = this.movies.findIndex((x) => x.id === id);
      this.movies[index].url = urlOfCover;

      // Not the best way of doing it...
      // Force re-render whenever the :key from the v-card loop changes!
      this.$forceUpdate();
    },
    filterMovies(type) {
      if (type === 'viewed') {
        this.filterStatus = 'viewed';
      } else {
        // eslint-disable-next-line
        if (type === 'notViewed') {
          this.filterStatus = 'notViewed';
        } else {
          this.filterStatus = null;
        }
      }
    },
  },
  mounted() {
    this.getMovies();
  },
};
</script>

<style scoped>
.btn {
  margin: 5px;
}

.card-img-top {
}
</style>
