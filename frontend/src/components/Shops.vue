<template>
  <div v-if="isObjectEmpty(shops)" class="text-center">
    <v-row justify="center">
      <v-col class="text-subtitle-1 text-center" cols="12">
        Waiting for Location authorization
      </v-col>
      <v-col>
        <v-progress-linear
          color="deep-purple accent-4"
          indeterminate
          rounded
          height="6"
        ></v-progress-linear>
      </v-col>
    </v-row>
  </div>
  <div v-else>
    <v-row>
      <v-col cols="12" sm="6" md="4" v-for="shop in shops.results" :key="shop.id">
        <shop :value="shop"></shop>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col>
        <v-pagination
          :value="page"
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
    position: null,
  }),
  computed: {
    page() {
      return parseInt(this.$route.query.page, 10) || 1;
    },
  },
  async mounted() {
    await this.userLocation();
  },
  methods: {
    isObjectEmpty(obj) {
      return Object.keys(obj).length === 0;
    },
    userLocation() {
      // Prompt the user to confirm to share his location
      // If the user accepts, we display the shops sorted by distance
      // Else, we display the shops sorted by id
      if (navigator.geolocation) {
        // Send an ajax request with the user's latitude and longitude
        navigator.geolocation.getCurrentPosition(async (position) => {
          this.position = position;
          await this.fetchShops();
        }, async () => {
          // Display shops by order if user does not want to share location
          await this.fetchShops();
        });
      } else {
        this.error = 'Geolocation is not supported by this browser';
      }
    },
    async fetchShops() {
      try {
        const params = {
          page: this.page,
        };
        if (this.position) {
          params.geo_lat = this.position.coords.latitude;
          params.geo_long = this.position.coords.longitude;
        }
        const shops = await axios.get('/api/shops', { params });
        this.shops = shops.data;
      } catch (e) {
        console.log(e);
      }
    },
    next(value) {
      if (parseInt(this.$route.query.page, 10) !== value) {
        this.$router.push({ path: '/', query: { page: value } });
      }
    },
  },
  watch: {
    async page() {
      await this.fetchShops();
    },
  },
};
</script>

<style scoped>

</style>
