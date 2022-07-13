<script lang="ts" setup>
import { ref } from '#imports'

const active = ref<boolean>(false)

</script>
<template lang="pug">
v-menu(v-model="active" :close-on-content-click="false")
  template(#activator="{ props }")
    v-chip(v-bind="props") Фильтры по монетам
  v-card
    v-card-text Выбор
    v-card-actions
      v-btn(@click="active = false") Закрыть
      v-spacer
      v-btn(@click="active = false" color="success") Применить
</template>

