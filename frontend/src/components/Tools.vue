<template>
  <div class="encode">
    <el-row :gutter="20" type="flex" justify="center">
      <el-col :span="8" class="right-col">
        <el-input
          type="textarea"
          :rows="30"
          placeholder="Input Here"
          v-model="text.input"
          resize="none"
          clearable
          v-on:input="convert"
          >
        </el-input>
      </el-col>
      <el-col :span="5" class="button-col">
        <el-row>
          <el-button-group>
            <el-button class='action' size="medium" v-on:click="urlencode">URL编码</el-button>
            <el-button class='action' size="medium" v-on:click="urlallencode">URL全编码</el-button>
            <el-button class='action' size="medium" v-on:click="urldecode">URL解码</el-button>
          </el-button-group>
        </el-row>
        <el-row>
          <el-button-group>
            <el-button class='action' size="small" v-on:click="b64encode">Base64编码</el-button>
            <el-button class='action' size="small" v-on:click="b64decode">Base64解码</el-button>
          </el-button-group>
          <el-button-group>
            <el-button class='action' size="small" v-on:click="hexencode">Hex 编码</el-button>
            <el-button class='action' size="small" v-on:click="hexdecode">Hex 解码</el-button>
          </el-button-group>
        </el-row>
        <el-row>
        <div class="hash">
          <el-select v-model="value" size='medium' placeholder="Hash">
              <el-option
                v-for="item in hashtype"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
          </el-select>
          <el-button class='action' size="medium" v-on:click="hashencode">Hash</el-button>
          </div>
        </el-row>
        <el-row>
          <el-button-group>
              <el-button class='action' size="medium" v-on:click="unicodeencode">Unicode编码</el-button>
              <el-button class='action' size="medium" v-on:click="unicodedecode">Unicode解码</el-button>
          </el-button-group>
        </el-row>
        <el-row>
          <el-button-group>
              <el-button class='action' size="medium" v-on:click="stringcharcode">String.FromChar En</el-button>
              <el-button class='action' size="medium" v-on:click="stringcharcodedecode">String.FromChar De</el-button>
          </el-button-group>
        </el-row>
        <el-row>
          <el-button-group>
              <el-button class='action' size="small" v-on:click="html10encode">HTML10en</el-button>
              <el-button class='action' size="small" v-on:click="html10decode">HTML10de</el-button>
          </el-button-group>
          <el-button-group>
              <el-button class='action' size="small" v-on:click="html16encode">HTML16en</el-button>
              <el-button class='action' size="small" v-on:click="html16decode">HTML16de</el-button>
          </el-button-group>
        </el-row>
        <el-row>
          <el-button-group>
              <el-button class='action' size="small" v-on:click="js8encode">JS8en</el-button>
              <el-button class='action' size="small" v-on:click="js8decode">JS8de</el-button>
          </el-button-group>
          <el-button-group>
              <el-button class='action' size="small" v-on:click="js16encode">JS16en</el-button>
              <el-button class='action' size="small" v-on:click="js16decode">JS16de</el-button>
          </el-button-group>
        </el-row>
        <el-row>
          <div class="hash">
          <el-select v-model="scale_value_from" size='small' style="width:100px" placeholder="Hash">
              <el-option
                v-for="item in scale"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
          </el-select>
          =>
          <el-select v-model="scale_value_to" size='small' style="width:100px" placeholder="Hash">
              <el-option
                v-for="item in scale"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
          </el-select>
          <el-button class='action' size="medium" v-on:click="scalConvert">进制转换</el-button>
          </div>
        </el-row>
        <el-row>
          <el-button-group>
              <el-button class='action' size="small" v-on:click="jsBeautify">JS Beautify</el-button>
              <el-button class='action' size="small" v-on:click="htmlBeautify">HTML Beautify</el-button>
          </el-button-group>
          <el-button class='action' type="danger" size="small" @click="execute" plain>EVAL</el-button>
          <el-button class='action' type="danger" size="small" v-on:click="clear" plain>CLEAR</el-button>
        </el-row>
      </el-col>
      <el-col :span="8" class="left-col">
        <el-input
          type="textarea"
          :rows="30"
          v-model="text.output"
          resize="none"
          readonly
          >
        </el-input>
      </el-col>
    </el-row>
  </div>
</template>

<script>
/* eslint-disable */
import base64 from 'crypto-js/enc-base64'
import utf8 from 'crypto-js/enc-utf8'
import latin1 from 'crypto-js/enc-latin1'
import hex from 'crypto-js/enc-hex'
import CryptoJS from 'crypto-js'
import js_beautify from 'js-beautify'

const hashTable = {
    md5: (val) => CryptoJS.MD5(val).toString(),
    sha1: (val) => CryptoJS.SHA1(val).toString(),
    sha256: (val) => CryptoJS.SHA256(val).toString(),
    sha512: (val) => CryptoJS.SHA512(val).toString(),
}

function urlencode (a,b) {
    return++b?'%'+([10]+a.charCodeAt().toString(16)).slice(-2):unescape(encodeURIComponent(a)).replace(/[^]/g, urlencode);
}

export default {
  name: 'Tools',
  data () {
    return {
      text: {
          input: "",
          output: ""
      },
      lastAction: undefined,
      hashtype: [
        {
          value: 'md5',
          label: 'MD5'
        },
        {
          value: 'sha1',
          label: 'SHA1'
        },
        {
          value: 'sha256',
          label: 'SHA256'
        },
        {
          value: 'sha512',
          label: 'SHA512'
        }
      ],
      value: 'md5',
      scale: [
        {
          value: '2',
          label: '2'
        },
        {
          value: '8',
          label: '8'
        },
        {
          value: '10',
          label: '10'
        },
        {
          value: '16',
          label: '16'
        }
      ],
      scale_value_from: '10',
      scale_value_to: '16'
    }
  },
  methods: {
    htmlBeautify () {
      this.lastAction = this.htmlBeautify
      let result = js_beautify.html(this.text.input, { indent_size: 2, space_in_empty_paren: true })
      this.output(result)
    },
    jsBeautify () {
      this.lastAction = this.jsBeautify
      let result = js_beautify.js(this.text.input, { indent_size: 2, space_in_empty_paren: true })
      this.output(result)
    },
    clear () {
      this.text.input = ""
      this.text.output = ""
    },
    hashencode () {
      this.lastAction = this.hashencode
      if (this.value in hashTable) {
        let result = eval('hashTable.'+ this.value + '("' + this.text.input + '")')
        this.output(result)
      }
    },
    output (value) {
      this.text.output = this.magic(value)
    },
    convert () {
      if(this.lastAction && this.lastAction instanceof Function) {
        this.lastAction()
      }
    },
    b64encode () {
      this.lastAction = this.b64encode
      this.output(base64.stringify(utf8.parse(this.text.input)))
    },
    b64decode () {
      let result
      this.lastAction = this.b64decode
      let bytes = base64.parse(this.text.input)
      try {
          result = utf8.stringify(bytes)
      } catch (e) {
          result = latin1.stringify(bytes)
      }
      this.output(result)
    },
    hexencode () {
      this.lastAction = this.hexencode
      let result = '0x' + hex.stringify(utf8.parse(this.text.input))
      this.output(result)
    },
    hexdecode () {
      let result
      this.lastAction = this.hexdecode
      let enc = this.text.input
      if (enc.startsWith('0x') || enc.startsWith('0X')) {
          enc = enc.substr(2)
      }
      let bytes = hex.parse(enc)
      try {
          result = utf8.stringify(bytes)
      } catch (e) {
          result = latin1.stringify(bytes)
      }
      this.output(result)
    },
    urlencode () {
      this.lastAction = this.urlencode
      this.output(encodeURIComponent(this.text.input))
    },
    urldecode () {
      this.lastAction = this.urldecode
      this.output(decodeURIComponent(this.text.input))
    },
    urlallencode () {
      this.lastAction = this.urlallencode
      this.output(urlencode(this.text.input))
    },
    html10encode () {
      this.lastAction = this.html10encode
      let result = this.text.input.split('').map(m => "&#" + m.charCodeAt() + ";").join('')
      this.output(result)
    },
    html10decode () {
      this.lastAction = this.html10decode
      let result = this.text.input.replace(/&#(\d+);?/g, (match, i) => String.fromCharCode(parseInt(i)))
      this.output(result)
    },
    htmlspecialchars () {
      this.lastAction = this.htmlspecialchars
      let result = this.text.input
          .replace(/&/g, '&amp;')
          .replace(/"/g, '&quot;')
          .replace(/'/g, '&#039;')
          .replace(/</g, '&lt;')
          .replace(/>/g, '&gt;')
      this.output(result)
    },
    html16encode () {
      this.lastAction = this.html16encode
      let result = this.text.input.split('').map(m => "&#x" + m.charCodeAt().toString(16) + ";").join('')
      this.output(result)
    },
    html16decode () {
      this.lastAction = this.html16decode
      let result = this.text.input.replace(/&#x([a-f0-9]+);?/ig, (match, i) => String.fromCharCode(parseInt(i, 16)))
      this.output(result)
    },
    js8encode () {
      this.lastAction = this.js8encode
      let result = this.text.input.split('').map(m => "\\" + m.charCodeAt().toString(8)).join('')
      this.output(result)
    },
    js8decode () {
      this.lastAction = this.js8decode
      let result = this.text.input.replace(/\\([0-7]+)/g, (match, i) => String.fromCharCode(parseInt(i, 8)))
      this.output(result)
    },
    js16encode () {
      this.lastAction = this.js16encode
      let result = this.text.input.split('').map(m => "\\x" + m.charCodeAt().toString(16)).join('')
      this.output(result)
    },
    js16decode () {
      this.lastAction = this.js16decode
      let result = this.text.input.replace(/\\x([a-f0-9]{1,4})/ig, (match, i) => String.fromCharCode(parseInt(i, 16)))
      this.output(result)
    },
    unicodeencode () {
      this.lastAction = this.unicodeencode
      let result = this.text.input.split('').map(m => {
          let pad = "0000"
          let str = m.charCodeAt().toString(16)
          return "\\u" + pad.substring(0, pad.length - str.length) + str
      }).join('')
      this.output(result)
    },
    unicodedecode () {
      this.lastAction = this.unicodedecode
      let result = this.text.input.replace(/\\u([a-fA-F0-9]{4})/g, (match, i) => String.fromCharCode(parseInt(i, 16)))
      this.output(result)
    },
    stringcharcode () {
      this.lastAction = this.stringcharcode
      let result = "String.fromCharCode(" + this.text.input.split('').map(m => m.charCodeAt()).join(',') + ")"
      this.output(result)
    },
    stringcharcodedecode () {
      this.lastAction = this.stringcharcodedecode
      let result = eval('String.fromCharCode(' + this.text.input + ')')
      this.output(result)
    },
    execute () {
        try {
            let result = eval(this.text.input)
            this.output(result)
        } catch (e) {}
    },
    scalConvert () {
      var input_text = this.text.input;
      var input_scale = this.scale_value_from;
      var output_scale = this.scale_value_to;
      var result = '';
      switch (input_scale){
        case '2':
          input_text = parseInt(input_text, 2);
          switch (output_scale) {
            case '10':
              result = input_text.toString(10);
              break;
            case '8':
              result = input_text.toString(8);
              break;
            case '16':
              result = input_text.toString(16);
              break;
          }
          break;
        case '8':
          input_text = parseInt(input_text, 8);
          switch (output_scale) {
            case '2':
              result = input_text.toString(2);
              break;
            case '10':
              result = input_text.toString(10);
              break;
            case '16':
              result = input_text.toString(16);
              break;
          }
          break;
        case '10':
          input_text = parseInt(input_text, 10);
          switch (output_scale) {
            case '2':
              result = input_text.toString(2);
              break;
            case '8':
              result = input_text.toString(8);
              break;
            case '16':
              result = input_text.toString(16);
              break;
          }
          break;
        case '16':
          input_text = parseInt(input_text, 16);
          switch (output_scale) {
            case '2':
              result = input_text.toString(2);
              break;
            case '8':
              result = input_text.toString(8);
              break;
            case '10':
              result = input_text.toString(10);
              break;
          }
          break;
      }
      this.output(result);
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
  .el-row {
    margin-bottom: 15px;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 4px;
  }

  .button-col {
    min-width: 410px;
  }

</style>
