<template>
  <v-snackbar
    v-model="show"
    :timeout="timeout"
    top
    outlined
    right
    :color="color"
  >
    {{ message }}
    <template #action="{ attrs }">
      <v-btn icon v-bind="attrs" @click="show = false">
        <v-icon>mdi-close</v-icon>
      </v-btn>
    </template>
  </v-snackbar>
</template>

<script>
export default {
  data() {
    return {
      show: false,
      message: '',
      color: '',
      timeout: 30 * 1000,
    };
  },

  created() {
    this.$store.subscribe((mutation, state) => {
      if (mutation.type === 'DISPLAY_SNACKBAR') {
        this.message = state.snackbar.content;
        this.color = state.snackbar.color;
        this.show = true;
      }
    });
  },
};
</script>
