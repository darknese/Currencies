<script lang="ts" setup>
import { ref } from '#imports'
import CoinFilter from '~/components/CoinFilter.vue'
import CoinUnload from '~/components/CoinUnload.vue'

const count = ref<number>(0)

</script>

<template lang="pug">
v-container
  v-row
    v-col
      coin-filter
    v-col
      coin-unload
  v-row
    v-col
      v-btn(@click="++count") {{ count }}
</template>


