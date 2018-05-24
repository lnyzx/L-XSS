<template>
<div>
    <el-menu
        id="header"
        :default-active="$route.path"
        mode="horizontal"
        :router="true"
        active-text-color="#ffd04b">
        <li class="menu-header"><strong>L`XSS</strong></li>
        <el-menu-item index="/">encode/decode</el-menu-item>
        <el-menu-item index="/record">
            <el-badge is-dot v-bind:value="new_record" class="item" hidden>
                record
            </el-badge>
        </el-menu-item>
        <el-menu-item index="/probe">probe</el-menu-item>
        <el-menu-item index="/about">about</el-menu-item>
        <el-button type="text" size="small" class="logout" v-on:click="logout()">Logout</el-button>
    </el-menu>
</div>
</template>

<script>
export default {
  name: 'menu',
  data () {
    return {
      new_record: 0
    }
  },
  methods: {
    logout: function () {
      alert('are you sure ?')
    }
  },
  notify_new_record () {
    this.$notify({
      title: '有一条新信息',
      message: '有一条新信息',
      type: 'warning'
    })
  },
  fetch_new_record () {
    // 通过axio结合后端api定时判断是否有新记录产生，逻辑判断放在哪？
    this.new_record = 2
    if (this.new_record > 0) {
      this.notify_new_record()
    }
  },
  fetch_record_interval () {
    setInterval(this.fetch_new_record, 1000)
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#header {
    position: fixed;
    width: 100%;
    top: 0px;
    z-index: 1;
    padding-left: 50px;
}
.logout {
    margin-left:30px;
    height: 60px;
    vertical-align: inherit;
    z-index: 9999;
    font-size: 15px;
}
.el-menu-item {
    font-size: 16px;
}
.menu-header {
    float: left;
    height: 60px;
    line-height: 60px;
    margin: 0;
    cursor: pointer;
    position: relative;
    box-sizing: border-box;
    border-bottom: 5px solid transparent;
}
</style>
