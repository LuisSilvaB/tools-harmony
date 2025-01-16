<script lang="ts" name="dashboard">
  import { Sidebar } from '@/components/layout/sidebar'
  import { defineComponent, ref } from 'vue'
  import { useJwtParser } from '@/composables/useJwtParser'

  export default defineComponent({
  components: { Sidebar },
  setup() {
    const { header, payload, setJwt } = useJwtParser()
    const tokenInput = ref('')

    const updateToken = () => {
      setJwt(tokenInput.value)
    }

    return { header, payload, tokenInput, updateToken }
  },
})

</script>
<template>
  <div class="p-2 ">
    {{payload}}
    <Sidebar />
  </div>
</template>
