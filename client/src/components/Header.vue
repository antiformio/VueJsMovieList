<template>
<div>
  <b-navbar fixed="top" toggleable="lg" type="dark" variant="dark">
    <b-navbar-brand>Filmes</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-row>
        <b-col cols="12" md="7">
          <b-navbar-nav>
            <b-button pill size="sm" variant="success" v-b-modal.movie-modal>
            Adicionar Filme
            </b-button>
          </b-navbar-nav>
        </b-col>

        <b-col cols="6" md="5">
          <b-navbar-nav>
            <b-select size="sm"
            v-model="selectedOption"
            :options="sortOptions"
            value-field="value"
            text-field="text"
            @change="sortBy">
            </b-select>
          </b-navbar-nav>
        </b-col>
      </b-row>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-form>
          <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
          <b-button size="sm" class="my-2 my-sm-0" type="submit">Pesquisar</b-button>
        </b-nav-form>

        <!--
        <b-nav-item-dropdown right>
          <template v-slot:button-content>
            <em>Utilizador</em>
          </template>
          <b-dropdown-item href="#">Perfil</b-dropdown-item>
          <b-dropdown-item href="#">Log-out</b-dropdown-item>
        </b-nav-item-dropdown>
        -->
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
  name: 'Header',
  data() {
    return {
      selectedOption: null,
      sortOptions: [
        { text: 'Todos', value: null },
        { text: 'Vistos', value: 'viewed' },
        { text: 'Por Ver', value: 'notViewed' },
      ],
    };
  },
  methods: {
    sortBy(sortType) {
      this.$emit('filter', sortType);
    },
  },
};
</script>

<style scoped>
</style>
