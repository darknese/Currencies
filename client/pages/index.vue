<script lang="ts" setup>
import { ref } from '#imports'
import CoinFilter from '~/components/CoinFilter.vue'
import CoinUnload from '~/components/CoinUnload.vue'
import CoinsView from '~/components/views/CoinsView.vue'
import NoChoiceCoinsView from '~/components/views/NoChoiceCoinsView.vue'
import OneChoiceCoinsView from '~/components/views/OneChoiceCoinsView.vue'

const choiceCoins = ref<string[]>([])

</script>

<template lang="pug">
v-container
  v-row
    v-col
      coin-filter(:choice="choiceCoins" @update="choiceCoins = $event")
    v-col.text-right(v-show="choiceCoins.length" :choice="choiceCoins")
      coin-unload
  v-row
    v-col
      no-choice-coins-view(v-if="choiceCoins.length === 0" )
      one-choice-coins-view(v-else-if="choiceCoins.length === 1" )
      coins-view(v-else)
</template>



