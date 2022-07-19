<script lang="ts" setup>
const headers: { name: string, value: string }[] = [
  { name: 'Код валюты', value: '1' },
  { name: 'Название валюты', value: '2' },
  { name: 'Цена', value: '3' },
  { name: 'Дата котировки', value: '4' },
  { name: 'Наминал', value: '5' },
]
</script>

<template lang="pug">
v-progress-linear(color="primary" indeterminate)
v-table(fixed-header)
  thead
    tr
      th(v-for="header in headers" :key="header.value") {{ header.name }}
  tbody
    tr
      td(v-for="header in headers" :key="header.value") {{ header.value }}
</template>

