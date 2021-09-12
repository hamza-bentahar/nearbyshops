import { extend, setInteractionMode } from 'vee-validate';
import {
  confirmed, email, min, required,
} from 'vee-validate/dist/rules';

setInteractionMode('eager');

extend('confirmed', {
  ...confirmed,
  message: 'Passwords must match',
});

extend('email', {
  ...email,
  message: 'Invalid email',
});

extend('min', {
  ...min,
  message: '{_field_} must be at least {length} characters long',
});

extend('required', {
  ...required,
  message: '{_field_} can not be empty',
});
