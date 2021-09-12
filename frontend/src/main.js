import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import vuetify from './plugins/vuetify';
import axios from './axiosConfig';

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App),
  async mounted() {
    const isAuth = await axios.get('/api/isauthenticated/');
    console.log(isAuth.data);
  },
}).$mount('#app');
