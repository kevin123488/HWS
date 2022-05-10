<template>
  <div>
      <input type="text"
      v-model="parentInputData"
      @keyup.enter="parentSend">
  </div>
</template>

<script>
export default {
    name:'AppParent',
    data: function() {
        return {
            parentInputData: '',
        }
    },
    methods: {
        parentSend: function() {
            this.$emit(this.parentInputData)
        }
    }
}
</script>

<style>

</style>