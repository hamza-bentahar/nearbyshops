<template>
  <validation-provider v-slot="{ errors }" :rules="rules" :name="name">
    <v-text-field
      :value="value"
      :label="label"
      :type="type"
      :error-messages="errors"
      @input="updateValue"
    />
  </validation-provider>
</template>

<script>
import { ValidationProvider } from 'vee-validate';

export default {
  name: 'BaseInput',
  components: {
    ValidationProvider,
  },
  props: {
    value: {
      type: String,
      default: '',
    },
    rules: {
      type: [String, Object],
      default: '',
    },
    name: {
      type: String,
      default: '',
    },
    type: {
      type: String,
      default: 'text',
    },
    label: {
      type: String,
      default: '',
    },
  },
  methods: {
    updateValue(val) {
      this.$emit('input', val);
    },
  },
};
</script>
