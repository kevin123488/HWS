<template>
  <div>
      <h1>AppChild</h1>
      <input type="text">
      <h3>AppData: {{ myMessage }}</h3>
      <h3>ParentData: {{ message }}</h3>

  </div>
</template>

<script>
export default {
    name: 'AppChild',
    props: {
        myMessage: String,
        message: String,
    }
}
</script>

<style>

</style>