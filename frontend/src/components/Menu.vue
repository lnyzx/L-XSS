<template>
<div>
    <el-menu
        id="header"
        :default-active="$route.path"
        mode="horizontal"
        :router="true"
        active-text-color="#ffd04b"
        >
        <li class="menu-header"><strong>L`XSS</strong></li>
        <el-menu-item index="/">encode/decode</el-menu-item>
        <el-menu-item index="/record">
            <el-badge is-dot v-bind:value="new_record" class="item" hidden>
                record
            </el-badge>
        </el-menu-item>
        <el-menu-item index="/probe">probe</el-menu-item>
        <el-menu-item index="/json">json</el-menu-item>
        <el-menu-item index="/about">about</el-menu-item>
        <el-button type="text" size="small" class="logout" v-on:click="logout()">Logout</el-button>
    </el-menu>
</div>
</template>

<script>
export default {
  name: 'vmenu',
  data () {
    return {
      new_record: 0,
      maxTime: 0,
      oldTitle: 'l`xss'
    }
  },
  methods: {
    logout () {
      this.$axios.get('/auth/?logout=1')
        .then(function (response) {
          location.href = '/auth/'
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    // 遍历比对time是否比现在最大的time更大，如果有则抛出notify
    fetch_all_record () {
      this.$axios.get('/data/?cmd=listallid')
        .then(response => {
          this.$store.state.dataNumber = response.data.length
          for (var i = 0; i < response.data.length; i++) {
            if (response.data[i].id > this.maxTime) {
              this.notify_new_record(response.data[i].ip, response.data[i].addr)
              this.maxTime = response.data[i].id
            }
          }
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    fetch_record_interval () {
      setInterval(this.fetch_all_record, 2000)
    },
    // click通知时跳转，element的notify的onClick和onClose好像有问题，无法正确触发，所以暂且不能用
    // redirect_2_record () {
    //   this.new_record = 0
    //   document.title = this.oldTitle
    //   window.location = '/auth/#/record'
    // },
    notify_new_record (ip, addr) {
      this.$notify({
        title: ip,
        message: addr,
        type: 'success',
        position: 'bottom-right',
        duration: 10000
      })
      this.$store.state.new_record += 1
      document.title = '【' + this.$store.state.new_record + '】条新记录'
    }
  },
  // 初始获取最大的time，排序逻辑由后端完成
  mounted () {
    this.$store.state.new_record = 0
    this.$axios.get('/data/?cmd=listallid')
      .then(response => {
        this.maxTime = response.data[0].id
      })
      .catch(function (error) {
        console.log(error)
      })
    setTimeout(this.fetch_record_interval(), 3000)
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
