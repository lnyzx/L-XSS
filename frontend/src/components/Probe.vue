<template>
  <div class="probe">
    <el-row :gutter="20" type="flex" justify="center">
      <el-col :span="13" class="left-col">
        <el-card shadow="never" class="card-left">
          <el-row type="flex" :gutter="15">
            <el-col :span="10">
              <el-select v-model="methodvalue" size='medium'>
                <el-option
                  v-for="item in requesMethod"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </el-col>
            <el-col :span="15"><el-input size="medium" v-model="url"></el-input></el-col>
            <el-col :span="20"><el-input size="medium" v-model="param"></el-input></el-col>
          </el-row>

          <el-row type="flex" :gutter="15">
            <el-col :span="13">
              <el-select v-model="csrfvalue" size='medium'>
                <el-option
                  v-for="item in CSRFlanguage"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </el-col>
            <el-col :span="6"><el-button class='action' type="warning" size="medium" v-on:click="createCSRF" plain>Create CSRF</el-button></el-col>
            <el-col :span="15">
              <el-select v-model="ajaxvalue" size='medium'>
                <el-option
                  v-for="item in AJAXlanguage"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </el-col>
            <el-col :span="6"><el-button class='action' type="warning" size="medium" v-on:click="createAJAX" plain>Create AJAX</el-button></el-col>
          </el-row>

          <el-row type="flex" :gutter="15">
            <el-col>
              <el-input
              type="textarea"
              :rows="25"
              placeholder="Write Your Probe Code Here"
              v-model="text.input"
              resize="none"
              class="inputtext"
              clearable>
              </el-input>
            </el-col>
          </el-row>

          <el-row type="flex" :gutter="15">
            <el-col :span="14">
              <el-select v-model="templatevalue" size='medium' @change="changeTemplate">
                <el-option
                  v-for="item in Templates"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </el-col>
            <el-col>
              <el-input placeholder="probe-name" v-model="probeName" size="medium">
                <template slot="prepend">{{ thisDomain }}</template>
                <template slot="append">.js</template>
              </el-input>
            </el-col>
            <el-col :span="5"><el-button class='action' type="danger" size="medium" v-on:click="createProbe" plain>Create Probe</el-button></el-col>
          </el-row>

        </el-card>
      </el-col>

      <el-col :span="8" class="right-col">
        <el-row>
          <el-card shadow="never">
            <b>CheatSheet</b>
            <el-table
              ref="singleTable"
              :data="cheatsheetData"
              highlight-current-row
              style="width: 100%">
              <el-table-column
                type="index">
              </el-table-column>
              <el-table-column
                label="name">
                <template slot-scope="scope">
                  <a :href="scope.row.cheaturl">{{ scope.row.cheatname }}</a>
                </template>
              </el-table-column>
              <el-table-column
                property="cheatdesc"
                label="describe">
              </el-table-column>
            </el-table>
          </el-card>
        </el-row>
        <el-row type="flex" :gutter="15">
          <el-card shadow="never">
            <b>Online Probe</b>
            <el-col>
              <el-table
                ref="singleTable"
                :data="probesData"
                highlight-current-row
                :row-class-name="tableRowClassName"
                @current-change="handleCurrentChange"
                style="width: 100%">
                <el-table-column
                  type="index">
                </el-table-column>
                <el-table-column
                  label="name"
                  width="120px">
                  <template slot-scope="scope">
                    <a :href="scope.row.probeurl">{{ scope.row.probename }}</a>
                  </template>
                </el-table-column>
                <el-table-column
                  property="probelink"
                  label="link">
                </el-table-column>
              </el-table>
            </el-col>
            <el-col>
              <div class="delete">
                <el-button type="danger" plain size="mini" v-on:click="deleteSingle">删除</el-button>
                <el-button type="danger" plain size="mini" v-on:click="deleteAll">清空</el-button>
              </div>
            </el-col>
          </el-card>
        </el-row>
      </el-col>
    </el-row>
  </div>
</template>

<script>
/* eslint-disable */
import codz from './payloadJS/csrf.js'

export default {
  name: 'Probe',
  data () {
    return {
      text: {
          input: ""
      },
      requesMethod: [
        {
          value: 'GET',
          label: 'GET'
        },
        {
          value: 'POST',
          label: 'POST'
        }
      ],
      methodvalue: 'GET',
      CSRFlanguage: [
        {
          value: 'html',
          label: 'HTML'
        },
        {
          value: 'js',
          label: 'JavaScript'
        },
        {
          value: 'php',
          label: 'PHP'
        }
      ],
      csrfvalue: 'CSRF Language',
      AJAXlanguage: [
        {
          value: '3',
          label: 'jQuery'
        },
        {
          value: '1',
          label: 'multipart/form-data'
        },
        {
          value: '2',
          label: 'application/x-www-form-urlencoded'
        }
      ],
      ajaxvalue: 'Content-Type',
      Templates: [],
      probesData: [],
      thisDomain: '',
      probeName: '',
      templatevalue: 'Templates',
      url: 'http://example.com',
      param: 'key1=value1&key2=value2',
      cheatsheetData: [
      {
        cheaturl: '/static/cheatsheet/lnyas-cheatsheet.txt',
        cheatname: 'Lnyas\'s cheatsheet',
        cheatdesc: 'Personal note'
      },
      ]
    }
  },
  methods: {
    //把每一行的索引放进row，以便handleCurrentChange调用
    tableRowClassName (current, index) {
        current.row.index = current.rowIndex
    },
    // 获取选中行的row
    handleCurrentChange (val) {
        this.currentRow = val;
    },
    output (value) {
      this.text.input = this.magic(value)
    },

    // template选择器变化时自动填入template的内容
    changeTemplate () {
      var template_url = this.thisDomain + 'static/templates/' + this.templatevalue
      this.$axios.get(template_url)
        .then(response => {
          var result = response.data.replace("%example-url%", this.thisDomain)
          this.output(result)
        })
        .catch(function (error) {
          console.log(error)
        })
    },

    // 根据input和probe的名字生成probe
    createProbe () {
      var probecontent = btoa(this.text.input)
      let postData = this.$qs.stringify({
        name: this.probeName,
        content: probecontent
      })
      this.$axios.post('/probe/?cmd=createprobe', postData)
        .then(response => {
          this.insertProbe(this.probeName)
          this.probeName = this.genProbeName()
          this.$message({
            type: 'success',
            message: '创建成功!'
          });
        })
      .catch(() => {
      })
    },

    // 将新创建的probe加入probesData表格中
    insertProbe (name) {
      name = name + '.js'
      var a = {}
      var this_url = this.thisDomain + name
      a['probeurl'] = this_url
      a['probename'] = name
      a['probelink'] = '<script src="' + this_url + '"></scr'+'ipt>'
      this.probesData.push(a)
    },

    // 根据url，param，method和[language,Content-Type]生成csrf和ajax代码，处理逻辑在前端
    createCSRF () {
      let result = codz().csrf(this.methodvalue, this.url, this.param, this.csrfvalue)
      this.output(result)
    },
    createAJAX () {
      let result = codz().ajax(this.methodvalue, this.url, this.param, this.ajaxvalue)
      this.output(result)
    },

    // 生成四位随机字符串作为probe名字
    genProbeName () {
      var tmp_name = Math.random().toString(36).substr(2, 4)
        return tmp_name
    },

    // 加载templates的名字
    getTemplatesName () {
      this.$axios.get('/probe/?cmd=getalltemplates')
        .then(response => {
          var tmp_data = {}
          for (var i = 0; i < response.data.length; i++) {
            var a = {}
            a.value = response.data[i]
            a.label = response.data[i]
            this.Templates.push(a)
          }
        })
        .catch(function (error) {
          console.log(error)
        })
    },

    // 加载所有probe的名字
    getProbesName () {
      this.probesData = []
      this.$axios.get('/probe/?cmd=getallprobe')
        .then(response => {
          for (var i = 0; i < response.data.length; i++) {
            var a = {}
            var this_url = this.thisDomain + response.data[i]
            a['probeurl'] = this_url
            a['probename'] = response.data[i]
            a['probelink'] = '<script src="' + this_url + '"></scr'+'ipt>'
            this.probesData.push(a)
          }
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    // 删除全部probe
    deleteAll () {
      this.$confirm('确定清空所有probe?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.probesData = []
        let postData = this.$qs.stringify({
          name: 'all'
        })
        this.$axios.post('/probe/?cmd=deleteprobe', postData)
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
    // 删除选中的一条probe
    deleteSingle () {
      this.$confirm('确定删除所选probe?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        let postData = this.$qs.stringify({
          name: this.currentRow.probename
        })
        this.$axios.post('/probe/?cmd=deleteprobe', postData)
          .then(response => {
            console.log(this.currentRow)
            this.probesData.splice(this.currentRow.index, 1)
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
  },
  mounted () {
    this.thisDomain = window.location.protocol + '//' + window.location.host + '/'
    // 随机一个probe名字
    this.probeName = this.genProbeName()

    // // 页面初始化时加载templates的名字
    this.getTemplatesName()

    // // 加载所有probe的名字
    this.getProbesName()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.el-select{
  width: 100%;
}

.delete {
  margin-top: 10px;
  margin-bottom: 10px;
}

.card-left {
  min-width: 390px;
}
</style>
