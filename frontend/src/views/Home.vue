<template>
  <hello-world />
</template>

<script>
import axios from 'axios';
import HelloWorld from '../components/HelloWorld.vue';

export default {
  name: 'Home',

  components: {
    HelloWorld,
  },
  async mounted() {
    try {
      const shops = await axios.get('/api/shops');
      console.log(shops);
    } catch (e) {
      console.log(e);
    }
  },
};
</script>
