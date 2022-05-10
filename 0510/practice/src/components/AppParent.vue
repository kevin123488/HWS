<template>
  <div id="appparent">
      <h1>AppParent</h1>
      <input type="text"
      v-model="parentInputData"
      @keyup.enter="parentSend">
      <h3>AppData: {{ myMessage }}</h3>
      <h3>ChildData: {{  }}</h3>
      <!-- <app-child></app-child> -->
      <app-child :message="parentInputData"></app-child>
  </div>
</template>

<script>
import AppChild from './AppChild.vue'
// import AppChild from './AppChild.vue'

export default {
    name:'AppParent',
    components: {
        AppChild
        // AppChild,
    },
    props: {
        myMessage: String,
    },
    data: function() {
        return {
            parentInputData: '',
        }
    },
    methods: {
        parentSend: function() {
            this.$emit('canYouHearMe', this.parentInputData)
        }
    }
}
</script>

<style>

</style>