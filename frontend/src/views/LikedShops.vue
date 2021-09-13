<template>
  <shops source="/api/likedshops"></shops>
</template>

<script>
import Shops from '../components/Shops.vue';

export default {
  name: 'LikedShops',
  components: {
    Shops,
  },
};
</script>

<style scoped>

</style>
