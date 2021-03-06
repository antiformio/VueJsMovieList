import Vue from 'vue';
import Router from 'vue-router';
import Ping from '@/components/Ping.vue';
import Movies from '@/components/Movies.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      component: Movies,
      meta: {
        title: 'Filmes App - Filipe Martins',
      },
      name: 'Movies',
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
});
