<template>
	<div id="app">
    <h1>App</h1>
    <input type="text"
    v-model="appInputData">
    <h3>ParentData: {{ parentData }}</h3>
    <h3>ChildData: {{  }}</h3>
    <app-parent @canYouHearMe="yesIcan" :my-message="appInputData"></app-parent>
    <app-child :my-message="appInputData"></app-child>
  </div>
</template>

<script>
import AppParent from './components/AppParent.vue'
import AppChild from './components/AppChild.vue'
    
export default {
  name: 'App',
  components: {
    AppParent,
    AppChild,
  },
  data: function() {
    return {
      appInputData: '',
      parentData: '',
      childData: '',
    }
  },
  methods: {
    yesIcan: function(parentInputData) {
      this.parentData = parentInputData

    },
    alsoIcan: function(childInputData) {
      this.childData = childInputData
    }
  }

  
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
