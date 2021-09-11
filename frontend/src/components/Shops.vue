<template>
  <v-row>
    <v-col cols="12" sm="6" md="4" v-for="shop in shops.results" :key="shop.id">
      <v-card outlined>
        <v-list-item three-line>
          <v-list-item-content>
            <div class="text-overline mb-4">
              {{ shop.city }}
            </div>
            <v-list-item-title class="text-h5 mb-1">
              {{ shop.name }}
            </v-list-item-title>
            <v-list-item-subtitle>
              {{ shop.distance === -1? '' : shop.distance + ' kms away'}}
            </v-list-item-subtitle>
          </v-list-item-content>

          <v-list-item-avatar tile size="80" color="grey">
            <img
              v-if="shop.picture"
              alt="Avatar"
              :src="shop.picture"
            >
          </v-list-item-avatar>
        </v-list-item>

        <v-card-actions>
          <v-btn outlined rounded text>Like</v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Shops',
  data: () => ({
    shops: {},
  }),
  async mounted() {
    try {
      const shops = await axios.get('/api/shops');
      this.shops = shops.data;
      console.log(this.shops);
    } catch (e) {
      console.log(e);
    }
  },
};
</script>

<style scoped>

</style>
