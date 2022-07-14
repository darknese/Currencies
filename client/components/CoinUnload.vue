<script lang="ts" setup>
import { ref } from '#imports'

const emit = defineEmits<{
  (e: 'unload', type: string): void
}>()

const active = ref<boolean>(false)
const unloadTypes: { key: string, name: string, icon: string }[] = [
  { key: 'pdf', name: 'Выгрузить в pdf', icon: 'file-pdf-box' },
  { key: 'xlsx', name: 'Выгрузить в xlsx', icon: 'file-excel-box' },
  { key: 'csv', name: 'Выгрузить в csv', icon: 'file-delimited' },
]
</script>
<template lang="pug">
v-menu(v-model="active")
  template(#activator="{ props }")
    v-btn(v-bind="props" icon flat)
      v-icon(color="success") mdi-download
  v-list
    v-list-item(
      v-for="unloadType in unloadTypes"
      @click="emit('unload', unloadType.key)"
      :key="unloadType.key"
    )
      v-list-item-icon(:icon="`mdi-${unloadType.icon}`" start)
      v-list-item-title {{ unloadType.name }}
</template>
