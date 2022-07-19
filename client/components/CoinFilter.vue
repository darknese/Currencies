<script lang="ts" setup>
import { computed, ref, useDataFetch } from '#imports'


export type RateType = {
  id: number
  name: string
  numeric: number
  code: string

}

const props = withDefaults(defineProps<{
    choice?: string[]
  }>(),
  {
    choice: () => ([])
  }
)

const emit = defineEmits<{
  (e: 'update', chosen: string[]): void
}>()

const { data: rates } = await useDataFetch('/coins/rates')

const active = ref<boolean>(false)
const selected = ref(props.choice)
const search = ref('')

const selectedAll = computed({
  get: () => (selected.value.length === (rates.value as RateType[]).length as unknown),
  set: (value: boolean) => {
    selected.value = value ? (rates.value as RateType[]).map(rate => rate.code) : []
  }
})

const titleText = computed<string>(() => {
  if (selectedAll.value){
    return 'Выбраны все валюты'
  }
  if (selected.value.length === 0){
    return 'Не выбрано ни одной валюты'
  } else {
    const firstRate = (rates.value as RateType[]).find(rate => rate.code === selected.value[0])
    return selected.value.length === 1
      ? `Выбрана валюта: ${firstRate.name}`
      : `Выбрана валюта: ${firstRate.name} и еще ${selected.value.length - 1}`
  }
})

const searchRates = computed(() => {
  if (search.value.length < 2) {
    return rates.value
  }
  const lowerSearch = search.value.toLowerCase()
  return (rates.value as RateType[]).filter(
    rate => rate.code.toLowerCase().includes(lowerSearch) || rate.name.toLowerCase().includes(lowerSearch)
  )
})

const apply = () => {
  emit('update', selected.value)
  search.value = ''
  active.value = false
}

</script>
<template lang="pug">
v-menu(v-model="active" :close-on-content-click="false" )
  template(#activator="{ props }")
    v-chip(v-bind="props") {{ titleText }}
  v-card
    v-text-field(v-model="search" label="Поиск" clearable hide-details)
    v-card-text(style="overflow-y: auto; height: 300px")
      v-list
        v-list-item.cursor_pointer
          input(v-model="selectedAll" type="checkbox" :id="selectedALLCodes")
          label.ml-2(for="selectedALLCodes") Все валюты
        v-list-item.cursor_pointer(v-for="rate in searchRates" :key="rate.code")
          input(v-model="selected" type="checkbox" :value="rate.code" :id="rate.code")
          label.ml-2(:for="rate.code") {{ rate.name }}
    v-card-actions
      v-btn(@click="active = false") Закрыть
      v-spacer
      v-btn(@click="apply" color="success") Применить
</template>


<style>
  .cursor_pointer > input, .cursor_pointer > label {
    cursor: pointer;
  }
</style>
