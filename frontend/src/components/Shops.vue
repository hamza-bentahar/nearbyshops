<template>
  <div>
    <v-row>
      <v-col cols="12" sm="6" md="4" v-for="shop in shops.results" :key="shop.id">
        <shop :value="shop"></shop>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col>
        <v-pagination
          v-model="page"
          :length="shops.total_pages"
          :total-visible="7"
          @input="next"
        ></v-pagination>
      </v-col>
    </v-row>
  </div>
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
    page: 1,
  }),
  async mounted() {
    await this.fetchShops();
  },
  methods: {
    async fetchShops() {
      try {
        const shops = await axios.get('/api/shops', {
          params: {
            page: this.page,
          },
        });
        this.shops = shops.data;
      } catch (e) {
        console.log(e);
      }
    },
    async next(value) {
      this.page = value;
      await this.fetchShops();
    },
  },
};
</script>

<style scoped>

</style>
