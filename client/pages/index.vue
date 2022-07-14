<script lang="ts" setup>
import { ref } from '#imports'
import CoinFilter from '~/components/CoinFilter.vue'
import CoinUnload from '~/components/CoinUnload.vue'

const headers: { name: string, value: string }[] = [
  { name: 'Код валюты', value: '1' },
  { name: 'Название валюты', value: '2' },
  { name: 'Цена', value: '3' },
  { name: 'Дата котировки', value: '4' },
  { name: 'Наминал', value: '5' },
]

const choiseCoins = ref<string[]>(['rub', '$'])

</script>

<template lang="pug">
v-container
  v-row
    v-col
      coin-filter
    v-col.text-right
      coin-unload
  v-row
    v-col
      v-table(fixed-header)
        thead
          tr
            th(v-for="header in headers" :key="header.value") {{ header.name }}
        tbody
          tr
            td(v-for="header in headers" :key="header.value") {{ header.value }}
</template>



