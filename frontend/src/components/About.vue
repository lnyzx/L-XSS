<template>
  <div class="about">
    <el-card class="box-card">
      <h3>Hello this is Lnyas</h3>
      <div>It's a very simple tool</div>
      and wish you have fun with it !
    </el-card>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: 'About',
  data () {
    return {
      text: {
          input: "",
          output: ""
      },
      lastAction: undefined,
    }
  },
  methods: {
  },
}
</script>

<style scoped>
  .box-card {
    margin-left: 120px;
  }
  .text {
    font-size: 14px;
  }

  .item {
    padding: 18px 0;
  }

  .box-card {
    width: 480px;
  }
</style>