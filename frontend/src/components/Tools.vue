<template>
  <div class="encode">
    <el-row :gutter="20" type="flex" justify="center">
      <el-col :span="8">
        <el-input
          type="textarea"
          :rows="30"
          placeholder="Input Here"
          v-model="text.input"
          resize="none"
          clearable>
        </el-input>
      </el-col>
      <el-col :span="5">
        <el-button-group>
            <el-button class='action' size="medium" v-on:click="urlencode">EncodeURI</el-button>
            <el-button class='action' size="medium" v-on:click="urlallencode">EncodeURIC</el-button>
            <el-button class='action' size="medium" v-on:click="urldecode">DecodeURI</el-button>
        </el-button-group>
        <el-button-group>
            <el-button class='action' size="medium" v-on:click="b64encode">EncodeBase64</el-button>
            <el-button class='action' size="medium" v-on:click="b64decode">DecodeBase64</el-button>
        </el-button-group>
        <el-button-group>
            <el-button class='action' size="medium" v-on:click="hexencode">EncodeHex</el-button>
            <el-button class='action' size="medium" v-on:click="hexdecode">DecodeHex</el-button>
        </el-button-group>
        <div class="hash">
        <el-select v-model="hashtype" size='medium' placeholder="Hash">
            <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value">
            </el-option>
        </el-select>
        <el-button class='action' size="medium" v-on:click="hashencode">Hash</el-button>
        </div>
        <el-button-group>
            <el-button class='action' size="medium" v-on:click="html16encode">EncodeUnicode(16)</el-button>
            <el-button class='action' size="medium" v-on:click="html16decode">DecodeUnicode(16)</el-button>
        </el-button-group>
        <el-button-group>
            <el-button class='action' size="medium" v-on:click="html10encode">EncodeUnicode(10)</el-button>
            <el-button class='action' size="medium" v-on:click="html10decode">DecodeUnicode(10)</el-button>
        </el-button-group>
        <el-button-group>
            <el-button class='action' size="medium" v-on:click="htmlentityencode">HTMLEntityEncode</el-button>
            <el-button class='action' size="medium" v-on:click="htmlentitydecode">HTMLEntityDecode</el-button>
        </el-button-group>
        <el-button-group>
            <el-button class='action' size="medium" v-on:click="fromcharcodeen">fromCharCodeEN</el-button>
            <el-button class='action' size="medium" v-on:click="fromcharcodede">fromCharCodeDE</el-button>
        </el-button-group>
        <div class="else">
          <el-button class='action' size="medium" v-on:click="jsbeautify">JS Beautify</el-button>
          <el-button class='action' size="medium" v-on:click="execute">EVAL CODZ</el-button>
          <el-button class='action' size="medium" v-on:click="clearcodz">CLEAR</el-button>
        </div>
      </el-col>
      <el-col :span="8">
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
    }
  },
  methods: {
    copyData () {
        return this.text.output
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
    execute () {
        try {
            let result = eval(this.text.input)
            this.output(result)
        } catch (e) {}
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
  .el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 4px;
  }
  .el-button-group {
    margin-bottom: 9px;
  }
  .hash {
    margin-bottom: 9px;
  }
  .el-row {
  }
  .action:hover {
    background-color: #FEF6E0;
    color: #D7B040;
    border-color:#FEF6E0;
  }
  .action:focus {
    background-color: #FEF6E0;
    color: #D7B040;
    border-color:#ffd04b;
  }

</style>
