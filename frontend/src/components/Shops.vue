<template>
  <v-row>
    <v-col cols="12" sm="6" md="4" v-for="shop in shops.results" :key="shop.id">
      <shop :value="shop"></shop>
    </v-col>
  </v-row>
</template>

<script>
import axios from 'axios';
import Shop from './Shop.vue';

export default {
  name: 'Shops',
  components: {
    Shop,
  },
  data: () => ({
    shops: {},
  }),
  async mounted() {
    try {
      const shops = await axios.get('/api/shops');
      this.shops = shops.data;
    } catch (e) {
      console.log(e);
    }
  },
};
</script>

<style scoped>

</style>
