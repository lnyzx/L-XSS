<template>
  <div class="record">
    <el-table
      v-loading="loading"
      :data="recordData"
      :row-class-name="tableRowClassName"
      style="width: 100%"
      border=true
      class="recordtable"
      highlight-current-row
      @current-change="handleCurrentChange">
      <el-table-column type="expand">
        <template slot-scope="props">
          <el-form label-position="left" inline class="table-expand">
            <el-form-item label="GET: ">
              <span>{{ props.row.get }}</span>
            </el-form-item>
            <el-form-item label="POST: ">
              <span>{{ props.row.post }}</span>
            </el-form-item>
            <el-form-item label="Cookie: ">
              <span>{{ props.row.cookies }}</span>
            </el-form-item>
            <el-form-item label="User-Agent: ">
              <span>{{ props.row.userAgent }}</span>
            </el-form-item>
            <el-form-item label="Header: ">
              <span>{{ props.row.header }}</span>
            </el-form-item>
            <el-form-item label="path: ">
              <span>{{ props.row.path }}</span>
            </el-form-item>
            <el-form-item label="port: ">
              <span>{{ props.row.port }}</span>
            </el-form-item>
          </el-form>
        </template>
      </el-table-column>
      <el-table-column
        label="时间"
        prop="time"
        width="200"
        sortable>
      </el-table-column>
      <el-table-column
        label="ip"
        prop="ip"
        width="150"
        sortable>
      </el-table-column>
      <el-table-column
        label="来源"
        prop="addr"
        width="350"
        sortable>
      </el-table-column>
      <el-table-column
        label="客户端"
        prop="client"
        width="350"
        sortable>
      </el-table-column>
      <el-table-column
        label="请求"
        prop="method"
        width="100"
        sortable>
      </el-table-column>
      <el-table-column
        label="携带数据"
        prop="data"
        sortable>
      </el-table-column>
    </el-table>
    <div class="block">
      <div class="delete">
        <el-button type="danger" plain size="mini" v-on:click="deleteSingle">删除</el-button>
        <el-button type="danger" plain size="mini" v-on:click="deleteAll">清空</el-button>
        <el-button plain size="mini" v-on:click="reFresh">刷新</el-button>
      </div>
      <el-pagination
        layout="prev, pager, next"
        :total="dataNum"
        class="pagination"
        :page-size="pageNumber"
        @current-change="changeCurrentPage">
      </el-pagination>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: 'Record',
  data () {
    return {
      recordData: [],
      loading: true,
      thisPage: 1,
      pageNumber: 15,
      result: 0,
      dataNum: this.$store.state.dataNumber
    }
  },
  methods: {
    // 刷新数据
    reFresh () {
      this.loading = true
      this.recordData = []
      this.getData()
    },
    //把每一行的索引放进row，以便handleCurrentChange调用
    tableRowClassName (current, index) {
        current.row.index = current.rowIndex
    },
    // 获取选中行的row
    handleCurrentChange (val) {
        this.currentRow = val;
    },
    // 删除全部记录
    deleteAll () {
      this.$confirm('确定清空所有记录?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.recordData = []
        let postData = this.$qs.stringify({
          id: 'all'
        })
        this.$axios.post('/data/?cmd=delete', postData)
          .then(response => {
            this.$message({
              type: 'success',
              message: '删除成功!'
            });
          })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        })
      })
    },
    // 删除选中的一条记录
    deleteSingle () {
      this.$confirm('确定删除所选记录?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        let postData = this.$qs.stringify({
          id: this.currentRow.id
        })
        this.$axios.post('/data/?cmd=delete', postData)
          .then(response => {
            this.recordData.splice(this.currentRow.index, 1)
            this.$message({
              type: 'success',
              message: '删除成功!'
            });
          })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        })       
      })
    },
    // 点击页码后更改currentpage
    changeCurrentPage (val) {
      this.thisPage = val
      this.loading = true
      this.recordData = []
      this.getData()
    },
    // 去除header中的重复属性
    deleteHeader (headerData) {
      delete headerData.User_Agent
      delete headerData.Cookie
      return headerData
    },
    // 合并cookie，post，get中的数据，取出key
    combineData (thisData) {
      var data_key = {};
      var get_keys = Object.keys(thisData.get_data)
      var post_keys = Object.keys(thisData.post_data)
      var cookie_keys = Object.keys(thisData.cookie_data)
      if (get_keys.length > 0) data_key.GET = get_keys
      if (post_keys.length > 0) data_key.POST = post_keys
      if (cookie_keys.length > 0) data_key.COOKIE = cookie_keys
      return JSON.stringify(data_key)
    },
    // 生成可绑定数据，包括页码
    generateData (result) {
      for (var i = 0; i < result.length; i++) {
        var thisData = JSON.parse(result[i])
        var tmp_data = {}
        tmp_data['time'] = thisData.req_formattime
        tmp_data['id'] = thisData.req_time
        tmp_data['ip'] = thisData.req_ip
        tmp_data['addr'] = thisData.req_ip_addr
        tmp_data['client'] = this.get_client_info(thisData.req_header.User_Agent)
        tmp_data['method'] = thisData.req_method
        tmp_data['data'] = this.combineData(thisData)
        tmp_data['get'] = JSON.stringify(thisData.get_data, null, "    ")
        tmp_data['post'] = JSON.stringify(thisData.post_data, null, "    ")
        tmp_data['cookies'] = JSON.stringify(thisData.cookie_data, null, "    ")
        tmp_data['userAgent'] =  JSON.stringify(thisData.req_header.User_Agent, null, "    ")
        tmp_data['header'] = JSON.stringify(this.deleteHeader(thisData.req_header), null, "    ")
        tmp_data['path'] =  JSON.stringify(thisData.req_path, null, "    ")
        tmp_data['port'] =  JSON.stringify(thisData.req_port, null, "    ")
        this.recordData.push(tmp_data)
      }
      this.loading = false
    },
    getData () {
      var result = []
      let postData = this.$qs.stringify({
        page: this.thisPage,
        page_number: this.pageNumber
      })
      this.$axios.post('/data/?cmd=list', postData)
        .then(response => {
          this.generateData(response.data)
        })
    },
    // 根据client判断操作系统，浏览器版本，from firesun
    get_client_info (agent) {
        var browser = "未知浏览器";
        var browser_version = "";
        if (agent.indexOf("Firefox/") > 0) {
            var bv = agent.match(/Firefox\/([^;)]+)+/i);
            browser = "Firefox";
            browser_version = bv[1]; //获取火狐浏览器的版本号
        } else if (agent.indexOf("Maxthon") > 0) {
            var bv = agent.match(/Maxthon\/([\d\.]+)/);
            browser = "傲游";
            browser_version = bv[1];
        } else if (agent.indexOf("MSIE") > 0) {
            var bv = agent.match(/MSIE\s+([^;)]+)+/i);
            browser = "IE";
            browser_version = bv[1]; //获取IE的版本号
        } else if (agent.indexOf("OPR") > 0) {
            var bv = agent.match(/OPR\/([\d\.]+)/);
            browser = "Opera";
            browser_version = bv[1];
        } else if (agent.indexOf("Edge") > 0) {
            //win10 Edge浏览器 添加了chrome内核标记 在判断Chrome之前匹配
            var bv = agent.match(/Edge\/([\d\.]+)/);
            browser = "Edge";
            browser_version = bv[1];
        } else if (agent.indexOf("Chrome") > 0) {
            var bv = agent.match(/Chrome\/([\d\.]+)/);

            browser = "Chrome";
            browser_version = bv[1]; //获取google chrome的版本号
        } else if (agent.indexOf('rv:') > 0 && agent.indexOf('Gecko') > 0) {
            var bv = agent.match(/rv:([\d\.]+)/);
            browser = "IE";
            browser_version = bv[1];
        }
        browser_version = browser_version.match(/^[0-9\.]+$/) ? browser_version : "未知";

        var os = '未知操作系统';
        if (agent.match(/win/i) && (agent.indexOf("95") > 0)) os = 'Windows 95';
        else if (agent.match(/win 9x/i) && (agent.indexOf("4.90") > 0)) os = 'Windows ME';
        else if (agent.match(/win/i) && agent.match(/98/i)) os = 'Windows 98';
        else if (agent.match(/win/i) && agent.match(/nt 6.0/i)) os = 'Windows Vista';
        else if (agent.match(/win/i) && agent.match(/nt 6.1/i)) os = 'Windows 7';
        else if (agent.match(/win/i) && agent.match(/nt 6.2/i)) os = 'Windows 8';
        else if (agent.match(/win/i) && agent.match(/nt 10.0/i)) os = 'Windows 10';
        else if (agent.match(/win/i) && agent.match(/nt 5.1/i)) os = 'Windows XP';
        else if (agent.match(/win/i) && agent.match(/nt 5/i)) os = 'Windows 2000';
        else if (agent.match(/win/i) && agent.match(/nt/i)) os = 'Windows NT';
        else if (agent.match(/win/i) && agent.match(/32/i)) os = 'Windows 32';
        else if (agent.match(/linux/i)) os = 'Linux';
        else if (agent.match(/unix/i)) os = 'Unix';
        else if (agent.match(/sun/i) && agent.match(/os/i)) os = 'SunOS';
        else if (agent.match(/ibm/i) && agent.match(/os/i)) os = 'IBM OS/2';
        else if (agent.match(/Mac/i) && agent.match(/PC/i)) os = 'Macintosh';
        else if (agent.match(/PowerPC/i)) os = 'PowerPC';
        else if (agent.match(/AIX/i)) os = 'AIX';
        else if (agent.match(/HPUX/i)) os = 'HPUX';
        else if (agent.match(/NetBSD/i)) os = 'NetBSD';
        else if (agent.match(/BSD/i)) os = 'BSD';
        else if (agent.match(/OSF1/i)) os = 'OSF1';
        else if (agent.match(/IRIX/i)) os = 'IRIX';
        else if (agent.match(/FreeBSD/i)) os = 'FreeBSD';
        else if (agent.match(/teleport/i)) os = 'teleport';
        else if (agent.match(/flashget/i)) os = 'flashget';
        else if (agent.match(/webzip/i)) os = 'webzip';
        else if (agent.match(/offline/i)) os = 'offline';

        return os + ' ' + browser + '(' + browser_version + ')';
    }
  },
  mounted() {
    this.$store.state.new_record = 0
    document.title = 'l`xss'
    this.getData()
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.record {
  margin-left: 100px;
  margin-right: 100px;
}
.block {
  display: flex;
  margin-top: 10px;
}
.pagination {
  margin: auto;
}
.table-expand label {
  font-weight: bold;
}
</style>
