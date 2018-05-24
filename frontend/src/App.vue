<template>
  <div id="app">
    <el-container>
      <vMenu/>
      <el-main><router-view/></el-main>
      <el-footer>@Lnyas</el-footer>
    </el-container>
  </div>
</template>

<script>
import vMenu from './components/Menu.vue'

export default {
  components: {vMenu},
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #2c3e50;
  margin-top: 60px;
}
.el-footer {
  margin-right:auto;
  margin-left: 20px;
}

</style>
