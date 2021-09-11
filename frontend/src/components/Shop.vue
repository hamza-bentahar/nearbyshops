<template>
  <v-card outlined>
    <v-list-item three-line>
      <v-list-item-content>
        <div class="text-overline mb-4">
          {{ value.city }}
        </div>
        <v-list-item-title class="text-h5 mb-1">
          {{ value.name }}
        </v-list-item-title>
        <v-list-item-subtitle>
          {{ value.distance === -1? '' : value.distance + ' kms away'}}
        </v-list-item-subtitle>
      </v-list-item-content>

      <v-list-item-avatar tile size="80" color="grey">
        <img
          v-if="value.picture"
          :alt="value.name"
          :src="value.picture"
        >
      </v-list-item-avatar>
    </v-list-item>

    <v-card-actions>
      <v-btn outlined rounded text>Like</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: 'Shop',
  props: {
    value: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style scoped>

</style>
