<template>
<div>
  <b-navbar fixed="top" toggleable="lg" type="dark" variant="dark">
    <b-navbar-brand>Filmes</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-button pill size="sm" variant="success" v-b-modal.movie-modal>
        Adicionar Filme
        </b-button>

        <b-dropdown
        class="ml-4"
        right text="Filtrar"
        size="sm"
        variant="primary"
        @change="onChange($event)">
            <b-dropdown-item active>Todos</b-dropdown-item>
            <b-dropdown-item>Vistos</b-dropdown-item>
            <b-dropdown-item>Por ver</b-dropdown-item>
        </b-dropdown>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-form>
          <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
          <b-button size="sm" class="my-2 my-sm-0" type="submit">Pesquisar</b-button>
        </b-nav-form>


        <b-nav-item-dropdown right>
          <!-- Using 'button-content' slot -->
          <template v-slot:button-content>
            <em>Utilizador</em>
          </template>
          <b-dropdown-item href="#">Perfil</b-dropdown-item>
          <b-dropdown-item href="#">Log-out</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</div>
</template>

<script>
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
    onChange(event) {
      console.log(event.target.value);
    },
  },
  mounted() {
    // eslint-disable-next-line
    this.$root.$on('bv::dropdown::change', bvEvent => {
      console.log('Dropdown is about to be shown', bvEvent);
    });
  },
};
</script>

<style scoped>
</style>
